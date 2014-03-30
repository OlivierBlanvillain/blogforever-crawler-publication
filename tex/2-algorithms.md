This section explains in detail the algorithms we developed to extract blog post articles as well as its variations for extracting authors, dates and comments. Our approach uses blog specific characteristics to build *extraction rules* which are applicable throughout a blog. Our focus is on minimising the algorithmic complexity while keeping our approach simple and generic.


Motivation
----------
Extracting metadata and content from HTML documents is a challenging task. Standards and format recommendations have been around for quite some time, strictly specifying how HTML documents should be organised @w3c2014. For instance the `<h1></h1>` tags have to contain the highest-level heading of the page and must not appear more than once per page @w3c2002. More recently, specifications such as microdata @whatwg2014 define ways to embed semantic information and metadata inside HTML documents, but these still suffer from very low usage: estimated to be used in less than 0.5% of websites @andrewrogers2014. In fact, the majority of websites rely on the generic `<span></span>` and `<div></div>` container elements with custom `id` or `class` attributes to organise the structure of pages, and more than 95% of pages do not pass HTML validation @brianwilson2008. Under such circumstances, relying on HTML structure to extract content from web pages is not viable and other techniques need to be employed.

Having blogs as our target websites, we made the following observations which play a central role in the extraction process^[Our experiments on a large dataset of blogs showed that failing tests were either due to a violation of one of these observations, or to an insufficient amount of text in posts. \edit{This is for instance the case of photoblogs where posts typically only contain a picture and a few words. Text might then not be sufficient to differentiate the article content from other elements of the page.} \TODO{The term "insufficient amount of text" needs a couple of lines more explanation. Why does this lead to a failure?}]:

\begin{enumerate}[label={(\alph*)}]
  \item\label{havefeedAssum} Blogs provide web feeds: structured and standardized views of the latest posts of a blog,
  \item\label{similarhtmlAssum} Posts of the same blog share a similar HTML structure.
\end{enumerate}

Web feeds usually contain about 20 blog posts @oita2010, often less than the total number of posts in blogs. Consequently, in order to effectively archive the entire content of a blog, it is necessary to download and process pages beyond the ones referenced in the web feed.


Content extraction overview
---------------------------
To extract content from blog posts, we proceed by building *extraction rules* from the data given in the blog's web feed. The idea is to use a set of *training data*, pairs of HTML pages and target content, to build an extraction rule capable of locating the target content on each HTML page.

Observation \ref{havefeedAssum} allows the crawler to obtain input for the extraction rule generation algorithm: each web feed entry contains a link to the corresponding web page as well as the blog post article (either abstract or full text), its title, authors and publication date. We call these fields *targets* as they constitute the data our crawler aims to extract. Observation \ref{similarhtmlAssum} guarantees the existence of an appropriate extraction rule, as well as its applicability to all posts of the blog.

#extractionAlgo shows the generic procedure we use to build extraction rules. The idea is quite simple: for each `(`*page, target*`)` input, compute, out of all possible extraction rules, the best one with respect to a certain `ScoreFunction`. The rule which is most frequently the *best rule* is then returned.

\extractionAlgo

One might notice that each *best rule* computation is independent and operates on a different input pair. This implies that #extractionAlgo is *embarrassingly parallel*: iterations of the outer loop can trivially be executed on multiple threads.

Functions in #extractionAlgo are voluntarily abstract at this point and will be explained in detail in the remaining of this section.
\hyperref[extractionrulesandstringsimilarity]{Subsection \ref*{extractionrulesandstringsimilarity}}
defines `AllRules`, `Apply` and the `ScoreFunction` we use for article extraction. In #timecomplexityandlinearreformulation we analyse the time complexity of #extractionAlgo and give a linear time reformulation using dynamic programming. Finally, #variationsforauthorsdatesandcomments shows how the `ScoreFunction` can be adapted to extract authors, dates and comments.

Extraction rules and string similarity
--------------------------------------
\label{extractionrulesandstringsimilarity}

In our implementation, rules are queries in the XML Path Language (XPath). Consequently, standard libraries can be used to parse HTML pages and apply extraction rules, providing the `Apply` function used in #extractionAlgo. We experimented with 3 types of XPath queries: selection over the HTML `id` attribute, selection over the HTML `class` attribute and selection using the relative path in the HTML tree. `id` attributes are expected to be unique, and `class` attributes have showed in our experiments to have better consistency than relative paths over pages of a blog. For these reasons we opt to always favour `class` over path, and `id` over `class`, such that the \coderef{allrulesAlgo} function returns a single rule per node.

\allrulesAlgo

Unsurprisingly, the choice of `ScoreFunction` greatly influences the running time and precision of the extraction process. When targeting articles, extraction rule scores are computed with a string similarity function comparing the extracted strings with the target strings. We chose the Sørensen–Dice coefficient similarity @dice1945, which is, to the best of our knowledge, the only string similarity algorithm fulfilling the following criteria:

  - \label{wordorderProp} Has low sensitivity to word ordering,
  - \label{lengthProp} Has low sensitivity to length variations,
  - \label{linearProp} Runs in linear time.

Properties \ref{wordorderProp} and \ref{lengthProp} are essential when dealing with cases where the blog's web feed only contains an abstract or a subset of the entire post article. #similarityTable gives examples to illustrate how these two properties hold for the Sørensen–Dice coefficient similarity but do not for *edit distance* based similarities such as the Levenshtein @levenshtein1966 similarity.

\similarityTable

The Sørensen–Dice coefficient similarity algorithm operates by first building sets of pairs of adjacent characters, also knows as *bigrams*, and then applying the *quotient of similarity* formula:

\similarityAlgo


Time complexity and linear reformulation
----------------------------------------
\label{timecomplexityandlinearreformulation}

With the functions \coderef{allrulesAlgo}, `Apply` and \coderef{similarityAlgo} (as `ScoreFunction`) being defined, the definition of #extractionAlgo for article extraction is now complete. We can therefore proceed with a time complexity analysis.

First, let's assume that we have at our disposal a linear time HTML parser that constructs an appropriate data structure, indexing HTML nodes on their `id` and `class` attributes, effectively making `Apply` $\in$ \Oof{1}. As stated before, the outer loop splits the input into independent computations and each call to \coderef{allrulesAlgo} returns (in linear time) at most as many rules as the number of nodes in its *page* argument. Therefore, the body of the inner loop will be executed \Oof{n} \TODO{A definition of n is missing (although it can be guessed).} \edit{I'm for leaving it like this, or changing \Oof{n} for "a linear number of". What do you think? } times. Because each extraction rule can return any subtree of the queried page, each call to \coderef{similarityAlgo} takes \Oof{n}, leading to an overall quadratic running time.

We now present #linearAlgo, a linear time reformulation of #extractionAlgo for article extraction using dynamic programming.

\linearAlgo

While very intuitive, the original idea of first generating extraction rules and then picking these best rules prevents us from effectively reusing previously computed bigrams (set of pairs of adjacent characters). For instance, when evaluating the extraction rule for the HTML root node, #extractionAlgo will obtain the complete string of the page and pass it to the \coderef{similarityAlgo} function. At this point, the information on where the string could be split into substrings with already computed bigrams is not accessible, and the bigrams of the page have to be computed by linearly traversing the entire string. To overcome this limitation and implement *memoization* over the bigrams computations, #linearAlgo uses a post-order traversal of the HTML tree and computes node bigrams from their children bigrams. This way, we avoid serializing HTML subtrees for each bigrams computation and have the guarantee that each character of the HTML page will be read at most once during the bigrams computation.

With bigrams computed in this dynamic programming manner, the overall time to compute all \coderef{bigramsAlgo}`(`*node.text*`)` is linear. To conclude the proof that #linearAlgo runs in linear time we show that all other computations of the inner loop can be done in constant *amortized* time. As the number of edges in a tree is one less than the number of nodes, the *amortized* number of bigrams unions per inner loop iteration tends to one. Each *quotient of similarity* computation requires one bigrams intersection and three bigrams length computations. Over a finite alphabet (we used printable ASCII), bigrams sizes have bounded size and each of these operations takes constant time.


Variations for authors, dates, comments
---------------------------------------
\label{variationsforauthorsdatesandcomments}

Using string similarity as the only score measurement leads to poor performance on author and date extraction, and is not suitable for comment extraction. This subsection presents variations of the `ScoreFunction` which addresses issues of these other types of content.

The case of authors is problematic because authors' names often appear in multiple places of a page, which results in several rules with maximum \coderef{similarityAlgo} score. The heuristic we use to get around this issue consists of adding a new component in the `ScoreFunction` for author extraction rules: the *tree distance* between the evaluated node and the post content node. This new component takes advantage of the positioning of a post's authors node which often is a direct child or shares its parent with the post content node.

Dates are affected by the same duplication issue, as well as the issue of inconsistencies of format between web feeds and web pages. Our solution for date extraction extends the `ScoreFunction` for authors by comparing the *extracted* string to multiple *targets*, each being a different string representation of the original date obtained from the web feed. For instance, if the feed indicates that a post was published at \stringliteral{Thu, 01 Jan 1970 00:00:00}, our algorithm will search for a rule that returns one of \stringliteral{Thursday January 1, 1970}, \stringliteral{1970-01-01}, \stringliteral{43 years ago} and so on. So far we do not support dates in multiple languages, but adding new target formats based on languages detection would be a simple extension of our date extraction algorithm.

Comments are usually available in separate web feeds, one per blog post. Similarly to blog feeds, comment feeds have a limited number of entries, and when the number of comments on a blog post exceeds this limit, comments have to be extracted from web pages. To do so, we use the following `ScoreFunction`:

  - Rules returning fewer HTML nodes than the number of comments on the feed are filtered out with a zero score,
  
  - The scores of the remaining rules are computed with the value of the *maximum weighted matching* in the *complete bipartite graph* $G = (U, V, E)$, where $U$ is the set of HTML nodes returned by the rule, $V$ is the set of target comment fields from the web feed (such as comment authors) and $E(u, v)$ has weight equal to \coderef{similarityAlgo}`(`*u, v*`)`.

Our crawler executes this algorithm on each post with an overflow on its comment feed, thus supporting blogs with multiple commenting engines. The comment content is extracted first, allowing us to narrow down the initial filtering by fixing a target number of comments. \TODO{This paragraph is hard to follow! What is "an overflow on its comment feed"? Do you mean comments content arriving by means of AJAX calls? Please explain. The second sentence of the paragraph is also not clear ("..narrow down ...fixint a target..."). Please rewrite this paragraph.} \edit{I'm for completely removing this paragraph because I these are very unimportant details about comment extraction. The point on "overflow on comment feed" is a repetition of the" Similarly to blog feeds..." sentence in the paragraph before the bullet points: if the comment feed is not full there is no need to extract comments from the page. The fact that we run this algorithm on each page to support multiple commenting engines is really a detail, I've only found one blog during my tests that used two different engines... Regarding the "comment content is extracted first", this is a small optimization I did to first get the exact number of comments by matching the comment content (which is usually more unique and accurate that doing a matching on author/date), and use this number to then accurately get the other fields. Let me know if you think that this is worth including...}

Regarding time complexity, computing the *tree distance* of each node of a graph to a single reference node can be done in linear time, and multiplying the number of targets by a constant factor does not affect the asymptotic computational complexity. Computing scores of comment extraction rules requires a more expensive algorithm. However, this is compensated by the fact that the proportion of candidates left, after filtering out rules not returning enough results, is very low in practice. Analogous reformulations to the one done with #linearAlgo can be straightforwardly applied on each `ScoreFunction` in order to minimize the time spent in \coderef{similarityAlgo}.

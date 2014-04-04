Our evaluation is articulated in two parts. First, we compare the article extraction procedure presented in #algorithms with three open-source projects capable of extracting articles and titles from web pages. The comparison will show that our blog-targeted solution has better performance both in terms of success rate and running time. Extraction of authors, dates and comments is not part of this evaluation because of the lack of publicly available competing projects and reference data sets.

Our experiments were run using *Debian GNU/Linux 7.2*, *Python 2.7* and an *Intel Core i7-3770 3.4 GHz* processor. Timing measurements were made on a single dedicated core with garbage collection disabled. The Git repository for this paper^[<https://github.com/OlivierBlanvillain/bfc-paper>] contains the necessary scripts and instructions to reproduce all the evaluation experiments presented in this section. The crawler source code is available under the MIT license from the project's website^[<https://github.com/BlogForever/crawler>].


Extraction success rates
------------------------
To evaluate article and title extraction from blog posts we compare our approach to three open source projects: Readability^[<https://github.com/gfxmonk/python-readability>], Boilerpipe @kohlschuetter2010 and Goose^[<https://github.com/GravityLabs/goose>], which are implemented in JavaScript, Java and Scala respectively. These projects are more generic than our blog-specific approach in the sense that they are able to identify and extract data directly from HTML source code, and do not make use of web feeds or structural similarities between pages of the same blog (observations \ref{havefeedAssum} and \ref{similarhtmlAssum}, #motivation). #precisionTable shows the extraction success rates for article and title on a test sample of 2300 blog posts from 230 blogs obtained from the Spinn3r dataset @burton2011.

\precisionTable

\input{runningtimeFigure.tex}

On our test dataset, #extractionAlgo outperformed the competition by 4.9% on article extraction and 10.1% on title extraction. It is important to stress that Readability, Boilerpipe and Goose rely on generic techniques such as word density, paragraph clustering and heuristics on HTML tagging conventions, which are designed to work for any type of web page. On the contrary, our algorithm is only suitable for pages providing web feeds, as they constitute the reference data used to build extraction rules. Therefore, results shown in #precisionTable should not be interpreted as a general quality evaluation of the different projects, but simply as evidences that our approach is more suitable when working with blogs.

Article extraction running times
--------------------------------
In addition to the quality of the extracted data we also evaluated the running time of the extraction procedure. The main point of interest is the ability of the extraction procedure to scale as the number of posts in the processed blog increases. This corresponds to the evaluation of a *NewCrawl* task, which is in charge of harvesting all published content on a blog.

#runningtime shows the cumulated time spent for each article extraction system (this excludes common tasks such as downloading pages and storing results) as a function of the number of blog posts processed. We used the Quantum Diaries^[<http://www.quantumdiaries.org>] blog for this experiment.

Data presented in this graph was obtained by taking the arithmetic mean over 10 measurements. These results are believed to be significant given that standard deviations are of the order of 2 milliseconds.

As illustrated in #runningtime, our approach spends the majority of its total running time between the initialisation and the processing of the first blog post. This initial increase of about 0.4 seconds corresponds to cost of executing #linearAlgo to compute extraction rule for articles. As already mentioned, this consists of computing the *best extraction rule* of each page referenced by the web feed and picking the most appropriate one. Once this extraction rule is computed, processing subsequent blog posts only requires parsing and applying the rule, which takes about 3 milliseconds per page and is barely visible on the scale of #runningtime. The other evaluated solutions do not function this way: each blog post is processed as new and independent input, leading to approximately linear running times.

The vertical dashed line at 15 processed blog posts represents a suitable point of comparison of the processing time per blog post. Indeed, as the web feed of our test blog contains\ 15 blog posts, the extraction rule computation performed by our approach includes the cost of entirely processing these 15 entries. That being said, comparing raw performance of algorithms implemented in different programming languages is not very informative given the high variation of running times observed across different programming languages @hundt2011.

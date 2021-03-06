Blogs disappear every day @johnson2008blogs. Losing data is obviously undesirable, but even more so when this data has historic, political or scientific value. In contrast to books, newspapers or centralized web platforms, there is no standard method \phantom{x}
\ \newline
or authority to ensure blog archiving and long-term digital preservation. Yet, blogs are an important part of today's web: WordPress reports more than 1 million new posts and 1.5 million new comments each day @wordpress2014. Blogs also showed to be an important resource during the 2011 Egyptian revolution by playing an instrumental role in the organization and implementation of protests @nahedeltantawy2012. The need to preserve this volatile communication medium is nowadays very clear.

Among the challenges in developing a blog archiving software is the design of a web crawler capable of automatically and efficiently traversing blogs to harvest their content. The sheer size of the blogosphere combined with an unpredictable publishing rate of new information call for a highly scalable system, while the lack of programmatic access to the complete blog content makes the use of automatic extraction techniques necessary. The variety of available blog publishing platforms offers a limited common set of properties that a crawler can exploit, further narrowed by the ever-changing structure of blog contents. Finally, an increasing number of blogs heavily rely on dynamically created content to present information, using the latest web technologies, hence invalidating traditional web crawling techniques.

A key characteristic of blogs which differentiates them from regular websites is their association with web feeds\ @lindahl2003weblogs. Their primary use is to provide a uniform subscription mechanism, thereby allowing users to keep track of the latest updates without the need to actually visit blogs. Concretely, a web feed is an XML file containing links to the latest blog posts along with their articles (abstract or full text) and associated metadata @board2007rss. While web feeds essentially solve the question of update monitoring, their limited size makes it necessary to download blog pages in order to harvest previous content.

This paper presents the open-source BlogForever Crawler, a key component of the BlogForever platform @kasioumis2013towards responsible for traversing blogs, extracting their content and monitoring their updates. Our main objective in this work is to design a crawler capable of extracting blog articles, authors, publication dates and comments. Our contributions can be summarized as follows:

  - We present a new algorithm to build extraction rules from web feeds. We then derive an optimized reformulation tied to a particular string similarity metric and show that this reformulated algorithm has a linear time complexity.
  
  - We show how to use this algorithm for blog article extraction and how it can be adapted to authors, publication dates and comments.
  
  - We present the overall crawler architecture and the specific components we implemented to efficiently traverse blogs. We explain how our design allows for both modularity and scalability.
  
  - We show how we make use of a complete web browser to render JavaScript powered web pages before processing them. This step allows our crawler to effectively harvest blogs built with modern technologies, such as the recently popular comment hosting services.
  
  - We evaluate the quality of extraction and the execution time of our algorithm against three state-of-the-art web article extraction algorithms.
  
Although our crawler implementation is integrated with the BlogForever platform, the presented techniques and algorithms are relevant for other applications related to Wrapper Generation and Web Data Extraction.

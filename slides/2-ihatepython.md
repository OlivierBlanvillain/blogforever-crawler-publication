I Hate Python
=============

----------------------------------------------------------

### What I'm not going to talk about:

- sdtlib documentation

- pip, virtualenv

- Byte String vs Unicode String

----------------------------------------------------------

### Things that bug me:

- Interfaces?  
  ↪ \ *you better like reading source code...*
  
- Type-checking?  
- Exceptions as control flow?  
  ↪ \ *you better like stack traces...*

- Immutability?  
  ↪ \ *just don't modify the thing...*

----------------------------------------------------------

## Interfaces

### *"We're all consenting adults here"*  

----------------------------------------------------------

# Nope.

----------------------------------------------------------

```python
      def parseHTML(page):
        """Parses a page to a tree html elements.

        @type  page: string
        @param page: the page to parse
        @rtype: xml.etree.ElementTree.Element
        @return: the root of the html tree
        """
```
  . . .

```python
        try:
          return lxml.html.fromstring(page)
        except (LookupError,
                UnicodeDecodeError,
                lxml.etree.XMLSyntaxError,
                lxml.etree.ParserError): # TBC
          try:
            return soupparser.fromstring(page)
          except Exception:
            return lxml.etree.Element("html")
```

----------------------------------------------------------

### lxml documentation:

![](img/lxml.png)

----------------------------------------------------------

## Type-checking

### *"If it looks like a duck and quacks like*

### *a duck, then it must be a duck"*

----------------------------------------------------------

![](img/sc.jpg)
    
```python
    max([ True, 2, [3, 4], {5: 6, 7: 8}, "nine", None ])
```

----------------------------------------------------------

```python
def bestPath(contentZipPages):
  """Given a list of content/page, computes the best XPath
  query that would return the content on each page.

  @type  contentZipPages: list of (string, etree._Element)
  @param contentZipPages: list of guiding (content, page)
  @rtype: string
  @return: a XPath extracting the content of each pages
  """
```
. . .

```python
  queries = ("/some/path", "/another/path", ...)
  dct = dict()
  ratio = lambda content, page, query: (
      levenshtein(content, extractFirst(page, query)), dct)
```
```python
  topQueriesHead = nlargest(
      10, queries, key=partial(ratio, *contentZipPages[0]))
```
```python
  topQueries = map(lambda (c, p):
      max(topQueriesHead, key=partial(ratio, c, p)),
      contentZipPages)
```
```python
  return max(set(topQueries), key=topQueries.count)
```
----------------------------------------------------------


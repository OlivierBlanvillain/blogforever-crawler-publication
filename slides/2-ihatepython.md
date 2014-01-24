I Hate Python
=============

----------------------------------------------------------

![](img/sc.jpg)

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
. . .

```python
  topQueriesHead = nlargest(
      6, queries, key=partial(ratio, *contentZipPages[0]))
```
```python
  topQueries = map(lambda (c, p):
      max(topQueriesHead, key=partial(ratio, c, p)),
      contentZipPages)
```
```python
  max(set(topQueries), key=topQueries.count)
```
----------------------------------------------------------


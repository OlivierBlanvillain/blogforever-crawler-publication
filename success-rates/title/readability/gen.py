import sys
from lxml.html.clean import Cleaner
from os import listdir
from re import sub as resub
from readability.readability import Document
from urllib2 import urlopen, HTTPError
import codecs

def cleanTags(string):
  htmlCleaned = Cleaner(allow_tags=[''], remove_unknown_tags=False, style=True
      ).clean_html(string or u"dummy")
  return resub(r"\s\s+" , " ", htmlCleaned)

def main():
  titles = sys.argv[1]
  for url in listdir(titles):
    print url
    with codecs.open(url, "w", encoding="utf-8") as out:
      try:
        html = urlopen(url.replace("{", "/")).read()
        out.write(cleanTags(Document(html).title()))
      except HTTPError:
        out.write("")

if __name__ == "__main__":
  main()

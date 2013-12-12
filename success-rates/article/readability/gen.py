import sys
from lxml.html.clean import Cleaner
from os import listdir
from re import sub as resub
from readability.readability import Document
from urllib2 import urlopen, HTTPError
import codecs

def main():
  contents = sys.argv[1]
  for url in listdir(contents):
    print url
    with codecs.open(url, "w", encoding="utf-8") as out:
      try:
        html = urlopen(url.replace("{", "/")).read()
        out.write((Document(html).summary()))
      except HTTPError:
        out.write("")

if __name__ == "__main__":
  main()

import sys
from boilerpipe.extract import Extractor
from os import listdir
from urllib2 import urlopen, HTTPError
import codecs

def main():
  contents = sys.argv[1]
  for url in listdir(contents):
    print url
    with codecs.open(url, "w", encoding="utf-8") as out:
      try:
        html = urlopen(url.replace("{", "/")).read()
        extracted = Extractor(html=html)
        out.write(extracted.getText())
      except HTTPError:
        out.write("")

if __name__ == "__main__":
  main()

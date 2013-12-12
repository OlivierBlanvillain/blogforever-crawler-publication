import sys
from goose import Goose
from os import listdir
import codecs

def main():
  contents = sys.argv[1]
  goose = Goose()
  for url in listdir(contents):
    print url
    with codecs.open(url, "w", encoding="utf-8") as out:
      try:
        extracted = goose.extract(url=url.replace("{", "/"))
        out.write(extracted.title)
      except (IOError, TypeError):
        out.write("")
        print "Error"

if __name__ == "__main__":
  main()

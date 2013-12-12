import sys
import codecs
from Levenshtein import ratio
from os import listdir

def bigrams(string):
  return set(map(lambda i: string[i : i + 2], xrange(len(string) - 1)))

def dicesCoeffSimilarity(string1, string2):
  bigrams1 = bigrams(string1)
  bigrams2 = bigrams(string2)
  intersection = bigrams1.intersection(bigrams2)
  return (2.0 * len(intersection)) / (len(bigrams1) + len(bigrams2))

def main():
  first = sys.argv[1]
  second = sys.argv[2]

  threshold = 0.5
  total = 0.0
  count = 0.0

  for page in listdir(first):
    with codecs.open(first + "/" + page, "r", encoding="utf-8") as f:
      firstpage = f.read()
    try:
      with codecs.open(second + "/" + page, "r", encoding="utf-8") as f:
        secondpage = f.read()
    except IOError:
      secondpage = u""
    if len(firstpage) > 20:
      ratio = dicesCoeffSimilarity(firstpage + ".", secondpage + ".")
      # ratio = ratio(firstpage + ".", secondpage + ".")
      total = total + 1.0
      if ratio > threshold:
        count = count + 1.0
      elif len(sys.argv) == 4:
        print page.replace("{", "/")

  print "{}: {}%".format(second, count/total * 100.0)


if __name__ == "__main__":
  main()

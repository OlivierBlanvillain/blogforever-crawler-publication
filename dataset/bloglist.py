from os import listdir
from itertools import imap

print "\n".join(set(imap(
  lambda _: _.split("{")[2],
  listdir("contents/"))))

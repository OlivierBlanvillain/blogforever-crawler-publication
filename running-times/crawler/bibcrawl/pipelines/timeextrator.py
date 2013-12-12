# """TimeExtrator"""

# from bibcrawl.utils.ohpython import *
# from bibcrawl.utils.parsing import parseHTML
# from bibcrawl.utils.stringsimilarity import cleanTags
# from boilerpipe.extract import Extractor
# from goose import Goose
# from readability.readability import Document
# from scrapy import log
# from time import time
# import gc
# import sys

# class TimeExtrator(object):
#   def process_item(self, item, spider):
#     gcenabled = gc.isenabled()
#     gc.disable()
#     try:
#       contentExtractor = lambda _: spider.contentExtractor(parseHTML(_))
#       boilerpipeExtractor = lambda _: Extractor(html=_).getText()
#       gooseExtractor = lambda _: Goose().extract(raw_html=_).cleaned_text
#       readabilityExtractor = lambda _: cleanTags(Document(_).summary())

#       # CE, BP, GO, RE
#       log.msg("{} {} {} {}".format(
#         timeMeThis(partial(contentExtractor,     item.rawHtml)),
#         timeMeThis(partial(boilerpipeExtractor,  item.rawHtml)),
#         timeMeThis(partial(gooseExtractor,       item.rawHtml)),
#         timeMeThis(partial(readabilityExtractor, item.rawHtml)),
#       ))
#     finally:
#       if gcenabled:
#         gc.enable()

# def timeMeThis(e):
#   t0 = time()
#   e()
#   return time() - t0

"""TimeExtrator"""

from bibcrawl.utils.ohpython import *
from bibcrawl.utils.parsing import parseHTML
from bibcrawl.utils.stringsimilarity import cleanTags
from boilerpipe.extract import Extractor
from goose import Goose
from readability.readability import Document
from scrapy import log
from time import time
import gc
import sys
from numpy import median, mean, std

class TimeExtrator(object):
  def process_item(self, item, spider):
    gcenabled = gc.isenabled()
    gc.disable()
    try:
      contentExtractor = lambda _: spider.contentExtractor(parseHTML(_))
      boilerpipeExtractor = lambda _: Extractor(html=_).getText()
      gooseExtractor = lambda _: Goose().extract(raw_html=_).cleaned_text
      readabilityExtractor = lambda _: cleanTags(Document(_).summary())

      # CE, BP, GO, RE
      ntimes = range(11)
      contents = map(
        lambda _: timeMeThis(partial(contentExtractor, item.rawHtml)),
        ntimes)
      boilerpipes = map(
        lambda _: timeMeThis(partial(boilerpipeExtractor, item.rawHtml)),
        ntimes)
      gooses = map(
        lambda _: timeMeThis(partial(gooseExtractor, item.rawHtml)),
        ntimes)
      readabilitys = map(
        lambda _: timeMeThis(partial(readabilityExtractor, item.rawHtml)),
        ntimes)

      log.msg("{} {} {} {} {} {} {} {}".format(
        mean(contents), std(contents),
        mean(boilerpipes), std(boilerpipes),
        mean(gooses), std(gooses),
        mean(readabilitys), std(readabilitys)
      ))
    finally:
      if gcenabled:
        gc.enable()

def timeMeThis(e):
  t0 = time()
  e()
  return time() - t0

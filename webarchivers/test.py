from selenium import webdriver
from os.path import dirname, join
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException
from time import sleep, time

def main():
  path = join(dirname(__file__), "/home/olivier/workspace/crawler/lib/phantomjs/bin/phantomjs")
  driver = webdriver.PhantomJS(path)

  url = "http://www.chancellors.co.uk/properties/search?map=false&area=New+Barnet&longitude=0&latitude=0&radius=5&saleType=Rent"
  buttonPath = "//a[@id='Loadmore']"
  pricesPath = "//div[@class='list-property clearfix']//h3"

  driver.get(url)
  # sleep(2)
  # clickWhileVisible(driver, buttonPath)
  # sleep(2)
  result = map(
    lambda _: _.get_attribute("innerHTML"),
    driver.find_elements_by_xpath(pricesPath))
  print "\n".join(result)

  driver.quit()

def clickWhileVisible(driver, xPath, maxDuration=5, stepDuration=0.5):
  try:
    timeout = time() + maxDuration
    while time() < timeout:
      driver.find_element_by_xpath(xPath).click()
      # "document.getElementsByClassName('fyre-text')[0].click()")
      sleep(stepDuration)
  except (ElementNotVisibleException, NoSuchElementException):
    pass

if __name__ == '__main__':
  main()

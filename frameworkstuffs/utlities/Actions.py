import logging
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Actions:

    def __init__(self, driver, log):
        self.driver = driver
        self.log = log

    def launch_url(self, url):
        self.driver.get(url)
        self.log.info("Launched URL "+url)

    def click_element(self, locator, elemname):
        webelement = self.driver.find_element(*locator)
        webelement.click()
        self.log.info("Clicked on element "+elemname)


    def sendKeys(self, locator, value, elemname):
        webelement = self.driver.find_element(*locator)
        webelement.send_keys(value)
        self.log.info("Entered value as "+value+" on element "+elemname)

    def dropdownSelection(self, locator, value, elemname):
        webelement = self.driver.find_element(*locator)
        ddelement = Select(webelement)
        ddelement.select_by_visible_text(value)
        self.log.info("Selecting value as " + value + " from the drop down " + elemname)

    def getText(self, locator, elemname):
        webelement = self.driver.find_element(*locator)
        text = webelement.text
        self.log.info("Returning text as "+text+" from element " + elemname)
        return text

    def waitForElementVisible(self, locator, timeout, elementName):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))

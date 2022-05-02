from selenium.webdriver.common.by import By

from frameworkstuffs.utlities.Actions import Actions
from pageObjects.LoginPage import LoginPage


class SummaryCartPage:

    def __init__(self, driver):
        self.driver = driver

    txtMsg = (By.XPATH, "//h1[@id='cart_title']/span")
    iconDelete = (By.XPATH, "//*[@title='Delete']")
    txtEmptyCartMsg = (By.CSS_SELECTOR, ".alert.alert-warning")

    def getItemCountMsg(self, log):
        actions = Actions(self.driver, log)
        return actions.getText(self.txtMsg, "Cart Item Count")

    def getSummartCartEmptyMsg(self, log):
        actions = Actions(self.driver, log)
        return actions.getText(self.txtEmptyCartMsg, "Empty Cart Msg")

    def emptyCart(self, log):
        actions = Actions(self.driver, log)
        actions.click_element(self.iconDelete, "Delete Icon")
        actions.waitForElementVisible(self.txtEmptyCartMsg, 30, "Empty Cart Message")




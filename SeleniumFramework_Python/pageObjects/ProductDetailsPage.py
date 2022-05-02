from selenium.webdriver.common.by import By

from frameworkstuffs.utlities.Actions import Actions
from pageObjects.LoginPage import LoginPage


class ProductDetailsPage:

    def __init__(self, driver):
        self.driver = driver

    dropdownSize = (By.XPATH, "//select[@id='group_1']")
    option_M_dropdownSize = (By.XPATH, "//select[@id='group_1']/option[@title='M']")
    btnAddToCart = (By.XPATH, "//p[@id='add_to_cart']//span[text()='Add to cart']")
    txtSuccessMsg= (By.XPATH, "(//div[@id='layer_cart']//span[@class='title'])[1]")
    btnProceedToCheckout = (By.XPATH, "//a[@title='Proceed to checkout']/span")

    def addItemToTheCart(self, log, size):
        actions = Actions(self.driver, log)
        actions.click_element(self.dropdownSize, "Size drop down")
        actions.click_element(self.option_M_dropdownSize, "Option M")
        actions.click_element(self.btnAddToCart, "Add to Cart Button")
        actions.waitForElementVisible(self.btnProceedToCheckout, 30, "Cart Pop Up")

    def getCartSuccessMessage(self, log):
        actions = Actions(self.driver, log)
        return actions.getText(self.txtSuccessMsg, "Success Message")

    def proceedingToTheSummaryPage(self, log):
        actions = Actions(self.driver, log)
        actions.click_element(self.btnProceedToCheckout, "Proceed to Checkout Button")




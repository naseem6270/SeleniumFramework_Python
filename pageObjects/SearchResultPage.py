from selenium.webdriver.common.by import By

from frameworkstuffs.utlities.Actions import Actions
from pageObjects.LoginPage import LoginPage
from pageObjects.ProductDetailsPage import ProductDetailsPage


class SearchResultPage:

    def __init__(self, driver):
        self.driver = driver

    sectionFirstResult = (By.XPATH, "//ul[@id='product_list']//a[@class='product-name']")

    def selectItem(self, log):
        actions = Actions(self.driver, log)
        productDetailsPage = ProductDetailsPage(self.driver)
        actions.click_element(self.sectionFirstResult, "First Result Item")
        return productDetailsPage


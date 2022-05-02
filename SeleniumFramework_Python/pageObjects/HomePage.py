from selenium.webdriver.common.by import By

from frameworkstuffs.utlities.Actions import Actions
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchResultPage import SearchResultPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    logoBrandHomePage = (By.XPATH, "//a[@title='My Store']/img")
    linkSignIn = (By.XPATH, "//div[@class='header_user_info']/a[@class='login']")
    txtFieldSearch = (By.NAME, "search_query")
    btnSearch = (By.NAME, "submit_search")

    def navigateToTheLoginPage(self, log):
        actions = Actions(self.driver, log)
        loginpage = LoginPage(self.driver)
        actions.click_element(self.linkSignIn, "Sign In link")
        return loginpage

    def searchProduct(self, log, itemToBeSearched):
        actions = Actions(self.driver, log)
        searchResultPage = SearchResultPage(self.driver)

        actions.click_element(self.txtFieldSearch, "Search text field")
        actions.sendKeys(self.txtFieldSearch, itemToBeSearched, "Search text field")
        actions.click_element(self.btnSearch, "Search button")
        return searchResultPage
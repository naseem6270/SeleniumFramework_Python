from selenium.webdriver.common.by import By

from frameworkstuffs.utlities.Actions import Actions


class MyAccountPage:
    def __init__(self, driver):
        self.driver = driver

    headerMyAccountPage = (By.XPATH, "//h1[@class='page-heading']")
    linkSignOut = (By.XPATH, "//a[@title='Log me out']")
    breadCrumbHomePage = (By.XPATH, "//div[contains(@class, 'breadcrumb')]//a[@title='Return to Home']")

    def getHeader(self, log):
        actions = Actions(self.driver, log)
        return actions.getText(self.headerMyAccountPage, "My Account Header")


    def signingOut(self, log):
        actions = Actions(self.driver, log)
        actions.click_element(self.linkSignOut, "Sign Out link")

    def navigateToTheHomePage(self, log):
        actions = Actions(self.driver, log)
        actions.click_element(self.breadCrumbHomePage, "Bread Crumb Home Page Icon")

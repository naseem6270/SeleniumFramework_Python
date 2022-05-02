import pytest
from selenium.webdriver.common.by import By

from frameworkstuffs.utlities.Actions import Actions
from pageObjects.MyAccountPage import MyAccountPage


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    txtFieldEmailID = (By.ID, "email")
    txtFieldPassword = (By.ID, "passwd")
    btnSubmit = (By.ID, "SubmitLogin")
    txtError = (By.XPATH, "//div[@class='alert alert-danger']/ol/li")

    def login(self, log, emailID, password):

        actions = Actions(self.driver, log)
        myAccount = MyAccountPage(self.driver)
        actions.click_element(self.txtFieldEmailID, "Username text field")
        actions.sendKeys(self.txtFieldEmailID, emailID, "Username text field")
        actions.click_element(self.txtFieldPassword, "Password text field")
        actions.sendKeys(self.txtFieldPassword, password, "Password text field")
        actions.click_element(self.btnSubmit, "Submit button")
        return myAccount
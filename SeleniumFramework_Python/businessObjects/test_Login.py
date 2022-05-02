import pytest

from frameworkstuffs.controller.BaseClass import BaseClass
from frameworkstuffs.utlities.Actions import Actions
from pageObjects.HomePage import HomePage
from testData.TestData import TestData


class TestLogin(BaseClass):

    @pytest.fixture(params=TestData.test_Login_Data)
    def get_login_data(self, request):
        return request.param

    @pytest.mark.loginScenarios
    def test_validlogin(self, get_login_data):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        actions = Actions(self.driver, log)
        actions.launch_url(get_login_data["url"])
        loginpage = homepage.navigateToTheLoginPage(log)
        myAccountPage = loginpage.login(log, get_login_data["emailID"], get_login_data["password"])
        myAccountPage.signingOut(log)

    @pytest.mark.InvalidloginScenarios
    def test_Invalidlogin(self, get_login_data):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        actions = Actions(self.driver, log)

        actions.launch_url(get_login_data["url"])
        loginpage = homepage.navigateToTheLoginPage(log)
        loginpage.login(log, get_login_data["emailID"], "Invalid Password")

        errorMsg = actions.getText(loginpage.txtError, "Error Message")

        assert errorMsg == "Authentication failed."

    @pytest.mark.InvalidloginScenarios
    def test_BlankUserId(self, get_login_data):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        actions = Actions(self.driver, log)

        actions.launch_url(get_login_data["url"])
        loginpage = homepage.navigateToTheLoginPage(log)
        loginpage.login(log, "", get_login_data["password"])

        errorMsg = actions.getText(loginpage.txtError, "Error Message")

        assert errorMsg == "An email address required."

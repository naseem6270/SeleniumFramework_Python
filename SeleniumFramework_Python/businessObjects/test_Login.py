import pytest
from selenium.webdriver.common import actions

from frameworkstuffs.controller.BaseClass import BaseClass
from frameworkstuffs.utlities.Actions import Actions
from pageObjects.HomePage import HomePage
from testData.TestData import TestData


class TestLogin(BaseClass):

    @pytest.fixture(params=TestData.test_Login_Data)
    def get_login_data(self, request):
        return request.param

    @pytest.fixture(autouse=True)
    def classobject(self):
        self.log = self.getLogger()
        self.homepage = HomePage(self.driver)
        self.actions = Actions(self.driver, self.log)


    @pytest.mark.loginScenarios
    @pytest.mark.run(order=1)
    def test_shouldLoginUser_WhenCredentialsAreValid(self, get_login_data):

        self.actions.launch_url(get_login_data["url"])
        loginpage = self.homepage.navigateToTheLoginPage(self.log)
        myAccountPage = loginpage.login(self.log, get_login_data["emailID"], get_login_data["password"])
        headerMyAccPage = myAccountPage.getHeader(self.log)
        assert headerMyAccPage == "MY ACCOUNT"
        myAccountPage.signingOut(self.log)

    @pytest.mark.InvalidloginScenarios
    @pytest.mark.run(order=2)
    def test_shouldNotLoginUser_WhenCredentialsAreInValid(self, get_login_data):


        self.actions.launch_url(get_login_data["url"])
        loginpage = self.homepage.navigateToTheLoginPage(self.log)
        loginpage.login(self.log, get_login_data["emailID"], "Invalid Password")

        errorMsg = self.actions.getText(loginpage.txtError, "Error Message")

        assert errorMsg == "Authentication failed."

    @pytest.mark.InvalidloginScenarios
    @pytest.mark.run(order=3)
    def test_shouldNotLoginUser_WhenPasswordIsBlank(self, get_login_data):
        self.actions.launch_url(get_login_data["url"])
        loginpage = self.homepage.navigateToTheLoginPage(self.log)
        loginpage.login(self.log, "", get_login_data["password"])

        errorMsg = self.actions.getText(loginpage.txtError, "Error Message")

        assert errorMsg == "An email address required."

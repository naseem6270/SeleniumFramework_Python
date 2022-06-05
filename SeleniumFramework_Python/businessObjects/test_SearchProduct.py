import pytest

from frameworkstuffs.controller.BaseClass import BaseClass
from frameworkstuffs.utlities.Actions import Actions
from pageObjects.HomePage import HomePage
from pageObjects.MyAccountPage import MyAccountPage
from pageObjects.ProductDetailsPage import ProductDetailsPage
from pageObjects.SummaryCartPage import SummaryCartPage
from testData.TestData import TestData
from selenium import webdriver


class TestSearchProduct(BaseClass):

    @pytest.fixture(params=TestData.test_Search_Data)
    def get_search_data(self, request):
        return request.param

    @pytest.fixture(params=TestData.test_Login_Data)
    def get_login_data(self, request):
        return request.param

    @pytest.mark.SearchProduct
    def test_shouldShowProductDetailsPage_WhenSelectItFromTheList(self, get_login_data, get_search_data):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        actions = Actions(self.driver, log)
        productDetailsPage = ProductDetailsPage(self.driver)


        actions.launch_url(get_login_data["url"])
        loginpage = homepage.navigateToTheLoginPage(log)
        myAccountPage = loginpage.login(log, get_login_data["emailID"], get_login_data["password"])
        myAccountPage.navigateToTheHomePage(log)
        searchResultPage = homepage.searchProduct(log, get_search_data["itemToBeSearched"])
        searchResultPage.selectItem(log)
        prodHeader = productDetailsPage.getProductHeader(log)
        assert prodHeader.strip() == "Faded Short Sleeves T-shirt"


    @pytest.mark.SearchProduct
    def test_shouldAddItemToTheCart(self, get_search_data):
        log = self.getLogger()
        actions = Actions(self.driver, log)

        productDetailsPage = ProductDetailsPage(self.driver)
        productDetailsPage.addItemToTheCart(log, get_search_data["size"])
        successtxt = productDetailsPage.getCartSuccessMessage(log)
        assert successtxt.strip() == "Product successfully added to your shopping cart".strip()

    @pytest.mark.SearchProduct
    def test_ShouldEmptyCart_WhenUserRemovesTheItem(self):
        log = self.getLogger()
        actions = Actions(self.driver, log)
        productDetailsPage = ProductDetailsPage(self.driver)
        myAccountPage = MyAccountPage(self.driver)
        summaryPage = SummaryCartPage(self.driver)

        productDetailsPage.proceedingToTheSummaryPage(log)
        summaryPage.emptyCart(log)
        emptyMsg = summaryPage.getSummartCartEmptyMsg(log)

        assert emptyMsg.strip() == "Your shopping cart is empty.".strip()
        myAccountPage.signingOut(log)

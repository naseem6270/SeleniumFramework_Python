import pytest

from frameworkstuffs.controller.BaseClass import BaseClass
from frameworkstuffs.utlities.Actions import Actions
from pageObjects.HomePage import HomePage
from pageObjects.MyAccountPage import MyAccountPage
from pageObjects.ProductDetailsPage import ProductDetailsPage
from pageObjects.SummaryCartPage import SummaryCartPage
from testData.TestData import TestData


class TestSearchProduct(BaseClass):

    @pytest.fixture(params=TestData.test_Search_Data)
    def get_search_data(self, request):
        return request.param

    @pytest.fixture(params=TestData.test_Login_Data)
    def get_login_data(self, request):
        return request.param

    @pytest.mark.SearchProduct
    def test_searchProduct(self, get_login_data, get_search_data):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        actions = Actions(self.driver, log)
        actions.launch_url(get_login_data["url"])
        loginpage = homepage.navigateToTheLoginPage(log)
        myAccountPage = loginpage.login(log, get_login_data["emailID"], get_login_data["password"])
        myAccountPage.navigateToTheHomePage(log)
        searchResultPage = homepage.searchProduct(log, get_search_data["itemToBeSearched"])
        searchResultPage.selectItem(log)

    @pytest.mark.SearchProduct
    def test_addingItemToTheCart(self, get_search_data):
        log = self.getLogger()
        actions = Actions(self.driver, log)

        productDetailsPage = ProductDetailsPage(self.driver)
        productDetailsPage.addItemToTheCart(log, get_search_data["size"])
        successtxt = productDetailsPage.getCartSuccessMessage(log)
        assert successtxt.strip() == "Product successfully added to your shopping cart".strip()
        productDetailsPage.proceedingToTheSummaryPage(log)

    @pytest.mark.SearchProduct
    def test_SummaryPage(self):
        log = self.getLogger()
        actions = Actions(self.driver, log)
        myAccountPage = MyAccountPage(self.driver)

        summaryPage = SummaryCartPage(self.driver)
        countMsg = summaryPage.getItemCountMsg(log)
        assert countMsg.strip() == "Your shopping cart contains: 1 product".strip()
        summaryPage.emptyCart(log)
        emptyMsg = summaryPage.getSummartCartEmptyMsg(log)

        assert emptyMsg.strip() == "Your shopping cart is empty.".strip()
        myAccountPage.signingOut(log)

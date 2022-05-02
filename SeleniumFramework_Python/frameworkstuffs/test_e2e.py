from frameworkstuffs.controller.BaseClass import BaseClass
from pageObjects.HomePage import Homepage


class TestOne(BaseClass):

    def test_e2e(self):
        self.driver.get("http://automationpractice.multiformis.com")
        homepage = Homepage(self.driver)

        homepage.login()








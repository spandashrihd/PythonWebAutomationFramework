import time
import pytest
import allure
import selenium
from selenium import webdriver

from tests.pageObjects.page_factory.loginPage_pf import LoginPage
from tests.pageObjects.page_factory.dashboardPage_pf import DashboardPage
from allure_commons.types import AttachmentType
from tests.constants.constants import Constants
import logging

from tests.pageObjects.pom.dashboardPage import DashboardPage


class TestVWOLogin:

    @pytest.mark.usefixtures("setup")
    @pytest.mark.qa
    def test_vwo_login_negative(self, setup):
        try:
            LOGGER = logging.getLogger(__name__)
            driver = setup
            driver.get(Constants.app_url())
            loginPage = LoginPage(driver)
            loginPage.login_to_vwo(user=self.username, pwd="123")
            error_msg_element = loginPage.error_msg()
            LOGGER.info("Negative test done")
            assert error_msg_element == "Your email, password, IP address or location did not match"

            if "Dashboard" not in driver.title:
                Constants.take_screenshot(driver, "test_vwo_login_negative")

        except Exception as e:
            print(e)


    def test_vwo_login_positive(self, setup):
        LOGGER = logging.getLogger(__name__)
        LOGGER.info("Starting the Testcase")
        driver = setup
        driver.get(Constants.app_url())
        loginPage = LoginPage(driver)
        loginPage.login_to_vwo(user=self.username, pwd=self.password)
        dashboard_page = DashboardPage(driver)
        username = dashboard_page.user_logged_in_text()
        assert "Dashboard" in driver.title
        assert "Aman Ji" == username
        time.sleep(5)

    @pytest.mark.usefixtures("setup")
    @pytest.mark.qa
    def test_vwo_login_negative_tc3(self, setup):
        pass

    @pytest.mark.usefixtures("setup")
    @pytest.mark.qa
    def test_vwo_login_negative_tc4(self, setup):
        pass


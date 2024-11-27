import pytest
import allure
import time


from selenium import webdriver
from tests.constants.constants import Constants
from tests.pageObjects.pom.loginPage import LoginPage
from tests.pageObjects.pom.dashboardPage import DashboardPage




# Assertions and use the Page Object class


# Webdriver Start
# User Interaction + Assertions
# Close Webdriver


@pytest.fixture()
def setup():
   driver = webdriver.Chrome()
   driver.maximize_window()
   driver.get(Constants.app_url())
   return driver


@allure.epic("VWO login test")
@allure.feature("TC#0 - VWO app negative test")
@pytest.mark.negative
def test_vwo_login_negative(setup):
   login_page = LoginPage(driver=setup)
   login_page.login_to_vwo(usr="contact+atb7x@thetestingacademy.com", pwd="Wingify@1235")
   time.sleep(2)
   error_message_element = login_page.get_error_msg_text()
   assert error_message_element == "Your email, password, IP address or location did not match"


@allure.epic("VWO login test")
@allure.feature("TC#1 - VWO app positive test")
@pytest.mark.positive
def test_vwo_login_positive(setup):
   login_page = LoginPage(driver=setup)
   login_page.login_to_vwo(usr="contact+atb7x@thetestingacademy.com", pwd="Wingify@1234")
   dashborad_login = DashboardPage(driver=setup)
   assert "Aman Ji" in dashborad_login.get_user_logged_in_text()



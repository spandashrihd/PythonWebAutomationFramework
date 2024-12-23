from allure_commons.types import AttachmentType
import allure
class Constants:
   def __init__(self):
       print("Constants are loaded")


   @staticmethod
   def app_url():
       return "https://app.vwo.com"


   @staticmethod
   def dashboard_url():
       return "https://app.vwo.com/#/dashboard"


   @staticmethod
   def take_screenshot(driver, name):
        allure.attach(driver.get_screenshot_as_png(), name=name,
                      attachment_type=AttachmentType.PNG)
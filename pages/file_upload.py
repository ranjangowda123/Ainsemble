from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.ie.webdriver import WebDriver

from utils.wait_statements import wait_for_click_element,wait_until_not_presence_of_element


class FileUpload:

    def __init__(self,driver:WebDriver):
        self.driver = driver

    upload_file = "Upload File"
    upload_icon = "(//android.widget.TextView[@text='CLICK TO UPLOAD']/preceding-sibling::android.view.ViewGroup)[last()]"
    save_file = "Save File"
    toaster = "//*[contains(@text, 'Asset is getting uploaded')]"


    def click_on_upload_file_button(self):
        wait_for_click_element(self.driver,AppiumBy.ACCESSIBILITY_ID,self.upload_file)

    def click_on_upload_icon(self):
        wait_for_click_element(self.driver,AppiumBy.XPATH,self.upload_icon)

    def click_on_file_upload(self):
        wait_for_click_element(self.driver,AppiumBy.ACCESSIBILITY_ID,self.save_file)

    def wait_for_toaster_disapper(self):
        wait_for_toaster = wait_until_not_presence_of_element(self.driver,AppiumBy.XPATH,self.toaster)
        print("Toaster Message disappeared?:", wait_for_toaster)

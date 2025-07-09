from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import StaleElementReferenceException
from selenium.webdriver.ie.webdriver import WebDriver
from utils.wait_statements import wait_for_click_element, wait_for_presence_of_all_elements


class FilePicker:


    def __init__(self,driver:WebDriver):
        self.driver = driver


    hamburger_button = "Show roots"
    downloads_button = '//android.widget.TextView[@resource-id="android:id/title" and @text="Downloads"]'
    downloads_page = "//android.widget.TextView[@text='Downloads']"


    def click_on_hamburger_button(self):
        wait_for_click_element(self.driver,AppiumBy.ACCESSIBILITY_ID,self.hamburger_button)

    def wait_for_downloads_button(self):
        try:
            wait_for_click_element(self.driver,AppiumBy.XPATH,self.downloads_button)
        except StaleElementReferenceException:
            wait_for_click_element(self.driver,AppiumBy.XPATH,self.downloads_button)

    def wait_for_downlods_page(self):
        wait_for_presence_of_all_elements(self.driver,AppiumBy.XPATH,self.downloads_page)

    def choose_file(self,file_name):
        file_element = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,f'new UiScrollable(new UiSelector().scrollable(true))'
            f'.scrollIntoView(new UiSelector().textContains("{file_name}"))')
        print("File element found. Clicking...")
        file_element.click()
        return file_name
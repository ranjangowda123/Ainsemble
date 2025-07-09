import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException
from selenium.webdriver.ie.webdriver import WebDriver
from utils.wait_statements import wait_for_click_element, wait_for_presence_of_element


class SongboardList:

    def __init__(self,driver:WebDriver):
        self.driver = driver


    songboard_list_plus_icon = " //android.widget.TextView[@text='Showing']/following-sibling::android.view.ViewGroup[3]"
    songboard_list_second_pluse_icon = "//android.widget.TextView[@text='Tap here to start']/following-sibling::android.view.ViewGroup"

    def click_on_songboard_list_plus_icon(self):
        wait_for_click_element(self.driver,AppiumBy.XPATH,self.songboard_list_plus_icon)

    def click_on_songboard_second_plus_icon(self):
        wait_for_click_element(self.driver,AppiumBy.XPATH,self.songboard_list_second_pluse_icon)


    def choose_created_songboards(self,name):
        try:
            sb_list_click = wait_for_presence_of_element(self.driver,AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiScrollable(new UiSelector().scrollable(true))'
                f'.scrollIntoView(new UiSelector().textContains("{name}"))')
            time.sleep(1)
            sb_list_click.click()
        except (AttributeError, TimeoutException):
            print(f"Failed to scroll and click on songboard:{name}")
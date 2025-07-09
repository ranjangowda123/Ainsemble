import random
import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException
from selenium.webdriver.ie.webdriver import WebDriver
from utils.wait_statements import wait_for_click_element, wait_only_for_element, wait_for_presence_of_element


class AssetDetails:


    def __init__(self,driver:WebDriver):
        self.driver = driver

    tick_mark = "//android.widget.TextView[contains(@text, 'Songboard')]/following-sibling::android.view.ViewGroup[1]/android.widget.ImageView"
    sb_name = "android.widget.EditText"
    save_songboard_button =  "Save"

    def click_on_tick_mark(self):
        wait_for_click_element(self.driver,AppiumBy.XPATH,self.tick_mark)

    def songboard_name(self):
        songboardname1 = f"Songboard_{random.randint(1,999)}"
        print("Songboard name is:",songboardname1)
        wait_only_for_element(self.driver,AppiumBy.CLASS_NAME,self.sb_name).send_keys(songboardname1)
        time.sleep(2)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,self.save_songboard_button).click()
        wait_for_click_element(self.driver,AppiumBy.XPATH,f"(//android.widget.TextView[@text='{songboardname1}']/preceding-sibling::android.view.ViewGroup)[3]")
        return songboardname1

    def choose_created_songboard(self,file_names):
        try:
            sb_list_click = wait_for_presence_of_element(self.driver,AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiScrollable(new UiSelector().scrollable(true))'
                f'.scrollIntoView(new UiSelector().textContains("{file_names}"))')
            time.sleep(1)
            sb_list_click.click()
        except (AttributeError,TimeoutException):
            print(f"Failed to scroll and click on songboard:{file_names}")
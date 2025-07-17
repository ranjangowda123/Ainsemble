import random

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver

from utils.wait_statements import wait_for_visibility_of_element


class SaveAiToSongboards:
    def __init__(self,driver:WebDriver):
        self.driver = driver
        self.ai_songboardname = "None"

    download_button = "//android.widget.TextView[@text='Download Lyrics']/following-sibling::android.view.ViewGroup[1]/android.widget.ImageView"
    enter_asset_title = "//android.widget.TextView[@text='Save Asset']/following-sibling::android.widget.EditText"
    songboards_dropdown = "//android.widget.TextView[@text='Save Asset']/following-sibling::android.view.ViewGroup[2]"
    click_on_new_songboard = "new UiSelector().text(\"+ New Song Board\")"
    songboard_name = "android.widget.EditText"
    save_ai_songboard = "Save"
    save_asset = 'Save Asset'


    def click_on_download_button(self):
        wait_for_visibility_of_element(self.driver,AppiumBy.XPATH,self.download_button).click()

    def enter_values_to_asset_title(self):
        assetname = f"Songboard_{random.randint(1, 9999)}"
        print("Songboard name is:", assetname)
        self.driver.find_element(AppiumBy.XPATH,self.enter_asset_title).send_keys(assetname)


    def click_on_songboards_dropdown(self):
        self.driver.find_element(AppiumBy.XPATH,self.songboards_dropdown).click()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,self.click_on_new_songboard).click()

    def save_songboard_from_ai(self):
        self.ai_songboardname = f"Songboard_{random.randint(1, 9999)}"
        print("Songboard name is:", self.save_ai_songboard)
        self.driver.find_element(AppiumBy.CLASS_NAME,self.songboard_name).send_keys(self.ai_songboardname)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,self.save_ai_songboard).click()

    def scroll_available_songboards(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,self.click_on_new_songboard).click()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().className("android.widget.ScrollView"))'
            f'.scrollIntoView(new UiSelector().text("{self.ai_songboardname}"))'
        ).click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,self.save_asset).click()





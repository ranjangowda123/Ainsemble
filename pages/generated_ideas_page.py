from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver

from utils.wait_statements import wait_for_presence_of_element


class GeneratedIdeasPage:
    def __init__(self, driver:WebDriver):
        self.driver = driver


    generated_lyrics_button = "//android.widget.TextView[@text='04:']/following-sibling::android.view.ViewGroup[5]/android.widget.TextView"



    def scroll_generated_ideas(self):
        wait_for_presence_of_element(self.driver,AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().textContains("04:"))')


    def click_on_generate_lyrics(self):
        self.driver.find_element(AppiumBy.XPATH,self.generated_lyrics_button).click()

    # alias, for better readability for one function click on generated lyrics
    click_on_view_lyrics = click_on_generate_lyrics



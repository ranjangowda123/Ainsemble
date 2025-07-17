from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from utils.wait_statements import wait_for_visibility_of_element


class AiModal:

    def __init__(self, driver:WebDriver,data):
        self.driver = driver
        self.data = data


    ai_modal_wait = 'new UiSelector().text("AI Song Idea")'
    enter_prompt = 'new UiSelector().className("android.widget.EditText").instance(0)'
    enter_mood = 'new UiSelector().className("android.widget.EditText").instance(1)'
    ideas = 'Generate Ideas'
    close_ai_button = '//android.widget.TextView[@text="Generate Ideas"]/following-sibling::android.view.ViewGroup[1]'
    exit_ai_session_button = 'Close and Exit AI Session'




    def wait_for_ai_modal(self):
        wait_for_visibility_of_element(self.driver,AppiumBy.ANDROID_UIAUTOMATOR,self.ai_modal_wait)


    def enter_prompt_and_mood(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,self.enter_prompt).send_keys(self.data["prompt"])
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,self.enter_mood).send_keys(self.data["mood"])
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.ideas).click()


    def close_ai_modal(self):
        self.driver.find_element(AppiumBy.XPATH,self.close_ai_button).click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.exit_ai_session_button).click()

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from utils.wait_statements import wait_only_for_element


class SignIn:

    # type hint or type annotation.
    def __init__(self,driver:WebDriver,data):
        self.driver = driver
        self.data = data

    sign_in_button = 'new UiSelector().text("Sign In")'
    email_field = '//android.widget.EditText[@text="Enter Email"]'
    password_field = "//android.widget.TextView[@text='Password']/following-sibling::android.widget.EditText"
    sign_up_button = "Submit"

    def click_on_sign_in_button(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,self.sign_in_button).click()

    def entering_email(self):
        wait_only_for_element(self.driver,AppiumBy.XPATH,self.email_field).send_keys(self.data["email"])

    def entering_password(self):
        self.driver.find_element(AppiumBy.XPATH,self.password_field).send_keys(self.data['password'])

    def click_on_sign_up_button(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,self.sign_up_button).click()
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def biometric(driver):
    try:
        biometric_txt = WebDriverWait(driver,30).until(expected_conditions.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().textContains("Would you like to enable biometric login for future logins?")')))
        if biometric_txt:
            print("Biometric Popup Found")
            driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Skip").click()
        else:
            print("No Buttons Found, Test Failed")
    except Exception as e:
        print("Error type",type(e).__name__)
        print("Error Message:", str(e))
        # driver.save_screenshot("biometric.png")
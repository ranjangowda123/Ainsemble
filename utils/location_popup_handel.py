import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def location_popup(driver):
    try:
        wait_for_popup = WebDriverWait(driver,30).until(expected_conditions.visibility_of_element_located((
            AppiumBy.ID,"com.android.permissioncontroller:id/permission_message")))
        if wait_for_popup:
            print("System Pop up Found")
            allow_button = driver.find_element(AppiumBy.ID,"com.android.permissioncontroller:id/permission_allow_foreground_only_button")
            allow_button.click()
            print("Clicked on While Using the app")
        else:
            print("No permission found continuing the test.")

    except TimeoutException:
        print("Permission popup not found within timeout, continuing the test.")

    except NoSuchElementException:
        print("Popup appeared but expected button not found.")

    except Exception as e:
        print("Error type:", type(e).__name__)
        print("Error Message:", str(e))
        # driver.save_screenshot("location_popup.png")


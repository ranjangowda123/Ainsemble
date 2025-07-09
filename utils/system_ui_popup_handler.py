from appium.webdriver.common.appiumby import AppiumBy


def handle_system_popup(driver, popup_name=""):
    try:
        alert_titles = driver.find_elements(AppiumBy.ID, "android:id/alertTitle")
        if alert_titles:
            print(f"{popup_name} popup detected:", alert_titles[0].text)
            driver.find_element(AppiumBy.ID, "android:id/aerr_close").click()
            print("Clicked to close the popup.")
        else:
            print(f"No {popup_name} popup found. Continuing test.")
    except Exception as e:
        print("Error type:", type(e).__name__)
        print("Error Message:", str(e))


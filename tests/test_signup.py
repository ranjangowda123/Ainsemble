# import requests
#
# from appium.webdriver.common.appiumby import AppiumBy
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
# from utils.get_dynamic_email import get_email
#
# def test_signup(driver):  # pytest knows to run the driver fixture first and give you the driver object to use inside your test.
#     # WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((
#     #     AppiumBy.ID,"com.android.permissioncontroller:id/permission_allow_foreground_only_button"))).click()
#     WebDriverWait(driver,30).until(expected_conditions.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Sign In")'))).click()
#     number = get_email()
#     email = f"ranjangowda246+{number}@gamil.com"
#     print(f"Email is:{email}")
#     driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Enter Email")').send_keys(email)
#
#
#     # WebDriverWait(driver,30).until(expected_conditions.element_to_be_clickable((
#     #     AppiumBy.ID,"com.android.permissioncontroller:id/permission_allow_one_time_button"))).click()
#     # WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((
#     #     AppiumBy.CLASS_NAME,"android.widget.EditText"))).send_keys(email)
#     # driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Submit").click()
#     # url = "http://20.55.0.20:8000/api/users/signup/"
#     # payload = {
#     # "email": email,
#     # "device": {
#     #     "device_id": "1111111111111111",
#     #     "latitude": "12321313",
#     #     "longitude": "1232131",
#     #     "operating_system": "android 14",
#     #     "os_version": "12312"
#     # }}
#     # response = requests.post(url,json=payload)
#     # print("..........",response.json())
#     # otp = response.json().get("otp")
#     # print(f"OTP is {otp}")
#     # WebDriverWait(driver,30).until(expected_conditions.visibility_of_element_located((
#     #     AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Didn\'t Receive OTP ?")')))
#     # otp_boxes = WebDriverWait(driver, 30).until(expected_conditions.visibility_of_all_elements_located((
#     #     AppiumBy.CLASS_NAME, "android.widget.EditText")))
#     # for box, digit in zip(otp_boxes, otp):
#     #     box.send_keys(digit)
#     # # driver.press_keycode(66)
#     # driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Submit").click()
#     # for i in range(2):
#     #     driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.EditText").instance(i)').send_keys("Ranjangowda@246")
#     # driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Save & Continue").click()
#

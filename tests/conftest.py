import os
import shutil
import subprocess
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
import allure
from datetime import datetime
from applitools.selenium import Eyes


@pytest.fixture(scope="function")     # To start the Appium driver before each test and close it after.
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.platform_version = "15"
    options.device_name = "emulator-5554"
    # adb shell dumpsys window | findstr "mCurrentFocus"
    # This will give both app package and app activity
    options.app_package = "com.raiseforart.ainsemble"
    options.app_activity = "com.raiseforart.ainsemble.MainActivity"
    # Don’t reset the app — just open it as-is without reinstalling or clearing data.
    options.no_reset = False
    options.automation_name = "UiAutomator2"
    # Automatically grants app permissions at install time.
    options.auto_grant_permissions = True
    # Keep session alive for 5 mins if idle
    options.new_command_timeout = 300



    driver = webdriver.Remote("http://127.0.0.1:4723" , options=options)
    # appium --log-level debug --log-timestamp

    yield driver
    # driver.quit()



# Capture Screenshots Automatically on Failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"Failure Screenshot - {time_stamp}",
                attachment_type=allure.attachment_type.PNG)


# Delete previous allure report

def pytest_sessionstart(session):
    print("Cleaning allure-report folder before starting tests...")
    # 	Tells Python: we’re targeting the allure-report/ folder.
    report_dir = "allure-report"
    # Checks if that folder exists locally.
    if os.path.exists(report_dir):
        # If yes → it deletes the entire folder and its contents recursively.
        shutil.rmtree(report_dir)

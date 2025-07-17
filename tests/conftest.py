import json
import os
import shutil
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
import allure
from datetime import datetime


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


# Delete previous Allure report and add environment.properties
def pytest_sessionstart(session):
    print("Cleaning allure-results folder before starting tests...")
    report_dir = "allure-results"

    if os.path.exists(report_dir):
        shutil.rmtree(report_dir)
        print("Previous Allure report deleted.")

    os.makedirs(report_dir, exist_ok=True)
    print("New Allure report created.")

    # Add environment.properties
    env_file = os.path.join(report_dir, "environment.properties")
    with open(env_file, "w") as f:
        f.write("Browser=Chrome\n")
        f.write("Environment=Dev\n")
        f.write("Platform=Android\n")
        f.write("Teseter=Ranjan\n")
    print("environment.properties created.")

    # Create categories.json
    categories =[
  {
    "name": "Element Not Found",
    "matchedStatuses": ["failed"],
    "messageRegex": ".*NoSuchElementException.*"
  },
  {
    "name": "Timeout Error",
    "matchedStatuses": ["failed"],
    "messageRegex": ".*TimeoutException.*"
  },
  {
    "name": "Assertion Failure",
    "matchedStatuses": ["failed"],
    "messageRegex": ".*AssertionError.*"
  },
  {
    "name": "Invalid Selector",
    "matchedStatuses": ["failed"],
    "messageRegex": ".*InvalidSelectorException.*"
  },
  {
    "name": "Session Error",
    "matchedStatuses": ["failed"],
    "messageRegex": ".*SessionNotCreatedException.*"
  },
  {
    "name": "Stale Element",
    "matchedStatuses": ["failed"],
    "messageRegex": ".*StaleElementReferenceException.*"
  },
  {
    "name": "Element Not Interactable",
    "matchedStatuses": ["failed"],
    "messageRegex": ".*ElementNotInteractableException.*"
  },
  {
    "name": "Index Error",
    "matchedStatuses": ["failed"],
    "messageRegex": ".*IndexError.*"
  },
  {
    "name": "Key Error",
    "matchedStatuses": ["failed"],
    "messageRegex": ".*KeyError.*"
  },
  {
    "name": "Value Error",
    "matchedStatuses": ["failed"],
    "messageRegex": ".*ValueError.*"
  },
  {
    "name": "Connection Error",
    "matchedStatuses": ["failed"],
    "messageRegex": ".*ConnectionRefusedError.*"
  },
  {
    "name": "Broken Test",
    "matchedStatuses": ["broken"]
  },
  {
    "name": "Unexpected Alert",
    "matchedStatuses": ["failed"],
    "messageRegex": ".*UnexpectedAlertPresentException.*"
  },
  {
    "name": "Generic Failure",
    "matchedStatuses": ["failed"]
  }
]
    categories_file = os.path.join(report_dir, "categories.json")
    with open(categories_file, "w") as f:
        json.dump(categories, f, indent=4)
    print("categories.json created.")

    # Executor for allure
    executor_data = {
        "name": "LocalRun",
        "type": "python",
        "buildName": "Mobile Automation Test",
        "reportUrl": "http://localhost:5050/allure",
        "buildOrder": 1
    }

    with open("allure-results/executor.json", "w") as f:
        json.dump(executor_data, f, indent=2)

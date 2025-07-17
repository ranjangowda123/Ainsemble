import json
import os
import time

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from pages.ai_idea_modal_page import AiModal
from pages.generated_ideas_page import GeneratedIdeasPage
from pages.save_ai_to_songboards import SaveAiToSongboards
from pages.sign_in_page import SignIn
from pages.songboard_list_page import SongboardList
from utils.enable_biometric import biometric
from utils.location_popup_handel import location_popup
from utils.system_ui_popup_handler import handle_system_popup

json_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'test_data', 'test_data.json'))
with open(json_path,encoding='utf-8') as f:  # ensures your file is read safely, even if it contains special characters.
    data = json.load(f)

def test_ai_songboard_creation(driver):
    with allure.step("Attach test input data"):
        allure.attach(json.dumps(data, indent=2), name="Test Data", attachment_type=allure.attachment_type.JSON)
    with allure.step("Handle all system popups"):
        # Handle Bluetooth permission system popup
        handle_system_popup(driver, "Bluetooth Warning")
        # Handle System UI permission system popup
        handle_system_popup(driver, "App Crash")
        # Handle Location popup
        location_popup(driver)
    with allure.step("Sign in using email and password"):
        # Clicking on Sign in button to sing up for existing user
        sign_in_page = SignIn(driver, data)
        sign_in_page.click_on_sign_in_button()
        # Entering user Email to email field
        sign_in_page.entering_email()
        # Entering user Password to password field
        sign_in_page.entering_password()
        # Clicking on submit button for login
        sign_in_page.click_on_sign_up_button()
        # Checking for enabling of Biometirc
    with allure.step("Enable biometric if asked"):
        biometric(driver)
    songboard_list = SongboardList(driver)
    songboard_list.click_on_songboard_list_ai_icon()
    ai_modal = AiModal(driver,data)
    ai_modal.wait_for_ai_modal()
    ai_modal.enter_prompt_and_mood()
    generated_ideas_page = GeneratedIdeasPage(driver)
    generated_ideas_page.scroll_generated_ideas()
    generated_ideas_page.click_on_generate_lyrics()
    generated_ideas_page.click_on_view_lyrics()
    save_ai_to_songboards = SaveAiToSongboards(driver)
    save_ai_to_songboards.click_on_download_button()
    save_ai_to_songboards.click_on_songboards_dropdown()
    save_ai_to_songboards.save_songboard_from_ai()
    save_ai_to_songboards.enter_values_to_asset_title()
    save_ai_to_songboards.scroll_available_songboards()
    generated_ideas_page.scroll_generated_ideas()
    element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Downloaded")')
    print(element.text)
    assert element.text == "Downloaded"
    ai_modal.close_ai_modal()
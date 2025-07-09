import os
import random
import time
import json
import allure

from pages.asset_details import AssetDetails
from pages.file_picker import FilePicker
from pages.file_upload import FileUpload
from pages.sign_in_page import SignIn
from pages.songboard_list_page import SongboardList
from utils.enable_biometric import biometric
from utils.location_popup_handel import location_popup
from utils.system_ui_popup_handler import handle_system_popup

json_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'test_data', 'test_data.json'))
with open(json_path,encoding='utf-8') as f:  # ensures your file is read safely, even if it contains special characters.
    data = json.load(f)

@allure.epic("Asset Management")
@allure.feature("Asset Creation")
@allure.story("Upload file to new songboard")
# @allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create new songboard and upload file")
@allure.description("This test logs in, navigates to songboard, and uploads a file. It validates that the flow works without crashes.")
def test_asset_creation(driver):
    # Attaches (test_data.json) as a downloadable section in the Allure report.
    # we can see exactly which email, password, filename, or any other test data was used in that test run — without opening any external files.
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
        sign_in_page  = SignIn(driver,data)
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
    with allure.step("Navigate to new songboard creation"):
        # clicking on plus icon in songboard list screen
        songboardlist = SongboardList(driver)
        songboardlist.click_on_songboard_list_plus_icon()
        # click on plus icon in empty songboard screen
        songboardlist.click_on_songboard_second_plus_icon()
    with allure.step("Start uploading file"):
        # click on file upload button from pluse icon
        fileupload = FileUpload(driver)
        fileupload.click_on_upload_file_button()
        # click on file upload icon
        fileupload.click_on_upload_icon()
    with allure.step("Choose file from Downloads"):
        # click on hamburger button
        filepicker = FilePicker(driver)
        filepicker.click_on_hamburger_button()
        # Waits for downloads button
        filepicker.wait_for_downloads_button()
        # waits for downloads page
        filepicker.wait_for_downlods_page()
        # choose file from the downloads page
        file_names = filepicker.choose_file(data["filename"])
    with allure.step("Upload File"):
        # Clicking on File Upload Save File Button
        fileupload.click_on_file_upload()
        # waits for toaster to disapper
        fileupload.wait_for_toaster_disapper()
    with allure.step("Saving Songbaord name"):
        save_sb = AssetDetails(driver)
        # click on tick mark to enter file name
        save_sb.click_on_tick_mark()
        # Save songboard details
        name = save_sb.songboard_name()
    with allure.step(f"Scroll and select songboard: {name})"):
        songboardlist.choose_created_songboards(name)
    with allure.step(f"Scroll and view created songboard: {name})"):
        save_sb.choose_created_songboard(file_names)


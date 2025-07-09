from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def wait_for_click_element(driver, by, locator, timeout=30):
    WebDriverWait(driver, timeout).until(expected_conditions.element_to_be_clickable((by, locator))).click()

def wait_only_for_element(driver, by, locator, timeout=30):
    return WebDriverWait(driver, timeout).until(expected_conditions.element_to_be_clickable((by, locator)))

def wait_for_presence_of_all_elements(driver,by,locator,timeout=30):
    WebDriverWait(driver, timeout).until(expected_conditions.presence_of_all_elements_located((by,locator)))

def wait_until_not_presence_of_element(driver,by,locator,timeout=30):
    return WebDriverWait(driver, timeout).until_not(expected_conditions.presence_of_element_located((by,locator)))

def wait_for_presence_of_element(driver,by,locator,timeout=30):
    return WebDriverWait(driver, timeout).until(expected_conditions.presence_of_element_located((by,locator)))
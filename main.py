from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from secrets import *
import time


driver = webdriver.Chrome()


def is_global_exist() -> bool:
    try:
        driver.find_element(By.CSS_SELECTOR, 'button[class ="c1p6lbu0 W(100%)"]')
        return True
    except NoSuchElementException:
        return False


def click_global():
    driver.find_element(By.CSS_SELECTOR, 'button[class ="c1p6lbu0 W(100%)"]').click()
    return None


driver.get("https://facebook.com/")
time.sleep(0.5)
facebook_email = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys(FACEBOOK_EMAIL)
facebook_pass = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')
facebook_pass_input = facebook_pass.send_keys(FACEBOOK_PASSWORD)
facebook_pass_enter = facebook_pass.send_keys(Keys.ENTER)
time.sleep(1)
ActionChains(driver).send_keys(Keys.ESCAPE).perform()

driver.get("https://tinder.com/app/recs")
time.sleep(5)
# sing_in_click
driver.find_element(By.CSS_SELECTOR, 'a[style^="--tui-button-background:var"]').click()
time.sleep(5)
# facebook signup click
driver.find_element(By.CSS_SELECTOR, 'div[class="W(100%) CenterAlign Py(8px) Typs(button-1)"]').click()
time.sleep(5)
#allow_click
driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Allow"]').click()
time.sleep(5)
# enable_click
driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Enable"]').click()
time.sleep(2)
ActionChains(driver).send_keys(Keys.ESCAPE).perform()
time.sleep(4)
ActionChains(driver).send_keys(Keys.ESCAPE).perform()

while True:
    if is_global_exist():
        click_global()
    ActionChains(driver).send_keys(Keys.LEFT).perform()
    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def find_item_by_name(items, item_name):
    return next((i for i in items if item_name in i.name), None)


def wait_for_visibility_of_element_css(driver, css, time_to_wait=6):
        try:
            element = WebDriverWait(driver, time_to_wait).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))
        except TimeoutException:
            element = False
        return element


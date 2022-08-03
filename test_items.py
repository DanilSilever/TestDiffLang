from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_add_button(browser):
    button = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#add_to_basket_form>button.btn-add-to-basket"))
    )
    time.sleep(5)
    assert button, "Didn't find add to basket button"

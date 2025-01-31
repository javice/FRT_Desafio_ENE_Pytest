# pages/main_page.py
# Clase MainPage para interactuar con la página principal
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://jxcehanp1uulmfid.vercel.app/?utm_source=podia&utm_medium=broadcast&utm_campaign=2279334'
        self.dropdown_locator = (By.CSS_SELECTOR, 'button[role="combobox"]')
        self.option_locator_template = '#{} [role="option"]'
        self.popup_locator = (By.XPATH, '//*[@id="radix-:R3jsq:"]')
        self.close_button_locator = (By.XPATH, '//*[@id="radix-:R3jsq:"]/div[2]/button')

    def open(self):
        self.driver.get(self.url)

    def get_dropdowns(self):
        return self.driver.find_elements(*self.dropdown_locator)

    def get_dropdown_options(self, aria_controls):
        return self.driver.find_elements(By.CSS_SELECTOR, self.option_locator_template.format(aria_controls.replace(":", "\\:")))

    def get_popup(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.popup_locator))

    def close_popup(self):
        self.driver.find_element(*self.close_button_locator).click()
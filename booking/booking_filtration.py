import time

from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_star_rating(self, *star_values):
        self.driver.execute_script("window.scrollTo(0, 2000)")
        time.sleep(3)
        try:
            dismiss_button = self.driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]')
            dismiss_button.click()
            time.sleep(3)
            star_filtration_box = self.driver.find_element(By.ID, "filter_group_class_:r26:")
            star_child_elements = star_filtration_box.find_elements(By.CSS_SELECTOR, "*")

            for star_value in star_values:
                for star_child_element in star_child_elements:
                    if star_child_element.get_attribute('data-filters-item') == f'class:class="{star_value}"':
                        star_child_element.click()


        except NoSuchElementException:
            star_filtration_box = self.driver.find_element(By.ID, "filter_group_class_:r26:")
            star_child_elements = star_filtration_box.find_elements(By.CSS_SELECTOR, "*")

            for star_value in star_values:
                for star_child_element in star_child_elements:
                    if star_child_element.get_attribute('data-filters-item') == f'class:class="{star_value}"':
                        star_child_element.click()

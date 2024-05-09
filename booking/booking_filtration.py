from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_star_rating(self):
        # scroll down before finding
        star_filtration_box = self.driver.find_element(By.ID, "filter_group_class_:rs:")
        star_child_elements = star_filtration_box.find_elements(By.CSS_SELECTOR, "*")

        for star_child_element in star_child_elements:
            if star_child_element.get_attribute('data-filters-item') == "class:class=1":
                star_child_element.click()
                break
            else:
                print(star_child_element.get_attribute('innerHTML'))



from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_star_rating(self):
        star_filtration_box = self.driver.find_element(By.ID, "filter_group_price_:rg:")
        star_child_elements = star_filtration_box.find_elements(By.CSS_SELECTOR, "*")
        print(len(star_child_elements))

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import booking.constands as const
from booking.booking_filtration import BookingFiltration


class Booking():
    def __init__(self, teardown=False):  # we can handle __exit__ function with teardown boolean
        self.teardown = teardown

    def __enter__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        self.driver = driver
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):  # double underscore function run in the end, because of "WITH" in main file
        if self.teardown:
            self.driver.quit()

    def land_first_page(self):
        self.driver.get(const.BASE_URL)

    def change_currency(self, currencyType):
        currency_element = self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='Prices in Sri Lankan Rupee']")
        currency_element.click()
        select_currency = self.driver.find_element(By.XPATH, f"(//div[contains(@class,'ea1163d21f')][normalize-space()='{currencyType}'])[1]")
        select_currency.click()

    def select_place_to_go(self, place_to_go):
        search_filed = self.driver.find_element(By.ID, ":re:")
        search_filed.click()
        search_filed.send_keys(place_to_go)

        first_result = self.driver.find_element(By.ID, "autocomplete-result-0")
        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.driver.find_element(By.CSS_SELECTOR, f'span[data-date="{check_in_date}"]')
        check_in_element.click()

        check_out_element = self.driver.find_element(By.CSS_SELECTOR, f'span[data-date="{check_out_date}"]')
        check_out_element.click()

    def select_adults(self, count):
        selection_element = self.driver.find_element(By.CSS_SELECTOR, 'button[aria-controls=":rf:"]')
        selection_element.click()
        decrease_btn = self.driver.find_element(By.XPATH, '//*[@id=":rf:"]/div/div[1]/div[2]/button[1]')
        while True:
            if decrease_btn.is_enabled():
                decrease_btn.click()
            else:
                break

        int_count = int(count)
        for i in range(int_count-1):
            increase_btn = self.driver.find_element(By.XPATH, '//*[@id=":rf:"]/div/div[1]/div[2]/button[2]')
            increase_btn.click()

        done_btn = self.driver.find_element(By.XPATH, '//*[@id=":rf:"]/button')
        done_btn.click()

    def click_search(self):
        search_btn = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        search_btn.click()

    def apply_filtration(self):
        filtration = BookingFiltration(driver=self.driver)
        filtration.apply_star_rating(2, 3, 4)
        filtration.low_to_high()
















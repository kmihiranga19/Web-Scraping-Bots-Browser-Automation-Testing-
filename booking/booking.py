from selenium import webdriver
import booking.constands as const


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

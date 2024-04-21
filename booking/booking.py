from selenium import webdriver
import booking.constands as const


class Booking(webdriver.Chrome):
    def __init__(self, driver=webdriver.Chrome()):
        self.driver = driver
        super(Booking, self).__init__()

    def land_first_page(self):
        self.get(const.BASE_URL)

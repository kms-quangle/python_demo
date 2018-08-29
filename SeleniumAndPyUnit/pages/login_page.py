from locators.locator_generator import LocatorGenerator
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self):
        print('LoginPage')
        locator_generator = LocatorGenerator()
        self.locator = locator_generator.get_locator(type(self).__name__)
        print(type(self.locator).__name__)


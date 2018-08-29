from locators.login_page_locator import LoginPageLocator


class LocatorGenerator:

    pageList = ["LoginPage"]

    def __init__(self):
        print('LocatorGenerator')

    def get_locator(self, classname):
        if classname in self.pageList:
            if classname == "LoginPage":
                return LoginPageLocator()



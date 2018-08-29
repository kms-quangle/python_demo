from custom.driver.chrome_driver_services import ChromeDriverManager


class DriverManager:
    driverListServices = ["ChromeDriverManager", "FirefoxDriverManager"]

    def get_driver(self, classname):
        if classname in self.driverListServices:
            if classname == 'ChromeDriverManager':
                return ChromeDriverManager()
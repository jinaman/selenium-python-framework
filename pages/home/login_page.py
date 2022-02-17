from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time
from base.basepage import BasePage

class LoginPage(BasePage):          #Al pasarle la clase SeleniumDriver para que herede, luego le tengo que pasar el driver con: super().__init__(driver)

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)         #Llamo al metodo init de la super clase (Seleniumdriver) y le paso el driver.
        self.driver = driver

    # Locators
    _login_xpath = "//a[contains(text(),'Sign In')]"
    _email_field = "email"
    _password_field = "password"
    _login_button = "//input[@value='Login']"

    def clickLoginLink(self):
        self.elementClick(self._login_xpath, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)       #No hace falta pasarle el locator type porque por default es ID, si lo puedo cambiar si quiero.

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, email="", password=""):      #Le pongo argumentos vacios por default. La funcio va a funcionar bien, y si no l pongo nada dejara vacio ese lugar.
        self.clickLoginLink()
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        time.sleep(3)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//h1[contains(text(),'My Courses')]",
                                       locatorType="xpath")                                          #("//*[@id='navbar']//span[text()='User Settings']", locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//span[contains(text(),'Your username or password is invalid. Please try again')]",
                                       locatorType="xpath")
        return result

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()

    def verifyLoginTitle(self):
        time.sleep(5)
        return self.verifyPageTitle("My Courses")

        # if "zzz" in self.getTitle():
        #     return True
        # else:
        #     return False

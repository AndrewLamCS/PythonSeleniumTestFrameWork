from selenium.webdriver.common.by import By
from pageObjects.ShopPage import ShopPage

class HomePage:
    """
    Page Object Model for the Home Page in the application.
    Provides methods to interact with elements on the Home Page.
    """

    def __init__(self, driver):
        """
        Initializes the HomePage object.

        Args:
            driver: The WebDriver instance used to interact with the browser.
        """
        self.driver = driver

    # Locators for elements on the Home Page
    shop = (By.CSS_SELECTOR, "a[href='/angularpractice/shop']")  # Locator for the 'Shop' link

    def shopItems(self):
        """

        """
        self.driver.find_element(*HomePage.shop).click()
        shopPage = ShopPage(self.driver)
        return shopPage
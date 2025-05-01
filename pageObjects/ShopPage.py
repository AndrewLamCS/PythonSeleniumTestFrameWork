from selenium.webdriver.common.by import By
from pageObjects.ConfirmPage import ConfirmPage

class ShopPage:
    """
    Page Object Model for the Shop Page in the application.
    Provides methods to interact with elements on the Shop Page.
    """

    def __init__(self, driver):
        """
        Initializes the ShopPage object.

        Args:
            driver: The WebDriver instance used to interact with the browser.
        """
        self.driver = driver

    # Locators for elements on the Shop Page
    cardTitle = (By.CSS_SELECTOR, ".card-title a")  # Locator for the titles of the product cards
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")  # Locator for the 'Add to Cart' buttons in the product cards
    shopCheckout = (By.XPATH, "//a[@class='nav-link btn btn-primary']")  # Locator for the shop checkout button in the navigation bar
    cartCheckout = (By.XPATH, "//button[@class='btn btn-success']")  # Locator for the cart checkout button

    def getCardTitles(self):
        """
        Gets all product card title elements.

        Returns:
            list[WebElement]: A list of WebElements representing the product card titles.
        """
        return self.driver.find_elements(*ShopPage.cardTitle)
    
    def getCardFooter(self):
        """
        Gets all 'Add to Cart' button elements in the product cards.

        Returns:
            list[WebElement]: A list of WebElements representing the 'Add to Cart' buttons.
        """
        return self.driver.find_elements(*ShopPage.cardFooter)
    
    def shopCheckoutItems(self):
        """
        Clicks the shop checkout button element in the navigation bar and navigates to the confirmation page.
        
        Returns:
            ConfirmPage: An instance of the ConfirmPage class initialized with the current driver.
        """
        self.driver.find_element(*ShopPage.shopCheckout).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage


    def cartCheckoutItems(self):
        """
        Gets the cart checkout button element.

        Returns:
            WebElement: The cart checkout button element.
        """
        return self.driver.find_element(*ShopPage.cartCheckout)
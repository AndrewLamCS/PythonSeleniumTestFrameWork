import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class BaseClass:
    
    def verifyLinkPresence(self, text):
        """
        Waits for the presence of a link with the specified text on the web page.

        Args:
            text (str): The visible text of the link to wait for.

        Returns:
            WebElement: The web element representing the link if found within the timeout.

        Raises:
            TimeoutException: If the link with the specified text is not found within the timeout period.
        """
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, text)))
    
    def selectOptionByText(self, locator, text):
        """
        Selects an option from a dropdown menu by its visible text.

        Args:
            locator (tuple): The locator for the dropdown element.
            text (str): The visible text of the option to select.
        """
        select = Select(locator)
        select.select_by_visible_text(text)

from tests.acceptance.locators.home_page import HomePageLocators
from tests.acceptance.page_model.base_page import BasePage


class HomePage(BasePage):
    @property #Just a Python thing, it has nothing to do with Selenium
    def url(self):
        return super(HomePage, self).url + '/'

    @property
    def blog_link(self):
        return self.driver.find_element(*HomePageLocators.NAVIGATION_LINK)
from moonrise import Moonrise
from Barnivore_Methods import BarnivoreMethods
from Barnivore_Elements import *


class BarnivoreTests(BarnivoreMethods):

    Moonrise.default_timeout = 5

    def suite_setup(self):
        self.open_browser("chrome", "--headless", "--no-sandbox")
        # self.open_browser("chrome", record_test=False)
        self.moon_driver.maximize_window()
        return super().suite_setup()
    
    def suite_teardown(self):
        self.cleanup_browser()
        return super().suite_teardown()
    
    
class SmokeSuite(BarnivoreTests):

    def test_setup(self):
        self.navigate_to_page("barnivore.com")
        self.verify_page_headers_present()
        self.verify_search_bar_present()
        return super().test_setup()

    @Moonrise.test
    def beer_page(self):
        self.click_element(f"link:{BeerPageElements.header_title}")
        self.main_page_is_loaded(BeerPageElements.header_title)
        self.filter_widget_checks(BeerPageElements.header_title)

    @Moonrise.test
    def cider_page(self):
        self.click_element(f"link:{CiderPageElements.header_title}")
        self.main_page_is_loaded(CiderPageElements.header_title)
        self.filter_widget_checks(CiderPageElements.header_title)

    @Moonrise.test
    def wine_page(self):
        self.click_element(f"link:{WinePageElements.header_title}")
        self.main_page_is_loaded(WinePageElements.header_title)
        self.filter_widget_checks(WinePageElements.header_title)

    @Moonrise.test
    def liquor_page(self):
        self.click_element(f"link:{LiquorPageElements.header_title}")
        self.main_page_is_loaded(LiquorPageElements.header_title)
        self.filter_widget_checks(LiquorPageElements.header_title)
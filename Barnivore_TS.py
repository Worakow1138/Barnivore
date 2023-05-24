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
        beer_page = BeerPageElements()
        self.click_element(f"link:{beer_page.header_title}")
        self.main_page_is_loaded(beer_page.header_title)
        self.filter_widget_checks(beer_page.filter_widget)

    @Moonrise.test
    def cider_page(self):
        cider_page = CiderPageElements()
        self.click_element(f"link:{cider_page.header_title}")
        self.main_page_is_loaded(cider_page.header_title)
        self.filter_widget_checks(cider_page.filter_widget)

    @Moonrise.test
    def wine_page(self):
        wine_page = WinePageElements()
        self.click_element(f"link:{wine_page.header_title}")
        self.main_page_is_loaded(wine_page.header_title)
        self.filter_widget_checks(wine_page.filter_widget)

    @Moonrise.test
    def liquor_page(self):
        liquor_page = LiquorPageElements()
        self.click_element(f"link:{liquor_page.header_title}")
        self.main_page_is_loaded(liquor_page.header_title)
        self.filter_widget_checks(liquor_page.filter_widget)
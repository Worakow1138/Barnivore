from moonrise import Moonrise
from Barnivore_Methods import BarnivoreMethods


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
        self.select_page_link("Beer")
        assert self.get_url() == "https://www.barnivore.com/beer"
        self.beer_filter_widget_present()

    @Moonrise.test
    def cider_page(self):
        self.select_page_link("Cider")
        assert self.get_url() == "https://www.barnivore.com/cider"
        self.cider_filter_widget_present()

    @Moonrise.test
    def wine_page(self):
        self.select_page_link("Wine")
        assert self.get_url() == "https://www.barnivore.com/wine"
        self.wine_filter_widget_present()

    @Moonrise.test
    def liquor_page(self):
        self.select_page_link("Liquor")
        assert self.get_url() == "https://www.barnivore.com/liquor"
        self.liquor_filter_widget_present()
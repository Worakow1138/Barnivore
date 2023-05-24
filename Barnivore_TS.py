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
        self.select_page_link(BarnivoreTests.beer_label)
        assert self.get_url() == "https://www.barnivore.com/beer"
        self.filter_widget_checks(BarnivoreMethods.beer_label)

    @Moonrise.test
    def cider_page(self):
        self.select_page_link(BarnivoreMethods.cider_label)
        assert self.get_url() == "https://www.barnivore.com/cider"
        self.filter_widget_checks(BarnivoreMethods.cider_label)

    @Moonrise.test
    def wine_page(self):
        self.select_page_link(BarnivoreMethods.wine_label)
        assert self.get_url() == "https://www.barnivore.com/wine"
        self.filter_widget_checks(BarnivoreMethods.wine_label)

    @Moonrise.test
    def liquor_page(self):
        self.select_page_link(BarnivoreMethods.liquor_label)
        assert self.get_url() == "https://www.barnivore.com/liquor"
        self.filter_widget_checks(BarnivoreMethods.liquor_label)
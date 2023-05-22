from moonrise import Moonrise
from Barnivore_Methods import BarnivoreMethods


class BarnivoreTests(BarnivoreMethods):

    Moonrise.default_timeout = 5

    def suite_setup(self):
        self.open_browser("chrome", "--headless", "--no-sandbox")
        self.moon_driver.maximize_window()
        return super().suite_setup()
    
    def suite_teardown(self):
        self.cleanup_browser()
        return super().suite_teardown()
    
    def test_setup(self):
        self.navigate_to_page("barnivore.com")
        return super().test_setup()
    
class HeaderSuite(BarnivoreTests):

    @Moonrise.test
    def beer_header(self):
        self.select_header_link("Beer")
        assert self.get_url() == "https://www.barnivore.com/beer"
        self.beer_filter_widget_present()

    @Moonrise.test
    def cider_header(self):
        self.select_header_link("Cider")
        assert self.get_url() == "https://www.barnivore.com/cider"
        self.cider_filter_widget_present()

    @Moonrise.test
    def wine_header(self):
        self.select_header_link("Wine")
        assert self.get_url() == "https://www.barnivore.com/wine"
        self.wine_filter_widget_present()

    @Moonrise.test
    def liquor_header(self):
        self.select_header_link("Liquor")
        assert self.get_url() == "https://www.barnivore.com/liquor"
        self.liquor_filter_widget_present()
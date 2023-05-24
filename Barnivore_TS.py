from moonrise import Moonrise
from Barnivore_Methods import BarnivoreMethods
from Barnivore_Elements import *


class BarnivoreTests(BarnivoreMethods):

    Moonrise.default_timeout = 5

    def suite_setup(self):
        self.open_browser("chrome", "--headless", "--no-sandbox")
        # self.open_browser("chrome", persist=True)
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
        page_to_test = BeerPageElements()
        self.click_element(f"link:{page_to_test.header_title}")
        self.main_page_is_loaded(page_to_test)
        self.filter_widget_checks(page_to_test.filter_widget)
        self.footer_checks()

    @Moonrise.test
    def cider_page(self):
        page_to_test = CiderPageElements()
        self.click_element(f"link:{page_to_test.header_title}")
        self.main_page_is_loaded(page_to_test)
        self.filter_widget_checks(page_to_test.filter_widget)
        self.footer_checks()

    @Moonrise.test
    def wine_page(self):
        page_to_test = WinePageElements()
        self.click_element(f"link:{page_to_test.header_title}")
        self.main_page_is_loaded(page_to_test)
        self.filter_widget_checks(page_to_test.filter_widget)
        self.footer_checks()

    @Moonrise.test
    def liquor_page(self):
        page_to_test = LiquorPageElements()
        self.click_element(f"link:{page_to_test.header_title}")
        self.main_page_is_loaded(page_to_test)
        self.filter_widget_checks(page_to_test.filter_widget)
        self.footer_checks()

    @Moonrise.test
    def ask_a_company_page(self):
        page_to_test = AskACompanyElements()
        self.click_element(f"link:{page_to_test.header_title}")
        self.main_page_is_loaded(page_to_test)
        self.footer_checks()

    @Moonrise.test
    def mobile_apps_test(self):
        page_to_test = AskACompanyElements()
        self.click_element(f"link:{page_to_test.header_title}")
        self.main_page_is_loaded(page_to_test)
        self.footer_checks()

    @Moonrise.test
    def contact_test(self):
        page_to_test = AskACompanyElements()
        self.click_element(f"link:{page_to_test.header_title}")
        self.main_page_is_loaded(page_to_test)
        self.footer_checks()

    @Moonrise.test
    def faq_test(self):
        page_to_test = AskACompanyElements()
        self.click_element(f"link:{page_to_test.header_title}")
        self.main_page_is_loaded(page_to_test)
        self.footer_checks()
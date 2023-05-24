from moonrise import Moonrise
from Barnivore_Test_Steps import BarnivoreTestSteps
from Barnivore_Elements import *


class BarnivoreTests(BarnivoreTestSteps):

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
        page_to_test = BeerPage()
        self.click_element(f"link:{page_to_test.header_title}")
        self.main_page_is_loaded(page_to_test)
        self.filter_widget_checks(page_to_test.filter_widget)
        self.footer_checks()

    @Moonrise.test
    def cider_page(self):
        page_to_test = CiderPage()
        self.click_element(f"link:{page_to_test.header_title}")
        self.main_page_is_loaded(page_to_test)
        self.filter_widget_checks(page_to_test.filter_widget)
        self.footer_checks()

    @Moonrise.test
    def wine_page(self):
        page_to_test = WinePage()
        self.click_element(f"link:{page_to_test.header_title}")
        self.main_page_is_loaded(page_to_test)
        self.filter_widget_checks(page_to_test.filter_widget)
        self.footer_checks()

    @Moonrise.test
    def liquor_page(self):
        page_to_test = LiquorPage()
        self.click_element(f"link:{page_to_test.header_title}")
        self.main_page_is_loaded(page_to_test)
        self.filter_widget_checks(page_to_test.filter_widget)
        self.footer_checks()

    @Moonrise.test
    def ask_a_company_page(self):
        page_to_test = AskACompanyPage()
        self.click_element(f"link:{page_to_test.header_title}")
        self.main_page_is_loaded(page_to_test)
        self.footer_checks()

    @Moonrise.test
    def mobile_apps_test(self):
        page_to_test = MobileAppPage()
        self.click_element(f"link:{page_to_test.header_title}")
        self.main_page_is_loaded(page_to_test)
        self.footer_checks()

    @Moonrise.test
    def contact_test(self):
        page_to_test = AskACompanyPage()
        self.click_element(f"link:{page_to_test.header_title}")
        self.main_page_is_loaded(page_to_test)
        self.footer_checks()

    @Moonrise.test
    def faq_test(self):
        page_to_test = FAQPage()
        self.click_element(f"link:{page_to_test.header_title}")
        self.main_page_is_loaded(page_to_test)
        self.footer_checks()
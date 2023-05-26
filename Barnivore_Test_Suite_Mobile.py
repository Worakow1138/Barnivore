from moonrise import Moonrise
from Barnivore_Test_Steps import BarnivoreTestSteps
from Barnivore_Elements import *


class BarnivoreTests(BarnivoreTestSteps):

    Moonrise.default_timeout = 5

    def suite_setup(self):
        self.open_browser("chrome", "--headless", "--no-sandbox")
        # self.open_browser("chrome", persist=True)
        self.moon_driver.set_window_size(360, 800)
        return super().suite_setup()
    
    def suite_teardown(self):
        self.cleanup_browser()
        return super().suite_teardown()
    
    
class BasicPageTests(BarnivoreTests):

    def suite_setup(self):
        self.beer_page = BeerPage()
        self.cider_page = CiderPage()
        self.wine_page = WinePage()
        self.liquor_page = LiquorPage()
        self.askacompany_page = AskACompanyPage()
        self.mobile_page = MobileAppPage()
        self.contact_page = ContactPage()
        self.faq_page = FAQPage()
        return super().suite_setup()

    def test_setup(self):
        self.navigate_to_page("barnivore.com")
        self.verify_page_headers_present()
        self.verify_search_bar_present()
        return super().test_setup()

    @Moonrise.test
    def beer_page_test(self):
        self.load_page(self.beer_page.header_title)
        self.page_url_check(self.beer_page.header_title)
        self.filter_widget_checks(self.beer_page.filter_widget)
        self.listing_products_check(self.beer_page.list_widget)
        self.mini_search_elements_check()
        self.footer_checks()

    @Moonrise.test
    def cider_page_test(self):
        self.load_page(self.cider_page.header_title)
        self.page_url_check(self.cider_page.header_title)
        self.filter_widget_checks(self.cider_page.filter_widget)
        self.listing_products_check(self.cider_page.list_widget)
        self.mini_search_elements_check()
        self.footer_checks()

    @Moonrise.test
    def wine_page_test(self):
        self.load_page(self.wine_page.header_title)
        self.page_url_check(self.wine_page.header_title)
        self.filter_widget_checks(self.wine_page.filter_widget)
        self.listing_products_check(self.wine_page.list_widget)
        self.mini_search_elements_check()
        self.footer_checks()

    @Moonrise.test
    def liquor_page_test(self):
        self.load_page(self.liquor_page.header_title)
        self.page_url_check(self.liquor_page.header_title)
        self.filter_widget_checks(self.liquor_page.filter_widget)
        self.listing_products_check(self.liquor_page.list_widget)
        self.mini_search_elements_check()
        self.footer_checks()

    @Moonrise.test
    def ask_a_company_page_test(self):
        self.load_page(self.askacompany_page.header_title)
        self.page_url_check(self.askacompany_page.header_title)
        self.company_text_checks(self.askacompany_page)
        self.mini_search_elements_check()
        self.footer_checks()

    @Moonrise.test
    def mobile_page_test(self):
        self.load_page(self.mobile_page.header_title)
        self.page_url_check(self.mobile_page.header_title)
        self.mobile_text_checks()
        self.mini_search_elements_check()
        self.footer_checks()

    @Moonrise.test
    def contact_page_test(self):
        self.load_page(self.contact_page.header_title)
        self.page_url_check(self.contact_page.header_title)
        self.contact_text_checks()
        self.mini_search_elements_check()
        self.footer_checks()

    @Moonrise.test
    def faq_page_test(self):
        self.load_page(self.faq_page.header_title)
        self.page_url_check(self.faq_page.header_title)
        self.mini_search_elements_check()
        self.footer_checks()  
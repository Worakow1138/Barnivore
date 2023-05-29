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
        self.home_page = HomePage(mobile=True)
        self.beer_page = BeerPage(mobile=True)
        self.cider_page = CiderPage(mobile=True)
        self.wine_page = WinePage(mobile=True)
        self.liquor_page = LiquorPage(mobile=True)
        self.askacompany_page = AskACompanyPage(mobile=True)
        self.mobile_page = MobileAppPage(mobile=True)
        self.contact_page = ContactPage(mobile=True)
        self.faq_page = FAQPage(mobile=True)
        return super().suite_setup()

    def test_setup(self):
        self.navigate_to_page("barnivore.com")
        self.get_web_element(CommonPageElements.beer_page_link)
        self.get_web_element(CommonPageElements.cider_page_link)
        self.get_web_element(CommonPageElements.wine_page_link)
        self.get_web_element(CommonPageElements.liquor_page_link)
        return super().test_setup()

    @Moonrise.test
    def home_page_test(self):
        self.page_url_check(self.home_page.header_title)
        self.verify_search_bar_present(self.home_page.search_widget)
        self.home_text_checks(self.home_page)
        self.footer_checks()
    
    @Moonrise.test
    def beer_page_test(self):
        self.load_page(self.beer_page.header_title)
        self.page_url_check(self.beer_page.header_title)
        self.filter_widget_checks(self.beer_page.filter_widget)
        self.listing_products_check(self.beer_page)
        self.search_elements_check(self.beer_page.search_widget)
        self.footer_checks()

    @Moonrise.test
    def cider_page_test(self):
        self.load_page(self.cider_page.header_title)
        self.page_url_check(self.cider_page.header_title)
        self.filter_widget_checks(self.cider_page.filter_widget)
        self.listing_products_check(self.cider_page)
        self.search_elements_check(self.cider_page.search_widget)
        self.footer_checks()

    @Moonrise.test
    def wine_page_test(self):
        self.load_page(self.wine_page.header_title)
        self.page_url_check(self.wine_page.header_title)
        self.filter_widget_checks(self.wine_page.filter_widget)
        self.listing_products_check(self.wine_page)
        self.search_elements_check(self.wine_page.search_widget)
        self.footer_checks()

    @Moonrise.test
    def liquor_page_test(self):
        self.load_page(self.liquor_page.header_title)
        self.page_url_check(self.liquor_page.header_title)
        self.filter_widget_checks(self.liquor_page.filter_widget)
        self.listing_products_check(self.liquor_page)
        self.search_elements_check(self.liquor_page.search_widget)
        self.footer_checks()

    @Moonrise.test
    def ask_a_company_page_test(self):
        # self.load_page(self.askacompany_page.header_title)
        self.navigate_to_page(f"https://www.barnivore.com/{CommonPageElements.url_mapping.get(self.askacompany_page.header_title)}")
        self.page_url_check(self.askacompany_page.header_title)
        self.company_text_checks(self.askacompany_page)
        self.search_elements_check(self.askacompany_page.search_widget)
        self.footer_checks()

    @Moonrise.test
    def mobile_page_test(self):
        # self.load_page(self.mobile_page.header_title)
        self.navigate_to_page(f"https://www.barnivore.com/{CommonPageElements.url_mapping.get(self.mobile_page.header_title)}")
        self.page_url_check(self.mobile_page.header_title)
        self.mobile_text_checks(self.mobile_page)
        self.search_elements_check(self.mobile_page.search_widget)
        self.footer_checks()

    @Moonrise.test
    def contact_page_test(self):
        # self.load_page(self.contact_page.header_title)
        self.navigate_to_page(f"https://www.barnivore.com/{CommonPageElements.url_mapping.get(self.contact_page.header_title)}")
        self.page_url_check(self.contact_page.header_title)
        self.contact_text_checks(self.contact_page)
        self.search_elements_check(self.contact_page.search_widget)
        self.footer_checks()

    @Moonrise.test
    def faq_page_test(self):
        # self.load_page(self.faq_page.header_title)
        self.navigate_to_page(f"https://www.barnivore.com/{CommonPageElements.url_mapping.get(self.faq_page.header_title)}")
        self.page_url_check(self.faq_page.header_title)
        self.faq_text_checks(self.faq_page)
        self.search_elements_check(self.faq_page.search_widget)
        self.footer_checks()  


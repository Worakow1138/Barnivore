from moonrise import Moonrise
from Barnivore_Test_Steps import BarnivoreTestSteps
from Barnivore_Elements import *


class BarnivoreTests(BarnivoreTestSteps):

    Moonrise.default_timeout = 5

    def suite_setup(self):
        self.open_browser("chrome", "--headless", "--no-sandbox")
        # self.open_browser("chrome", persist=True)
        self.moon_driver.set_window_size(768, 1024)
        return super().suite_setup()
    
    def suite_teardown(self):
        self.cleanup_browser()
        return super().suite_teardown()
    
    
class BasicPageTests(BarnivoreTests):

    def suite_setup(self):
        self.home_page = HomePage()
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
        self.get_web_element(CommonPageElements.beer_page_link)
        self.get_web_element(CommonPageElements.cider_page_link)
        self.get_web_element(CommonPageElements.wine_page_link)
        self.get_web_element(CommonPageElements.liquor_page_link)
        self.get_web_element(CommonPageElements.ask_a_company_page_link)
        self.get_web_element(CommonPageElements.mobile_apps_page_link)
        self.get_web_element(CommonPageElements.contact_page_link)
        self.get_web_element(CommonPageElements.faq_page_link)
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
        self.load_page(self.askacompany_page.header_title)
        self.page_url_check(self.askacompany_page.header_title)
        self.company_text_checks(self.askacompany_page)
        self.search_elements_check(self.askacompany_page.search_widget)
        self.footer_checks()

    @Moonrise.test
    def mobile_page_test(self):
        self.load_page(self.mobile_page.header_title)
        self.page_url_check(self.mobile_page.header_title)
        self.mobile_text_checks(self.mobile_page)
        self.search_elements_check(self.mobile_page.search_widget)
        self.footer_checks()

    @Moonrise.test
    def contact_page_test(self):
        self.load_page(self.contact_page.header_title)
        self.page_url_check(self.contact_page.header_title)
        self.contact_text_checks(self.contact_page)
        self.search_elements_check(self.contact_page.search_widget)
        self.footer_checks()

    @Moonrise.test
    def faq_page_test(self):
        self.load_page(self.faq_page.header_title)
        self.page_url_check(self.faq_page.header_title)
        self.faq_text_checks(self.faq_page)
        self.search_elements_check(self.faq_page.search_widget)
        self.footer_checks()  

class CompanySearchTests(BarnivoreTests):

    def suite_setup(self):
        self.home_page = HomePage()
        self.search_page = SearchResultsPage()
        return super().suite_setup()
    
    def test_setup(self):
        self.navigate_to_page("barnivore.com")
        self.get_web_element(CommonPageElements.beer_page_link)
        self.get_web_element(CommonPageElements.cider_page_link)
        self.get_web_element(CommonPageElements.wine_page_link)
        self.get_web_element(CommonPageElements.liquor_page_link)
        self.get_web_element(CommonPageElements.ask_a_company_page_link)
        self.get_web_element(CommonPageElements.mobile_apps_page_link)
        self.get_web_element(CommonPageElements.contact_page_link)
        self.get_web_element(CommonPageElements.faq_page_link)
        self.get_web_element(self.home_page.search_widget.search_bar)
        self.get_web_element(self.home_page.search_widget.search_button)
        return super().test_setup()
    
    def company_search_test_steps(self, company_name, home_page: HomePage, search_page: SearchResultsPage):
        self.search_for_product(home_page.search_widget, company_name)
        assert self.get_text(search_page.list_widget.list_header) == f"Search results for {company_name}"
        self.search_elements_check(search_page.search_widget, company_name)
        self.results_are_from_company(company_name, search_page.list_widget)
        self.results_have_links_to_products(search_page.list_widget)
        self.results_have_correct_labels(search_page.list_widget)
        self.footer_checks()
    
    @Moonrise.test
    def diageo(self):
        self.company_search_test_steps("Diageo", self.home_page, self.search_page)
        

    @Moonrise.test
    def anheuser_busch(self):
        self.company_search_test_steps("Anheuser-Busch", self.home_page, self.search_page)

    @Moonrise.test
    def pernod_ricard(self):
        self.company_search_test_steps("Pernod Ricard", self.home_page, self.search_page)

    @Moonrise.test
    def constellation_brands(self):
        self.company_search_test_steps("Constellation Brands", self.home_page, self.search_page)

    @Moonrise.test
    def victory_brewing_company(self):
        self.company_search_test_steps("Victory Brewing Company", self.home_page, self.search_page)

    @Moonrise.test
    def brown_forman(self):
        self.company_search_test_steps("Brown-Forman", self.home_page, self.search_page)

    @Moonrise.test
    def sabmiller(self):
        self.company_search_test_steps("SABMiller", self.home_page, self.search_page)

    @Moonrise.test
    def bacardi(self):
        self.company_search_test_steps("Bacardi", self.home_page, self.search_page)

    @Moonrise.test
    def molson_coors_brewing_company(self):
        self.company_search_test_steps("Molson Coors Brewing Company", self.home_page, self.search_page)

    @Moonrise.test
    def beam_suntory(self):
        self.company_search_test_steps("Beam Suntory", self.home_page, self.search_page)
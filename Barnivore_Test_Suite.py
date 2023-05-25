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

    def suite_setup(self):
        self.beer_page = BeerPage()
        self.cider_page = CiderPage()
        self.wine_page = WinePage()
        self.liquor_page = LiquorPage()
        self.askacompany_page = AskACompanyPage()
        self.mobile_page = MobileAppPage()
        self.contact_page = ContactPage()
        return super().suite_setup()

    def test_setup(self):
        self.navigate_to_page("barnivore.com")
        self.verify_page_headers_present()
        self.verify_search_bar_present()
        return super().test_setup()

    @Moonrise.test
    def beer_page_test(self):
        self.load_page(self.beer_page)
        self.page_url_check(self.beer_page)
        self.filter_widget_checks(self.beer_page)
        self.listing_products_check(self.beer_page)
        self.footer_checks(self.beer_page)

    @Moonrise.test
    def cider_page_test(self):
        self.load_page(self.cider_page)
        self.page_url_check(self.cider_page)
        self.filter_widget_checks(self.cider_page)
        self.listing_products_check(self.cider_page)
        self.footer_checks(self.cider_page)

    @Moonrise.test
    def wine_page_test(self):
        self.load_page(self.wine_page)
        self.page_url_check(self.wine_page)
        self.filter_widget_checks(self.wine_page)
        self.listing_products_check(self.wine_page)
        self.footer_checks(self.wine_page)

    @Moonrise.test
    def liquor_page_test(self):
        self.load_page(self.liquor_page)
        self.page_url_check(self.liquor_page)
        self.filter_widget_checks(self.liquor_page)
        self.listing_products_check(self.liquor_page)
        self.footer_checks(self.liquor_page)

    @Moonrise.test
    def ask_a_company_page_test(self):
        self.load_page(self.askacompany_page)
        self.page_url_check(self.askacompany_page)
        self.footer_checks(self.askacompany_page)

    @Moonrise.test
    def mobile_page_test(self):
        self.load_page(self.mobile_page)
        self.page_url_check(self.mobile_page)
        self.footer_checks(self.mobile_page)

    @Moonrise.test
    def contact_page_test(self):
        self.load_page(self.contact_page)
        self.page_url_check(self.contact_page)
        self.footer_checks(self.contact_page)

    @Moonrise.test
    def faq_page_test(self):
        faq_page = FAQPage()
        self.load_page(faq_page)
        self.page_url_check(faq_page)
        self.footer_checks(faq_page)
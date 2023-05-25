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
        beer = BeerPage()
        self.load_page(beer)
        self.page_url_check(beer)
        self.filter_widget_checks(beer)
        self.listing_products_check(beer)
        self.footer_checks(beer)

    @Moonrise.test
    def cider_page(self):
        cider = CiderPage()
        self.load_page(cider)
        self.page_url_check(cider)
        self.filter_widget_checks(cider)
        self.listing_products_check(cider)
        self.footer_checks(cider)

    @Moonrise.test
    def wine_page(self):
        wine = WinePage()
        self.load_page(wine)
        self.page_url_check(wine)
        self.filter_widget_checks(wine)
        self.listing_products_check(wine)
        self.footer_checks(wine)

    @Moonrise.test
    def liquor_page(self):
        liquor = LiquorPage()
        self.load_page(liquor)
        self.page_url_check(liquor)
        self.filter_widget_checks(liquor)
        self.listing_products_check(liquor)
        self.footer_checks(liquor)

    @Moonrise.test
    def ask_a_company_page(self):
        askacompany = AskACompanyPage()
        self.load_page(askacompany)
        self.page_url_check(askacompany)
        self.footer_checks(askacompany)

    @Moonrise.test
    def mobile_apps_page(self):
        mobile_page = MobileAppPage()
        self.load_page(mobile_page)
        self.page_url_check(mobile_page)
        self.footer_checks(mobile_page)

    @Moonrise.test
    def contact_page(self):
        contact_page = ContactPage()
        self.load_page(contact_page)
        self.page_url_check(contact_page)
        self.footer_checks(contact_page)

    @Moonrise.test
    def faq_page(self):
        faq_page = FAQPage()
        self.load_page(faq_page)
        self.page_url_check(faq_page)
        self.footer_checks(faq_page)
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
        self.load_page(BeerPage)
        self.page_url_check(BeerPage)
        self.filter_widget_checks(BeerPage)
        self.footer_checks(BeerPage)

    @Moonrise.test
    def cider_page(self):
        self.load_page(CiderPage)
        self.page_url_check(CiderPage)
        self.filter_widget_checks(CiderPage)
        self.footer_checks(CiderPage)

    @Moonrise.test
    def wine_page(self):
        self.load_page(WinePage)
        self.page_url_check(WinePage)
        self.filter_widget_checks(WinePage)
        self.footer_checks(WinePage)

    @Moonrise.test
    def liquor_page(self):
        self.load_page(LiquorPage)
        self.page_url_check(LiquorPage)
        self.filter_widget_checks(LiquorPage)
        self.footer_checks(LiquorPage)

    @Moonrise.test
    def ask_a_company_page(self):
        self.load_page(AskACompanyPage)
        self.page_url_check(AskACompanyPage)
        self.footer_checks(AskACompanyPage)

    @Moonrise.test
    def mobile_apps_page(self):
        self.load_page(MobileAppPage)
        self.page_url_check(MobileAppPage)
        self.footer_checks(MobileAppPage)

    @Moonrise.test
    def contact_page(self):
        self.load_page(ContactPage)
        self.page_url_check(ContactPage)
        self.footer_checks(ContactPage)

    @Moonrise.test
    def faq_page(self):
        self.load_page(FAQPage)
        self.page_url_check(FAQPage)
        self.footer_checks(FAQPage)
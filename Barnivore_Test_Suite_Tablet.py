from moonrise import Moonrise
from Barnivore_Test_Steps import BarnivoreTestSteps
from Barnivore_Elements import *
from typing import Union


class BarnivoreTests(BarnivoreTestSteps):

    Moonrise.default_timeout = 5

    def suite_setup(self):
        self.open_browser("chrome", "--headless", "--no-sandbox", shutter_speed=0.2)
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
        self.search_elements_check(self.home_page.search_widget)
        self.home_text_checks(self.home_page)
        self.footer_checks()
    
    @Moonrise.test
    def beer_page_test(self):
        self.load_page(self.beer_page.header_title)
        self.page_url_check(self.beer_page.header_title)
        self.filter_widget_checks(self.beer_page.filter_widget)
        self.listing_products_check(self.beer_page)
        self.search_elements_check(self.beer_page.search_widget, find_booze=True)
        self.footer_checks()

    @Moonrise.test
    def cider_page_test(self):
        self.load_page(self.cider_page.header_title)
        self.page_url_check(self.cider_page.header_title)
        self.filter_widget_checks(self.cider_page.filter_widget)
        self.listing_products_check(self.cider_page)
        self.search_elements_check(self.cider_page.search_widget, find_booze=True)
        self.footer_checks()

    @Moonrise.test
    def wine_page_test(self):
        self.load_page(self.wine_page.header_title)
        self.page_url_check(self.wine_page.header_title)
        self.filter_widget_checks(self.wine_page.filter_widget)
        self.listing_products_check(self.wine_page)
        self.search_elements_check(self.wine_page.search_widget, find_booze=True)
        self.footer_checks()

    @Moonrise.test
    def liquor_page_test(self):
        self.load_page(self.liquor_page.header_title)
        self.page_url_check(self.liquor_page.header_title)
        self.filter_widget_checks(self.liquor_page.filter_widget)
        self.listing_products_check(self.liquor_page)
        self.search_elements_check(self.liquor_page.search_widget, find_booze=True)
        self.footer_checks()

    @Moonrise.test
    def ask_a_company_page_test(self):
        self.load_page(self.askacompany_page.header_title)
        self.page_url_check(self.askacompany_page.header_title)
        self.company_text_checks(self.askacompany_page)
        self.search_elements_check(self.askacompany_page.search_widget, find_booze=True)
        self.footer_checks()

    @Moonrise.test
    def mobile_page_test(self):
        self.load_page(self.mobile_page.header_title)
        self.page_url_check(self.mobile_page.header_title)
        self.mobile_text_checks(self.mobile_page)
        self.search_elements_check(self.mobile_page.search_widget, find_booze=True)
        self.footer_checks()

    @Moonrise.test
    def contact_page_test(self):
        self.load_page(self.contact_page.header_title)
        self.page_url_check(self.contact_page.header_title)
        self.contact_text_checks(self.contact_page)
        self.search_elements_check(self.contact_page.search_widget, find_booze=True)
        self.footer_checks()

    @Moonrise.test
    def faq_page_test(self):
        self.load_page(self.faq_page.header_title)
        self.page_url_check(self.faq_page.header_title)
        self.faq_text_checks(self.faq_page)
        self.search_elements_check(self.faq_page.search_widget, find_booze=True)
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
        self.search_elements_check(self.home_page.search_widget)
        return super().test_setup()
    
    def company_search_test_steps(self, company_name, home_page: HomePage, search_page: SearchResultsPage):
        self.search_for_product(home_page.search_widget, company_name)
        assert self.get_text(search_page.list_widget.list_header) == f"Search results for {company_name}"
        self.search_elements_check(search_page.search_widget, company_name, find_booze=True)
        self.results_are_from_company(company_name, search_page.list_widget)
        self.results_have_links_to_products(search_page.list_widget)
        self.results_have_correct_labels(search_page.list_widget, self.get_web_elements(search_page.list_widget.list_items))
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

    @Moonrise.test
    def non_existent_company(self):
        company_name = "Purple Drink, LLC"
        self.search_for_product(self.home_page.search_widget, company_name)
        assert self.get_text(self.search_page.list_widget.list_header) == f"Search results for {company_name}"
        self.search_elements_check(self.search_page.search_widget, company_name, find_booze=True)
        assert self.search_page.invalid_entry_text in self.get_text(CommonPageElements.main_content_element)

class ProductEvaluationTests(BarnivoreTests):

    def suite_setup(self):
        self.home_page = HomePage()
        self.search_page = SearchResultsPage()
        return super().suite_setup()
    
    def test_setup(self):
        self.company_name = "Diageo"
        self.navigate_to_page("barnivore.com")
        self.search_elements_check(self.home_page.search_widget)
        self.search_for_product(self.home_page.search_widget, self.company_name)
        self.search_elements_check(self.search_page.search_widget, self.company_name, find_booze=True)
        self.get_web_element(self.search_page.list_widget.list_items)
        return super().test_setup()
    
    @Moonrise.test
    def vegan_friendly(self):
        product_label = self.search_page.list_widget.vegan_friendly
        product = self.find_first_product_of_type(self.search_page.list_widget, product_label)
        product_name = self.search_page.list_widget.get_product_name(product)

        self.load_product_page(product_name)
        self.product_page_checks(self.search_page.product_widget, product_name, self.company_name, product_label)
        self.results_are_from_company(self.company_name, self.search_page.list_widget)
        self.results_have_correct_labels(self.search_page.list_widget, self.get_web_elements(self.search_page.list_widget.list_items))
        self.search_elements_check(self.search_page.search_widget, find_booze=True)
        self.footer_checks()

    @Moonrise.test
    def not_vegan_friendly(self):
        product_label = self.search_page.list_widget.not_vegan_friendly
        product = self.find_first_product_of_type(self.search_page.list_widget, product_label)
        product_name = self.search_page.list_widget.get_product_name(product)
        
        self.load_product_page(product_name)
        self.product_page_checks(self.search_page.product_widget, product_name, self.company_name, product_label)
        self.results_are_from_company(self.company_name, self.search_page.list_widget)
        self.results_have_correct_labels(self.search_page.list_widget, self.get_web_elements(self.search_page.list_widget.list_items))
        self.search_elements_check(self.search_page.search_widget, find_booze=True)
        self.footer_checks()


    @Moonrise.test
    def unknown_label(self):
        product_label = self.search_page.list_widget.unknown
        product = self.find_first_product_of_type(self.search_page.list_widget, product_label)
        product_name = self.search_page.list_widget.get_product_name(product)
        
        self.load_product_page(product_name)
        self.product_page_checks(self.search_page.product_widget, product_name, self.company_name, product_label)
        self.results_are_from_company(self.company_name, self.search_page.list_widget)
        self.results_have_correct_labels(self.search_page.list_widget, self.get_web_elements(self.search_page.list_widget.list_items))
        self.search_elements_check(self.search_page.search_widget, find_booze=True)
        self.footer_checks()

class AskACompanyTests(BarnivoreTests):

    def suite_setup(self):
        self.brand_name = "Victory"
        self.your_name = "Barnivore User"
        return super().suite_setup()
    
    def test_setup(self):
        self.ask_a_company_page = AskACompanyPage()
        self.navigate_to_page(f"barnivore.com/{CommonPageElements.url_mapping.get(self.ask_a_company_page.header_title)}")
        self.company_text_checks(self.ask_a_company_page)
        self.search_elements_check(self.ask_a_company_page.search_widget, find_booze=True)
        self.footer_checks()
        return super().test_setup()

    @Moonrise.test
    def english(self):
        language = "English"
        question_available = True
        non_vegan_response_available = True
        vegan_response_available = True
        self.ask_a_company_test_steps(self.ask_a_company_page, language, self.brand_name, self.your_name, question_available, non_vegan_response_available, vegan_response_available)

    @Moonrise.test
    def french(self):
        language = "French"
        question_available = True
        non_vegan_response_available = True
        vegan_response_available = True
        self.ask_a_company_test_steps(self.ask_a_company_page, language, self.brand_name, self.your_name, question_available, non_vegan_response_available, vegan_response_available)

    @Moonrise.test
    def hebrew(self):
        language = "Hebrew"
        question_available = True
        non_vegan_response_available = False
        vegan_response_available = False
        self.ask_a_company_test_steps(self.ask_a_company_page, language, self.brand_name, self.your_name, question_available, non_vegan_response_available, vegan_response_available)

    @Moonrise.test
    def danish(self):
        language = "Danish"
        question_available = True
        non_vegan_response_available = True
        vegan_response_available = True
        self.ask_a_company_test_steps(self.ask_a_company_page, language, self.brand_name, self.your_name, question_available, non_vegan_response_available, vegan_response_available)

    @Moonrise.test
    def ukrainian(self):
        language = "Ukrainian"
        question_available = True
        non_vegan_response_available = True
        vegan_response_available = True
        self.ask_a_company_test_steps(self.ask_a_company_page, language, self.brand_name, self.your_name, question_available, non_vegan_response_available, vegan_response_available)

    @Moonrise.test
    def arabic(self):
        language = "Arabic"
        question_available = True
        non_vegan_response_available = False
        vegan_response_available = False
        self.ask_a_company_test_steps(self.ask_a_company_page, language, self.brand_name, self.your_name, question_available, non_vegan_response_available, vegan_response_available)

    @Moonrise.test
    def brazilian_portuguese(self):
        language = "Brazilian Portuguese"
        question_available = True
        non_vegan_response_available = True
        vegan_response_available = False
        self.ask_a_company_test_steps(self.ask_a_company_page, language, self.brand_name, self.your_name, question_available, non_vegan_response_available, vegan_response_available)

    @Moonrise.test
    def croat(self):
        language = "Croat"
        question_available = True
        non_vegan_response_available = False
        vegan_response_available = False
        self.ask_a_company_test_steps(self.ask_a_company_page, language, self.brand_name, self.your_name, question_available, non_vegan_response_available, vegan_response_available)

    @Moonrise.test
    def dutch(self):
        language = "Dutch"
        question_available = True
        non_vegan_response_available = True
        vegan_response_available = True
        self.ask_a_company_test_steps(self.ask_a_company_page, language, self.brand_name, self.your_name, question_available, non_vegan_response_available, vegan_response_available)

    @Moonrise.test
    def finnish(self):
        language = "Finnish"
        question_available = True
        non_vegan_response_available = True
        vegan_response_available = False
        self.ask_a_company_test_steps(self.ask_a_company_page, language, self.brand_name, self.your_name, question_available, non_vegan_response_available, vegan_response_available)

    @Moonrise.test
    def german(self):
        language = "German"
        question_available = True
        non_vegan_response_available = True
        vegan_response_available = True
        self.ask_a_company_test_steps(self.ask_a_company_page, language, self.brand_name, self.your_name, question_available, non_vegan_response_available, vegan_response_available)

    @Moonrise.test
    def greek(self):
        language = "Greek"
        question_available = True
        non_vegan_response_available = False
        vegan_response_available = False
        self.ask_a_company_test_steps(self.ask_a_company_page, language, self.brand_name, self.your_name, question_available, non_vegan_response_available, vegan_response_available)

    @Moonrise.test
    def hindi(self):
        language = "Hindi"
        question_available = True
        non_vegan_response_available = False
        vegan_response_available = False
        self.ask_a_company_test_steps(self.ask_a_company_page, language, self.brand_name, self.your_name, question_available, non_vegan_response_available, vegan_response_available)

    @Moonrise.test
    def icelandic(self):
        language = "Icelandic"
        question_available = True
        non_vegan_response_available = False
        vegan_response_available = False
        self.ask_a_company_test_steps(self.ask_a_company_page, language, self.brand_name, self.your_name, question_available, non_vegan_response_available, vegan_response_available)

    @Moonrise.test
    def italian(self):
        language = "Italian"
        question_available = True
        non_vegan_response_available = True
        vegan_response_available = False
        self.ask_a_company_test_steps(self.ask_a_company_page, language, self.brand_name, self.your_name, question_available, non_vegan_response_available, vegan_response_available)

    @Moonrise.test
    def japanese(self):
        language = "Japanese"
        question_available = True
        non_vegan_response_available = False
        vegan_response_available = False
        self.ask_a_company_test_steps(self.ask_a_company_page, language, self.brand_name, self.your_name, question_available, non_vegan_response_available, vegan_response_available)

    @Moonrise.test
    def korean(self):
        language = "Korean"
        question_available = True
        non_vegan_response_available = False
        vegan_response_available = False
        self.ask_a_company_test_steps(self.ask_a_company_page, language, self.brand_name, self.your_name, question_available, non_vegan_response_available, vegan_response_available)

    @Moonrise.test
    def norwegian(self):
        language = "Norwegian"
        question_available = True
        non_vegan_response_available = False
        vegan_response_available = False
        self.ask_a_company_test_steps(self.ask_a_company_page, language, self.brand_name, self.your_name, question_available, non_vegan_response_available, vegan_response_available)

    @Moonrise.test
    def polish(self):
        language = "Polish"
        question_available = True
        non_vegan_response_available = False
        vegan_response_available = False
        self.ask_a_company_test_steps(self.ask_a_company_page, language, self.brand_name, self.your_name, question_available, non_vegan_response_available, vegan_response_available)

    @Moonrise.test
    def portuguese(self):
        language = "Portuguese"
        question_available = True
        non_vegan_response_available = True
        vegan_response_available = True
        self.ask_a_company_test_steps(self.ask_a_company_page, language, self.brand_name, self.your_name, question_available, non_vegan_response_available, vegan_response_available)

    @Moonrise.test
    def russian(self):
        language = "Russian"
        question_available = True
        non_vegan_response_available = True
        vegan_response_available = True
        self.ask_a_company_test_steps(self.ask_a_company_page, language, self.brand_name, self.your_name, question_available, non_vegan_response_available, vegan_response_available)

    @Moonrise.test
    def slovak(self):
        language = "Slovak"
        question_available = True
        non_vegan_response_available = False
        vegan_response_available = False
        self.ask_a_company_test_steps(self.ask_a_company_page, language, self.brand_name, self.your_name, question_available, non_vegan_response_available, vegan_response_available)

    @Moonrise.test
    def slovenian(self):
        language = "Slovenian"
        question_available = True
        non_vegan_response_available = False
        vegan_response_available = False
        self.ask_a_company_test_steps(self.ask_a_company_page, language, self.brand_name, self.your_name, question_available, non_vegan_response_available, vegan_response_available)

    @Moonrise.test
    def spanish(self):
        language = "Spanish"
        question_available = True
        non_vegan_response_available = True
        vegan_response_available = True
        self.ask_a_company_test_steps(self.ask_a_company_page, language, self.brand_name, self.your_name, question_available, non_vegan_response_available, vegan_response_available)

    @Moonrise.test
    def swedish(self):
        language = "Swedish"
        question_available = True
        non_vegan_response_available = False
        vegan_response_available = False
        self.ask_a_company_test_steps(self.ask_a_company_page, language, self.brand_name, self.your_name, question_available, non_vegan_response_available, vegan_response_available)
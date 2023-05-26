from moonrise import Moonrise
from Barnivore_Elements import *
import re

class BarnivoreTestSteps(Moonrise):

    def verify_page_headers_present(self):
        self.get_web_element(MainPageElements.beer_page_link)
        self.get_web_element(MainPageElements.cider_page_link)
        self.get_web_element(MainPageElements.wine_page_link)
        self.get_web_element(MainPageElements.liquor_page_link)
        self.get_web_element(MainPageElements.ask_a_company_page_link)
        self.get_web_element(MainPageElements.mobile_apps_page_link)
        self.get_web_element(MainPageElements.contact_page_link)
        self.get_web_element(MainPageElements.faq_page_link)

    def verify_search_bar_present(self):
        self.get_web_element(HomePage.search_bar)
        self.get_web_element(HomePage.search_button)

    def load_page(self, header_title):
        self.click_element(f"link:{header_title}")

    def page_url_check(self, header_title):
        assert self.moon_driver.current_url == f"https://www.barnivore.com/{MainPageElements.url_mapping.get(header_title)}"
    
    def filter_widget_checks(self, filter_widget):
        self.get_web_element(FilterElements.filter_title)
        self.get_web_element(FilterElements.filter_parent_element)
        for letter in filter_widget.letter_filter_buttons.values():
            self.get_web_element(letter)
        for veganosity in filter_widget.veganosity_filter_buttons.values():
            self.get_web_element(veganosity)
        if filter_widget.country_element:
            self.get_web_element(filter_widget.country_element)

    def listing_products_check(self, list_widget):
        self.get_web_element(list_widget.list_header)
        assert re.search("(Displaying products 1 - 50 of .* in total)", self.get_text(ListElements.displaying_products))
        assert len(self.get_web_elements(ListElements.list_items)) == 50

    def mini_search_elements_check(self):
        self.get_web_element(SearchBarElements.mini_search_bar)
        self.get_web_element(SearchBarElements.mini_search_button)
        assert self.get_web_element(SearchBarElements.find_booze_label).text == "Find Booze:"

    def company_text_checks(self, page):
        content_text = self.get_text(AskACompanyPage.main_content_element)
        assert AskACompanyPage.ask_a_company_paragraph in content_text
        assert AskACompanyPage.the_question_title in content_text
        assert AskACompanyPage.the_response_title in content_text

        assert page.the_question_text in self.get_text(AskACompanyPage.question_element)
        assert page.vegan_response in self.get_text(AskACompanyPage.vegan_response_element)
        assert page.non_vegan_response in self.get_text(AskACompanyPage.non_vegan_response_element)

        self.get_web_element(AskACompanyPage.question_language_selector)
        self.get_web_element(AskACompanyPage.vegan_response_language_selector)
        self.get_web_element(AskACompanyPage.non_vegan_response_language_selector)
        self.get_web_element(AskACompanyPage.brand_name_input)
        self.get_web_element(AskACompanyPage.sender_name_input)

    def footer_checks(self):
        self.get_web_element(MainPageElements.pdr_label)
        self.get_web_element(MainPageElements.vegan_beer_label)
        self.get_web_element(MainPageElements.vegan_wine_label)
        self.get_web_element(MainPageElements.vegan_liquor_label)
        assert self.get_text(MainPageElements.copyright_label) == 'Contents copyright © 2023 Thrust Labs. All rights reserved.\nContact Us | Terms of Use/Privacy Policy'
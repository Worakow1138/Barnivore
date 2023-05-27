from moonrise import Moonrise
from Barnivore_Elements import *
import re

class BarnivoreTestSteps(Moonrise):

    def verify_search_bar_present(self):
        self.get_web_element(HomePage.search_bar)
        self.get_web_element(HomePage.search_button)

    def load_page(self, header_title):
        self.click_element(f"link:{header_title}")

    def page_url_check(self, header_title):
        assert self.moon_driver.current_url == f"https://www.barnivore.com/{MainPageElements.url_mapping.get(header_title)}"
    
    def filter_widget_checks(self, filter_widget: FilterElements):
        self.get_web_element(FilterElements.filter_title)
        self.get_web_element(FilterElements.filter_parent_element)
        for letter in filter_widget.letter_filter_buttons.values():
            self.get_web_element(letter)
        for veganosity in filter_widget.veganosity_filter_buttons.values():
            self.get_web_element(veganosity)
        if filter_widget.country_element:
            self.get_web_element(filter_widget.country_element)

    def listing_products_check(self, list_widget: ListElements):
        self.get_web_element(list_widget.list_header)
        assert re.search("(Displaying products 1 - 50 of .* in total)", self.get_text(ListElements.displaying_products))
        assert len(self.get_web_elements(ListElements.list_items)) == 50

    def mini_search_elements_check(self, search_widget: SearchBarElements):
        self.get_web_element(search_widget.mini_search_bar)
        self.get_web_element(search_widget.mini_search_button)
        assert self.get_text(search_widget.find_booze_label) == "Find Booze:"

    def company_text_checks(self, page: AskACompanyPage):
        content_text = self.get_text(MainPageElements.main_content_element)
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

    def mobile_text_checks(self):
        assert MobileAppPage.mobile_page_text in self.get_text(MainPageElements.main_content_element)
        self.get_web_element(MobileAppPage.beer_link)
        self.get_web_element(MobileAppPage.cider_link)
        self.get_web_element(MobileAppPage.wine_link)
        self.get_web_element(MobileAppPage.liquor_link)

    def contact_text_checks(self, contact_page: ContactPage):
        assert contact_page.contact_page_text in self.get_text(MainPageElements.main_content_element)
        self.get_web_element(ContactPage.barnivore_contact_email)
        if contact_page.ask_a_company_link:
            self.get_web_element(contact_page.ask_a_company_link)

    def faq_text_checks(self):
        content_text = self.get_text(MainPageElements.main_content_element)
        assert FAQPage.can_you_check_text in content_text
        assert FAQPage.where_info_text in content_text
        assert FAQPage.vegan_friendly_text in content_text
        assert FAQPage.add_filter_text in content_text
        assert FAQPage.diatomaceous_earth_text in content_text
        assert FAQPage.country_text in content_text
        assert FAQPage.glue_text in content_text
        assert FAQPage.sugar_text in content_text
        assert FAQPage.cross_contamination_text in content_text
        assert FAQPage.terms_of_use_text in content_text

        self.get_web_element(FAQPage.ask_a_company_link)
        self.get_web_element(FAQPage.want_to_help_link)
        self.get_web_element(FAQPage.contact_page_link)
        self.get_web_element(FAQPage.get_in_touch_link)
        self.get_web_element(FAQPage.terms_of_use_link)

    def footer_checks(self):
        self.get_web_element(MainPageElements.pdr_label)
        self.get_web_element(MainPageElements.vegan_beer_label)
        self.get_web_element(MainPageElements.vegan_wine_label)
        self.get_web_element(MainPageElements.vegan_liquor_label)
        assert self.get_text(MainPageElements.copyright_label) == 'Contents copyright © 2023 Thrust Labs. All rights reserved.\nContact Us | Terms of Use/Privacy Policy'
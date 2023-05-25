from moonrise import Moonrise
from Barnivore_Elements import *

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
        self.get_web_element(filter_widget.filter_title)
        self.get_web_element(filter_widget.filter_parent_element)
        for letter in filter_widget.letter_filter_buttons.values():
            self.get_web_element(letter)
        for veganosity in filter_widget.veganosity_filter_buttons.values():
            self.get_web_element(veganosity)
        if filter_widget.country_element:
            self.get_web_element(filter_widget.country_element)

    def listing_products_check(self, list_widget):
        self.get_web_element(list_widget.list_header)

    def footer_checks(self):
        self.get_web_element(MainPageElements.pdr_label)
        self.get_web_element(MainPageElements.vegan_beer_label)
        self.get_web_element(MainPageElements.vegan_wine_label)
        self.get_web_element(MainPageElements.vegan_liquor_label)
        self.get_web_element(MainPageElements.copyright_label) == 'Contents copyright © 2023 Thrust Labs. All rights reserved.\nContact Us | Terms of Use/Privacy Policy'
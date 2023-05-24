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

    def main_page_is_loaded(self, page):
        assert self.moon_driver.current_url == f"https://www.barnivore.com/{page.url_mapping.get(page.header_title)}"
    
    def filter_widget_checks(self, filter_widget):
        self.get_web_element(filter_widget.filter_title)
        self.get_web_element(filter_widget.filter_parent_element)
        for letter in filter_widget.letter_filter_buttons.values():
            self.get_web_element(letter)
        for veganosity in filter_widget.veganosity_filter_buttons.values():
            self.get_web_element(veganosity)
        if filter_widget.country_element:
            self.get_web_element(filter_widget.country_element)

    def footer_checks(self, page):
        self.get_web_element(page.pdr_label)
        self.get_web_element(page.vegan_beer_label)
        self.get_web_element(page.vegan_wine_label)
        self.get_web_element(page.vegan_liquor_label)
        self.get_web_element(page.copyright_label) == 'Contents copyright © 2023 Thrust Labs. All rights reserved.\nContact Us | Terms of Use/Privacy Policy'
from moonrise import Moonrise
from Barnivore_Elements import *

class BarnivoreMethods(Moonrise):

    def verify_page_headers_present(self):
        self.get_web_element(f"link:{BeerPageElements.header_title}")
        self.get_web_element(f"link:{CiderPageElements.header_title}")
        self.get_web_element(f"link:{WinePageElements.header_title}")
        self.get_web_element(f"link:{LiquorPageElements.header_title}")
        self.get_web_element(f"link:{AskACompanyElements.header_title}")
        self.get_web_element(f"link:{MobileAppElements.header_title}")
        self.get_web_element(f"link:{ContactElements.header_title}")
        self.get_web_element(f"link:{FAQElements.header_title}")

    def verify_search_bar_present(self):
        self.get_web_element(HomePageElements.search_bar)
        self.get_web_element(HomePageElements.search_button)

    def main_page_is_loaded(self, page_title):
        page_title = page_title.lower()
        assert self.moon_driver.current_url == f"https://www.barnivore.com/{page_title}"
    
    def filter_widget_checks(self, filter_widget):
        self.get_web_element(filter_widget.filter_title)
        self.get_web_element(filter_widget.filter_parent_element)
        for letter in filter_widget.letter_filter_buttons.values():
            self.get_web_element(letter)
        for veganosity in filter_widget.veganosity_filter_buttons.values():
            self.get_web_element(veganosity)
        if filter_widget.country_element:
            self.get_web_element(filter_widget.country_element)
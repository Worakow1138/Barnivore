from moonrise import Moonrise
from Barnivore_Elements import *

class BarnivoreMethods(Moonrise):

    def verify_page_headers_present(self):
        self.get_web_element("link:Beer")
        self.get_web_element("link:Cider")
        self.get_web_element("link:Wine")
        self.get_web_element("link:Liquor")
        self.get_web_element("link:Ask a Company")
        self.get_web_element("link:Mobile Apps")
        self.get_web_element("link:Contact")
        self.get_web_element("link:FAQ")

    def verify_search_bar_present(self):
        self.get_web_element(MainPageElements.search_bar)
        self.get_web_element(MainPageElements.search_button)

    def select_page_link(self, header_title):
        self.click_element(f"link:{header_title}")

    def get_url(self):
        return self.moon_driver.current_url
    
    def filter_widget_checks(self, header_page):
        filter_widget = FilterElements(header_page)
        self.get_web_element(filter_widget.filter_title)
        self.get_web_element(filter_widget.filter_parent_element)
        for letter in filter_widget.letter_filter_buttons.values():
            self.get_web_element(letter)
        for veganosity in filter_widget.veganosity_filter_buttons.values():
            self.get_web_element(veganosity)

    def beer_filter_widget_present(self):
        self.filter_widget_checks("beer")

    def cider_filter_widget_present(self):
        self.filter_widget_checks("cider")

    def wine_filter_widget_present(self):
        self.filter_widget_checks("wine")

    def liquor_filter_widget_present(self):
        self.filter_widget_checks("liquor")
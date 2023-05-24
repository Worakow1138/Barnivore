from moonrise import Moonrise
from Barnivore_Elements import *

class BarnivoreMethods(Moonrise):

    def verify_page_headers_present(self):
        self.get_web_element(f"link:{BeerPageElements.header_title}")
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

    def main_page_is_loaded(self, page_title):
        page_title = page_title.lower()
        assert self.moon_driver.current_url == f"https://www.barnivore.com/{page_title}"
    
    def filter_widget_checks(self, header_page):
        filter_widget = FilterElements(header_page)
        self.get_web_element(filter_widget.filter_title)
        self.get_web_element(filter_widget.filter_parent_element)
        for letter in filter_widget.letter_filter_buttons.values():
            self.get_web_element(letter)
        for veganosity in filter_widget.veganosity_filter_buttons.values():
            self.get_web_element(veganosity)
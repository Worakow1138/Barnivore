from moonrise import Moonrise


class FilterWidget(Moonrise):

    filter_title = "//h2[text()='Filters']"
    filter_parent_element = "css:#content > div.filter"
    by_letter_element = "//b[text()='By Letter:]"
    by_veganosity_element = "//b[text()='By veganosity:']"

    def __init__(self, page):
        self.page = page.lower()
        self.letter_filter_buttons = {
            "0-9": f"//a[@href='/{self.page}/0-9' and text()='0-9']",
            "a-f": f"//a[@href='/{self.page}' and text() = 'A-F']",
            "g-l": f"//a[@href='/{self.page}/g-l' and text() = 'G-L']",
            "m-r": f"//a[@href='/{self.page}/m-r' and text() = 'M-R']",
            "s-t": f"//a[@href='/{self.page}/s-t' and text() = 'S-T']",
            "u-z": f"//a[@href='/{self.page}/u-z' and text() = 'U-Z']"
        }
        self.veganosity_filter_buttons = {
            "Everything": f"//a[@href='/{self.page}?vfilter=All' and text() = 'Everything']",
            "Only Vegan": f"//a[@href='/{self.page}?vfilter=Vegan' and text() = 'Only Vegan']",
        }
        self.country_element = {
            "beer": "//label[contains(text(),'Country:')]",
            "cider": "//label[contains(text(),'Country:')]",
            "wine": "//label[contains(text(),'Region:')]",
        }

# class HeaderWidgets:

    # header_titles = 

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

    def select_page_link(self, header_title):
        self.click_element(f"link:{header_title}")

    def get_url(self):
        return self.moon_driver.current_url
    
    def filter_widget_checks(self, header_page):
        filter_widget = FilterWidget(header_page)
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
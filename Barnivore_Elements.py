

class FilterElements:

    filter_title = "//h2[text()='Filters']"
    filter_parent_element = "css:#content > div.filter"
    by_letter_element = "//b[text()='By Letter:]"
    by_veganosity_element = "//b[text()='By veganosity:']"
    country_element_mapping = {
        "beer": "//label[contains(text(),'Country:')]",
        "cider": "//label[contains(text(),'Country:')]",
        "wine": "//label[contains(text(),'Region:')]",
    }

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
        self.country_element = self.country_element_mapping.get(self.page)

class MainPageElements:

    pdr_label = "//div[@id='footer']/p[text()='Please Drink Responsibly']"
    vegan_beer_label = "//div[@id='footer']//a[@href='/beer/' and text()='Vegan Beer']"
    vegan_wine_label = "//div[@id='footer']//a[@href='/wine/' and text()='Vegan Wine']"
    vegan_liquor_label = "//div[@id='footer']//a[@href='/beer/' and text()='Vegan Beer']"
    copyright_label = "#footer > p:nth-child(3)"
    url_mapping = {
        "Beer": "beer",
        "Cider": "cider",
        "Wine": "wine",
        "Liquor": "liquor",
        "Ask a Company": "askacompany",
        "Mobile Apps": "mobile",
        "Contact": "contact",
        "FAQ": "faq"
    }

class HomePage(MainPageElements):

    search_bar = "#big-search > input.ui-autocomplete-input"
    search_button = "#big-search > input[type=submit]:nth-child(2)"

class BeerPage(MainPageElements):

    header_title = "Beer"
    def __init__(self):
        self.filter_widget = FilterElements(self.header_title)

class CiderPage(MainPageElements):

    header_title = "Cider"
    def __init__(self):
        self.filter_widget = FilterElements(self.header_title)

class WinePage(MainPageElements):

    header_title = "Wine"
    def __init__(self):
        self.filter_widget = FilterElements(self.header_title)

class LiquorPage(MainPageElements):

    header_title = "Liquor"
    def __init__(self):
        self.filter_widget = FilterElements(self.header_title)

class AskACompanyPage(MainPageElements):

    header_title = "Ask a Company"

class MobileAppPage(MainPageElements):

    header_title = "Mobile Apps"

class ContactPage(MainPageElements):

    header_title = "Contact"

class FAQPage(MainPageElements):

    header_title = "FAQ"

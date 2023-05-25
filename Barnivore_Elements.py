

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

    def __init__(self, page_title):
        self.page_title = page_title.lower()
        self.letter_filter_buttons = {
            "0-9": f"//a[@href='/{self.page_title}/0-9' and text()='0-9']",
            "a-f": f"//a[@href='/{self.page_title}' and text() = 'A-F']",
            "g-l": f"//a[@href='/{self.page_title}/g-l' and text() = 'G-L']",
            "m-r": f"//a[@href='/{self.page_title}/m-r' and text() = 'M-R']",
            "s-t": f"//a[@href='/{self.page_title}/s-t' and text() = 'S-T']",
            "u-z": f"//a[@href='/{self.page_title}/u-z' and text() = 'U-Z']"
        }
        self.veganosity_filter_buttons = {
            "Everything": f"//a[@href='/{self.page_title}?vfilter=All' and text() = 'Everything']",
            "Only Vegan": f"//a[@href='/{self.page_title}?vfilter=Vegan' and text() = 'Only Vegan']",
        }
        self.country_element = self.country_element_mapping.get(self.page_title)

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
    beer_page_link = "link:Beer"
    cider_page_link = "link:Cider"
    wine_page_link = "link:Wine"
    liquor_page_link = "link:Liquor"
    ask_a_company_page_link = "link:Ask a Company"
    mobile_apps_page_link = "link:Mobile Apps"
    contact_page_link = "link:Contact"
    faq_page_link = "link:FAQ"

class ListElements:

    def __init__(self, page_title):
        self.page_title = page_title.lower()
        self.list_header = f"//*[@id='content']/h1[contains(text(),'Listing {self.page_title}s')]"

class HomePage(MainPageElements):

    search_bar = "#big-search > input.ui-autocomplete-input"
    search_button = "#big-search > input[type=submit]:nth-child(2)"

class BeerPage(MainPageElements):

    header_title = "Beer"
    def __init__(self):
        self.filter_widget = FilterElements(self.header_title)
        self.list_widget = ListElements(self.header_title)

class CiderPage(MainPageElements):

    header_title = "Cider"
    def __init__(self):
        self.filter_widget = FilterElements(self.header_title)
        self.list_widget = ListElements(self.header_title)

class WinePage(MainPageElements):

    header_title = "Wine"
    def __init__(self):
        self.filter_widget = FilterElements(self.header_title)
        self.list_widget = ListElements(self.header_title)

class LiquorPage(MainPageElements):

    header_title = "Liquor"
    def __init__(self):
        self.filter_widget = FilterElements(self.header_title)
        self.list_widget = ListElements(self.header_title)

class AskACompanyPage(MainPageElements):

    header_title = "Ask a Company"
    def __init__(self):
        self.list_widget = ListElements(self.header_title)

class MobileAppPage(MainPageElements):

    header_title = "Mobile Apps"
    def __init__(self):
        self.list_widget = ListElements(self.header_title)

class ContactPage(MainPageElements):

    header_title = "Contact"
    def __init__(self):
        self.list_widget = ListElements(self.header_title)

class FAQPage(MainPageElements):

    header_title = "FAQ"
    def __init__(self):
        self.list_widget = ListElements(self.header_title)
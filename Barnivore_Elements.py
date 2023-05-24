

class FilterElements:

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

class MainPageElements:

    search_bar = "#big-search > input.ui-autocomplete-input"
    search_button = "#big-search > input[type=submit]:nth-child(2)"
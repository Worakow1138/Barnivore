

class FilterElements:

    filter_title = "//h2[text()='Filters']"
    filter_parent_element = "css:#content > div.filter"
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

    displaying_products = "#content > div:nth-child(5)"
    list_items = "#content > ul > li"

    def __init__(self, page_title):
        self.page_title = page_title.lower()
        self.list_header = f"//*[@id='content']/h1[contains(text(),'Listing {self.page_title}s')]"

class HomePage:

    search_bar = "#big-search > input.ui-autocomplete-input"
    search_button = "#big-search > input[type=submit]:nth-child(2)"

class SearchBarElements:

    find_booze_label = "#searchbox > form > label"
    mini_search_bar = "#searchbox > form > input.search"
    mini_search_button = "#searchbox > form > input[type=submit]:nth-child(3)"

class BeerPage:

    header_title = "Beer"
    def __init__(self):
        self.filter_widget = FilterElements(self.header_title)
        self.list_widget = ListElements(self.header_title)

class CiderPage:

    header_title = "Cider"
    def __init__(self):
        self.filter_widget = FilterElements(self.header_title)
        self.list_widget = ListElements(self.header_title)

class WinePage:

    header_title = "Wine"
    def __init__(self):
        self.filter_widget = FilterElements(self.header_title)
        self.list_widget = ListElements(self.header_title)

class LiquorPage:

    header_title = "Liquor"
    def __init__(self):
        self.filter_widget = FilterElements(self.header_title)
        self.list_widget = ListElements(self.header_title)

class AskACompanyPage:

    header_title = "Ask a Company"
    main_content_element = "div#content"
    question_element = "#questions > div.bodycopy"
    vegan_response_element = "#vegan_responses > div.bodycopy"
    non_vegan_response_element = "#nonvegan_responses > div.bodycopy"
    question_language_selector = "#questions > select"
    brand_name_input = "#txtBrandName"
    sender_name_input = "#txtYourName"
    non_vegan_response_language_selector = "#nonvegan_responses > select"
    vegan_response_language_selector = "#vegan_responses > select"
    ask_a_company_paragraph = """
    Ask a company
    Barnivore relies on input from readers like you to check (and double check!) with your favourite drink makers to see what's in their products.
    Checking with a company is simple. All you need to do is send them an email with one of our standard questions (see below) and forward us the response so we can add it to the list and help the rest of the world enjoy vegan drinks!
    If you get a response that isn't awesome, please (politely!) let them know how you feel! We've got a sample response you can use here.
    """.strip().replace("    ","")
    the_question_title = """
    The Question
    Here's the Standard Question we prefer everyone uses:
    """.strip().replace("    ","")
    the_response_title = """
    The Response
    If the company responds that everything's vegan friendly, be sure to thank them and let them know how important this is to you!
    If, on the other hand, the company isn't totally vegan friendly, it can help to send them a polite reminder. Here's an example you can use:
    IF THE PRODUCTS ARE NOT VEGAN:
    """.strip().replace("    ","")

    def __init__(self, language="English", brand_name = "[BRAND NAME]", your_name = "[YOUR NAME]"):
        self.brand_name = brand_name
        self.your_name = your_name

        self.the_question_dict = {
        "English": """Hi, I'm helping to update a global online directory (over 54,000 entries so far) of vegan-friendly alcohol, http://www.barnivore.com/, and I was hoping you could provide some information about """+brand_name+""".
        Does """+self.brand_name+""" contain any animal ingredients (such as milk/lactose/casein, eggs, cochineal, honey, animal-derived enzymes, etc) or are animal products used in the processing/filtration of the product (such as isinglass, gelatin, etc)?
        Also, is your product manufactured or bottled anywhere else in the world (by a sub-licensee, for instance) that might use a different processing system, thus making them unsuitable for vegans?
        Thanks,
        """+self.your_name+"""
        """,
        "French": """Bonjour,
        J'aide à la mise à jour d'un site Internet listant des boissons alcoolisées végétaliennes (www.barnivore.com ; plus de 54 000 inscriptions) et j'espérais que vous puissiez m’informer davantage sur vos produits.
        
        Est-ce que vos produits contiennent de quelconques produits d'origine animale (comme du lait/caséine/lactose, de la cochenille, des œufs, du miel, etc.) ou est-ce qu'un quelconque produit d'origine animale est utilisé dans la fabrication/filtration des produits (par exemple : du ichtyocolle, de la gélatine, etc.) ?
        
        Outre cela, vos produits sont-ils fabriqués ou embouteillés ailleurs dans le monde (sous licence, par exemple) qui pourrait utiliser un système de traitement différent, les rendant ainsi inadaptés aux végétaliens?
        Je vous remercie,
        """+self.your_name+"""
        (Thanks, Marie-Sarah, Monique, and Greg!)
        """
        }

        self.non_vegan_dict = {
        "English": """Thank you for the response. I am very disappointed to hear that you use animal products in your products. While I understand that these ingredients may not be present in the final product, I wish to avoid products that use these ingredients at all, as do many others.
        My understanding is that there are fining alternatives that do not utilize animal products, as evidenced by the wide variety of vegan-friendly companies listed on http://www.barnivore.com. Many wineries, breweries, and distillers are now using these techniques, and I would encourage you to look into these alternatives so that we can enjoy your wines in the future.
        """+self.your_name+"""
        (Thanks, Jennifer!)
        """
        }
        
        self.vegan_dict = {
        "English": """Thanks for letting me know, I'm very happy to learn that your products are vegan! I'm looking forward to enjoying them.
        Cheers,
        """+your_name+"""
        (Thanks, Tim!)
        """
        }
        
        self.set_language(language)

    def set_language(self, language):
        self.the_question_text = self.the_question_dict.get(language).strip().replace("        ","")
        self.non_vegan_response = self.non_vegan_dict.get(language).strip().replace("        ","")
        self.vegan_response = self.vegan_dict.get(language).strip().replace("        ","")

    def set_brand_name(self, new_brand_name):
        self.the_question_text = self.the_question_text.replace(self.brand_name, new_brand_name)
        self.brand_name = new_brand_name

    def set_your_name(self, new_name):
        self.the_question_text = self.the_question_text.replace(self.your_name, new_name)
        self.vegan_response = self.vegan_response.replace(self.your_name, new_name)
        self.non_vegan_response = self.non_vegan_response.replace(self.your_name, new_name)
        self.your_name = new_name


class MobileAppPage:

    header_title = "Mobile Apps"
    def __init__(self):
        self.list_widget = ListElements(self.header_title)

class ContactPage:

    header_title = "Contact"
    def __init__(self):
        self.list_widget = ListElements(self.header_title)

class FAQPage:

    header_title = "FAQ"
    def __init__(self):
        self.list_widget = ListElements(self.header_title)
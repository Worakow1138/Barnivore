

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
    main_content_element = "div#content"
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
    mobile_page_text = """
    Barnivore on the go
    An official Barnivore app is in the works! For details, check out our Patreon page.
    In the meantime, some developers have put some things together for you.
    Note that these apps use Barnivore data, but they're written by third parties and we don't have any connection to them. The information in the apps may be older than what's in Barnivore, and we don't have any input or control over how well they might work.
    To find one, go to your app store of choice and search for "vegan alcohol" or something similar, and you should find something. Maybe check it against a few recent Barnivore entries before you lock in to your home page :)
    Want to go old school? Technically, a printout is a mobile-friendly format, and we've got printable lists of beer, cider, wine, and liquor for you.
    We are working, ever so slowly, on our own official app, so stay tuned and wait for announcements on Twitter and Patreon.
    """.strip().replace("    ","")
    large_patreon_link = "//a[@href='https://www.patreon.com/barnivore' and text()='Patreon page']"
    small_patreon_link = "//a[@href='https://www.patreon.com/barnivore' and text()='Patreon']"
    twitter_link = "//a[@href='https://twitter.com/barnivore/' and text()='Twitter']"
    beer_link = "//a[@href='/printable/beer' and text()='beer']"
    cider_link = "//a[@href='/printable/cider' and text()='cider']"
    wine_link = "//a[@href='/printable/wine' and text()='wine']"
    liquor_link = "//a[@href='/printable/liquor' and text()='liquor']"


class ContactPage:

    header_title = "Contact"
    contact_page_text = """
    Contact Us
    Team Barnivore can be reached by emailing contact@barnivore.com.
    Want to know if a drink is vegan?
    Do these things:
    Use the search box
    We log all failed searches and look into what's missing.
    Contact the company yourself
    It's optional, but it's certainly faster! If you get some information for a check or a double check, please email the info to us and we'll add it to the list so everyone can enjoy it. We have easy instructions and an email template you can cut and paste available here.
    """.strip().replace("    ","")
    barnivore_contact_email = "//a[@href='mailto:contact@barnivore.com' and text()='contact@barnivore.com']"
    ask_a_company_link = "//a[@href='/askacompany' and text()='available here.']"

class FAQPage:

    header_title = "FAQ"
    can_you_check_text = """
    Do you know/Can you check if [product X] is vegan?
    Generally speaking, if a product isn't already on the list, we don't know any more about it than you do, and the only thing we can do is contact the company and ask them.
    We encourage people to do this themselves (it takes about the same amount of time as it takes to ask us) and pass on the information so we can update the list - it's not because we're lazy, but more because the more people that ask a company about their ingredients, the better the chance that a) we'll be able to see if the responses differ, which indicates the credibility of the company, and b) companies will notice that lots of people actually care what they put into their bodies, and they might actually change their products to reflect this.
    You can get the instructions on how to help out (including a sample question to ask) over on our ask a company page.
    """.strip().replace("    ","")
    where_info_text = """
    Where do you get your information?
    From you! In some cases we'll contact companies directly, and sometimes they even get in touch with us, but generally the stuff on the site came from readers like you who got in touch with a company they cared about, asked a few questions, and then forwarded the response to us.
    You can get the instructions on how to do that (including a sample question to ask) over on our contact page.
    The story doesn't end there however — after a while, the information gets out of date, or someone decides they just don't trust the answer that's on the site. That's where the double check comes into play, which is a powerful thing, because sometimes people... well, they don't lie, but they don't always know what they're talking about. That, and processes and recipes can change over time (and sometimes for the better!) It really makes a difference when people take the time to contact a company that's already in the list, just to be sure.
    """.strip().replace("    ","")
    vegan_friendly_text = """
    What do you mean by "Vegan Friendly"?
    We're glad you asked! In keeping with the user-submitted theme described above, we look at the question that was asked, the answer that came back, and judge the entry accordingly. We know we're not the sole decider of what counts as vegan, and that's where you come in...
    In some cases, the answer listed might not be enough for your liking. In that case, we recommend you move on to another alcohol, or better still, get in touch with the company, ask the questions that are bugging you, and then forward us the answers!
    This isn't a cop-out, just a reasonable compromise, in our opinion. We publish as much information as we can about each company, and if we get a reply that's clearly not good enough, we'll follow up ourselves before we add it, but the reality is that keeping up with user submissions can seriously cut into our drinking time (along with our every other part of the day time, you guys are awesome with your submissions!)
    """.strip().replace("    ","")
    add_filter_text = """
    Can you add a filter to just show the non-vegan drinks?
    We get why you'd want that, but here's the thing: while we've got a lot of listings, we don't have anywhere near a complete set of alcohol products produced worldwide (want to help with that?)
    If we showed a list of all the drinks we knew weren't vegan, yes, it'd help you see what to avoid, but it'd also suggest to a lot of readers that if it's not on the non-vegan list, it must be vegan, when the reality is we might just not know.
    And hey, while you're searching the vegan list, you might just find a new thing you wouldn't have otherwise tried, supporting more vegan-friendly companies. Which is cool.
    """.strip().replace("    ","")
    diatomaceous_earth_text = """
    Is Diatomaceous earth vegan?
    We rely on two backup sources for our guidelines on Diatomaceous earth and veganism: the first is Wikipedia, which actually clarifies (heh, "clarifies") that it's fossilized algae (specifically diatoms, which is where the name comes from.)
    Of course, we wouldn't recommend Wikipedia as a primary source for anything as important as this, so we also rely on the fine folks at the Vegetarian Resource Group, who've invested a lot of time and money into determining what is and what isn't vegan-friendly in the wide world of food. According to their research, DE is considered vegan.
    """.strip().replace("    ","")
    country_text = """
    Can a drink be vegan in one country and not in another?
    Unfortunately, yes. Some beverages (beers and liquors, primarily) are licensed to various regions and are then manufactured by different companies in those countries, and their filtration methods might vary. We see this in Australia a lot for some reason. Wherever we know about it, we make every effort to mention this practice, but as our information is based on what's sent to us we don't check beyond that.
    To reduce your risks, you have a few options: the first is to drink locally, as the information we receive is usually from a head office and not a licensee. The second, which goes for everything in Barnivore, is to double check for yourself, mentioning specifically where you live (and please pass on any info you find to us so we can help others!
    """.strip().replace("    ", "")
    glue_text = """
    What about the glue used on the bottle labels? Is that vegan?
    We don't specifically ask about label glue. As we say in "What do you mean by 'vegan friendly'," we picked a basic level of criteria to watch for, focusing for the most part on ingredients. All information we have on any product, including the full responses from the companies, are shown with each listing, so you can make your own decision.
    The general consensus has been that label glue was something not enough companies would even know about, and including it in the "standard question" would result in fewer responses of any kind to be returned. We didn't feel like this was a compromise; there are many vegans out there who don't worry about these things, and there are vegans who do. We're not the vegan police, and while this is the definition we've opted to go with, you may have another opinion and we respect that and invite you to investigate further.
    If label glue is a concern for you, there are a few options: you can drink from cans or opt for draft beer, or you can check with the companies you're interested in, and then share the information with the rest of the Barnivore community.
    """.strip().replace("    ","")
    sugar_text = """
    How about if the sugar is filtered with bone char?
    Same as above, basically. Again, if you want to know more about a company, we try to make it as easy as possible for you to reach out to them.
    """.strip().replace("    ","")
    cross_contamination_text = """
    What about cross contamination?
    Some companies will make multiple products on the same equipment, and some of those products may not be vegan. We treat this scenario the same as the "may contain" warnings in ingredients, which are generally there to warn people in case of allergies, and give those cases a pass.
    Yes, this means that there may be trace amounts of whatever was in the pipes the day before (assuming the cleaning process didn't get it all,) but we don't believe it's anyone's intent to sneak animal ingredients into your drink (vs something like isinglass, which is just gross.) If this concerns you from a purity perspective, we encourage you to frequent companies with a fully vegan product line.
    """.strip().replace("    ","")
    terms_of_use_text = """
    Can I use your information on my site/app/book?
    Most probably. There are just a few things we want to be careful about. Check out our Terms of Use section for details.
    Still have questions? Get in touch!
    """.strip().replace("    ","")

    ask_a_company_link = "//a[@href='/askacompany' and text()='ask a company page']"
    want_to_help_link = "//a[@href='/askacompany' and text()='want to help with that?']"

    contact_page_link = "//a[@href='/contact' and text()='contact page']"
    get_in_touch_link = "//a[@href='/contact' and text()='Get in touch!']"

    terms_of_use_link = "//a[@href='/terms' and text()='Terms of Use']"
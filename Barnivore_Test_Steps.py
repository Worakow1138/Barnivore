from moonrise import Moonrise
from Barnivore_Elements import *
import re
from typing import Union

class BarnivoreTestSteps(Moonrise):

    def load_page(self, header_title):
        """Attempt to select a link with a given header_title
        """
        self.click_element(f"link:{header_title}")

    def page_url_check(self, header_title):
        """Verify if the current URL matches the expected URL for the given header_title
        """
        assert self.moon_driver.current_url == f"https://www.barnivore.com/{CommonPageElements.url_mapping.get(header_title)}", "The current URL does not match the expected URL"

    def home_text_checks(self, home_page: HomePage):
        """Verify that text on the home page matches expected text.
        Verify that the "submit a check of your own" link is present.
        """
        self.get_web_element(home_page.home_title)
        first_column, second_column = self.get_web_elements(home_page.column_elements)[0].text, self.get_web_elements(home_page.column_elements)[1].text
        number_match = re.search(r'Our (\d+(?:,\d+)*) entries', second_column)
        number = number_match.group(1)
        home_page.second_column_text = home_page.second_column_text.replace("{}", number)
        assert home_page.first_column_text == first_column, "Column 1 of the home page text does not match expected text"
        assert home_page.second_column_text == second_column, "Column 2 of the home page text does not match expected text"
        self.get_web_element(home_page.ask_a_company_link)
    
    def filter_widget_checks(self, filter_widget: FilterElements):
        """Verify that the expected filter elements are present.
        """
        self.get_web_element(filter_widget.filter_title)
        self.get_web_element(filter_widget.filter_parent_element)
        for filter, letter in filter_widget.letter_filter_buttons.items():
            if filter != filter_widget.all_filter:
                self.get_web_element(letter)
        for veganosity in filter_widget.veganosity_filter_buttons.values():
            self.get_web_element(veganosity)
        if filter_widget.country_element:
            self.get_web_element(filter_widget.country_element)

    def listing_products_check(self, page: Union[BeerPage, CiderPage, WinePage, LiquorPage]):
        """Verify that the expected list elements are present for a default version of the expected page
        """
        assert self.get_text(page.list_widget.list_header) == f"Listing {page.header_title.lower()}s A-F", "List title did not display correctly"
        assert re.search(f"(Displaying products 1 - 50 of .* in total)", self.get_text(page.list_widget.displaying_products)), "List subtitle did not display correctly"
        assert len(self.get_web_elements(page.list_widget.list_items)) == 50, "Number of listed items did not equal 50"

    def search_elements_check(self, search_widget: SearchBarElements, value="", find_booze=False):
        """Verify that the search elements are present, with or without a pre-loaded value or the "Find Booze:" label
        """
        self.get_web_element(search_widget.search_bar)
        self.get_web_element(search_widget.search_button)
        if find_booze:
            assert self.get_text(search_widget.find_booze_label) == "Find Booze:", "Find Booze: label was not present"
        assert self.get_web_element(search_widget.search_bar).get_attribute("value") == value, "Search bar did not possess expected value"

    def company_text_checks(self, page: AskACompanyPage):
        """Verify that expected text is displayed on the "Ask a Company" page
        """
        content_text = self.get_text(CommonPageElements.main_content_element)
        assert page.ask_a_company_paragraph in content_text, "Ask a Company intro paragraph was not found"
        assert page.the_question_title in content_text, "The Qustion title was not found"
        assert page.the_response_title in content_text, "The Response title was not found"

        assert page.the_question_text in self.get_text(page.question_element), "Default Question text was not found"
        assert page.vegan_response in self.get_text(page.vegan_response_element), "Default Vegan Response text was not found"
        assert page.non_vegan_response in self.get_text(page.non_vegan_response_element), "Default Non Vegan Response text was not found"

        self.get_web_element(page.question_language_selector)
        self.get_web_element(page.vegan_response_language_selector)
        self.get_web_element(page.non_vegan_response_language_selector)
        self.get_web_element(page.brand_name_input)
        self.get_web_element(page.sender_name_input)

    def mobile_text_checks(self, page: MobileAppPage):
        """Verify that expected text is displayed on the "Mobile Apps" page
        """
        assert page.mobile_page_text in self.get_text(CommonPageElements.main_content_element), "'Barnivore on the go' text was not present"
        self.get_web_element(page.beer_link)
        self.get_web_element(page.cider_link)
        self.get_web_element(page.wine_link)
        self.get_web_element(page.liquor_link)

    def contact_text_checks(self, contact_page: ContactPage):
        """Verify that expected text is displayed on the "Contact" page
        """
        assert contact_page.contact_page_text in self.get_text(CommonPageElements.main_content_element), "'Contact Us' text was not present"
        self.get_web_element(contact_page.barnivore_contact_email)
        if contact_page.ask_a_company_link:
            self.get_web_element(contact_page.ask_a_company_link)

    def faq_text_checks(self, page: FAQPage):
        """Verify that expected text is displayed on the "FAQ" page
        """
        content_text = self.get_text(CommonPageElements.main_content_element)
        assert page.can_you_check_text in content_text, "Can you check text was not present"
        assert page.where_info_text in content_text, "Where Info text was not present"
        assert page.vegan_friendly_text in content_text, "What do you mean text was not present"
        assert page.add_filter_text in content_text, "Can you add a filter text was not present"
        assert page.diatomaceous_earth_text in content_text, "Diatomaceous earth text was not present"
        assert page.country_text in content_text, "Country text was not present"
        assert page.glue_text in content_text, "Glue text was not present"
        assert page.sugar_text in content_text, "Sugar text was not present"
        assert page.cross_contamination_text in content_text, "Cross contamination text was not present"
        assert page.terms_of_use_text in content_text, "Terms of use text was not present"

        self.get_web_element(page.ask_a_company_link)
        self.get_web_element(page.want_to_help_link)
        self.get_web_element(page.contact_page_link)
        self.get_web_element(page.get_in_touch_link)
        self.get_web_element(page.terms_of_use_link)

    def footer_checks(self):
        """Verify that expected elements are present in the footer
        """
        self.get_web_element(CommonPageElements.pdr_label)
        self.get_web_element(CommonPageElements.vegan_beer_label)
        self.get_web_element(CommonPageElements.vegan_wine_label)
        self.get_web_element(CommonPageElements.vegan_liquor_label)
        assert self.get_text(CommonPageElements.copyright_label) == 'Contents copyright © 2023 Thrust Labs. All rights reserved.\nContact Us | Terms of Use/Privacy Policy'

    def search_for_product(self, search_widget: SearchBarElements, product):
        """Search for a specific product via the search bar
        """
        self.input_text(search_widget.search_bar, product)
        self.click_element(search_widget.search_button)

    def results_are_from_company(self, company_name, list_widget: ListElements):
        """Verify that all displayed products are from a specific company
        """
        for product in self.get_web_elements(list_widget.list_items):
            assert company_name in list_widget.get_company_name(product), f"'{list_widget.get_company_name(product)}' does not contain '{company_name}'"

    def results_have_correct_labels(self, list_widget: ListElements, products: list):
        """Verify that all displayed products have the correct labels
        """
        for product in products:
            label = list_widget.get_label(product)
            assert label == list_widget.vegan_friendly or label == list_widget.not_vegan_friendly or label == list_widget.unknown, f"'{list_widget.get_product_name(product)}' does not a label of either {list_widget.vegan_friendly}, {list_widget.not_vegan_friendly}, or {list_widget.unknown}"
            assert list_widget.colors.get(label) == product.get_attribute("class"), f"{list_widget.get_product_name(product)}'s label did not match expected color"

    def results_have_links_to_products(self, list_widget: ListElements):
        """Verify that all displayed products have links to their product names
        """
        for product in self.get_web_elements(list_widget.list_items):
            self.get_web_element(f"link:{list_widget.get_product_name(product)}")

    def find_first_product_of_type(self, list_widget: ListElements, product_label: str):
        """Find and return the first product of given product_label
        """
        for product in self.get_web_elements(list_widget.list_items):
            if list_widget.get_label(product) == product_label and product.get_attribute("class") == list_widget.colors.get(product_label):
                return product
        else:
            print("Could not find any matching product")

    def load_product_page(self, product_name: str):
        """Attempt to click on a given product_name and verify that the correct product page is loaded
        """
        self.click_element(f"link:{product_name}")
        assert product_name.lower().replace(" ","-") in self.moon_driver.current_url, f'The current URL does not match {product_name.lower().replace(" ","-")}'

    def product_page_checks(self, product_widget: ProductElements, product_name: str, product_company:str, product_label: str):
        """Verify that a specified product_name is labeled as a given product_label in the product page's header.
        Verify that all other expected web elements are displayed on the product page
        """
        assert self.get_text(product_widget.product_header) == f"{product_name} is {product_label}", f"{self.get_text(product_widget.product_header)} does not list {product_label} in the header"

        self.get_web_element(f"//*[@id='content']/table/tbody/tr[1]/td[contains(text(), 'by {product_company}')]")
        self.get_web_element(product_widget.address_element)
        self.get_web_element(product_widget.phone_element)
        self.get_web_element(product_widget.email_element)
        self.get_web_element(product_widget.url_element)
        self.get_web_element(product_widget.checked_by_element)
        self.get_web_element(product_widget.double_checked_by_element)
        self.get_web_element(product_widget.added_element)
        self.get_web_element(product_widget.double_checked_time_element)
        self.get_web_element("//p[contains(text(),'Company email')]")

    def verify_list_in_alphabetical_order(self, list_widget: ListElements, products: list):
        """Verify that a given list of products is in alphabetical order
        """
        product_list = []
        for product in products:
            product_list.append(list_widget.get_product_name(product).lower())
        sorted_list = sorted(product_list)
        assert product_list == sorted_list, f"List is not in alphabetical order, go to {self.moon_driver.current_url} to confirm"

    def products_from_country(self, list_widget: ListElements, country_name: str, products: list):
        """Verify that a given list of products are all labeled as coming from a specified country_name
        """
        for product in products:
            assert country_name in list_widget.get_company_name(product), f"{list_widget.get_product_name(product)} does not have {country_name} in title"

    def verify_results_are_vegan(self, list_widget: ListElements, products: list):
        """Verify that all products within a given list are label as Vegan Friendly
        """
        for product in products:
            assert list_widget.get_label(product) == list_widget.vegan_friendly, f"{list_widget.get_label(product)} was not labeled as {list_widget.vegan_friendly}"

    def filtered_headers_check(self, page: Union[BeerPage, CiderPage, WinePage, LiquorPage], filter: str = "", country_name: str = None, vegan_only: bool = False):
        """Verify that the header title for a list of filtered products displays the expected text
        """
        header_title = page.header_title.lower()
        vegan_str = ""
        if vegan_only:
            vegan_str = "vegan"
        if country_name and filter == FilterElements.all_filter:
            assert self.get_text(page.list_widget.list_header) == f"Listing {filter.lower()} {vegan_str} {header_title}s from {country_name}".replace("  ", " "), f"{self.get_text(page.list_widget.list_header)} did not match 'Listing {filter.lower()} {vegan_str} {header_title}s from {country_name}'".replace("  ", " ")
        elif country_name:
            assert self.get_text(page.list_widget.list_header) == f"Listing {vegan_str} {header_title}s {filter} from {country_name}".replace("  ", " "), f"{self.get_text(page.list_widget.list_header)} did not match 'Listing {vegan_str} {header_title}s {filter} from {country_name}'".replace("  ", " ")
        else:
            assert self.get_text(page.list_widget.list_header) == f"Listing {vegan_str} {header_title}s {filter}".replace("  ", " "), f"{self.get_text(page.list_widget.list_header)} did not match 'Listing {vegan_str} {header_title}s {filter}'".replace("  ", " ")

        subheader_text = self.get_text(page.list_widget.displaying_products)
        if "all" in subheader_text:
            assert re.search(f"(Displaying all .* products)", subheader_text), "'Displaying all products' text was not found"
        else:
            assert re.search(f"(Displaying products .* - .* of .* in total)", subheader_text), "'Displaying products from x to y in of z in total' was not found"

    def verify_results_are_within_filtered_range(self, list_widget: ListElements, filter: str, products: list):
        """Verify that filtered results are within the filtered range
        """
        for product in products:
            assert list_widget.get_product_name(product)[0] >= filter.split("-")[0], f'{list_widget.get_product_name(product)} begins with a charcter that comes before {filter.split("-")[0]}'
            assert list_widget.get_product_name(product)[0] <= filter.split("-")[1], f'{list_widget.get_product_name(product)} begins with a charcter that comes after {filter.split("-")[1]}'

    def filter_test_steps(self, page: Union[BeerPage, CiderPage, WinePage, LiquorPage], filter: str, country: str = None, vegan_only: bool = False):
        """Test steps for filtering data and verifying results
        """
        self.click_element(f"link:{filter}")
        if vegan_only:
            self.click_element(f"link:{page.filter_widget.only_vegan_filter}")
        else:
            self.click_element(f"link:{page.filter_widget.everything_filter}")

        products = self.get_web_elements(page.list_widget.list_items)

        assert len(self.get_web_elements(page.list_widget.list_items)) <= 50, "List of products was longer than 50"
        if filter != page.filter_widget.all_filter:
            self.verify_results_are_within_filtered_range(page.list_widget, filter, products)
        if vegan_only:
            self.verify_results_are_vegan(page.list_widget, products)
        self.filtered_headers_check(page, filter, country, vegan_only)
        self.verify_list_in_alphabetical_order(page.list_widget, products)
        if country:
            self.products_from_country(page.list_widget, country, products)
        self.results_have_correct_labels(page.list_widget, products)

        self.search_elements_check(page.search_widget, find_booze=True)
        self.footer_checks()

    def set_page_brand_and_sender_names(self, ask_a_company_page: AskACompanyPage, brand_name: str, name: str):
        """Clear the "Brand Name" and "Your Name" input fields, enter given brand_name and name data, 
        and set the ask_a_company_page object to expect text from the given brand_name and name
        """
        self.get_web_element(ask_a_company_page.brand_name_input).clear()
        self.get_web_element(ask_a_company_page.sender_name_input).clear()
        self.input_text(ask_a_company_page.brand_name_input, brand_name)
        self.input_text(ask_a_company_page.sender_name_input, name)
        ask_a_company_page.set_brand_name(brand_name)
        ask_a_company_page.set_your_name(name)

    def select_language_options(self, ask_a_company_page: AskACompanyPage, language: str, question: bool = True, non_vegan_response: bool = True, vegan_response: bool = True):
        """Set all requested language options to the specified language
        """
        ask_a_company_page.set_language(language)

        if question:
            self.select_from_list_by_label(ask_a_company_page.question_language_selector, language)
        if non_vegan_response:
            self.select_from_list_by_label(ask_a_company_page.non_vegan_response_language_selector, language)
        if vegan_response:
            self.select_from_list_by_label(ask_a_company_page.vegan_response_language_selector, language)

    def ask_a_company_text_checks(self, ask_a_company_page: AskACompanyPage, question: bool = True, non_vegan_response: bool = True, vegan_response: bool = True):
        """Verify that all requested, mutable text fields display expected text 
        """
        if question:
            assert self.get_text(ask_a_company_page.question_element) == ask_a_company_page.the_question_text, "Question field does not match expected text"
        if non_vegan_response:
            assert self.get_text(ask_a_company_page.non_vegan_response_element) == ask_a_company_page.non_vegan_response, "Non Vegan Response field does not match expected text"
        if vegan_response:
            assert self.get_text(ask_a_company_page.vegan_response_element) == ask_a_company_page.vegan_response, "Vegan Response field does not match expected text"

    def ask_a_company_test_steps(self, ask_a_company_page: AskACompanyPage, language: str, brand_name: str, your_name: str, question: bool = True, non_vegan_response: bool = True, vegan_response: bool = True):
        """Test Steps for perfomring Ask a Company Page tests
        """
        self.select_language_options(ask_a_company_page, language, question=question, non_vegan_response=non_vegan_response, vegan_response=vegan_response)
        self.ask_a_company_text_checks(ask_a_company_page, question=question, non_vegan_response=non_vegan_response, vegan_response=vegan_response)
        self.set_page_brand_and_sender_names(ask_a_company_page, brand_name, your_name)
        self.ask_a_company_text_checks(ask_a_company_page, question=question, non_vegan_response=non_vegan_response, vegan_response=vegan_response)

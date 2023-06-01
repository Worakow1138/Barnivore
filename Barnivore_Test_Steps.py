from moonrise import Moonrise
from Barnivore_Elements import *
import re
from typing import Union

class BarnivoreTestSteps(Moonrise):

    def load_page(self, header_title):
        self.click_element(f"link:{header_title}")

    def page_url_check(self, header_title):
        assert self.moon_driver.current_url == f"https://www.barnivore.com/{CommonPageElements.url_mapping.get(header_title)}"

    def home_text_checks(self, home_page: HomePage):
        self.get_web_element(home_page.home_title)
        first_column, second_column = self.get_web_elements(home_page.column_elements)[0], self.get_web_elements(home_page.column_elements)[1]
        assert home_page.first_column_text == first_column.text
        assert home_page.second_column_text == second_column.text
        self.get_web_element(home_page.ask_a_company_link)
    
    def filter_widget_checks(self, filter_widget: FilterElements):
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
        assert self.get_web_element(page.list_widget.list_header).text == f"Listing {page.header_title.lower()}s A-F"
        assert re.search(f"(Displaying products 1 - 50 of .* in total)", self.get_text(page.list_widget.displaying_products))
        assert len(self.get_web_elements(page.list_widget.list_items)) == 50

    def search_elements_check(self, search_widget: SearchBarElements, value="", find_booze=False):
        self.get_web_element(search_widget.search_bar)
        self.get_web_element(search_widget.search_button)
        if find_booze:
            assert self.get_text(search_widget.find_booze_label) == "Find Booze:"
        assert self.get_web_element(search_widget.search_bar).get_attribute("value") == value

    def company_text_checks(self, page: AskACompanyPage):
        content_text = self.get_text(CommonPageElements.main_content_element)
        assert page.ask_a_company_paragraph in content_text
        assert page.the_question_title in content_text
        assert page.the_response_title in content_text

        assert page.the_question_text in self.get_text(page.question_element)
        assert page.vegan_response in self.get_text(page.vegan_response_element)
        assert page.non_vegan_response in self.get_text(page.non_vegan_response_element)

        self.get_web_element(page.question_language_selector)
        self.get_web_element(page.vegan_response_language_selector)
        self.get_web_element(page.non_vegan_response_language_selector)
        self.get_web_element(page.brand_name_input)
        self.get_web_element(page.sender_name_input)

    def mobile_text_checks(self, page: MobileAppPage):
        assert page.mobile_page_text in self.get_text(CommonPageElements.main_content_element)
        self.get_web_element(page.beer_link)
        self.get_web_element(page.cider_link)
        self.get_web_element(page.wine_link)
        self.get_web_element(page.liquor_link)

    def contact_text_checks(self, contact_page: ContactPage):
        assert contact_page.contact_page_text in self.get_text(CommonPageElements.main_content_element)
        self.get_web_element(contact_page.barnivore_contact_email)
        if contact_page.ask_a_company_link:
            self.get_web_element(contact_page.ask_a_company_link)

    def faq_text_checks(self, page: FAQPage):
        content_text = self.get_text(CommonPageElements.main_content_element)
        assert page.can_you_check_text in content_text
        assert page.where_info_text in content_text
        assert page.vegan_friendly_text in content_text
        assert page.add_filter_text in content_text
        assert page.diatomaceous_earth_text in content_text
        assert page.country_text in content_text
        assert page.glue_text in content_text
        assert page.sugar_text in content_text
        assert page.cross_contamination_text in content_text
        assert page.terms_of_use_text in content_text

        self.get_web_element(page.ask_a_company_link)
        self.get_web_element(page.want_to_help_link)
        self.get_web_element(page.contact_page_link)
        self.get_web_element(page.get_in_touch_link)
        self.get_web_element(page.terms_of_use_link)

    def footer_checks(self):
        self.get_web_element(CommonPageElements.pdr_label)
        self.get_web_element(CommonPageElements.vegan_beer_label)
        self.get_web_element(CommonPageElements.vegan_wine_label)
        self.get_web_element(CommonPageElements.vegan_liquor_label)
        assert self.get_text(CommonPageElements.copyright_label) == 'Contents copyright © 2023 Thrust Labs. All rights reserved.\nContact Us | Terms of Use/Privacy Policy'

    def search_for_product(self, search_widget: SearchBarElements, product):
        self.input_text(search_widget.search_bar, product)
        self.click_element(search_widget.search_button)

    def results_are_from_company(self, company_name, list_widget: ListElements):
        for product in self.get_web_elements(list_widget.list_items):
            assert company_name in list_widget.get_company_name(product)

    def results_have_correct_labels(self, list_widget: ListElements, products: list):
        for product in products:
            label = list_widget.get_label(product)
            assert label == list_widget.vegan_friendly or label == list_widget.not_vegan_friendly or label == list_widget.unknown
            assert list_widget.colors.get(label) == product.get_attribute("class"), f"{list_widget.get_product_name(product)} did not match"

    def results_have_links_to_products(self, list_widget: ListElements):
        for product in self.get_web_elements(list_widget.list_items):
            self.get_web_element(f"link:{list_widget.get_product_name(product)}")

    def find_first_product_of_type(self, list_widget: ListElements, product_label: str):
        for product in self.get_web_elements(list_widget.list_items):
            if list_widget.get_label(product) == product_label and product.get_attribute("class") == list_widget.colors.get(product_label):
                return product
        else:
            print("Could not find any matching product")

    def load_product_page(self, product_name: str):
        self.click_element(f"link:{product_name}")
        assert product_name.lower().replace(" ","-") in self.moon_driver.current_url

    def product_page_checks(self, product_widget: ProductElements, product_name: str, product_company:str, product_label: str):
        assert self.get_text(product_widget.product_header) == f"{product_name} is {product_label}"

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

    def list_in_alphabetical_order(self, list_widget: ListElements, products: list):
        product_list = []
        for product in products:
            product_list.append(list_widget.get_product_name(product).lower())
        sorted_list = sorted(product_list)
        assert product_list == sorted_list, f"List is not in alphabetical order, go to {self.moon_driver.current_url} to confirm"

    def products_from_country(self, list_widget: ListElements, country_name: str, products: list):
        for product in products:
            assert country_name in list_widget.get_company_name(product), f"{list_widget.get_product_name(product)} does not have {country_name} in title"

    def results_are_vegan(self, list_widget: ListElements, products: list):
        for product in products:
            assert list_widget.get_label(product) == list_widget.vegan_friendly

    def filtered_headers_check(self, page: Union[BeerPage, CiderPage, WinePage, LiquorPage], filter: str = "", country_name: str = None, vegan_only: bool = False):
        header_title = page.header_title.lower()
        vegan_str = ""
        if vegan_only:
            vegan_str = "vegan"
        if country_name and filter == FilterElements.all_filter:
            assert self.get_text(page.list_widget.list_header) == f"Listing {filter.lower()} {vegan_str} {header_title}s from {country_name}".replace("  ", " ") 
        elif country_name:
            assert self.get_text(page.list_widget.list_header) == f"Listing {vegan_str} {header_title}s {filter} from {country_name}".replace("  ", " ")
        else:
            assert self.get_text(page.list_widget.list_header) == f"Listing {vegan_str} {header_title}s {filter}".replace("  ", " ")

        subheader_text = self.get_text(page.list_widget.displaying_products)
        if "all" in subheader_text:
            assert re.search(f"(Displaying all .* products)", subheader_text)
        else:
            assert re.search(f"(Displaying products .* - .* of .* in total)", subheader_text)

    def results_are_within_filtered_range(self, list_widget: ListElements, filter: str, products: list):
        for product in products:
            assert list_widget.get_product_name(product)[0] >= filter.split("-")[0]
            assert list_widget.get_product_name(product)[0] <= filter.split("-")[1], list_widget.get_product_name(product)

    def filter_test_steps(self, page: Union[BeerPage, CiderPage, WinePage, LiquorPage], filter: str, country: str = None):
        self.click_element(f"link:{filter}")

        self.click_element(f"link:{page.filter_widget.everything_filter}")
        assert len(self.get_web_elements(page.list_widget.list_items)) <= 50
        self.filtered_headers_check(page, filter, country)

        self.click_element(f"link:{page.filter_widget.only_vegan_filter}")
        assert len(self.get_web_elements(page.list_widget.list_items)) <= 50
        self.filtered_headers_check(page, filter, country, vegan_only=True)

        self.search_elements_check(page.search_widget, find_booze=True)
        self.footer_checks()

    def set_page_brand_and_sender_names(self, ask_a_company_page: AskACompanyPage):
        self.get_web_element(ask_a_company_page.brand_name_input).clear()
        self.get_web_element(ask_a_company_page.sender_name_input).clear()
        self.input_text(ask_a_company_page.brand_name_input, "Victory")
        self.input_text(ask_a_company_page.sender_name_input, "Drinker")
        ask_a_company_page.set_brand_name("Victory")
        ask_a_company_page.set_your_name("Drinker")
    
    def set_question_language(self, ask_a_company_page: AskACompanyPage, language: str):
        ask_a_company_page.set_language(language)
        self.select_from_list_by_label(ask_a_company_page.question_language_selector, language)

        assert self.get_text(ask_a_company_page.question_element) ==  ask_a_company_page.the_question_text

        self.set_page_brand_and_sender_names(ask_a_company_page)

        assert self.get_text(ask_a_company_page.question_element) ==  ask_a_company_page.the_question_text

    def set_response_language(self, ask_a_company_page: AskACompanyPage, language: str):
        ask_a_company_page.set_language(language)
        self.select_from_list_by_label(ask_a_company_page.non_vegan_response_language_selector, language)
        self.select_from_list_by_label(ask_a_company_page.vegan_response_language_selector, language)

        assert self.get_text(ask_a_company_page.non_vegan_response_element) == ask_a_company_page.non_vegan_response
        assert self.get_text(ask_a_company_page.vegan_response_element) == ask_a_company_page.vegan_response

        self.set_page_brand_and_sender_names(ask_a_company_page)

        assert self.get_text(ask_a_company_page.non_vegan_response_element) == ask_a_company_page.non_vegan_response
        assert self.get_text(ask_a_company_page.vegan_response_element) == ask_a_company_page.vegan_response
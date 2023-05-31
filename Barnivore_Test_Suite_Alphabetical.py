def filter_test_steps(self, page: Union[BeerPage, CiderPage, WinePage, LiquorPage], filter: str, country: str = None, vegan_only: bool = False):
        self.click_element(f"link:{filter}")
        if vegan_only:
            self.click_element(f"link:{page.filter_widget.only_vegan_filter}")
        else:
            self.click_element(f"link:{page.filter_widget.everything_filter}")

        products = self.get_web_elements(page.list_widget.list_items)

        assert len(self.get_web_elements(page.list_widget.list_items)) <= 50
        if filter != page.filter_widget.all_filter:
            self.results_are_within_filtered_range(page.list_widget, filter, products)
        if vegan_only:
            self.results_are_vegan(page.list_widget, products)
        self.filtered_headers_check(page, filter, country, vegan_only)
        self.list_in_alphabetical_order(page.list_widget, products)
        if country:
            self.products_from_country(page.list_widget, country, products)
        self.results_have_correct_labels(page.list_widget, products)

        self.search_elements_check(page.search_widget, find_booze=True)
        self.footer_checks()
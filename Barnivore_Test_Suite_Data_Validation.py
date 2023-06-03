from moonrise import Moonrise
from Barnivore_Test_Steps import BarnivoreTestSteps
from Barnivore_Elements import *

class DataValidationTestSuite(BarnivoreTestSteps):
    """Validatate that filters on the "Beer", "Cider", "Wine", and "Liquor" pages correctly filter available product data and that this data is presented alphabetically
    """

    Moonrise.default_timeout = 5

    def suite_setup(self):
        self.open_browser("chrome", "--headless", "--no-sandbox", shutter_speed=0.5)
        self.moon_driver.set_window_size(1920, 1080)
        return super().suite_setup()
    
    def suite_teardown(self):
        self.cleanup_browser()
        return super().suite_teardown()

class BeerPageTestsUSA(DataValidationTestSuite):

    def suite_setup(self):
        self.beer_page = BeerPage()
        self.country = "USA"
        super().suite_setup()
        self.navigate_to_page("barnivore.com")
        self.load_page(self.beer_page.header_title)
        self.filter_widget_checks(self.beer_page.filter_widget)
    
    def test_setup(self):
        self.select_from_list_by_label(self.beer_page.filter_widget.region_element, self.country)
        return super().test_setup()
    
    @Moonrise.test
    def all_filter(self):
        self.filter_test_steps(self.beer_page, self.beer_page.filter_widget.all_filter, self.country)

    @Moonrise.test
    def all_filter_vegan(self):
        self.filter_test_steps(self.beer_page, self.beer_page.filter_widget.all_filter, self.country, vegan_only=True)

    @Moonrise.test
    def zero_nine_filter(self):
        self.filter_test_steps(self.beer_page, self.beer_page.filter_widget.zero_nine_filter, self.country)

    @Moonrise.test
    def zero_nine_filter_vegan(self):
        self.filter_test_steps(self.beer_page, self.beer_page.filter_widget.zero_nine_filter, self.country, vegan_only=True)

    @Moonrise.test
    def a_f_filter(self):
        self.filter_test_steps(self.beer_page, self.beer_page.filter_widget.a_f_filter, self.country)

    @Moonrise.test
    def a_f_filter_vegan(self):
        self.filter_test_steps(self.beer_page, self.beer_page.filter_widget.a_f_filter, self.country, vegan_only=True)

    @Moonrise.test
    def g_l_filter(self):
        self.filter_test_steps(self.beer_page, self.beer_page.filter_widget.g_l_filter, self.country)

    @Moonrise.test
    def g_l_filter_vegan(self):
        self.filter_test_steps(self.beer_page, self.beer_page.filter_widget.g_l_filter, self.country, vegan_only=True)

    @Moonrise.test
    def m_r_filter(self):
        self.filter_test_steps(self.beer_page, self.beer_page.filter_widget.m_r_filter, self.country)

    @Moonrise.test
    def m_r_filter_vegan(self):
        self.filter_test_steps(self.beer_page, self.beer_page.filter_widget.m_r_filter, self.country, vegan_only=True)

    @Moonrise.test
    def s_t_filter(self):
        self.filter_test_steps(self.beer_page, self.beer_page.filter_widget.s_t_filter, self.country)

    @Moonrise.test
    def s_t_filter_vegan(self):
        self.filter_test_steps(self.beer_page, self.beer_page.filter_widget.s_t_filter, self.country, vegan_only=True)

    @Moonrise.test
    def u_z_filter(self):
        self.filter_test_steps(self.beer_page, self.beer_page.filter_widget.u_z_filter, self.country)

    @Moonrise.test
    def u_z_filter_vegan(self):
        self.filter_test_steps(self.beer_page, self.beer_page.filter_widget.u_z_filter, self.country, vegan_only=True)

class CiderPageTestsUSA(DataValidationTestSuite):

    def suite_setup(self):
        self.cider_page = CiderPage()
        self.country = "USA"
        super().suite_setup()
        self.navigate_to_page("barnivore.com")
        self.load_page(self.cider_page.header_title)
        self.filter_widget_checks(self.cider_page.filter_widget)
    
    def test_setup(self):
        self.select_from_list_by_label(self.cider_page.filter_widget.region_element, self.country)
        return super().test_setup()
    
    @Moonrise.test
    def all_filter(self):
        self.filter_test_steps(self.cider_page, self.cider_page.filter_widget.all_filter, self.country)

    @Moonrise.test
    def all_filter_vegan(self):
        self.filter_test_steps(self.cider_page, self.cider_page.filter_widget.all_filter, self.country, vegan_only=True)

    @Moonrise.test
    def zero_nine_filter(self):
        self.filter_test_steps(self.cider_page, self.cider_page.filter_widget.zero_nine_filter, self.country)

    @Moonrise.test
    def zero_nine_filter_vegan(self):
        self.filter_test_steps(self.cider_page, self.cider_page.filter_widget.zero_nine_filter, self.country, vegan_only=True)

    @Moonrise.test
    def a_f_filter(self):
        self.filter_test_steps(self.cider_page, self.cider_page.filter_widget.a_f_filter, self.country)

    @Moonrise.test
    def a_f_filter_vegan(self):
        self.filter_test_steps(self.cider_page, self.cider_page.filter_widget.a_f_filter, self.country, vegan_only=True)

    @Moonrise.test
    def g_l_filter(self):
        self.filter_test_steps(self.cider_page, self.cider_page.filter_widget.g_l_filter, self.country)

    @Moonrise.test
    def g_l_filter_vegan(self):
        self.filter_test_steps(self.cider_page, self.cider_page.filter_widget.g_l_filter, self.country, vegan_only=True)

    @Moonrise.test
    def m_r_filter(self):
        self.filter_test_steps(self.cider_page, self.cider_page.filter_widget.m_r_filter, self.country)

    @Moonrise.test
    def m_r_filter_vegan(self):
        self.filter_test_steps(self.cider_page, self.cider_page.filter_widget.m_r_filter, self.country, vegan_only=True)

    @Moonrise.test
    def s_t_filter(self):
        self.filter_test_steps(self.cider_page, self.cider_page.filter_widget.s_t_filter, self.country)

    @Moonrise.test
    def s_t_filter_vegan(self):
        self.filter_test_steps(self.cider_page, self.cider_page.filter_widget.s_t_filter, self.country, vegan_only=True)

    @Moonrise.test
    def u_z_filter(self):
        self.filter_test_steps(self.cider_page, self.cider_page.filter_widget.u_z_filter, self.country)

    @Moonrise.test
    def u_z_filter_vegan(self):
        self.filter_test_steps(self.cider_page, self.cider_page.filter_widget.u_z_filter, self.country, vegan_only=True)

class WinePageTestsUSA(DataValidationTestSuite):

    def suite_setup(self):
        self.wine_page = WinePage()
        self.country = "USA"
        super().suite_setup()
        self.navigate_to_page("barnivore.com")
        self.load_page(self.wine_page.header_title)
        self.filter_widget_checks(self.wine_page.filter_widget)
    
    def test_setup(self):
        self.select_from_list_by_label(self.wine_page.filter_widget.region_element, self.country)
        return super().test_setup()
    
    @Moonrise.test
    def all_filter(self):
        self.filter_test_steps(self.wine_page, self.wine_page.filter_widget.all_filter, self.country)

    @Moonrise.test
    def all_filter_vegan(self):
        self.filter_test_steps(self.wine_page, self.wine_page.filter_widget.all_filter, self.country, vegan_only=True)

    @Moonrise.test
    def zero_nine_filter(self):
        self.filter_test_steps(self.wine_page, self.wine_page.filter_widget.zero_nine_filter, self.country)

    @Moonrise.test
    def zero_nine_filter_vegan(self):
        self.filter_test_steps(self.wine_page, self.wine_page.filter_widget.zero_nine_filter, self.country, vegan_only=True)

    @Moonrise.test
    def a_f_filter(self):
        self.filter_test_steps(self.wine_page, self.wine_page.filter_widget.a_f_filter, self.country)

    @Moonrise.test
    def a_f_filter_vegan(self):
        self.filter_test_steps(self.wine_page, self.wine_page.filter_widget.a_f_filter, self.country, vegan_only=True)

    @Moonrise.test
    def g_l_filter(self):
        self.filter_test_steps(self.wine_page, self.wine_page.filter_widget.g_l_filter, self.country)

    @Moonrise.test
    def g_l_filter_vegan(self):
        self.filter_test_steps(self.wine_page, self.wine_page.filter_widget.g_l_filter, self.country, vegan_only=True)

    @Moonrise.test
    def m_r_filter(self):
        self.filter_test_steps(self.wine_page, self.wine_page.filter_widget.m_r_filter, self.country)

    @Moonrise.test
    def m_r_filter_vegan(self):
        self.filter_test_steps(self.wine_page, self.wine_page.filter_widget.m_r_filter, self.country, vegan_only=True)

    @Moonrise.test
    def s_t_filter(self):
        self.filter_test_steps(self.wine_page, self.wine_page.filter_widget.s_t_filter, self.country)

    @Moonrise.test
    def s_t_filter_vegan(self):
        self.filter_test_steps(self.wine_page, self.wine_page.filter_widget.s_t_filter, self.country, vegan_only=True)

    @Moonrise.test
    def u_z_filter(self):
        self.filter_test_steps(self.wine_page, self.wine_page.filter_widget.u_z_filter, self.country)

    @Moonrise.test
    def u_z_filter_vegan(self):
        self.filter_test_steps(self.wine_page, self.wine_page.filter_widget.u_z_filter, self.country, vegan_only=True)

class LiquorPageTests(DataValidationTestSuite):

    def suite_setup(self):
        self.liquor_page = LiquorPage()
        super().suite_setup()
        self.navigate_to_page("barnivore.com")
        self.load_page(self.liquor_page.header_title)
        self.filter_widget_checks(self.liquor_page.filter_widget)

    @Moonrise.test
    def zero_nine_filter(self):
        self.filter_test_steps(self.liquor_page, self.liquor_page.filter_widget.zero_nine_filter)

    @Moonrise.test
    def zero_nine_filter_vegan(self):
        self.filter_test_steps(self.liquor_page, self.liquor_page.filter_widget.zero_nine_filter, vegan_only=True)

    @Moonrise.test
    def a_f_filter(self):
        self.filter_test_steps(self.liquor_page, self.liquor_page.filter_widget.a_f_filter)

    @Moonrise.test
    def a_f_filter_vegan(self):
        self.filter_test_steps(self.liquor_page, self.liquor_page.filter_widget.a_f_filter, vegan_only=True)

    @Moonrise.test
    def g_l_filter(self):
        self.filter_test_steps(self.liquor_page, self.liquor_page.filter_widget.g_l_filter)

    @Moonrise.test
    def g_l_filter_vegan(self):
        self.filter_test_steps(self.liquor_page, self.liquor_page.filter_widget.g_l_filter, vegan_only=True)

    @Moonrise.test
    def m_r_filter(self):
        self.filter_test_steps(self.liquor_page, self.liquor_page.filter_widget.m_r_filter)

    @Moonrise.test
    def m_r_filter_vegan(self):
        self.filter_test_steps(self.liquor_page, self.liquor_page.filter_widget.m_r_filter, vegan_only=True)

    @Moonrise.test
    def s_t_filter(self):
        self.filter_test_steps(self.liquor_page, self.liquor_page.filter_widget.s_t_filter)

    @Moonrise.test
    def s_t_filter_vegan(self):
        self.filter_test_steps(self.liquor_page, self.liquor_page.filter_widget.s_t_filter, vegan_only=True)

    @Moonrise.test
    def u_z_filter(self):
        self.filter_test_steps(self.liquor_page, self.liquor_page.filter_widget.u_z_filter)

    @Moonrise.test
    def u_z_filter_vegan(self):
        self.filter_test_steps(self.liquor_page, self.liquor_page.filter_widget.u_z_filter, vegan_only=True)
from carritus import Catalog, Carritus
from nose.tools import assert_equals


class TestCarritus():

    catalog = None
    carritus = None

    @classmethod
    def setup_class(cls):
        cls.catalog = Catalog()
        cls.catalog.add_item_catalog('potatoes', 2.5)
        cls.catalog.add_item_catalog('tralara', 1.5)

    def setup(self):
        self.carritus = Carritus(self.catalog)

    def teardown(self):
        self.carritus.clear()

    def test_carritus_is_empty(self):
        assert_equals(len(self.carritus.list_items()), 0,(self.carritus.list_items()))

    def test_carritus_has_one_item(self):
        self.carritus.add_item('potatoes', 2)
        assert_equals(len(self.carritus.list_items()), 1)

    def test_calculate_final_price(self):

        self.carritus.add_item('potatoes', 2)
        self.carritus.add_item('tralara', 3)
        assert_equals(self.carritus.calculate_total_price(), 9.5)

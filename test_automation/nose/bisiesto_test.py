
from bisiesto import es_bisiesto
from nose.tools import assert_equals


class TestEsBisiesto():

    def test_year_is_bisiesto(self):
        assert_equals(es_bisiesto(2020), 'Es bisiesto')
        assert_equals(es_bisiesto(2000), 'Es bisiesto', es_bisiesto(2000))

    def test_year_is_not_bisiesto(self):
        assert_equals(es_bisiesto(2100), 'No es bisiesto')
        assert_equals(es_bisiesto(2019), 'No es bisiesto')
        assert_equals(es_bisiesto(2018), 'No es bisiesto')

    def test_incorrect_type(self):
        assert_equals(es_bisiesto('a'), "Error: Should be a integer")
        assert_equals(es_bisiesto(1.0), "Error: Should be a integer")
        assert_equals(es_bisiesto(-5), "Error: Should be a positive number")
 
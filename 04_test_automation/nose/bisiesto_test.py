
from bisiesto import es_bisiesto
from nose.tools import assert_equals


class TestEsBisiesto():

    def test_year_is_bisiesto(self):
        assert_equals(es_bisiesto(2020), 'Is leap year')
        assert_equals(es_bisiesto(2000), 'Is leap year', es_bisiesto(2000))

    def test_year_is_not_bisiesto(self):
        assert_equals(es_bisiesto(2100), 'Is not leap year')
        assert_equals(es_bisiesto(2019), 'Is not leap year')
        assert_equals(es_bisiesto(2018), 'Is not leap year')

    def test_incorrect_type(self):
        assert_equals(es_bisiesto('a'), "Error: Should be a integer")
        assert_equals(es_bisiesto(1.0), "Error: Should be a integer")
        assert_equals(es_bisiesto(-5), "Error: Should be a positive number")

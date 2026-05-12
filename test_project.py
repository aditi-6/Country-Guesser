import pytest # type: ignore
import time
from project import get_country, give_hint, validate_guess, calculate_score 


def test_give_hint():
    country =({"capital": ["Paris"], "region": "Europe", "population": 67000000})
    assert give_hint (country, "capital") == "Paris"  
    assert give_hint(country, "region") == "Europe"
    assert give_hint(country, "population") == 67000000


def test_calculate_score():
    start_time= time.time()-10
    assert calculate_score(start_time, []) == pytest.approx(900, abs=5)
    assert calculate_score(start_time, ["population"]) == pytest.approx(800, abs=5)


    
def test_validate_guess():
    country = {"name": {"common": "France"}}
    assert validate_guess("france", country) == True
    assert validate_guess("FRANCE", country) == True
    assert validate_guess("Germany", country) == False
   
import pytest
from is_even import is_even
class TestIsEven():
    
    def test_even_number(self):
        assert is_even(6) == True

    def test_odd_number(self):
        assert is_even(7) == False
        

if __name__ == '__main__':
    pytest.main()

import pytest
import postcode

postcode.load_database()

positive_values = [
    'ec1a 1bb',  # all lower
    'EC1A 1BB',  # special cases
    'BS98 1TL',
    'CF10 1BH',
    'CV4 8UW',
    'DA1 1RT',
    'SW1W 0NY',  # normal
    'M1 1AE',
    'B33 8TH',
    'CR2 6XH',
    'DN55 1PT',
    'PO16 7GZ',
    'GU16 7HF'
]

negative_values = [
    'QN55 1PT',   # Bad letter in 1st position
    'QN55 1PT',   # Bad letter in 1st position
    'DI55 1PT',   # Bad letter in 2nd position
    'W1Z 0AX',    # Bad letter in 3rd position
    'EC1Z 1BB',   # Bad letter in 4th position
    'DN55 1CT',   # Bad letter in 2nd group
    'A11A 1AA',   # Invalid digits in 1st group
    'AA11A 1AA',  # 1st group too long
    'AA11 1AAA',  # 2nd group too long
    'AA11 1AAA',  # 2nd group too long
    'AAA 1AA',    # No digit in 1st group
    'AA 1AA',     # No digit in 1st group
    'A 1AA',      # No digit in 1st group
    '1A 1AA',     # Missing letter in 1st group
    '1 1AA',      # Missing letter in 1st group
    '11 1AA',     # Missing letter in 1st group
    'AA1 1A',     # Missing letter in 2nd group
    'AA1 1',      # Missing letter in 2nd group
    'AB1 1AA'     # The infamous !!
]


@pytest.fixture(params=positive_values)
def good_value(request):
    return request.param


@pytest.fixture(params=negative_values)
def evil_value(request):
    return request.param


def test_positive_v(good_value):
    assert postcode.validate_code(good_value),\
        'Invalid code in the positive text'


def test_negative_v(evil_value):
    assert not postcode.validate_code(evil_value),\
        'Valid code in the negative text'

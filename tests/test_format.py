
import os, sys
sys.path.insert(1, os.getcwd())
import pytest
import postcode


UGLY_VALUES = [
    'gir 0aa', 'b33 8th', 'bx1 1lt', 'cf99 1na',
    'cr2 6xh', 'dn55 1pt', 'ec1a 1bb', 'gu16 7hf',
    'm1 1ae', 'po16 7gz', 'sw1w 0ny',
    'w1a 0ax', 'w1k 7aa'
]


@pytest.fixture(params=UGLY_VALUES)
def ugly_value(request):
    return request.param


def test_formatting(ugly_value):
    nice = postcode.format_code(ugly_value)
    assert postcode.naive_validation(nice),\
        'Code validation failed'

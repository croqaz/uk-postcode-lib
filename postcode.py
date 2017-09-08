#! /usr/bin/env python3.6

"""
The library supports validating and formatting post codes for UK.
"""

import re
import sys
import unittest


# Naive regex validation
CODE_REGEX = '[A-PR-UWYZ](([A-HK-Y]?\d\d?)|(\d[A-HJKPSTUW])|'\
    '([A-HK-Y]\d[ABEHMNPRV-Y]))[ ]?\d[ABD-HJLNP-UW-Z]{2}'
VALID_CODE = re.compile('^{}$'.format(CODE_REGEX), re.I)


def validate_code(code):
    """
    Input: a code as string.
    Output: a boolean.
    """
    return bool(VALID_CODE.match(code))


def format_code(code):
    """
    Input: a badly formatted code as string, possibly without spaces.
    Output: a standard formatted code.
    """
    # Minimal size is A99AA, 5 letters
    # Maximum size is DN55 1PT, 8 letters
    assert len(code) > 4 and len(code) < 9, 'The code size is invalid'
    code = code.upper()
    # From start up to the last 3 letters
    out_code = code[:-3].strip()
    # Only the last 3 letters
    inw_code = code[-3:].strip()
    return '{} {}'.format(out_code, inw_code)


if __name__ == '__main__':
    # Minimalistic command line app
    # Grab the last param and consider it to be a postcode
    code = sys.argv[-1]
    if not code.endswith('.py'):
        code = format_code(code)
        print('\nFormatted code ::', code)
        valid = 'valid' if validate_code(code) else 'invalid'
        print('The code is {}.\n'.format(valid))
    else:
        print('\nYou must provide a post-code, '
              'to be formatted and validated.\n')

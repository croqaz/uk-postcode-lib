#! /usr/bin/env python3.6

import sys
from __init__ import format_code, naive_validation

if __name__ == '__main__':
    # Minimalistic command line app
    # Grab the last param and consider it to be a postcode
    code = sys.argv[-1]
    if not code.endswith('.py'):
        code = format_code(code)
        print('\nFormatted code ::', code)
        valid = 'valid' if naive_validation(code) else 'invalid'
        print('The code is {}.\n'.format(valid))
    else:
        print('\nYou must provide a post-code, '
              'to be formatted and validated.\n')

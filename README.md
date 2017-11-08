
# UK-postcode-lib
[![Build Status](https://travis-ci.org/croqaz/uk-postcode-lib.svg?branch=master)](https://travis-ci.org/croqaz/uk-postcode-lib) ![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

#### Simple UK post-code validation and formatting.

---

This library includes the post-codes from the *Code-Point Open data*, november 2017.

To update the data, you must download the archive from OS Code-Point Open, or Doogal GB, extract it the folder `CSV` and run the `import_csv.py` script.


Motivation: Regex validation is hard to maintain and only goes so far. There are no libraries for checking that the post-code is `postally` valid.

**Note**: This library is just as good as the database included in it. If some post-codes are missing, or are deprecated, it's because I'm using free data.


## Usage

### As a command line app

Format and validate a post-code:

    $ python3.6 postcode "M1 1AE"


### As a python library

### `postcode.format_code(code: str, join: bool=True)`

This function returns a string, or a tuple, depending if the `join` param is True.

Example:

```python
import postcode

postcode.format_code('M11ae')
# M1 1AE
postcode.format_code('w1k 7aa')
# W1K 7AA
postcode.format_code('ab11aa', join=False)
# ('AB1', '1AA')
```

### `postcode.naive_validation(code: str) -> bool`

This function validates a code, using a REGEX. The code is not guaranteed to be postally valid.

Example:

```python
postcode.naive_validation('M1 1AE')
# True
postcode.naive_validation('ab11aa')
# True
postcode.naive_validation('A 1AA') # No digit in 1st group
# False
```

### `postcode.validate_code(code: str) -> bool`

This function validates a code, using the database. Before calling it, you must call the `load_database()` function.

Example:

```python
postcode.load_database()

postcode.validate_code('M1 1AE')
# True
postcode.validate_code('AB11AA')
# False
```

-----

Free database downloads:

* [OS Code-Point Open post-codes](https://www.ordnancesurvey.co.uk/business-and-government/products/code-point-open.html) (updated quarterly: February, May, August and November)
* [Doogal GB Postcodes](https://www.doogal.co.uk/UKPostcodes.php) (older data)

Resources:

* Stackoverflow 1: https://stackoverflow.com/questions/164979/uk-postcode-regex-comprehensive
* Stackoverflow 2: https://stackoverflow.com/questions/13969461/javascript-uk-postcode-validation
* Online tester: [Royal Mail Postcode Finder](http://www.royalmail.com/find-a-postcode)

Similar tools:

* [UK postcode utils on PyPi](https://pypi.python.org/pypi/uk-postcode-utils)
* [Parsing a UK postcode on Activestate](https://github.com/ActiveState/code/tree/master/recipes/Python/279004_Parsing_a_UK_postcode)
* [UK Postcode Validation, JavaScript and PHP](https://www.braemoor.co.uk/software/postcodes.shtml)

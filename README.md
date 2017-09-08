
# UK-postcode-lib

#### Simple UK post-code validation and formatting.

---

This library includes the post-codes from the Code-Point Open data, august 2017.

To update the data, you must download the archive from OS Code-Point Open, or Doogal GB, extract it the folder `CSV` and run the `csv_to_list.py` script.


Motivation: Regex validation is hard to maintain and only goes so far. There are no libraries for checking that the post-code is `postally` valid.

Free database:

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

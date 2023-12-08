import re
from flask import request

class PostcodeChecker():
    def check(self, postcode):
        if postcode is None:
            return False
        else:
            return re.match(
                r"^[A-Za-z]{1,2}\d{1,2}[A-Za-z]?\s*\d[A-Za-z]{2}$",
                postcode
            ) is not None
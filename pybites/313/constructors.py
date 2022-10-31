import re


class DomainException(Exception):
    """Raised when an invalid is created."""


class Domain:

    _domain_pattern = re.compile(r".*\.[a-z]{2,3}$")

    def __init__(self, name):
        # validate a current domain (r'.*\.[a-z]{2,3}$' is fine)
        # if not valid, raise a DomainException
        if not self._domain_pattern.match(name):
            raise DomainException
        self.name = name

    # next add a __str__ method and write 2 class methods
    # called parse_url and parse_email to construct domains
    # from an URL and email respectively

    def __str__(self):
        return self.name

    @classmethod
    def parse_url(cls, url):
        return cls(url.split("//")[-1].split("/")[0])

    @classmethod
    def parse_email(cls, email):
        return cls(email.split("@")[-1])

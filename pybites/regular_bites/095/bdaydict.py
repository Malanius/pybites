MSG = "Hey {}, there are more people with your birthday!"


class BirthdayDict(dict):
    """Override dict to print a message every time a new person is added that has
    the same birthday (day+month) as somebody already in the dict"""

    def __setitem__(self, name, birthday):
        for existing_bday in self.values():
            if (
                birthday.month == existing_bday.month
                and birthday.day == existing_bday.day
            ):
                print(MSG.format(name))
        super().__setitem__(name, birthday)

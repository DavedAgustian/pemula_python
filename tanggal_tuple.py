class MyDateTime(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __add__(self, other):
        if isinstance(other, MyDelta):
            result = MyDateTime(day=self.day + other.days,
                                month =self.month + other.months,
                                year=self.year + other.years)
            return result
    def __str__(self):
        return ( '%d,%d,%d ' % (self.year, self.month, self.day))

class MyDelta(object):
    def __init__(self, years=0, months=0, days=0):
        # type: (object, object, object) -> object
        self.years = years
        self.months = months
        self.days = days

date = MyDateTime(2013,2,6)
delta = MyDelta(months=10)
print(date+delta)

class Calendar(object):
    months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    
    def __init__(self, day=1, month=1, year=1900):
        self.__day = day
        self.__month = month
        self.__year = year

    def leapyear_style_1(self, y):
        if y % 400 == 0:
            # y can divide 400 
            # y is leap year
            return 1
        elif y % 4 == 0:
            # y can divide 4
            if y % 100 == 0:
                # y can divide 100
                # is not a leap year
                return 0
            # is a leap year
            return 1
        return 0
    def leapyear(self, y):
        if y % 4:
            # y % 4 -> true means y can not divide 4
            # is not a leap year
            return 0
        else:
            if y % 100 :
                # y can divide 4 and y can not divide 100
                # is a leap year
                return 1
            else:
                if y % 400:
                    # y can divide 100 but y can not divide 400
                    # is not a leap year
                    return 0
                else:
                    # y can divide 100 and also 400
                    # is a leap year
                    return 1

    def set(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year

    def get():
        return (self, self.__day, self.__month, self.__year)

    def advance(self):
        months = Calendar.months
        max_days = months[self.__month-1]
        if self.__month == 2:
            max_days += self.leapyear(self.__year)
        if self.__day == max_days:
            self.__day = 1
            if (self.__month == 12):
                self.__month = 1
                self.__year += 1
            else:
                self.__month += 1
        else:
            self.__day += 1

    def __str__(self):
        return str(self.__day) + "/" + str(self.__month) + "/" + str(self.__year)

if __name__ == "__main__":
    x = Calendar(28,2,2316)
    print(x)
    x.advance()
    print(x)
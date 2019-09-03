from simple_calendar import Calendar
from simple_clock import Clock

class CalendarClock(Clock, Calendar):
    def __init__(self, day, month, year, hours = 0, minutes = 0, seconds = 0):
        Calendar.__init__(self, day, month, year)
        Clock.__init__(self, hours, minutes, seconds)

    def __str__(self):
        return Calendar.__str__(self) + ", " + Clock.__str__(self)

if __name__ == "__main__":
    x = CalendarClock(24,12,57)
    print(x)
    print("In 1000 days and 1000s:")
    # Next 1000 seconds
    for i in range(1000):
        x.tick()
    # Next 1000 days
    for i in range(1000):
        x.advance()

    print(x)
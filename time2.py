"""
    This module contains code related to
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to complete the exercises in Chapter 17: Classes and Methods in Think Python 2
    
    Note: Using Python 3.9.0
"""
class Time:
    """
        Represents the time of day

        attributes: hour, minute, second
    """
    def __init__(self, hour = 0, minute = 0, second = 0):
        """
            Initializes the Time object

            self: self-referential
            hour: int
            minute: int
            second: int or float
        """
        self.second = ((((hour * 60) + minute) * 60) + second)

    
    def __str__(self):
        """
            Returns a string representation of the time

            self: self-referential

            return: string
        """
        minutes, second = divmod(self.second, 60)
        hour, minute = divmod(minutes, 60)
        return '%.2d:%.2d:%.2d' % (hour, minute, second)


    def __add__(self, other):
        """
            Adds two Time objects or a Time object and a number.
            
            other: Time object or number of seconds

            return: int or float (seconds)
        """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)


    def __radd__(self, other):
        """
            Adds two Time objects or a Time object and a number.

            self: self-referential
            other: Time

            return: int or float (seconds)
        """
        return self.__add__(other)


    def is_valid(self):
        """
            Determine if a Time object satisfies the invariants

            self: self-referential

            return: boolean; True if satisfies the invariants, False otherwise
        """
        return (self.second >= 0) and (self.second < (24 * 60 * 60))


    def print_time(self):
        """
            Prints a string representation of time

            self: self-referential
        """
        print(str(self))
    

    def time_to_int(self):
        """
            Compute the time since midnight

            self: self-referntial

            return: int
        """
        return self.second


    def is_after(self, other):
        """
            Determines if this Time object is after another

            self: self-referential
            other: Time

            return: boolean; True if this Time object comes after the other, False otherwise
        """
        return self.second > other.second


    def add_time(self, other):
        """
            Adds two time objects.

            self: self-referential
            other: Time

            return: int
        """
        assert self.is_valid() and other.is_valid()
        seconds = self.second + other.second
        return int_to_time(seconds)


    def increment(self, seconds):
        """
            Increment Time object by an amount in seconds
            
            self: self-referential
            seconds: int or float

            return: int
        """
        seconds += self.second
        return int_to_time(seconds)


def int_to_time(seconds):
    """
        Make a new Time object

        seconds: int (seconds since midnight)

        return: Time
    """
    return Time(0, 0, seconds)

def main():
    """
        Main function
    """
    start = Time(10, 30, 00)
    start.print_time()

    end = start.increment(1337)
    end.print_time()

    print("Let's see if the end time comes after the start")
    print(end.is_after(start))

    print("Now printing using __str__")
    print(start, end)

    start = Time(9, 45)
    duration = Time(1, 35)
    print("Adding time together.")
    print(start + duration)
    print(start + 1337)
    print(1337 + start)

    print("And now for an example of using polymorphism.")
    t1 = Time(7, 43)
    t2 = Time(7, 41)
    t3 = Time(7, 37)
    total = sum([t1, t2, t3])
    print(total)


if __name__ == '__main__':
    main()
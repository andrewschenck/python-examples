def the_easy_way():
    """ An Iterable object wrapped in for loop sugar. """

    iterable = (1, 2, 3, 4, 5)

    for i in iterable:
        print(i)


def the_hard_way():
    """
    Behind the scenes:

        * An Iterable implements __iter__, which returns an Iterator.
        * An Iterator implements __next__, which returns the next
          item in in the Iterator.
        * When the Iterator is exhausted, StopIteration is raised.
    """

    iterable = (1, 2, 3, 4, 5)

    iterator = iterable.__iter__()
    while True:
        try:
            i = next(iterator)
            print(i)
        except StopIteration:
            break

def slightly_harder():
    """ Equivalent to the_hard_way, all syntactic sugar removed. """

    iterable = (1, 2, 3, 4, 5)

    iterator = iterable.__iter__()
    while True:
        try:
            i = iterator.__next__()
            print(i)
        except StopIteration:
            break

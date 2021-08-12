"""Set Objects for Python

In terms of Set Objects, "writing", "adding" and "editing" data is essentially the same thing as JavaScript Set Objects.

A Set is a collection of unique values.

Each value may occur only once in a Set.

A Set can hold any values of any data type.
"""

from flatten import flatten


class Set():

    def __init__(self, array=[]):
        if not isinstance(array, list):
            raise TypeError(f'{array} is not a list')

        self.list = list(flatten(array))

    def __len__(self):
        return len(self.list)

    def __getattr__(self, size):
        return len(self.list)

    def add(self, value):
        if not value in self.list:
            self.list.append(value)

        return self.list

    def clear(self):
        self.list.clear()
        return None

    def delete(self, value):
        if not value in self.list:
            return False

        self.list.remove(value)
        return True

    def has(self, value):
        if value in self.list:
            return True
        else:
            return False

    def keys(self):
        keys = []
        for el in self.list:
            keys.append(el)

        return keys

    def values(self):
        values = []
        for el in self.list:
            values.append(el)

        return values

    def entries(self):
        array = []
        for el in self.list:
            array.append([el, el])

        return array

    def for_each(self, callbackFn):
        args_name = callbackFn.__code__.co_varnames[:callbackFn.__code__.co_argcount]
        args_len = len(args_name)

        if callable(callbackFn) == False:
            raise TypeError(f'{callbackFn} is not callable')
        elif args_len > 3:
            raise TypeError(
                f'{args_name[2]} takes 3 positional arguments but 4 were given')

        for i, el in enumerate(self.list):
            if args_len == 1:
                callbackFn(el)
            elif args_len == 2:
                callbackFn(el, i)
            elif args_len == 3:
                callbackFn(el, i, self.list)

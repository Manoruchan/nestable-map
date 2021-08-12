"""Map Objects for Python

In terms of Map Objects, "writing", "adding" and "editing" data is essentially the same thing as JavaScript Map Objects.

A Map object holds key-value pairs where the keys can be any datatype.

A Map object remembers the original insertion order of the keys.

A Map object has a property that represents the size of the map.
"""


class Map():

    def __init__(self, array=[]):
        for el in array:
            if not isinstance(el, list) or len(el) != 2:
                raise TypeError(f'{array[0]} is not a list')

        self.list = array

    def __len__(self):
        return len(self.list)

    def __getattr__(self, size):
        return len(self.list)

    def clear(self):
        self.list.clear()
        return None

    def delete(self, key):
        if not key in self.keys():
            return False

        for el in self.list:
            if el[0] == key:
                self.list.remove(el)
        return True

    def get(self, key):
        if not key in self.keys():
            return None

        for el in self.list:
            if el[0] == key:
                return el[1]

    def has(self, key):
        if key in self.keys():
            return True
        else:
            return False

    def set(self, key, value):
        for el in self.list:
            if el[0] == key:
                el[1] == value

        if not key in self.keys():
            self.list.append([key, value])

        return self.list

    def keys(self):
        keys = []
        for el in self.list:
            keys.append(el[0])

        return keys

    def values(self):
        values = []
        for el in self.list:
            values.append(el[1])

        return values

    def entries(self):
        array = []
        for el in self.list:
            array.append([el[0], el[1]])

        return array

    def for_each(self, callbackFn):
        args_name = callbackFn.__code__.co_varnames[:callbackFn.__code__.co_argcount]
        args_len = len(args_name)

        if callable(callbackFn) == False:
            raise TypeError(f'{callbackFn} is not callable')
        elif args_len > 2:
            raise TypeError(
                f'{args_name[2]} takes 2 positional arguments but 3 were given')

        for el in self.list:
            if args_len == 1:
                callbackFn(el[1])
            elif args_len == 2:
                callbackFn(el[1], el[0])


class Advanced_Map(Map):
    pass

import unittest
from Map import Map


class MapTest(unittest.TestCase):

    def test_basic_map_operations(self):
        map = Map()
        map.set('a', 1)
        self.assertEqual(1, map.size)
        self.assertEqual(True, map.has('a'))
        self.assertEqual(1, map.get('a'))
        map.delete('a')
        self.assertEqual(False, map.has('a'))
        self.assertEqual(None, map.get('a'))
        map.clear()
        self.assertEqual(0, map.size)

    def test_get_keys_and_values_from_map(self):
        map = Map()
        map.set('a', 1)
        map.set('b', 2)
        map.set('c', 3)
        map.set('d', 4)
        self.assertEqual(['a', 'b', 'c', 'd'], map.keys())
        self.assertEqual([1, 2, 3, 4], map.values())
        map.clear()
        self.assertEqual([], map.keys())
        self.assertEqual([], map.values())

    def test_map_forEach(self):
        map = Map()
        map.set('a', 1)
        map.set('b', 2)
        map.set('c', 3)

        lst = []

        def cb(val):
            if val == 1 or val == 3:
                lst.append(val)
        map.for_each(cb)
        self.assertEqual([1, 3], lst)

        lst.clear()

        def cb1(val, key):
            if key == 'a':
                lst.append(key)
            if val == 2:
                lst.append(val)
        map.for_each(cb1)
        self.assertEqual(['a', 2], lst)


if __name__ == "__main__":
    unittest.main()

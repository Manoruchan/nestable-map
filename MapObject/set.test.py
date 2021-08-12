import unittest
from Set import Set


class SetTest(unittest.TestCase):

    def test_basic_Set_operations(self):
        s = Set()
        s.add('a')
        self.assertEqual(1, s.size)
        self.assertEqual(True, s.has('a'))
        s.add('a')
        self.assertEqual(1, s.size)
        self.assertEqual(True, s.has('a'))
        s.delete('a')
        self.assertEqual(False, s.has('a'))
        s.clear()
        self.assertEqual(0, s.size)

    def test_get_keys_and_values_from_Set(self):
        s = Set()
        s.add('a')
        s.add('b')
        s.add('c')
        s.add('d')
        self.assertEqual(['a', 'b', 'c', 'd'], s.keys())
        self.assertEqual(['a', 'b', 'c', 'd'], s.values())
        s.clear()
        self.assertEqual([], s.keys())
        self.assertEqual([], s.values())

    def test_Set_forEach(self):
        s = Set()
        s.add('a')
        s.add('b')
        s.add('c')

        lst = []

        def cb(val):
            if val == 'a' or val == 'c':
                lst.append(val)
        s.for_each(cb)
        self.assertEqual(['a', 'c'], lst)

        lst.clear()

        def cb1(val, i, arr):
            if val == 'a':
                lst.append(val)
            if i == 2:
                lst.append(arr[i])
        s.for_each(cb1)
        self.assertEqual(['a', 'c'], lst)


if __name__ == "__main__":
    unittest.main()

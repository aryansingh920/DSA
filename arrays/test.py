import unittest
from reverseArray import reverseArray
# Replace `your_module_name` with the actual module name
from main import Array


class TestReverseArray(unittest.TestCase):

    def test_reverseArray(self):
        self.assertEqual(reverseArray([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverseArray([]), [])
        self.assertEqual(reverseArray([42]), [42])
        self.assertEqual(reverseArray(["a", "b", "c"]), ["c", "b", "a"])

    def test_Array_class(self):
        arr_obj = Array([1, 2, 3])
        self.assertEqual(arr_obj.reverse(), [3, 2, 1])

        arr_obj = Array([])
        self.assertEqual(arr_obj.reverse(), [])

        arr_obj = Array(["apple", "banana", "cherry"])
        self.assertEqual(arr_obj.reverse(), ["cherry", "banana", "apple"])


if __name__ == '__main__':
    unittest.main()

import unittest
from lab2x import Stack


class StackTester(unittest.TestCase):

    def test_push1_size(self):
        item = 5
        s = Stack()
        s.push(item)
        self.assertEqual(1, s.size())

    def test_push1_items(self):
        s = Stack()
        s.push(5)
        self.assertEqual([5], s.items)

    def test_push2_size(self):
        s = Stack()
        s.push(5)
        s.push(6)
        self.assertEqual(2, s.size())


    def test_push2_pop1_value(self):
        s = Stack()
        s.push(8)
        s.push(9)
        self.assertEqual(9, s.pop())

    def test_push2_pop2_size(self):
        s = Stack()
        s.push("Glob")
        s.push("Blob")
        s.pop()
        s.pop()
        self.assertEqual(0, s.size())

    def test_push2_pop2_value(self):
        s = Stack()
        s.push("Glob")
        s.push("Blob")
        s.pop()
        self.assertEqual("Glob", s.pop())



if __name__ == '__main__':
    unittest.main()        

import unittest
import bbb
import p2a


class MyTestCase(unittest.TestCase):
    def test_b(self):
        # self.assertEquals(bbb.check_b("3"), "No", '11')
        self.assertEquals(bbb.check_b("ruldrdlu"), "Yes", '22')
        self.assertEquals(bbb.check_b("ddludrdurrdduurllluu"), "No", '33')

    def test_p2a(self):
        self.assertEquals(p2a.calc('10'), '9')
        self.assertEquals(p2a.calc('6'), '5')
        self.assertEquals(p2a.calc('-4'), '-5')

    def test_p2b(self):
        self.assertEquals(p2b.calc('b2 a3 c4'), 'Normal')
        self.assertEquals(p2b.calc('a1 b2 e2'), 'Check')


if __name__ == '__main__':
    unittest.main()

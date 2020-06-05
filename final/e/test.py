import sys
import unittest
import e


class MyTestCase(unittest.TestCase):

    def setUp(self):
        super(MyTestCase, self).setUp()
        self.longMessage = True

    # def test_b(self):
    #     # self.assertEquals(bbb.check_b("3"), "No", '11')
    #     self.assertEquals(bbb.check_b("ruldrdlu"), "Yes", '22')
    #     self.assertEquals(bbb.check_b("ddludrdurrdduurllluu"), "No", '33')

    def test1(self):
        self.single_file_test('001')
        self.single_file_test('002')
        self.single_file_test('003')

    def single_file_test(self, sn):
        with open(r'C:\mts\work\olim\samples-005006\win\E\input%s.txt' % sn, 'r') as infile:
            istr = infile.readline()
        with open(r'C:\mts\work\olim\samples-005006\win\E\output%s.txt' % sn, 'r') as outfile:
            ostr = outfile.read().rstrip()

        self.assertEquals(e.calc(istr), ostr, 'Error in %s' % sn)

    # def test_p2b(self):
    #     self.assertEquals(p2b.calc('b2 a3 c4'), 'Normal')
    #     self.assertEquals(p2b.calc('a1 b2 e2'), 'Check')


if __name__ == '__main__':
    unittest.main()

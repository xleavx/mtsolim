import sys
import unittest
import a


class MyTestCase(unittest.TestCase):
    # def test_b(self):
    #     # self.assertEquals(bbb.check_b("3"), "No", '11')
    #     self.assertEquals(bbb.check_b("ruldrdlu"), "Yes", '22')
    #     self.assertEquals(bbb.check_b("ddludrdurrdduurllluu"), "No", '33')

    def test_a(self):
        self.assertEquals(a.calc('1 2 2003'), '0', 'msg')
        self.assertEquals(a.calc('2 29 2008'), '1')
        self.assertEquals(a.calc('31 32 2003'), '0', 'msg 2')
        self.assertEquals(a.calc('09 09 2008'), '0')
        self.assertEquals(a.calc('19 09 2008'), '1')
        self.assertEquals(a.calc('13 19 2008'), '0')
        #self.assertTrue(filecmp(...), 'You error message')

    def test1(self):
        self.single_file_test('001')
        self.single_file_test('002')

    def single_file_test(self, sn):
        with open(r'C:\mts\work\olim\samples-005006\win\A\input%s.txt' % sn, 'r') as infile:
            istr = infile.readline()
        with open(r'C:\mts\work\olim\samples-005006\win\A\output%s.txt' % sn, 'r') as outfile:
            ostr = outfile.read().rstrip()

        self.assertEquals(a.calc(istr), ostr, 'Error in %s' % sn)

    # def test_p2b(self):
    #     self.assertEquals(p2b.calc('b2 a3 c4'), 'Normal')
    #     self.assertEquals(p2b.calc('a1 b2 e2'), 'Check')


if __name__ == '__main__':
    unittest.main()

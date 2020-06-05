import sys
import unittest
import c


class MyTestCase(unittest.TestCase):
    # def test_b(self):
    #     # self.assertEquals(bbb.check_b("3"), "No", '11')
    #     self.assertEquals(bbb.check_b("ruldrdlu"), "Yes", '22')
    #     self.assertEquals(bbb.check_b("ddludrdurrdduurllluu"), "No", '33')

    def test1(self):
        self.assertEquals(c.calc('K9A10J2'), 'AKJ1092')
        self.assertEquals(c.calc('Q'), 'Q')
        #self.assertTrue(filecmp(...), 'You error message')

    def test_a1(self, capsys):
        print("hello")
        sys.stderr.write("world\n")
        captured = capsys.readouterr()
        assert captured.out == "hello\n"
        assert captured.err == "world\n"
        print("next")
        captured = capsys.readouterr()
        assert captured.out == "next\n"

    # def test_p2b(self):
    #     self.assertEquals(p2b.calc('b2 a3 c4'), 'Normal')
    #     self.assertEquals(p2b.calc('a1 b2 e2'), 'Check')


if __name__ == '__main__':
    unittest.main()

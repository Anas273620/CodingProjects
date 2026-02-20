import unittest
import Main

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = Main.do_stuff(test_param)
        self.assertEqual(result, 15)
        
    def test_do_stuff2(self):
        test_param = 'fdfgjhkhgf'
        result = Main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)
        
    def test_do_stuff3(self):
        test_param = None
        result = Main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')
        
    def test_do_stuff4(self):
        test_param = ''
        result = Main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')
        
unittest.main()
        
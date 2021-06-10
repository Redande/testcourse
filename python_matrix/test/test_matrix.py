import unittest

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.matrix'
@points('1.matrix')
class MatrixTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module(exercise, 'fi')

    def test_print_matrix(self):
        reload_module(self.module)
        output = get_stdout()
        self.assertEqual(output, '[[1, 3], [2, 4]]', 'Transpoosimatriisi ei ole täysin oikea')

if __name__ == '__main__':
    unittest.main()
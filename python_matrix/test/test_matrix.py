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
        split_output = output.split('\n')
        output_length = len(split_output)
        if output_length > 2:
            error_msg = "Tulostit liikaa rivejä, matriisin tulosteen pitäisi olla kahden rivin pituinen"
        else:
            error_msg = "Tulostit liian vähän rivejä, matriisin tulosteen pitäisi olla kahden rivin pituinen"
        self.assertEqual(len(split_output), 2, error_msg)
        self.assertEqual(split_output[0].replace(' ', '') == '[1,3]', "Matriisin ensimmäinen rivi ei ole oikein")
        self.assertEqual(split_output[1].replace(' ', '') == '[2,4]' "Matriisin toinen rivi ei ole oikein")

if __name__ == '__main__':
    unittest.main()
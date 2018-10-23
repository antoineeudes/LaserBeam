# /src/tests.py
import unittest
import random
from box import Box
from obstacles import Transporter, ForwardSlashMirror, BackSlashMirror, Aether

class BoxTest(unittest.TestCase):

    """ Test case utilise pour tester les fonctions de la classe Box """

    def test_init(self):

        """ Test le fonctionnement des methodes '__init__' et '__getitem__' """

        nb_lines = random.randint(3, 26)
        nb_cols = random.randint(3, 26)

        box = Box(nb_lines, nb_cols, [(0, 0, Transporter([])), (0, 1, ForwardSlashMirror()), (1, 0, BackSlashMirror())])

        self.assertTrue(isinstance(box[0, 0], Transporter))
        self.assertTrue(isinstance(box[0, 1], ForwardSlashMirror))
        self.assertTrue(isinstance(box[1, 0], BackSlashMirror))
        self.assertTrue(isinstance(box[1, 1], Aether))

    def test_find_exits(self):

        """ Test le fonctionnement de la methode 'find_exits' """

        box = Box(26, 26, [(0, 0, Transporter([(1, 1), (2, 2)])), (1, 1, Transporter([(0, 0), (2, 2)])), (2, 2, Transporter([(0, 0), (1, 1)]))])
        exits = box.find_exits('>A')

        self.assertIn('>B', exits)
        self.assertIn('>C', exits)
        self.assertEqual(len(exits), 2)




if __name__ == '__main__':
    unittest.main()

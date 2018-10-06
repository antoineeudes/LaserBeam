import numpy as np
import string

class Grid:
    def __init__(self, n1, m1):

        """ cree une grille de n1 lignes et m1 colonnes """

        if n1 < 3:
            raise ValueError('You did not requested enough lines')
        if m1 < 3:
            raise ValueError('You did not requested enough columns')
        if n1 > 26:
            raise ValueError('You requested too many lines')
        if m1 > 26:
            raise ValueError('You requested too many columns')
        self._n = n1
        self._m = m1
        self._cells = []
        for i in range(n1):
            self._cells.append(m1*[' '])


    @property
    def n(self):

        """ permet d'acceder au nombre de lignes """

        return self._n


    @property
    def m(self):

        """ permet d'acceder au nombre de colonne """

        return self._m


    @property
    def cells(self):

        """ retourne le tableau de valeur de la grille """

        return self._cells


    def set_cells(self, i, j, cell):

        """ permet de modifier la valeur de la cellule i,j de la grille """

        self._cells[i][j] = cell
    def set_mirror(self, a, b):
        self.set_cells(ord(a)-65, ord(b)-65, '/')
    def set_backmirror(self, a, b):
        self.set_cells(ord(a)-65, ord(b)-65, '\\')
    def __str__(self):
        x_list = string.ascii_uppercase[0:self.n]
        y_list = string.ascii_uppercase[0:self.m]
        string1 = ' ' + str(x_list) + '\n'
        for i in range(self.n):
            s = ''
            for j in range(self.m):
                s += self.cells[i][j]
            string1 += str(y_list[i]) + s + str(y_list[i]) + '\n'
        string1 += ' ' + str(x_list)
        return string1



if __name__ == '__main__':
    G = Grid(3, 3)
    for i in range(G.n):
        for j in range(G.m):
            G.set_backmirror(i, j)

    print(G)

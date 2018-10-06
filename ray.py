from grid import *


def is_in_grid(grid, i, j):

    """ verifie si la cellule i,j appartient a la grille grid """

    if i < 0 or j < 0:
        return False
    if i >= grid.n or j >= grid.m:
        return False
    return True


def starting_point(entry_letter, direction):

    """ definie le point d'entree du laser beam en donnant une lettre et un direction """

    k = ord(entry_letter)-65
    if direction == '^':
        i = -1
        j = k
    elif direction == 'v':
        i = 0
        j = k
    elif direction == '>':
        i = k
        j = 0
    elif direction == '<':
        i = k
        j = -1
    else:
        raise ValueError('Invalid direction')
    return (i, j)


def ending_letters(i, j):

    """ donne les lettres d'entee en fontion des numeros i,j du point de sortie du laser """

    return (chr(i+65), chr(j+65))


def next_point(i, j, direction):

    """ definie le point suivant le point i,j dans le parcours du laser en fonction de la direction """

    if direction == '<':
        return (i, j-1)
    if direction == '>':
        return (i, j+1)
    if direction == '^':
        return (i-1, j)
    else:
        return (i+1, j)


def is_mirror(grid, i, j, direction):

    """ retourne un booleen verifiant si le point i,j est un miroir et actualise la direction du laser """

    if grid.cells[i][j] == '/':
        if direction == '^':
            return True, '>'
        if direction == 'v':
            return True,'<'
        if direction == '<':
            return True,'v'
        if direction == '>':
            return True,'^'

    if grid.cells[i][j] == '\\':
        if direction == '^':
            return True,'<'
        if direction == 'v':
            return True,'>'
        if direction == '<':
            return True,'^'
        if direction == '>':
            return True,'v'
    return False, direction


def simulate_ray(grid, entry_letter, direction):

    """ simule le parcours d'un rayon """
    i, j = starting_point(entry_letter, direction)
    previous_point = (i, j)
    while is_in_grid(grid, i, j):
        mirror, direction = is_mirror(grid, i, j, direction)
        grid.set_cells(i, j, direction)
        (i0, j0) = (i, j)
        previous_point = i, j
        i, j = next_point(i, j, direction)
    return ending_letters(i0, j0)

import random


class Particle:
    def __init__(self, x, y, dx, dy):
        assert (dx in {-1, 0, 1}) and (dy in {-1, 0, 1}), "invalid dx/dy"
        assert (dx != 0) or (dy != 0), "invalid dx/dy"
        self._x = x
        self._y = y
        self._dx = dx
        self._dy = dy
    @property
    def x(self): return self._x
    @property
    def y(self): return self._y
    @property
    def dx(self): return self._dx
    @property
    def dy(self): return self._dy
    def __str__(self):
        return "<{}, {}, {}, {}>".format(self._x, self._y, self._dx, self._dy)


class Aether:
    def __init__(self):
        pass
    @property
    def char_representation(self):
        return ' '
    def step(self, particle):
        """
        >>> print(Aether().step(Particle(0, 0, 1, 0)))
        <1, 0, 1, 0>
        """
        return Particle(particle.x + particle.dx,
                        particle.y + particle.dy,
                        particle.dx,
                        particle.dy)

class ForwardSlashMirror:
    def __init__(self):
        pass
    @property
    def char_representation(self):
        return '/'
    def step(self, particle):
        """
        >>> print(ForwardSlashMirror().step(Particle(0, 1, 1, 0)))
        <0, 0, 0, -1>
        """
        dx = -particle.dy
        dy = -particle.dx
        return Particle(particle.x + dx, particle.y + dy, dx, dy)

class BackSlashMirror:
    def __init__(self):
        pass
    @property
    def char_representation(self):
        return '\\'
    def step(self, particle):
        """
        >>> print(BackSlashMirror().step(Particle(1, 1, 1, 0)))
        <1, 2, 0, 1>
        """
        dx = particle.dy
        dy = particle.dx
        return Particle(particle.x + dx, particle.y + dy, dx, dy)

class HorizontalMirror:
    def __init__(self):
        pass
    @property
    def char_representation(self):
        return '-'
    def step(self, particle):
        """
        >>> print(HorizontalMirror().step(Particle(1, 1, 1, 0)))
        <2, 1, 1, 0>
        >>> print(HorizontalMirror().step(Particle(1, 1, 0, 1)))
        <1, 0, 0, -1>
        """
        dx = particle.dx
        dy = -particle.dy
        return Particle(particle.x + dx, particle.y + dy, dx, dy)

class VerticalMirror:
    def __init__(self):
        pass
    @property
    def char_representation(self):
        return '|'
    def step(self, particle):
        """
        >>> print(VerticalMirror().step(Particle(1, 1, 1, 0)))
        <0, 1, -1, 0>
        >>> print(VerticalMirror().step(Particle(1, 1, 0, 1)))
        <1, 2, 0, 1>
        """
        dx = -particle.dx
        dy = particle.dy
        return Particle(particle.x + dx, particle.y + dy, dx, dy)

class SquareMirror:
    def __init__(self):
        pass
    @property
    def char_representation(self):
        return '#'
    def step(self, particle):
        """
        >>> print(SquareMirror().step(Particle(1, 1, 1, 0)))
        <0, 1, -1, 0>
        >>> print(SquareMirror().step(Particle(1, 1, 0, 1)))
        <1, 0, 0, -1>
        """
        dx = -particle.dx
        dy = -particle.dy
        return Particle(particle.x + dx, particle.y + dy, dx, dy)

class Transporter:
    def __init__(self, o):
        self._outputs = o

    @property
    def char_representation(self):
        return 'o'
    def step(self, particle):
        """
        >>> print(Transporter([(4, 5)]).step(Particle(1, 1, 1, 0)))
        <5, 5, 1, 0>
        >>> print(Transporter([(4, 5)]).step(Particle(1, 1, 0, 1)))
        <4, 6, 0, 1>
        """
        if len(self._outputs) > 0:
            x, y = random.choice(self._outputs)
            dx = particle.dx
            dy = particle.dy
            return Particle(x + dx, y + dy, dx, dy)
        else:
            return None
    ##########################################################################
    ### Code ajoute a la version du professeur
    ##########################################################################
    def __str__(self):
        return str(self.x) + str(self.y)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# /src/box.py
import string
from .obstacles import BackSlashMirror, Transporter, ForwardSlashMirror, SquareMirror, VerticalMirror, HorizontalMirror, Aether, Particle
import random

int_letter_couples = list(zip(range(0, len(string.ascii_uppercase)),
                              string.ascii_uppercase))
int_to_letter = { int:letter for (int, letter) in int_letter_couples }
letter_to_int = { letter:int for (int, letter) in int_letter_couples }


class Box:
    def __init__(self, width, height, elements):
        assert (width >= 3) and (width <= 26), "invalid width"
        assert (height >= 3) and (height <= 26), "invalid height"
        self._width = width
        self._height = height
        self._grid = dict()
        for (x, y, element) in elements:
            self._grid[x, y] = element
    @property
    def width(self):
        """
        >>> Box(26, 25, []).width
        26
        """
        return self._width
    @property
    def height(self):
        """
        >>> Box(26, 25, []).height
        25
        """
        return self._height
    def __getitem__(self, key):
        x, y = key
        assert (x >= 0) and (x < self._width)
        assert (y >= 0) and (y < self._height)
        if key in self._grid:
            return self._grid[key]
        else:
            return Aether()
    def string_with_trace(self, trace = None):
        def char_repr(x, y, t):
            if (t != None) and ((x, y) in t):
                return '.'
            else:
                return self[x, y].char_representation
        rule = " " + string.ascii_uppercase[0:self._width] + " "
        lines = []
        lines.append(rule)
        for y in range(0, self._height):
            letter = int_to_letter[y]
            elements = [char_repr(x, y, trace) for x in range(0, self._width)]
            lines.append("".join([letter] + elements + [letter]))
        lines.append(rule)
        return "\n".join(lines)
    def __str__(self):
        return self.string_with_trace()
    def _particle_of_string(self, description):
        """
        >>> print(Box(3, 3, [])._particle_of_string('<A'))
        <2, 0, -1, 0>
        """
        assert (len(description) == 2)
        direction, letter = description
        assert (letter in string.ascii_uppercase)
        if direction == '>':
            return Particle(0, letter_to_int[letter], 1, 0)
        elif direction == '<':
            return Particle(self._width - 1, letter_to_int[letter], -1, 0)
        elif direction == 'v':
            return Particle(letter_to_int[letter], 0, 0, 1)
        elif direction == '^':
            return Particle(letter_to_int[letter], self._height - 1, 0, -1)
        else:
            assert False, "invalid direction"
    def _string_of_particle(self, particle):
        """
        >>> Box(3, 3, [])._string_of_particle(Particle(2, 3, -1, 0))
        'vC'
        """
        if particle.x < 0:
            return "<" + int_to_letter[particle.y]
        elif particle.x >= self._width:
            return ">" + int_to_letter[particle.y]
        elif particle.y < 0:
            return "^" + int_to_letter[particle.x]
        elif particle.y >= self._height:
            return "v" + int_to_letter[particle.x]
        else:
            assert False, "particle is still in the box"
    def _is_particle_in_box(self, particle):
        """
        >>> Box(3, 3, [])._is_particle_in_box(Particle(2, 3, -1, 0))
        False
        >>> Box(3, 3, [])._is_particle_in_box(Particle(2, 2, -1, 0))
        True
        """
        return (particle.x >= 0) and (particle.x < self._width) \
           and (particle.y >= 0) and (particle.y < self._height)
    def simulate_with_trace(self, description):
        particle = self._particle_of_string(description)
        trace = set()
        while self._is_particle_in_box(particle):
            trace.add((particle.x, particle.y))
            particle = self[particle.x, particle.y].step(particle)
            if particle == None: return None, trace
        return self._string_of_particle(particle), trace
    def simulate(self, description):
        """
        >>> Box(3, 3, [(0, 0, BackSlashMirror())]).simulate('>A')
        'vA'
        >>> Box(3, 3, [(0, 0, HorizontalMirror())]).simulate('>A')
        '>A'
        >>> Box(26, 26, [(25, 25, HorizontalMirror())]).simulate('vZ')
        '^Z'
        >>> Box(26, 26, [(25, 25, Transporter([(0, 0)])), (0, 0, Transporter([(25, 25)]))]).simulate('vZ')
        'vA'
        """
        exit_desc, trace = self.simulate_with_trace(description)
        return exit_desc

    def find_exits(self, description):
        return sorted(self.find_exits_recursive(self._particle_of_string(description), dict()))

    def find_exits_recursive(self, particle, seen):
        exits = set([])
        while self._is_particle_in_box(particle):
            x, y, dx, dy = particle.x, particle.y, particle.dx, particle.dy
            if isinstance(self[x, y], Transporter):
                for transporter in self[x, y]._outputs:
                    particle.x, particle.y = transporter[0], transporter[1]
                    if not (transporter.__str__(), dx, dy) in seen: # permet de ne pas rester piege dans un cycle
                        seen[transporter.__str__(), dx, dy] = True
                        exits = exits|self.find_exits_recursive(Aether().step(particle), seen)
                return exits
            particle = self[x, y].step(particle)
        exits.add(self._string_of_particle(particle))
        return exits

def build_interactively():
    def input_dimension(text):
        res = input(text)
        assert res.isdigit(), "invalid dimension"
        return int(res)
    width = input_dimension("width? ")
    height = input_dimension("height? ")
    mirrors = []
    holes = []
    elem_desc = input("element? ")
    while elem_desc:
        assert len(elem_desc) == 3, "invalid element description"
        x, y, kind = elem_desc
        assert x in string.ascii_uppercase, "invalid coordinate"
        assert y in string.ascii_uppercase, "invalid coordinate"
        x = letter_to_int[x]
        y = letter_to_int[y]
        if kind == 'o':
            holes.append((x, y))
        else:
            if kind == '/': mirror_obj = ForwardSlashMirror()
            elif kind == '\\': mirror_obj = BackSlashMirror()
            elif kind == '-': mirror_obj = HorizontalMirror()
            elif kind == '|': mirror_obj = VerticalMirror()
            elif kind == '#': mirror_obj = SquareMirror()
            else: assert False, "invalid element kind"
            mirrors.append((x, y, mirror_obj))
        elem_desc = input("element? ")
    transporters = []
    for idx, (x, y) in enumerate(holes):
        other_holes = holes[:idx] + holes[idx+1:]
        transporters.append((x, y, Transporter(other_holes)))
    return Box(width, height, mirrors + transporters)

def generate_random_box(width, height):
    mirrors = []
    holes = []
    number_elements = random.randint(0, width*height)
    kinds_of_elements = ['o', '/', '\\', '#', '|', '-']
    for i in range(number_elements):
        kind = random.choice(kinds_of_elements)
        xposition = random.randint(0, width-1)
        yposition = random.randint(0, height-1)
        if kind == 'o':
            holes.append((xposition, yposition))
        else:
            if kind == '/': mirror_obj = ForwardSlashMirror()
            elif kind == '\\': mirror_obj = BackSlashMirror()
            elif kind == '-': mirror_obj = HorizontalMirror()
            elif kind == '|': mirror_obj = VerticalMirror()
            elif kind == '#': mirror_obj = SquareMirror()
            else: assert False, "invalid element kind"
            mirrors.append((xposition, yposition, mirror_obj))
    transporters = []
    for idx, (x, y) in enumerate(holes):
        other_holes = holes[:idx] + holes[idx+1:]
        transporters.append((x, y, Transporter(other_holes)))
    return Box(width, height, mirrors + transporters)

def random_entry_point(number_of_cols, number_of_lines):
    kinds_of_directions = ['<', '>', '^', 'v']
    direction = random.choice(kinds_of_directions)
    if direction == '<' or direction == '>':
        limit = number_of_lines
    elif direction == '^' or direction == 'v':
        limit = number_of_lines
    else:
        raise ValueError('incorrect direction')
    letter = int_to_letter[random.randint(0, limit-1)]
    return direction + letter


if __name__ == "__main__":
    import doctest
    doctest.testmod()

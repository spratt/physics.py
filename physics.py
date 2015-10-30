#!/usr/bin/env python3
"""physics.py
Written by Simon Pratt

Inspired by: http://gafferongames.com/game-physics/integration-basics/
"""
class Coord:
    """A pair of coordinates x,y

    >>> origin = Coord()
    >>> origin.x
    0
    >>> origin.y
    0
    """

    def __init__(self, x = 0, y = 0):
        """Initializes a pair of coordinates x,y
        
        >>> unit = Coord(1,1)
        >>> unit.x
        1
        >>> unit.y
        1
        """
        self.x = x
        self.y = y

    def __repr__(self):
        """Python representation of a coordinate.

        >>> unit = Coord(1,1)
        >>> unit
        Coord(1,1)
        """
        return "Coord({})".format(self)

    def __str__(self):
        """String representation of a coordinate.
        
        >>> "{}".format(Coord())
        '0,0'
        """
        return "{},{}".format(self.x, self.y)

    def __add__(self, c):
        return Coord(self.x + c.x, self.y + c.y)

    def __mul__(self, m):
        return Coord(self.x * m, self.y * m)

class Object:
    """Something with mass, position, velocity, and acceleration.

    >>> o = Object()
    >>> o.m
    1
    >>> o.p
    Coord(0,0)
    >>> o.v
    Coord(0,0)
    >>> o.a
    Coord(0,0)
    """

    def __init__(self, m = 1, p = None, v = None, a = None):
        """Initializes an Object.

        >>> o = Object(2)
        >>> o.m
        2
        >>> o.p
        Coord(0,0)
        >>> o.v
        Coord(0,0)
        >>> o.a
        Coord(0,0)
        """
        self.m = m
        self.p = Coord() if p == None else p
        self.v = Coord() if v == None else v
        self.a = Coord() if a == None else a

    def __repr__(self):
        """Python representation of an Object.

        >>> o = Object()
        >>> o
        Object(m=1,p=Coord(0,0),v=Coord(0,0),a=Coord(0,0))
        """
        return "Object(m={},p={},v={},a={})".format(self.m,
                                                    repr(self.p),
                                                    repr(self.v),
                                                    repr(self.a))

class Physics:
    EULER = 1
    RK4 = 2

    @staticmethod
    def integrate(method = EULER, o = None, dt = 1, t = 1):
        """Integrates by a specified method.

        >>> o = Object(a = Coord(10, 0))
        >>> Physics.integrate(Physics.EULER, o, 1, 5)
        >>> o
        Object(m=1,p=Coord(100,0),v=Coord(50,0),a=Coord(10,0))
        >>> Physics.integrate(o = o, dt = 1, t = 5)
        >>> o
        Object(m=1,p=Coord(450,0),v=Coord(100,0),a=Coord(10,0))
        """
        if o == None:
            return
        elif method == Physics.EULER:
            return Physics.euler(o, dt, t)
        else:
            raise "Not yet implemented."

    @staticmethod
    def euler(o, dt, t):
        """Integrates by by the explicit Euler method.

        >>> o = Object(a = Coord(10, 0))
        >>> Physics.euler(o, 1, 10)
        >>> o
        Object(m=1,p=Coord(450,0),v=Coord(100,0),a=Coord(10,0))
        """
        while t > 0:
            o.p += o.v * dt
            o.v += o.a * dt
            t -= dt        
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()

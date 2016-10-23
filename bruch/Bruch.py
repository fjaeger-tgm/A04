import math

class Bruch(object):
    def __init__(self, *args):
        """:param args: args kann sein: - Zähler,Nenner
                                        - Zähler
                                        - Bruch Objekt"""
        if (len(args) == 1):
            #Falls
            if(isinstance(args[0],Bruch)):
                self.zaehler = args[0].zaehler
                self.nenner = args[0].nenner
            else:
                self.zaehler = args[0]
                self.nenner = 1
        else:
            self.zaehler = args[0]
            self.nenner = args[1]

        if (not isinstance(self.nenner, int)):
            raise TypeError("float Nenner")

        if (not isinstance(self.zaehler, int)):
            raise TypeError("float Zaehler")

        if (self.nenner == 0):
            raise ZeroDivisionError("x/0 == :(")
        if (self.zaehler < 0 and self.nenner < 0):
            self.zaehler = -self.zaehler
            self.nenner = -self.nenner


    def __int__(self):
        """
        :return: Das Ergebnis des Bruchs ohne Nachkommastellen
        """
        return int(self.nenner/self.nenner)

    def __str__(self):
        """
        :return: Ein String der entweder nur eine Zahl oder einen Bruch ausgibt
        """
        if(self.nenner == 1):
            return '(%d)' % (self.zaehler)
        else:
            return '(%d/%d)' % (self.zaehler,self.nenner)

    def __float__(self):
        return float(self.zaehler/self.nenner)

    #def kgV(self,nenner1,nenner2):
        #mal = 1
        #while True:
        #    vielfaches = nenner1 * mal
        #    try:
        #        for z in [nenner1,nenner2]:
        #            rest = (vielfaches % z)
        #            if not rest:
        #                pass
        #            else:
        #                raise
        #        break
        #    except:
        #        pass
        #    mal += 1
        #return vielfache
    def kgV(self,n1,n2):
        """
        :param n1: erster der zwei Nenner zur Suche des kgVs
        :param n2: zweiter der zwei Nenner zur Suche des kgVs
        :return: gibt das kleinste gemeinsame Vielfache der zwei Nenner aus
        """
        return n1*n2 // math.gcd(n1,n2)

    def __add__(self, other):
        """

        :param other: Objekt dass addiert wird
        :return: Addition der beiden Brüche
        """
        if (isinstance(other,Bruch)):
            return Bruch(self.zaehler + other.zaehler,self.kgV(self.nenner,other.nenner))
        else:
            bother = Bruch(other)
            return Bruch((self.zaehler*bother.nenner) + (bother.zaehler * self.nenner),
                         self.kgV(self.nenner, bother.nenner))

    def __iadd__(self, other):
        """

        :param other: Zahl die zum Bruch hinzugerechnet wird
        :return: Addition der Zahl zum Bruch
        """
        return self + other

    def __radd__(self, other):
        """

        :param other: Variable für die Addition
        :return: reflektierte Addition
        """
        return self + other

    def __sub__(self, other):
        """
        :param other: Subtraend
        :return: Differenz der Brüche
        """
        if (isinstance(other,Bruch)):
            return Bruch(self.zaehler - other.zaehler,self.kgV(self.nenner,other.nenner))
        else:
            bother = Bruch(other)
            return Bruch((self.zaehler*bother.nenner) - (bother.zaehler * self.nenner),
                         self.kgV(self.nenner, bother.nenner))
    def __isub__(self, other):
        """
        :param other: Zahl die subtrahiert wird
        :return:Subtraktion der Zahlen
        """
        return self - other

    def __rsub__(self, other):
        """
        :param other:negative Zahl die subtrahiert wird
        :return:negative Subtraktion der Zahlen
        """
        return -self + other

    def __mul__(self, other):
        """
        :return: das Produkt einer Multiplikation zweier Brüche
        """
        other = Bruch(other)
        return Bruch(self.zaehler * other.zaehler, self.nenner * other.nenner)

    def __imul__(self, other):
        """
        :param other:Multiplikationsfaktor
        :return:Ergebnis = Ergebnis * other
        """
        return self * other

    def __rmul__(self, other):
        """

        :param other:
        :return:dasselbe wie mul aber: other * self
        """
        return self * other


    def __invert__(self):
        """

        :return:Kehrwert des Bruches
        """
        return Bruch(self.nenner,self.zaehler)

    def __abs__(self):
        """
        :return:Absolute Werte des Bruches
        """
        return Bruch(abs(self.zaehler), abs(self.nenner))

    def __neg__(self):
        """
        :return:negativer Bruch
        """
        return Bruch(-self.zaehler,self.nenner)

    def _Bruch__makeBruch(v):
        """
        :param v: Zähler des Bruches
        :return: Bruch mit Zähler v
        """
        return Bruch(v)

    def __pow__(self, power):
        """

        :param power:Exponent
        :return: Wert der Potenz
        """
        return Bruch(self.zaehler ** power,self.nenner ** power)

    def __eq__(self, other):
        """
        :param other: Objekt das verglichen wird
        :return: boolean, je nachdem ob sie falsch sind oder nicht
        """
        return float(self) == float(other)

    def __gt__(self, other):
        """

        :param other: Objekt das verglichen wird
        :return: True, wenn self größer ist
        """
        return float(self) > float(other)

    def __lt__(self, other):
        """
        :param other: Objekt das verglichen wird
        :return: True, wenn self kleiner ist
        """
        return float(self) < float(other)

    def __ge__(self, other):
        """
        :param other: Objekt das verglichen wird
        :return: True, wenn self größer oder gleich ist
        """
        return float(self) >= float(other)

    def __le__(self, other):
        """
        :param other: Objekt das verglichen wird
        :return: True, wenn self kleiner oder gleich ist
        """
        return float(self) <= float(other)

    def __truediv__(self, other):
        """
        :param other: Objekt das der Divisor ist
        :return: Quotient der Division
        """
        bother = Bruch(other)
        return self * ~bother

    def __itruediv__(self, other):
        """
        :param other: Objekt das der Divisor ist
        :return: Ergebnis = Ergebnis / other
        """
        return self / other

    def __rtruediv__(self, other):
        """
        :param other: Objekt das der Dividend ist
        :return: gibt den Qoutient der Division aus
        """
        return Bruch.__truediv__(other, self)

    def __iter__(self):
        """
        :return: gibt eine iterierbare Liste zurück
        """
        for i in self.zaehler, self.nenner:
            yield i




import unittest


class ClassificadorTriangulo:
    def __init__(self, ladoa, ladob, ladoc):
        self.__ladoa = ladoa
        self.__ladob = ladob
        self.__ladoc = ladoc
        if ((self.__ladob - self.__ladoc) < self.__ladoa < (self.__ladob + self.__ladoc)) and (
                (self.__ladoa - self.__ladoc) < self.__ladob < (self.__ladoa + self.__ladoc)) and (
                (self.__ladoa - self.__ladob) < self.__ladoc < (self.__ladoa + self.__ladob)):
            self.__triangulo = True
        else:
            self.__triangulo = False

    def tipo_triangulo(self):
        if self.__triangulo:
            if (self.__ladoa != self.__ladob) and (self.__ladoa != self.__ladoc) and (self.__ladob != self.__ladoc):
                if self.triangulo_retangulo():
                    return "Triângulo retângulo"
                else:
                    return "Triângulo escaleno"
            elif (self.__ladoa == self.__ladob) and (self.__ladoa == self.__ladoc) and (self.__ladob == self.__ladoc):
                return "Triângulo equilátero"
            else:
                if self.triangulo_retangulo():
                    return "Triângulo retângulo"
                else:
                    return "Triângulos isósceles"
        else:
            return "Não é um Triângulo"

    def triangulo_retangulo(self):
        lista = [self.__ladob, self.__ladoc, self.__ladoa]
        hipo = max(lista)
        lista.remove(hipo)
        if ((((lista[0]) ** 2) + (lista[1] ** 2)) ** (1 / 2)) == hipo:
            return True
        else:
            return False


class TestTriangulo(unittest.TestCase):
    def test_tipos(self):
        a = ClassificadorTriangulo(5, 4, 3)
        b = ClassificadorTriangulo(8, 7, 5)
        c = ClassificadorTriangulo(3, 3, 3)
        d = ClassificadorTriangulo(3, 4, 3)
        self.assertEqual(a.tipo_triangulo(), "Triângulo retângulo")
        self.assertEqual(b.tipo_triangulo(), "Triângulo escaleno")
        self.assertEqual(c.tipo_triangulo(), "Triângulo equilátero")
        self.assertEqual(d.tipo_triangulo(), "Triângulos isósceles")
        print(a.tipo_triangulo())
        print(b.tipo_triangulo())
        print(c.tipo_triangulo())
        print(d.tipo_triangulo())

    def test_triangulo(self):
        a = ClassificadorTriangulo(5, 4, 3)
        self.assertEqual(a.tipo_triangulo(), "Não é um Triângulo")


unittest.main()

from os import system
system('cls')

class Triangles:

    def __init__(self, a_side, b_side, c_side) -> None:
        self.a_side = a_side
        self.b_side = b_side
        self.c_side = c_side

    def to_be_or_not_to_be(self) -> str:
        if (self.a_side + self.b_side > self.c_side 
            and self.a_side + self.c_side > self.b_side 
            and self.c_side + self.b_side > self.a_side):
            return (f'Треугольник с такими сторонами СУЩЕСТВУЕТ')
                
        return (f'Треугольник с такими сторонами НЕ СУЩЕСТВУЕТ')

    def kind_of_triangle(self) -> str:
        if self.a_side == self.b_side == self.c_side:
                return (f'Это раВносторонний треугольник')
        elif (self.a_side ** 2 + self.b_side **2 == self.c_side **2 
                or self.a_side ** 2 + self.c_side ** 2 == self.b_side ** 2 
                or self.c_side ** 2 + self.b_side ** 2 == self.a_side ** 2):
            if (self.a_side == self.b_side 
                or self.b_side == self.c_side 
                or self.a_side == self.c_side):
                return (f'Это ПРЯМОУГОЛЬНЫЙ РАВНОБЕДРЕННЫЙ треугольник')
            else:
                return (f'Это ПРЯМОУГОЛЬНЫЙ треугольник (разносторонний)')
        elif (self.a_side == self.b_side 
              or self.b_side == self.c_side 
              or self.a_side == self.c_side):
            return (f'Это РАВНОБЕДРЕННЫЙ треугольник')
        
        else:
            return (f'Это раЗносторонний треугольник (НЕ прямоугольный)')

tr1 = Triangles(3, 4, 5)
tr2 = Triangles(3, 3, 5)
tr3 = Triangles(3, 4, 10)               # Не существует

print(f'{tr1.to_be_or_not_to_be()},\n{tr1.kind_of_triangle()}') 
print(f'{tr2.to_be_or_not_to_be()},\n{tr2.kind_of_triangle()}')     
print(tr3.to_be_or_not_to_be())


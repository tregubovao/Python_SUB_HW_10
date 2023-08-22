import os
os.system('cls')
import fractions

class Fractions:
    def __init__(self, chisl: int, znam: int) -> None:
        self.chisl = chisl
        self.znam = znam
    def frac_create(self):        
        return fractions.Fraction(self.chisl, self.znam)
    
    def frac_mult(self, other):
        """ Функция умножения дробей """
        return f'{self.chisl * other.chisl}/{self.znam * other.znam}'
    
    def frac_add(self, other):
        """ Функция сложения дробей """
        ch_res = self.chisl * other.znam + other.chisl * self.znam
        zn_res = self.znam * other.znam
        return f'{ch_res}/{zn_res}'
    
    def square_of_frac(self):
        """Возведение дроби в квадрат """
        return f'{self.chisl ** 2}/{self.znam ** 2}'
    
    def __add__(self, obj):
        return (fractions.Fraction(self.chisl, self.znam) 
                + fractions.Fraction(obj.chisl, obj.znam))
    
    
    
fr1 = Fractions(1, 2)
fr2 = Fractions(1, 3)

print(fr1.frac_create())
print(fr2.frac_create())
print(fr1.frac_create() * fr2.frac_create())

print(fr1 + fr2)

print(fr1.square_of_frac())
print(fr2.square_of_frac())

print(fr1.frac_mult(fr2))
print(fr1.frac_add(fr2))
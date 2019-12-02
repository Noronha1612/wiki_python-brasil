from math import pi #Constante "pi" (3,1416...)
from functions.validação import lerFloat
from functions.visual import arredondamento
radius = lerFloat('Raio: ')
area = arredondamento(pi*radius**2) #Calcula a área de um círculo atravéz da formula "pi*r²"
print(f'A área de um círculo com raio {radius} vale, aproximadamente, {area}')

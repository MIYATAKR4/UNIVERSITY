import math
a = eval(input('Digite o valor de a:'))
b = eval(input('Digite o valor de b:'))
c = eval(input('Digite o valor de c:'))

delta = b**2 * 4 * a * c

if delta < 0:
    print('não existem soluções reais.')
if delta == 0:
    raiz = (-b + math.sqrt(delta)) / (2 * a)
    print('a equação tem uma única solução:', raiz)
if delta > 0:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    print(' existem duas raízes reais:', raiz1, 'e:', raiz2)

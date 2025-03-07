'''Tablas de verdad en python 
JERARQUIA DE OPERADORES
1.()
2.**
3.+ -
4.* / %
5.> < != == >== <==
6.NOT
7.AND
8.OR
9. =
'''
op1 = True
op2 = True
op3 = op1 and op2
print(op3)

op4 = not op2

op1 = False
op2 = True
op3 = False
op4 = True
resultado = not op1 and (op2 or op3 and not op1) and not op4
from cmath import log
import math
from re import L

#Funcoes limites laterais
def limiteLateralEsquerdo(valorNumerico, coeficientes, grau, incrementer, a, variavel2):
    while math.fabs(variavel2 - a) >= incrementer:
        if(math.fabs(variavel2 - a) < 5 * incrementer):
            print("f(" + str(variavel2) + ") =",
                  round(valorNumerico(coeficientes, grau, variavel2), int(math.fabs(math.log(incrementer, 10)) - 1)))
        variavel2 += incrementer
    print("Limite a esquerda")

def limiteLateralDireito(valorNumerico, coeficientes, grau, incrementer, a, variavel1):
    while math.fabs(variavel1 - a) >= incrementer:
        if(math.fabs(variavel1 - a) < 5 * incrementer):
            print("f(" + str(variavel1) + ") =",
                round(valorNumerico(coeficientes, grau, variavel1), int(math.fabs(math.log(incrementer, 10)) - 1)))
        variavel1 -= incrementer
    print("Limite a direita")
    input()

incrementer = 10 ** (-5)
print("Qual tipo de sua função ?")
print("(1) Polinomio (2) Trigonometrica (3) Funcao Racional (4) Logaritmica (5) Exponencial")
tipo = int(input())

if(type(tipo) != int):
    print("Variavel nao inteira")
    exit()

#Polinomio
if(tipo == 1):
    def valorNumerico(list, grau, variavel):
        expressao = 0
        for i in range(grau):
            expressao += list[i] * variavel ** (grau - i)
        return expressao

    coeficientes = []
    grau = int(input("Qual o grau do polinomio? "))
    print("Digite os coeficientes da esquerda para direita convencional: ")
    for i in range(grau + 1):
        coeficientes += [float(input())]
    a = float(input("x tende a qual valor ?"))
    variavel1 = a + 1
    variavel2 = a - 1
    limiteLateralEsquerdo(valorNumerico, coeficientes, grau, incrementer, a, variavel2)
    limiteLateralDireito(valorNumerico, coeficientes, grau, incrementer, a , variavel1)

#Trigonometrica
elif(tipo == 2):
    print("(1) Seno, (2) Cosseno, (3) Tangente, (4) Cotangente, (5) Secante, (6) Cossecante")
    tipo_trigonometrico = int(input())
    coeficientes = []
    grau = 0
    if(type(tipo) != int):
        print("Variavel nao inteira")
        exit()
    if(tipo_trigonometrico == 1):
        print("(1) Expressao Simples ou (2) Expressao Composta")
        aux = int(input())
        if(aux == 1):
            def valorNumerico(list, grau, variavel):
                expressao = math.sin(list[0] * variavel + list[1])
                return expressao

            print("Digite conforme a expressao: sen(ax+b)")
            for i in range(2):
                coeficientes += [float(input())]
            a = float(input("x tende a qual valor ?"))
            variavel1 = a + 1
            variavel2 = a - 1
            limiteLateralEsquerdo(valorNumerico, coeficientes, grau, incrementer, a, variavel2)
            limiteLateralDireito(valorNumerico, coeficientes, grau, incrementer, a , variavel1)

        else:
            def valorNumerico(list, grau, variavel):
                expressao = list[0] * \
                    math.sin(list[1] * variavel ** list[2] + list[3])
                return expressao

            print("Digite conforme a expressao: a*sen(bx^n + c)")
            for i in range(4):
                coeficientes += [float(input())]
            a = float(input("x tende a qual valor ?"))
            variavel1 = a + 1
            variavel2 = a - 1
            limiteLateralEsquerdo(valorNumerico, coeficientes, grau, incrementer, a, variavel2)
            limiteLateralDireito(valorNumerico, coeficientes, grau, incrementer, a , variavel1)
    
    if(tipo_trigonometrico == 2):
        print("(1) Expressao Simples ou (2) Expressao Composta")
        aux = int(input())
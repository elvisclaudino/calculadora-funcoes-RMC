import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as numpy
import math as math

def menu_principal():
    print("---CALCULADORA---")  # MENU INICIAL
    print("1 - Funções do Segundo Grau")
    print("2 - Exponenciais")
    print("3 - Matrizes")
    print("4 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    return opcao

def menu_funcao_2grau():  # MENU DE FUNÇÕES DO SEGUNDO GRAU
    print("MENU FUNÇÕES 2 GRAU")
    print("1- Calcular raízes")
    print("2- Calcular função")
    print("3- Calcular Vértice")
    print("4- Gerar gráfico")
    print("5- Voltar")
    opcao = int(input('Qual sua opção?'))
    return opcao

def menu_funcao_exponencial():
    print("MENU FUNÇÕES EXPONENCIAIS")  # MENU FUNÇÕES EXPONENCIAIS
    print("1- CRESCENTE ou DECRESCENTE")
    print("2- 𝒇(𝒙)=𝒂𝒃𝒙")
    print("3- Gerar Gráfico")
    print("4- Voltar")
    opcao = int(input('Qual sua opção?'))
    return opcao

def menuMatrizes():  # função de menu das matrizes
    print("Estas sao as opcoes de calculo disponiveis para matrizes:")
    print("1-Determinante.")
    print("2-Multiplicação.")
    print("3-Transposta.")
    print("4-Retornar ao menu anterior")
    opcao = int(input('Qual sua opção?'))
    return opcao

def menuretry():
    print("1 - Deseja realizar outra operação")
    print("2 - Voltar ao menu")

def geradorGraph():  # FUNÇÕES DE GERAR GRÁFICOS
    print("Selecionado Gerador de gráficos")
    print(15 * '-=')
    graphX = []
    graphY = []
    numeroPontos = int(input("Digite o num de pontos:"))
    for cont in range(numeroPontos):
        graphX.append(int(input("Onde deseja posicionar os pontos no eixo X: ")))
        graphY.append((a * (graphX[cont] ** 2)) + (b * graphX[cont]) + c)
        print(15 * '-=')
    print(graphX)
    print(graphY)
    matplotlib.pyplot.plot(graphX, graphY)
    matplotlib.pyplot.show()

def calculo_funcao_2grau(a, b, c):
    x = float(input("Digite o valor de X: "))
    conta = (a*(x**2)) + (b*x) + c
    print(15* '-=')
    print("Sua função resultou em ", conta)

def fxabx():  # CALCULAR A FUNÇÃO
    print("A opção selecionada foi 𝒇(𝒙)=𝒂𝒃𝒙:")
    x = float(input('Qual o valor de X? '))
    valor = a * (b ** x)
    print(('O valor final é de {}').format(valor))
    print(15 * '-=')
    return x

def funcaoExponencial(a, x):
    return (a ** x)

def coletaMatriz():  # coleta a matriz
    numeroLinhas = int(input('Insira o número de linhas da matriz: '))
    numeroColunas = int(input('Insira o número de colunas da matriz: '))

    matriz = []
    linha = []

    for i in range(0, numeroLinhas):
        for j in range(0, numeroColunas):
            linha.append(float(input("Valor da posição {} x {}: ".format(i, j))))
        matriz.append(linha)
        linha = []

    matriz = np.array(matriz)
    return matriz

def matrizes():  # função de calculo das matrizes
    print("informe a matriz q irá ultilizar, com seu numero de linhas, colunas e seus coeficientes")
    matriz = coletaMatriz()

    while True:
        opcao = menuMatrizes()

        if opcao == 1:
            calcularDeterminante(matriz)
        # elif opcao == 2:
        # calcularMultiplicacao(matriz)

        elif opcao == 3:
            break

# ------------------------------ FUNÇÕES---------------------------------#
menu_selecao = menu_principal()
while menu_selecao > 5 or menu_selecao < 1:
    print(15 * '-=')
    print('Opção inexistente!')
    print(15 * '-=')
    menu_selecao = menu_principal()

while menu_selecao > 0 and menu_selecao < 5:
    if menu_selecao == 1:
        print("A opção selecionada foi Funções do Segundo Grau")
        valor_a = float(
            input("Digite um numero para a variável a: "))  # solicita ao usuário q informe o valor da variável A
        valor_b = float(
            input("Digite um numero para a variável b: "))  # solicita ao usuário q informe o valor da variável B
        valor_c = float(
            input("Digite um numero para a variável c: "))  # solicita ao usuário q informe o valor da variável C
        delta = ((valor_b) ** 2) - (4 * valor_a * valor_c)  # acumula o valor e realiza o calculo do delta

        while delta < 0:
            print("O delta é negativo, selecione novamente as variáveis")  # caso o delta der negativo
            valor_a = float(
                input("Digite um numero para a variável a: "))  # solicita ao usuário q informe o valor da variável A
            valor_b = float(
                input("Digite um numero para a variável b: "))  # solicita ao usuário q informe o valor da variável B
            valor_c = float(
                input("Digite um numero para a variável c: "))  # solicita ao usuário q informe o valor da variável C
            delta = ((valor_b) ** 2) - (4 * valor_a * valor_c)  # acumula o valor e realiza o calculo do delta

        valor_x1 = (-(valor_b) + ((delta) ** (1 / 2))) / (2 * valor_a)  # Calcula o valor do x1
        valor_x2 = (-(valor_b) - ((delta) ** (1 / 2))) / (2 * valor_a)  # Calcula o valor do x2

        valor_xV = -(valor_b) / (2 * valor_a)  # X do vértice
        valor_yV = -(delta) / (4 * valor_a)  # Y do vértice

        opcao_funcao_2grau = menu_funcao_2grau()

        if opcao_funcao_2grau > 5 or opcao_funcao_2grau < 1:  # Caso o usuário digite uma opção inválida
            print(15 * '-=')
            print('Opção inexistente!')
            print(15 * '-=')
            menu_funcao_2grau()
            opcao_funcao_2grau = menu_funcao_2grau()

        if opcao_funcao_2grau == 1:  # RAIZ SELECIONADA
            print("Raiz selecionada")
            print(15 * '-=')
            print('Valor de x1: {}'.format(round(valor_x1), 2))
            print('Valor de x2: {}'.format(round(valor_x2), 2))
            print(15 * '-=')

            op_return = menuretry()
            op_return = int(input("Digite opção para selecionar"))
            while op_return > 2 or op_return < 1:
                op_return = menuretry()
                op_return = int(input("Digite opção para selecionar"))
            if op_return == 1:
                continue
            elif op_return == 2:
                menu_selecao = menu_principal()

        if opcao_funcao_2grau == 2:
            print("Selecionado Calcular função")
            print("𝑓(𝑥)=𝑎𝑥2 +𝑏𝑥 +𝑐 ")
            calculo_funcao_2grau(valor_a, valor_b, valor_c)

            op_return = menuretry()
            op_return = int(input("Digite opção para selecionar"))
            while op_return > 2 or op_return < 1:
                op_return = menuretry()
                op_return = int(input("Digite opção para selecionar"))
            if op_return == 1:
                continue
            elif op_return == 2:
                menu_selecao = menu_principal()

        if opcao_funcao_2grau == 3:
            print('Selecionado Calcular Vértice')  # Calcula o vértice com os valores informados pelo usuário
            print('XV = {} | YV = {}'.format(valor_xV, valor_yV))

            op_return = menuretry()
            op_return = int(input("Digite opção para selecionar"))
            while op_return > 2 or op_return < 1:
                op_return = menuretry()
                op_return = int(input("Digite opção para selecionar"))
            if op_return == 1:
                continue
            elif op_return == 2:
                menu_selecao = menu_principal()

        if opcao_funcao_2grau == 4:
            print("A opção selecionada foi GERAR GRÁFICO")

            eixo_x = []
            eixo_y = []
            zero = []

            variacao = abs(valor_x1 - valor_x2)
            if variacao < 3:
                variacao = 3
            print(variacao)

            for x in np.arange(valor_x1 - variacao, valor_x2 + variacao, variacao / 100):  # Plota o gráfico
                y = valor_a * (x ** 2) + valor_b * (x) + valor_c
                eixo_x.append(x)
                eixo_y.append(y)
                zero.append(0.0)
            plt.plot(eixo_x, eixo_y, color="blue")
            plt.plot(eixo_x, zero, color="black")
            plt.show()

            op_return = menuretry()
            op_return = int(input("Digite opção para selecionar"))
            while op_return > 2 or op_return < 1:
                op_return = menuretry()
                op_return = int(input("Digite opção para selecionar"))
            if op_return == 1:
                continue
            elif op_return == 2:
                menu_selecao = menu_principal()

        else:
            menu_selecao = menu_principal()

    if menu_selecao == 2:
        print("A opção selecionada foi Funções Exponenciais")  # Pede ao usuário que informe o valor das variáveis
        a = float(input("Digite um numero para a variável a: "))
        b = float(input("Digite um numero para a variável b: "))
        escolha = menu_funcao_exponencial()

        if escolha > 4 or escolha < 1:
            print(15 * '-=')
            print("OPÇÃO INEXISTENTE")
            print(15 * '-=')

        elif escolha == 1:
            print("A opção selecionada foi CRESCENTE ou DECRESCENTE")
            if a > 0:
                print('A função é CRESCENTE')  # Informa se a função é crescente ou decrescente
            else:
                print('A função é DESCRESCENTE')
            op_return = menuretry()
            op_return = int(input("Digite opção para selecionar"))
            while op_return > 2 or op_return < 1:
                op_return = menuretry()
                op_return = int(input("Digite opção para selecionar"))
            if op_return == 1:
                continue
            elif op_return == 2:
                menu_selecao = menu_principal()

        elif escolha == 2:
            print("A opção selecionada foi 𝒇(𝒙)=𝒂𝒃𝒙:")  # Realizar o cálculo
            x = float(input('Qual o valor de X? '))
            valor = a * (b ** x)
            print(('O valor final é de {}').format(valor))
            print(15 * '-=')

            op_return = menuretry()
            op_return = int(input("Digite opção para selecionar"))
            while op_return > 2 or op_return < 1:
                op_return = menuretry()
                op_return = int(input("Digite opção para selecionar"))
            if op_return == 1:
                continue
            elif op_return == 2:
                menu_selecao = menu_principal()

        elif escolha == 3:
            print("A opção selecionada foi GERAR GRÁFICO")  # Gerar gráficos

            vetorX = np.arange(-7, 7, 0.1)

            print(vetorX)

            vetorY = []
            for x in vetorX:
                vetorY.append(funcaoExponencial(a, x))

            print(vetorY)

            fig = plt.figure(figsize=(5, 5))

            plt.plot(vetorX, vetorY, label='Funcao Exponencial', color='g')  # Plota o gráfico

            plt.title('f(x) = a^x')
            plt.xlabel('eixo x')
            plt.ylabel('eixo y')
            plt.legend()
            plt.grid(True, which='both')
            plt.axhline(y=0, color='k')
            plt.axvline(x=0, color='k')
            plt.show()
            fig.savefig('Fexp.png')

            op_return = menuretry()  # Pede ao jogador se o mesmo deseja retornar ao menu ou realizar outra operação
            op_return = int(input("Digite opção para selecionar"))
            while op_return > 2 or op_return < 1:
                op_return = menuretry()
                op_return = int(input("Digite opção para selecionar"))
            if op_return == 1:
                continue
            elif op_return == 2:
                menu_selecao = menu_principal()

        else:  # Caso seja desejado voltar
            menu_selecao = menu_principal()

    if menu_selecao == 3:  # MATRIZES
        opcao_matriz = menuMatrizes()

        if opcao_matriz == 1:
            matriz = coletaMatriz()
            print(matriz)
            print("Determinante da matriz")
            print(round(abs(np.linalg.det(matriz)), 2))

            op_return = menuretry()  # Pede ao jogador se o mesmo deseja retornar ao menu ou realizar outra operação
            op_return = int(input("Digite opção para selecionar"))
            while op_return > 2 or op_return < 1:
                op_return = menuretry()
                op_return = int(input("Digite opção para selecionar"))
            if op_return == 1:
                continue
            elif op_return == 2:
                menu_selecao = menu_principal()

        elif opcao_matriz == 2:
            print('Matriz A:')
            A = coletaMatriz()
            print(A)
            print('Matriz B: ')
            B = coletaMatriz()
            print(B)
            multiplicacao = np.dot(A, B)
            print(f'Multiplicação entre matriz AxB: {multiplicacao}')

            op_return = menuretry()  # Pede ao jogador se o mesmo deseja retornar ao menu ou realizar outra operação
            op_return = int(input("Digite opção para selecionar"))
            while op_return > 2 or op_return < 1:
                op_return = menuretry()
                op_return = int(input("Digite opção para selecionar"))
            if op_return == 1:
                continue
            elif op_return == 2:
                menu_selecao = menu_principal()

        elif opcao_matriz == 3:
            matriz = coletaMatriz()
            transposta = np.transpose(matriz)
            print(f'Transposta da matriz: {transposta}')

            op_return = menuretry()  # Pede ao jogador se o mesmo deseja retornar ao menu ou realizar outra operação
            op_return = int(input("Digite opção para selecionar"))
            while op_return > 2 or op_return < 1:
                op_return = menuretry()
                op_return = int(input("Digite opção para selecionar"))
            if op_return == 1:
                continue
            elif op_return == 2:
                menu_selecao = menu_principal()

        else: # CASO O USUÁRIO OPTE POR SAIR
            menu_selecao = menu_principal()
    else:
        print('Programa encerrado')
        break
#!/usr/bin/env python3

from os import system

operations = {
    's': 'subtração', 
    'a': 'adição', 
    'm': 'multiplicação', 
    'd': 'divisão'
    }

msg_opers = ' \n Selecione uma operação: \n > s-subtração \n > a-adicao \n > m-multiplicação \n > d-divisão \n\n>> '

# Verifica se a operation informada existe na lista de operações disponíveis
def has_operation(operation):
    return operation in operations.keys()

# 
def capture_operation():
    operation = input(msg_opers)

    if not has_operation(operation):
        system('clear')
        print(" \n Operação inválida! Escolha uma opção válida")
        return capture_operation()

    return operation

def calculate(operation, num1, num2):
    msg = ''
    result = 0.0

    if operation == 's':
        result = num1 - num2
        msg = '{} - {} = {}'.format(num1, num2, result)

    elif operation == 'a':
        result = num1 + num2
        msg = '{} + {} = {}'.format(num1, num2, result)

    elif operation == 'm':
        result = num1 * num2
        msg = '{} * {} = {}'.format(num1, num2, result)

    elif operation == 'd':
        if num1 == 0:
            print("O primeiro número não pode ser igual a zero!")
            return 

        result = num1 / num2
        msg = '{} / {} = {}'.format(num1, num2, result)

    return 'Resultado: {}'.format(msg)

def capture_numbers():
    num1 = input('Informe o primeiro numero  : ')
    num2 = input('Informe o segundo numero   : ')

    return (num1, num2)

def again():

    opcao = input('\n\nRealizar novo calculo? S - sim, N - não\n >>')
    if opcao.upper() == 'S':
        system('clear')
        main()
    else:
        print('\n\n Obrigado por usar nossa calculador! Até breve! ')
        return

def main():

    print("\n\n--------------------------------")
    print("--------  CALCULADORA ----------")
    print("--------------------------------\n\n")

    operation = capture_operation()
    (num1, num2) = capture_numbers()

    result = calculate(operation, float(num1), float(num2))
    print(result)

    again()


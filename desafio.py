# Soluções desafio - Target Sistemas.

"""1) Observe o trecho de código abaixo:

int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça

{

K = K + 1;

SOMA = SOMA + K;

}

imprimir(SOMA);



Ao final do processamento, qual será o valor da variável SOMA?
"""

# SOLUÇÃO 01:

INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K += 1
    SOMA = SOMA + K

print(SOMA)
#>>> 91

"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo 
valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa 
na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci 
e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
"""

# SOLUÇÃO 02:

def check_fibonacci(number):
    a, b = 0, 1
    
    while a <= number:
        if a == number:
            return True
        a, b = b, a + b

    return False

# Solicita ao usuário que informe um número e checa se o valor informado é um número.
try:
    input_number = int(input("Informe um número: "))
except ValueError:
    print("Por favor, insira um número válido.")
    exit()

# Checando se o número pertence à sequência de Fibonacci
if check_fibonacci(input_number):
    print(f"{input_number} pertence à sequência de Fibonacci.")
else:
    print(f"{input_number} não pertence à sequência de Fibonacci.")


"""
3) Descubra a lógica e complete o próximo elemento:



a) 1, 3, 5, 7, ___

b) 2, 4, 8, 16, 32, 64, ____

c) 0, 1, 4, 9, 16, 25, 36, ____

d) 4, 16, 36, 64, ____

e) 1, 1, 2, 3, 5, 8, ____

f) 2,10, 12, 16, 17, 18, 19, ____
"""

# SOLUÇÃO 03:

# a) 1, 3, 5, 7, ___
# Adiciona 2 ao número anterior.
# O próximo número é 7 + 2 = 9.

# b) 2, 4, 8, 16, 32, 64, ___
# Multiplica o número anterior por 2.
# O próximo número é 64 * 2 = 128.

# c) 0, 1, 4, 9, 16, 25, 36, ___
# Eleva o número anterior ao quadrado.
# O próximo número é 6^2 = 36.

# d) 4, 16, 36, 64, ___
# Os números estão sendo elevados ao quadrado.
# O próximo número é 8^2 = 64.

# e) 1, 1, 2, 3, 5, 8, ___
# Uma sequência de Fibonacci.
# O próximo número é 8 + 5 = 13.

# f) 2, 10, 12, 16, 17, 18, 19, ___
# Combinação de adição e padrão.
# O próximo número é 19 + 1 = 20.

# Portanto:

# a) 9
# b) 128
# c) 36
# d) 64
# e) 13
# f) 20

"""
4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente.
Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. 
Seu objetivo é descobrir qual interruptor controla qual lâmpada.
Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, 
qual interruptor controla cada lâmpada?
"""

# SOLUÇÃO 04:

# Antes da primeira ida a sala das lâmpadas:
# - Deixo um interruptor ligado e marco como sendo o interruptor 'A'.

# Na primeira ida à sala das lâmpadas:
# - Entrando na sala, vejo qual das luzes esta acesa;
# - Retiro a lâmpada que estava acesa e já sei que aquele é o soquete 
# do interruptor 'A', portanto, marco o soquete 'A'.


# Antes de ir pela segunda vez a sala das lâmpadas:
# - Deixo outro interruptor ligado;
# - Marco como interruptor 'B'.

# Na segunda ida à sala das lampadas:
# - Novamente, checo qual das luzes está acesa e já descubro qual pertence ao interruptor 'B';
# - Retiro a lâmpada que estava acesa, marco o soquete 'B'.


# Portanto podemos concluir que:
# - O útimo interruptor que sobrou é o 'C'.
# - Que pertence ao único soquete que sobrou que é o 'C'.

"""
5) Escreva um programa que inverta os caracteres de um string.


IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;
"""

# SOLUÇÃO 05:

def invert_string(string):
    reverse = ""

    for char in string:
        reverse = char + reverse

    return reverse

# Exemplo de uso:
original_string = input("Digite uma string: ")
inverted_string = invert_string(original_string)

print(f"A string invertida é: {inverted_string}")


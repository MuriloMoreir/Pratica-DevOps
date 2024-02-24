# Importações para o Código
from random import randint  # Importa a função randint da biblioteca random para gerar números aleatórios
from time import sleep  # Importa a função sleep da biblioteca time para fazer o programa esperar

tupla = ('PEDRA', 'PAPEL', 'TESOURA')  # Define uma tupla com as opções do jogo
computador = randint(0, 2)  # Gera um número aleatório entre 0 e 2 para a jogada do computador
print('Suas opções: \n[ 0 ] PEDRA \n[ 1 ] PAPEL \n[ 2 ] TESOURA')  # Exibe as opções de jogada para o usuário
jogador = int(input('Qual é a sua jogada ?'))  # Coleta a escolha do jogador através do input e converte para inteiro

print('JO')  # Simula a contagem regressiva do jogo
sleep(1)  # Espera 1 segundo
print('KEN')  # Continuação da contagem
sleep(1)  # Espera mais 1 segundo
print('PO!!!')  # Fim da contagem
sleep(1)  # Espera mais 1 segundo

print('-=' * 12)  # Exibe uma linha de separação
print('Computador jogou {}'.format(tupla[computador]))  # Mostra a jogada do computador usando a tupla
print('Jogador jogou {} '.format(tupla[jogador]))  # Mostra a jogada do jogador usando a tupla
print('-=' * 12)  # Exibe outra linha de separação

# Verifica o resultado do jogo comparando a escolha do computador com a do jogador
if computador == 0:  # Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!')  # Caso o jogador digite um número fora das opções

elif computador == 1:  # Computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!')  # Caso o jogador digite um número fora das opções

elif computador == 2:  # Computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')  # Caso o jogador digite um número fora das opções

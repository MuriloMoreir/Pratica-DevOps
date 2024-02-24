# Pedra, Papel e Tesoura

Um simples jogo de pedra, papel e tesoura implementado em Python. Neste jogo, você compete contra o computador, que escolhe sua jogada aleatoriamente. O resultado é determinado pela comparação das escolhas, seguindo as regras clássicas do jogo.

## Como Jogar

Ao executar o script, você verá três opções:

- [0] PEDRA
- [1] PAPEL
- [2] TESOURA

Você deve escolher uma das opções inserindo 0, 1 ou 2, conforme sua jogada desejada. Após a escolha, o jogo simula um pequeno suspense com "JO", "KEN", "PO!!!" e revela as jogadas tanto do computador quanto do jogador, juntamente com o resultado do confronto.

### Regras

- Pedra vence Tesoura (amassa ou quebra)
- Tesoura vence Papel (corta)
- Papel vence Pedra (embrulha)

### Resultados

Após ambas as jogadas serem reveladas, o jogo mostra o resultado, que pode ser:

- Jogador vence
- Computador vence
- Empate

Além disso, se uma jogada inválida for feita (algo que não seja 0, 1 ou 2), o jogo informará que foi uma "JOGADA INVÁLIDA!".

## Código

O script utiliza a biblioteca random para gerar a jogada do computador de forma aleatória e a biblioteca time para criar um efeito de suspense durante a revelação das jogadas. A lógica do jogo é implementada utilizando estruturas condicionais para comparar as escolhas e determinar o resultado.

from random import randint
from time import sleep

# Tupla com as possíveis jogadas
tupla = ('PEDRA', 'PAPEL', 'TESOURA')

# Escolha aleatória do computador
computador = randint(0, 2)

# Apresentação das opções para o jogador
print('Suas opções: \n[ 0 ] PEDRA \n[ 1 ] PAPEL \n[ 2 ] TESOURA')

# Entrada da jogada do jogador
jogador = int(input('Qual é a sua jogada ?'))

# Simulação do "JO", "KEN", "PO!!!"
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

# Apresentação das jogadas
print('-=' * 12)
print('Computador jogou {}'.format(tupla[computador]))
print('Jogador jogou {} '.format(tupla[jogador]))
print('-=' * 12)

# Lógica para determinar o resultado
if computador == 0: # Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 1: # Computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2: # Computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')


Divirta-se jogando pedra, papel e tesoura contra o computador!

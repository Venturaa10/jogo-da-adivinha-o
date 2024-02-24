import os
import random

def jogar():
    '''
    TITULO PERSONALIZADO
    '''
    os.system('cls')
    titulo = 'Bem vindo ao jogo de adivinhação'
    print('-'*len(titulo))
    print(titulo)
    print('-'*len(titulo))

    '''
    random.random -> Chamando a função random da biblioteca random
    round -> tirando as casas decimais do número gerado
    random.randrange(start,stop,step) - > O número vai começar no 1 e vai para no 100.
    '''

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000
    # print(numero_secreto)


    '''Nivel do Jogo'''
    nivel = int(input('''
        NIVEIS DE DIFICULDADE
        1 - FÁCIL
        2 - MÉDIO
        3 - DIFÍCIL

Digite o número correspondente ao nível que deseja: '''))

    if nivel == 1:
        total_de_tentativas = 15
    elif nivel == 2:
        total_de_tentativas = 10
    else: 
        total_de_tentativas = 5

    '''
    Linha de código abaixo é usado no laço while
    '''
    # rodada = 1

    '''LAÇOS DE REPETIÇÕES
    Enquanto rodada for menor ou igual ao número de tentativas disponiveis, o código sera executado
    .format() -> Uma outra maneira de manipular string
    print('Tentativa: {} de {}'.format(rodada,total_de_tentativas))
    '''

    # while(rodada <= total_de_tentativas):
    for rodada in range(1,total_de_tentativas + 1):
        print(f'Tentativa: {rodada} de {total_de_tentativas}')
        
        
        chute = int(input('Digite um número entre 1 e 100: '))
        print(f'Número escolhido pelo usuario: {chute}\n')

        if(chute < 1 or chute > 100):
            os.system('cls')
            print('Número invalido!\nDigite um número entre 1 e 100')
            continue

        acertou = chute == numero_secreto
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto

        '''
        Condição if e else criada para comparar os valores do chute e o número secreto
        Estou usando os parenteses nas condições apenas por boa pratica do projeto
        Break -> Se o usuario acertar, o laço para
        '''
        if acertou:
            os.system('cls')
            print(f'Você acertou o número secreto: {numero_secreto} e teve uma pontuação de {pontos} pontos.')
            break
        else:
            os.system('cls')
            if(chute_maior):
                print('Você Errou')
                print('O número secreto é menor\n') 
            elif(chute_menor):
                '''Os pontos perdidos é o número secreto - valor do chute do usuario.
                abs() -> Retorna valor absoluto, ou seja, -10 retorna 10
                '''
                print('Você Errou')
                print('O número secreto é maior\n')
            pontos_perdidos = abs(numero_secreto - chute) 
            pontos = pontos - pontos_perdidos
        '''
        Linha de código abaixo é usado no laço while
        '''
        # rodada = rodada +1

    print('Fim de jogo\n')

if(__name__ == "__main__"):
    jogar()
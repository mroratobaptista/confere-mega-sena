# Jogos Bolão Mega Sena

# Dolfo - BOLÃO
JOGOS_DOLFO = []
JOGOS_DOLFO.append('5 8 12 19 48 51'.split())
JOGOS_DOLFO.append('8 22 28 35 38 58'.split())
JOGOS_DOLFO.append('3 11 32 36 43 59'.split())
JOGOS_DOLFO.append('9 11 16 19 32 56'.split())
JOGOS_DOLFO.append('14 27 32 40 42 45'.split())

# Bruno - BOLÃO
JOGOS_BRUNO = []
JOGOS_BRUNO.append('03 19 20 31 46 55'.split())
JOGOS_BRUNO.append('01 26 12 16 17 59'.split())
JOGOS_BRUNO.append('15 39 43 13 21 09'.split())
JOGOS_BRUNO.append('34 06 03 20 17 37'.split())
JOGOS_BRUNO.append('09 15 16 21 34 39'.split())

# Caique - BOLÃO
JOGOS_CAIQUE = []
JOGOS_CAIQUE.append('05 10 23 25 30 31'.split())
JOGOS_CAIQUE.append('07 13 15 18 24 27'.split())
JOGOS_CAIQUE.append('12 17 21 33 39 44'.split())
JOGOS_CAIQUE.append('12 14 28 42 45 55'.split())
JOGOS_CAIQUE.append('05 10 27 37 43 54'.split())

# Flavio - BOLÃO
JOGOS_FLAVIO = []
JOGOS_FLAVIO.append('4 13 18 22 38 45'.split())
JOGOS_FLAVIO.append('3 14 22 27 40 50'.split())
JOGOS_FLAVIO.append('1 12 16 20 21 51'.split())
JOGOS_FLAVIO.append('6 8 29 34 35 55'.split())
JOGOS_FLAVIO.append('25 29 33 37 46 55'.split())

# José - BOLÃO
JOGOS_JOSE = []
JOGOS_JOSE.append('03 05 12 34 38 52'.split())
JOGOS_JOSE.append('01 09 15 23 39 42'.split())
JOGOS_JOSE.append('22 25 37 40 58 59'.split())
JOGOS_JOSE.append('08 13 17 28 34 46'.split())
JOGOS_JOSE.append('10 16 21 24 33 47'.split())

# Lucas - BOLÃO
JOGOS_LUCAS = []
JOGOS_LUCAS.append('02 04 25 33 55 56'.split())
JOGOS_LUCAS.append('10 13 21 44 47 51'.split())
JOGOS_LUCAS.append('14 19 30 39 52 54'.split())
JOGOS_LUCAS.append('7 9 22 24 40 45'.split())
JOGOS_LUCAS.append('20 21 38 42 50 57'.split())

# Raphael - BOLÃO
JOGOS_RAPHAEL = []
JOGOS_RAPHAEL.append('02 04 11 13 20 22'.split())
JOGOS_RAPHAEL.append('07 09 13 14 17 25'.split())
JOGOS_RAPHAEL.append('11 14 18 21 22 26'.split())
JOGOS_RAPHAEL.append('25 27 30 33 37 40'.split())
JOGOS_RAPHAEL.append('22 27 31 33 34 42'.split())

# Matheus - BOLÃO
JOGOS_MATHEUS = []
JOGOS_MATHEUS.append('7 14 34 42 45 60'.split())
JOGOS_MATHEUS.append('2 3 7 24 34 35'.split())
JOGOS_MATHEUS.append('1 12 34 35 45 49'.split())
JOGOS_MATHEUS.append('17 22 26 35 45 47'.split())
JOGOS_MATHEUS.append('15 16 29 48 49 55'.split())

# Thiago - BOLÃO
JOGOS_THIAGO = []
JOGOS_THIAGO.append('3 4 16 29 35 49'.split())
JOGOS_THIAGO.append('7 27 31 44 47 59'.split())
JOGOS_THIAGO.append('16 27 35 42 48 56'.split())
JOGOS_THIAGO.append('2 6 29 33 44 57'.split())
JOGOS_THIAGO.append('12 18 47 49 53 60'.split())

# Mariana - PARTICULAR
JOGOS_MARIANA = []
JOGOS_MARIANA.append('6 35 45 47 57 60'.split())
JOGOS_MARIANA.append('1 12 21 37 45 59'.split())

# NÚMEROS SORTEADOS
NUMEROS_SORTEADOS = '22 35 17 42 41 20'.split()
NUMEROS_SORTEADOS = [int(n) for n in NUMEROS_SORTEADOS]

SENA = 'R$ 325.250.216'
QUINA = 'R$ '
QUADRA = 'R$ '

QUANTIDADE_ACERTO_JOGO = 0


def conferir_quantos_numeros_acertou(numeros_sorteados, jogo):
    cont = 0

    nome_jogo = jogo.get('nome')
    numeros_jogo = jogo.get('numeros')

    for n in numeros_jogo:
        if n in numeros_sorteados:
            cont += 1

    print(f'{nome_jogo} - {numeros_jogo} - ACERTOU: {cont}')

    return cont


def montar_dicionario_jogo(nome, numeros):
    return {'nome': nome, 'numeros': numeros}


def conferir_jogos(jogos):
    cont = 1
    acertos = 0

    dono_jogo = jogos.get('dono_jogo')
    jogos = jogos.get('jogos')

    len(dono_jogo)

    qtd_tracos = len('---------------------')
    total_letras = qtd_tracos - (len(dono_jogo) + 8)
    tracinhos = int(total_letras / 2)
    tracinhos = tracinhos * '-'

    print('---------------------')
    print(f'{tracinhos} JOGOS {dono_jogo} {tracinhos}')

    for j in jogos:
        # ORGANIZA EM ORDEM CRESCENTE
        j = [int(n) for n in j]
        j.sort()

        jogo = montar_dicionario_jogo(nome=f'{dono_jogo} {cont}', numeros=j)
        acertos += conferir_quantos_numeros_acertou(NUMEROS_SORTEADOS, jogo)

        cont += 1

    print(f'{dono_jogo} ACERTO TOTAL: {acertos}')


if __name__ == '__main__':

    print('---------------------')
    print('- CONFERE MEGA SENA -')
    print('----------- BY MUBE -')

    JOGOS_DOLFO = {'dono_jogo': 'DOLFO', 'jogos': JOGOS_DOLFO}
    JOGOS_BRUNO = {'dono_jogo': 'BRUNO', 'jogos': JOGOS_BRUNO}
    JOGOS_CAIQUE = {'dono_jogo': 'CAIQUE', 'jogos': JOGOS_CAIQUE}
    JOGOS_FLAVIO = {'dono_jogo': 'FLAVIO', 'jogos': JOGOS_FLAVIO}
    JOGOS_JOSE = {'dono_jogo': 'JOSE', 'jogos': JOGOS_JOSE}
    JOGOS_LUCAS = {'dono_jogo': 'LUCAS', 'jogos': JOGOS_LUCAS}
    JOGOS_RAPHAEL = {'dono_jogo': 'RAPHAEL', 'jogos': JOGOS_RAPHAEL}
    JOGOS_MATHEUS = {'dono_jogo': 'MATHEUS', 'jogos': JOGOS_MATHEUS}
    JOGOS_THIAGO = {'dono_jogo': 'THIAGO', 'jogos': JOGOS_THIAGO}
    JOGOS_MARIANA = {'dono_jogo': 'MARIANA', 'jogos': JOGOS_MARIANA}

    conferir_jogos(JOGOS_DOLFO)
    conferir_jogos(JOGOS_BRUNO)
    conferir_jogos(JOGOS_CAIQUE)
    conferir_jogos(JOGOS_FLAVIO)
    conferir_jogos(JOGOS_JOSE)
    conferir_jogos(JOGOS_LUCAS)
    conferir_jogos(JOGOS_RAPHAEL)
    conferir_jogos(JOGOS_MATHEUS)
    conferir_jogos(JOGOS_THIAGO)
    conferir_jogos(JOGOS_MARIANA)

    print('---------------------')
    print('------ PREMIOS ------')

    print(f'SENA {SENA}')
    print(f'QUINA {QUINA}')
    print(f'QUADRA {QUADRA}')

    print('---------------------')
    print('-- FELIZ ANO NOVO ---')
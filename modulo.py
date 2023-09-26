# função para banco minusculo e alfabética

def para_minusculo(lista_teams):
    aux = []
    for i in range(len(lista_teams)):          # colocar palavras em minusculo
        t = str(lista_teams[i]).lower()        # convertendo em str e alterando
        aux.append(t)                          # adicionando a lista auxiliar
    aux.sort()
    return aux


# função para verificação se está maiusculo ou minusculo e espaçado


def verificar_palavra(nome_pokemon):
    if nome_pokemon.isupper():
        nome_pokemon.lower()
    elif nome_pokemon.islower():
        print()
    else:
        nome_pokemon.lower()
        print(nome_pokemon)

# função para remover espaço


def para_espaco(nome_pokemon):
    n = len(nome_pokemon)
    if nome_pokemon[0] == " " or nome_pokemon[n-1] == " ":
        nome = nome_pokemon.strip()
    nome = nome_pokemon.replace(" ", "_")
    return nome


# funcao para verificar se existe em db


def existe_Pokemon(nome_pokemon, db):
    ex = False
    for i in range(len(db)):
        if db[i] == nome_pokemon:
            ex = True
            break
    return ex


# função para verificar index do Pokemon na lista


def index_Pokemon(nome_pokemon, db):
    for i in range(len(db)):
        if db[i] == nome_pokemon:
            index_Pokemon = i
            break
    return index_Pokemon


# função para adicionar Pokemon na lista


def adicionar(nome_pokemon, db):
    if not existe_Pokemon(nome_pokemon, db):
        print(db)
        nome_pokemon.lower()                       # minusculo
        nome_pokemon2 = para_espaco(nome_pokemon)
        db.append(nome_pokemon2)
        db.sort()
        return db


# função para editar nome de um Pokemon


def editar(nome_atual, novo_nome, db):
    if existe_Pokemon(nome_atual, db) and not existe_Pokemon(novo_nome, db):
        index = index_Pokemon(nome_atual, db)
        db[index] = novo_nome
        db.sort()
        return db


# função para apagar nome de um Pokemon


def deletar(nome_pokemon, db):
    if existe_Pokemon(nome_pokemon, db):
        index = index_Pokemon(nome_pokemon, db)
        del (db[index])
        return db


def somar(v1, v2):
    return v1 + v2

# para_espaco(" nome aqui ")
# para_espaco("nome aqui ")
# para_espaco(" nome aqui")
# para_espaco("nome aqui")

# verificar_palavra("CASA")

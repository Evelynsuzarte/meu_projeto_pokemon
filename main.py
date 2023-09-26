from fastapi import FastAPI
from pydantic import BaseModel, validator
import requests
import modulo

app = FastAPI()

# visualizar pokemon - lista original
request = requests.get("https://pokeapi.co/api/v2/pokemon/")
data_json = request.json()
data_aux = data_json["results"]
data = []
for dic in data_aux:
    data.append(dic["name"])  
db = modulo.para_minusculo(data)


# validação de nome
class Pokemon(BaseModel):
    nome: str

    @validator("nome")
    def validate_nome(cls, n: str):
        if type(n) != str:
            raise TypeError("O item não é string")
        return n


# root
@app.get("/")
def read_root():
    return {"Evelyn": "World"}


# lista de pokemons
@app.get("/pokemons")
def pokemons():
    return db


# adicionar pokemon na lista
@app.post("/pokemons/add")
def adicionarPokemon(nome_pokemon):
    global db
    data_base = modulo.adicionar(nome_pokemon, db)
    db = data_base
    return db


# editar nome de um pokemon
@app.put("/pokemons/editar")
def editarPokemon(nome_pokemon, nome_novo):
    global db
    data_base = modulo.editar(nome_pokemon, nome_novo, db)
    db = data_base
    return db


# apagar nome do pokemon
@app.delete("/pokemons/apagar")
def apagarPokemon(nome_pokemon):
    global db
    data_base = modulo.deletar(nome_pokemon, db)
    db = data_base
    return db


# atualizar banco de dados
@app.get("/pokemons/at")
def atualizarLista():
    return db


#nome = Pokemon.validate_nome(2212)
#print(nome)



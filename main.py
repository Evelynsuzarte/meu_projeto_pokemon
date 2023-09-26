from fastapi import FastAPI
from pydantic import BaseModel, validator
import requests
import modulo

"""from .endpoints import team, certificate

app.include_router(team.router, prefix="/team")
app.include_router(certificate.router, prefix="/certificate")"""

app = FastAPI()


# validação de nome
class Time(BaseModel):
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


# visualizar times - lista original
request = requests.get("https://pokeapi.co/api/v2/pokemon/")
data_json = request.json()
data = data_json["results"]
data2 = []
#db = modulo.para_minusculo(data)

for linha in data:
    print (linha["name"])
    data2.append(linha["name"])  
    # for valor in linha.keys(): 
    #     print (linha["name"], valor)  

db = modulo.para_minusculo(data2)
print(db)
# lista de times
@app.get("/teams")
def teams():
    return db


# adicionar time na lista
@app.post("/teams/add")
def adicionarTime(nome_pokemon):
    global db
    data_base = modulo.adicionar(nome_pokemon, db)
    db = data_base
    return db


# editar nome de um time
@app.put("/teams/editar")
def editarTime(nome_pokemon, nome_novo):
    global db
    data_base = modulo.editar(nome_pokemon, nome_novo, db)
    db = data_base
    return db


# apagar nome do time
@app.delete("/teams/apagar")
def apagarTime(nome_pokemon):
    global db
    data_base = modulo.deletar(nome_pokemon, db)
    db = data_base
    return db


# atualizar banco de dados
@app.get("/teams/at")
def atualizarLista():
    return db


#nome = Time.validate_nome(2212)
#print(nome)



from fastapi import FastAPI
from pydantic import BaseModel

class pessoaRequest(BaseModel):
    name: str

app = FastAPI()

database = [{"name": "João", "id": 1},{"name": "Maria", "id": 2},{"name": "José", "id": 3}]

@app.get("/pessoas")
def read_item():
    return {"pessoas": database};

@app.get("/pessoas/{pessoa_id}")
def read_item(pessoa_id: int):
    for item in database:
        if item['id'] == pessoa_id:
            return item
    return {"message": "Pessoa não encontrada"}

@app.put("/pessoas/{pessoa_id}")
def update_item(pessoa_id: int, request: pessoaRequest):
    for item in database:
        if item['id'] == pessoa_id:
            item.update(request)
            return item
    return {"message": "Pessoa não encontrada"}

@app.post("/pessoas")
def create_item(request: pessoaRequest):
    database.append({
        "name": request.name,
        "id": len(database) + 1
    })
    return database[len(database) - 1]

@app.delete("/pessoas/{pessoa_id}")
def delete_item(pessoa_id: int):
    for item in database:
        if item['id'] == pessoa_id:
            database.remove(item)
            return {"message": "Pessoa removida com sucesso"}
    return {"message": "Pessoa não encontrada"}

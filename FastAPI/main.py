from typing import List, Optional
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Definicja klasy Mountains
class Mountains(BaseModel):
    name: str
    height: float  # Wysokość w metrach
    location: str  # Lokalizacja
    mountain_id: Optional[int] = None

# Prowizoryczna "baza danych" dla obiektów Mountains
database: List[Mountains] = []

# Endpoint: Zwraca wszystkie elementy z bazy danych
@app.get("/mountains")
def get_all_mountains() -> List[Mountains]:
    return database

# Endpoint: Zwraca element o wybranym ID
@app.get("/mountains/{mountain_id}")
def get_mountain(mountain_id: int) -> Mountains:
    mountains = [x for x in database if x.mountain_id == mountain_id]
    if not mountains:
        raise HTTPException(status_code=404, detail="Mountain not found")
    return mountains[0]

# Dodaje element do bazy danych
@app.post("/mountains")
def add_mountain(mountain: Mountains) -> Mountains:
    new_id = len(database) + 1  # Proste generowanie ID
    mountain.mountain_id = new_id
    database.append(mountain)
    return mountain

# Endpoint: Aktualizuje element o podanym ID
@app.put("/mountains/{mountain_id}")
def update_mountain(mountain_id: int, mountain: Mountains) -> Mountains:
    for i, existing_mountain in enumerate(database):
        if existing_mountain.mountain_id == mountain_id:
            updated_mountain = mountain.copy(update={"mountain_id": mountain_id})
            database[i] = updated_mountain
            return updated_mountain
    raise HTTPException(status_code=404, detail="Mountain not found")

# Endpoint: Usuwa element o podanym ID
@app.delete("/mountains")
def delete_mountain(mountain_id: int) -> dict:
    for i, existing_mountain in enumerate(database):
        if existing_mountain.mountain_id == mountain_id:
            deleted_mountain = database.pop(i)
            return {"message": "Mountain deleted successfully", "deleted_mountain": deleted_mountain}
    raise HTTPException(status_code=404, detail="Mountain not found")

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


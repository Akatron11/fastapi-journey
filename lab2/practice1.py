from fastapi import FastAPI, Body 

app = FastAPI()

crew = [
    {"id": 1, "name": "Cosmo", "role": "Captain"},
    {"id": 2, "name": "Alice", "role": "Engineer"},
    {"id": 3, "name": "Bob", "role": "Scientist"}
]

@app.post("/add_crew/")
async def add_crew(name: str = Body(...), role: str = Body(...)):
    if crew:
        new_id = crew[-1]["id"] + 1
    else:
        new_id = 1
        
    new_member = {"id": new_id, "name": name, "role": role}
    crew.append(new_member)
    
    return new_member
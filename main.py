from fastapi import FastAPI
from wallclock import Wallclock


app = FastAPI()
wallclock_list = []


@app.get("/")
def wallclock_shop():
    print(f"Inside Wallclock shop...")
    return {"message": "Welcome to the wallclock shop !"}

@app.post("/new-wallclock")
def add_new_wallclock(wallclock: Wallclock):
    wallclock_list.append(wallclock.dict())
    return wallclock_list

@app.get("/wallclocks")
def get_all_wallclocks():
    return wallclock_list

@app.delete("/wallclock/{id}")
def delete_wallclock_by_id(id: int):
    for wallclock in wallclock_list:
        if wallclock['id'] == id:
            wallclock_id = wallclock_list.index(wallclock)
            wallclock_list.pop(wallclock_id)
            return wallclock_list
    
    return {"message": "Wallclock not found"}
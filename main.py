import uvicorn
from fastapi import FastAPI
from joblib import load
from schemas.employee import Employee
from config.db import con
from models.index import employee

app = FastAPI()

#get all employee
@app.get("/api/employee")
async def index():
   data = con.execute(employee.select()).fetchall()
   return{
      "success": True,
      "employee": data
   }

#insert employee data into database
@app.post("/api/employee/store")
async def store(employe:Employee):
   data = con.execute(employee.insert().values(
      name = employe.name,
      email = employe.email,
      age = employe.age,
      country = employe.country
   ))

   if data.is_insert:
      return{
         "success": True,
         "message": "Employee store succesful"
      }
   else:
      return {
         "success": False,
         "message": "Something went wrong"
      }

#get edit employee
@app.get("/api/employee/edit/{id}")
async def edit(id:int):
   data = con.execute(employee.select().where(employee.c.id == id)).fetchall()
   return {
      "success": True,
      "employee": data
   }

#update employee
@app.put("/api/employee/update/{id}")
async def update(employe:Employee, id:int):
   data = con.execute(employee.update().where(employee.c.id == id).values(
      name = employe.name,
      email = employe.email,
      age = employe.age,
      country = employe.country
   ))

   if data:
      return{
         "success": True,
         "message": "Employee update successful"
      }
   else:
      return{
         "success": False,
         "message": "Something went wrong"
      }

#destroy employee
@app.delete("/api/employee/destroy/{id}")
async def destroy(id:int):
   data = con.execute(employee.delete().where(employee.c.id == id))
   return{
      "success": True,
      "message": "Employee destroy successful"
   }



if __name__ == '__main__':
   uvicorn.run(app, host='127.0.0.1', port=8000)
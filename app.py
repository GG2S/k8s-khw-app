from fastapi import FastAPI

app=FastAPI()

@app.get("/")
defroot():
return {"message":"hello kube!"}
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


app = FastAPI()
oauth_scheme = OAuth2PasswordBearer(tokenUrl="login")

@app.post("/login")
# Dependency Injection when using Depends()
async def get_token(request_form: OAuth2PasswordRequestForm = Depends()):
    print(f"The request Form: {request_form}")
    # allowed_users = ["Dove", "Austin"]
    # if request_form.username not in allowed_users:
    #     raise HTTPException(status_code=401)
    return {"access_token": "some-token", "token_type": "bearer"}


@app.get("/test")
async def get_something(token: str = Depends(oauth_scheme)):
    return {"message": "you did it!", "token": token}


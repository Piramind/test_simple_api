from fastapi import FastAPI

app = FastAPI()

@app.get('/name={name}&message={message}/')
def get_hello(name: str , message: str):
    return f"Hello {name}! {message}!"
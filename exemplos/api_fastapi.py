from fastapi import FastAPI

app =  FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
    Endpoint que exibe uma mensagem de boas vindas ao mundo da programação
    
    '''
    return { 'Hello': 'World!'}

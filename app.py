from flask  import Flask 

app = Flask ("ola") #criando uma instancia da classe flask

@app.route('/') #decorator para criar rotas para o site, nesse caso uma raiz (/)
def ola(): #definição de função
    return ("ola mundo")
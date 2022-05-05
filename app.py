from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Diego Batista - https://github.com/apokalypsi/devopslab-7aso"

if __name__ == '__main__':
    app.run()
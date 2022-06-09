from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)


@app.route("/")
def pagina_inicial():
    return "Diego Batista - https://github.com/apokalypsi/devopslab-7aso"


if __name__ == '__main__':
    import os

    porta = int(os.getenv('PORT'))
    app.run('0.0.0.0', port=porta)

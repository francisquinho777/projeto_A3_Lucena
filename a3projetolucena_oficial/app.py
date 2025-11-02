from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dicionário para armazenar votos
votos = {
    "Saúde e bem-estar": 0,
    "Limpeza e melhorias": 0,
    "Educação e cultura": 0,
    "Esporte e lazer": 0,
    "Ação social e cidadania": 0
}

@app.route('/')
def index():
    return render_template('index.html', votos=votos)

@app.route('/votar', methods=['POST'])
def votar():
    escolha = request.form.get('projeto')
    if escolha in votos:
        votos[escolha] += 1
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

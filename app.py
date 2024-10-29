from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicial():
    return render_template('index.html')

@app.route('/linux')
def sobre():
    return render_template('linux.html')

@app.route('/office')
def contato():
    return render_template('office.html')

@app.route('/windows')
def dados():
    return render_template('windows.html')

@app.route('/programacao')  # Corrigi a indentação aqui
def programacao():
    return render_template('programacao.html')

if __name__ == '__main__':
    app.run(debug=True)
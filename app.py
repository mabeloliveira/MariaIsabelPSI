from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index(): 
    return 'Compre sua faixa da TOLF' 

@app.route('/compras')
def compras():
    #return '<ul><li>Arroz</li></ul>'   
    return render_template('compras.html')

@app.route('/mercados')
def mercados():
    return render_template('mercados.html')

if __name__                                                                                                                                                                                                                                                                                                                    == 'main':
    app.run()
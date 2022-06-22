from clase.graficos import *

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def graf():

    #grafico de Barras General

    graficoG = graficos("Progreso indicadores general", "general")
    barG_img = graficoG.crearGrafico()

    #grafico de Barras mes enero

    graficoG = graficos("Progreso indicadores enero", "Enero")
    barE_img = graficoG.crearGrafico()

    return render_template('index.html', barG_url = barG_img, barE_url = barE_img)

if __name__ == '__main__':
   app.run(debug = True)
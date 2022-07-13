from clase.factoryGraficos import *

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def graf():

    #grafico de Barras General

    graficoG = GraficoFactory.get_grafico("GraficoBarra","Progreso indicadores general", "general", "indicador1")
    barG_img = graficoG.crearGrafico()

    #grafico de Barras mes especifico

    graficoE =  GraficoFactory.get_grafico("GraficoBarra","Progreso indicadores Enero", "Enero","indicador1")
    barE_img = graficoE.crearGrafico()

    return render_template('index.html', barG_url = barG_img, barE_url = barE_img)

if __name__ == '__main__':
   app.run(host="localhost",port=7000,debug = True)
from clase.graficos import *

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def graf():

    #print(list_indicadores)

    #grafico de Barras General

    graficoG = graficos("Progreso indicadores general", "Febrero")
    graficoG.crearGrafico()
    barG_img = 'static/images/barG_chart.svg'

    #grafico de Barras mes enero

    #list_indicadores.plot(x = 'nombre_indicador', y = 'Enero' , kind='bar' ,title = 'Progreso indicadores Mes de Enero')
    #plt.gcf().subplots_adjust(bottom= 0.20)
    #plt.xlabel('Indicadores')
    #plt.ylabel('Progreso')
    #plt.xticks(rotation = 45, horizontalalignment = 'center')
    #plt.savefig('static/images/barE_chart.svg')
    #barE_img = 'static/images/barE_chart.svg'
    return render_template('index.html', barG_url = barG_img)

if __name__ == '__main__':
   app.run(debug = True)
import matplotlib.pyplot as plt
import pandas as pd 
import csv


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def graf():
    plt.style.use('ggplot')

    list_indicadores = pd.read_csv('indicador.csv', index_col=None)

    print(list_indicadores)

    #grafico de Barras General

    list_indicadores.plot(x = 'nombre_indicador', y = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'], kind='bar' ,title = 'Progreso indicadores Mes a Mes')
    plt.gcf().subplots_adjust(bottom= 0.20)
    plt.xlabel('Indicadores')
    plt.ylabel('Progreso')
    plt.xticks(rotation = 45, horizontalalignment = 'center')
    plt.savefig('static/images/barG_chart.svg')
    barG_img = 'static/images/barG_chart.svg'

    #grafico de Barras 

    list_indicadores.plot(x = 'nombre_indicador', y = 'Enero' , kind='bar' ,title = 'Progreso indicadores Mes de Enero')
    plt.gcf().subplots_adjust(bottom= 0.20)
    plt.xlabel('Indicadores')
    plt.ylabel('Progreso')
    plt.xticks(rotation = 45, horizontalalignment = 'center')
    plt.savefig('static/images/barE_chart.svg')
    barE_img = 'static/images/barE_chart.svg'
    return render_template('index.html', barG_url = barG_img, barE_url = barE_img)



if __name__ == '__main__':
   app.run(debug = True)
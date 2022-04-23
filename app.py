import pygal
import json

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def graf():
    with open('datos.json','r') as datos_file:
        data = json.load(datos_file)
        
    #ejemplo grafico de barras
    bar_chart = pygal.Bar()
    bar_chart.title = "Grafico de barras"
    mark_list = [x['mark'] for x in data]
    bar_chart.add('ejemplo',mark_list)
    bar_chart.x_labels = [x['year'] for x in data]
    bar_chart.render_to_file('static/images/bar_chart.svg')
    bar_img = 'static/images/bar_chart.svg'

    #ejemplo grafico de linea

    line_chart = pygal.Line() 
  
    line_chart.title = 'Grafico de lineas'
    line_chart.add('ejemplo',mark_list)
    line_chart.x_labels = [x['year'] for x in data]
    line_chart.render_to_file('static/images/line_chart.svg')
    line_img = 'static/images/line_chart.svg'



    return render_template('index.html',bar_url = bar_img, line_url = line_img)



if __name__ == '__main__':
   app.run(debug = True)
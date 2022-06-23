from collections import abc
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
from abc import ABCMeta, abstractstaticmethod

class Igrafico(metaclass = ABCMeta):

    @abstractstaticmethod
    def crearGrafico():
        pass

class GraficoBarra(Igrafico):
    def __init__(self, titulo, mes):
        self.indicadores = pd.read_csv('indicador.csv', index_col=None)
        self.ejeX = "Indicadores"
        self.ejeY = "Progreso"
        self.titulo = titulo

        if(mes == "general"):
            column = self.indicadores.columns.values
            mes = np.delete(column,0)
            
        self.mes = mes

    def crearGrafico(self):
        plt.style.use('ggplot')
        self.indicadores.plot(x = 'nombre_indicador', y = self.mes, kind='bar' ,title = self.titulo)
        plt.gcf().subplots_adjust(bottom= 0.20)
        plt.xlabel(self.ejeX)
        plt.ylabel(self.ejeY)
        plt.xticks(rotation = 45, horizontalalignment = 'center')
        ruta = 'static/images/' + self.titulo + '.svg'
        plt.savefig(ruta)
        return ruta

class GraficoFactory():
    
    @staticmethod
    def get_grafico(graficotype, titulo, mes):
        try:
            if graficotype == "GraficoBarra":
                return GraficoBarra(titulo, mes)
            raise AssertionError("Grafico no encontrado :c")
        except AssertionError as _e:
            print(_e)

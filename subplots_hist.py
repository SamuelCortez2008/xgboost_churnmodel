"""
Código para ploteo de subplots de Histogramas

Autor: Samuel Cortez
"""

# librería para el manejo de datos
import pandas as pd

# librerías de visualización
import seaborn as sns
import matplotlib.pyplot as plt


class visualizacion_sns:

    def __init__(self, y_min, y_max) -> None:
        """
        Se inicializan los intervalos que identifican los cuartiles 
        """
        self.y_min = y_min
        self.y_max = y_max
        pass
    
    def sns_vis_subplots(self, df: pd.DataFrame, col_list: list, title: str, categoria:str = None, method_sns = sns.histplot):
        """
        Subplots con los histogramas de las variables de proceso
        
        @parametros:
        -------------------------
        df: DataFrame, dataset con las variables de proceso
        cols_list: list, arreglo con los nombres de las columnas a plotear
        title: str, Titulo superior de la figura.
        categoria: str, nombre de columna categórica 
        
        @return:
        ------------------------
        Figura subplots
        
        """
        sns.set(style = 'darkgrid')
        
        if categoria is not None:
            col_list = col_list + [categoria]
            n_vars = len(col_list) -1
        else:
            n_vars = len(col_list)
                
        self.df_ = df[col_list]
        nrows = int(n_vars/2)
        fig_hist, ax_hist = plt.subplots(nrows = nrows, ncols = 2, figsize = (18,14))
        fig_hist.suptitle(title,  fontsize = 18, y = 1)
        j, k = 0, 0
        cond = True
            
        for i, col in enumerate(col_list[:n_vars]):
            method_sns(data = self.df_ , x = col, ax = ax_hist[k][j], hue = categoria, kde = True)
            
            if method_sns is  sns.histplot:
                q1_col = self.df_ [col].quantile(0.25)
                q3_col = self.df_ [col].quantile(0.75)
                IQR = q3_col -q1_col
                Lim_sup_ = q3_col + 1.5*IQR
                Lim_inf_ = q1_col - 1.5*IQR
                        
                ax_hist[k][j].vlines(q1_col,self.y_min,self.y_max, colors = 'k')
                ax_hist[k][j].vlines(q3_col,self.y_min,self.y_max, colors = 'k')
            
            if i >= (nrows-1):
                if cond:
                    cond = not(cond)
                else:
                    k -= 1
                j = 1
            else:
                k += 1

        plt.tight_layout()
        plt.show()

if __name__ == '__main__':
    print('Programa para plotear subplots')
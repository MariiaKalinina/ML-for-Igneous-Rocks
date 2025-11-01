import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class Visualizer:
    def __init__(self):
        plt.style.use('seaborn-v0_8')
        self.csfont = {'fontname':'Times New Roman'}
    
    def plot_lithology_distributions(self, data):
        """Визуализация распределений параметров по литологии"""
        parameters_list = ['ГК ', 'ГГпК', 'ПС', 'КС']
        
        fig = plt.figure(figsize=(15, 10))
        
        for index, param in enumerate(parameters_list):
            ax = plt.subplot(2, 2, index + 1)
            sns.histplot(data=data, x=param, hue='Литология', stat="probability", 
                        kde=True, bins=20)
            plt.title(f'Распределение {param} по литологии', **self.csfont)
            plt.xlabel(param, **self.csfont)
            plt.ylabel('Вероятность', **self.csfont)
        
        plt.tight_layout()
        plt.show()
    
    def plot_correlation_heatmap(self, data):
        """Построение тепловой карты корреляций"""
        numeric_data = data.select_dtypes(include=[np.number])
        plt.figure(figsize=(10, 8))
        sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', center=0)
        plt.title('Корреляционная матрица параметров', **self.csfont)
        plt.tight_layout()
        plt.show()

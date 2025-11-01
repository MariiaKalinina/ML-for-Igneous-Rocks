import pandas as pd
import numpy as np

class DataPreprocessor:
    def __init__(self):
        self.well_logs = None
        self.thermal_logs = None
        self.lithology = None
    
    def prepare_well_logs(self, data):
        """Подготовка данных каротажа"""
        # Удаление ненужных столбцов
        data.drop(['Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8'], 
                 axis=1, inplace=True)
        
        # Переименование столбцов
        data.rename(columns={'Глубина': 'Глубина_КС'}, inplace=True)
        data.rename(columns={'ГК': 'ГК '}, inplace=True)
        data.rename(columns={'Глубина_ГК': 'Глубина_ГК '}, inplace=True)
        data.rename(columns={'ГГК-п ': 'ГГпК'}, inplace=True)
        data.rename(columns={'Глубина_ГГК-п': 'Глубина_ГГпК'}, inplace=True)
        
        # Разделение на каротаж и термометрию
        well_logs = data[['Глубина_ГК ', 'ГК ', 'Глубина_ГГпК', 'ГГпК', 
                         'Глубина_ПС', 'ПС', 'Глубина_КС', 'КС']].drop(0)
        well_logs['Глубина_ПС'] = well_logs['Глубина_ПС'] - 0.04
        
        thermal_logs = data[['Sample ID', 'Top Depth', 'TC initial', 'Offset', 'Depth_TC']]
        
        self.well_logs = well_logs
        self.thermal_logs = thermal_logs
        return well_logs, thermal_logs
    
    def prepare_lithology_data(self, lithology_data):
        """Подготовка литологических данных"""
        lithology = lithology_data[['Кровля', 'Подошва', 'Литология']].dropna()
        self.lithology = lithology
        return lithology
    
    def merge_well_logs(self, well_logs):
        """Объединение данных ГИС с единой привязкой по глубине"""
        def filter_numeric_range(df, column_name, lower_bound, upper_bound, step):
            df[column_name] = pd.to_numeric(df[column_name], errors='coerce')
            filtered_df = df[(df[column_name] >= lower_bound) & (df[column_name] <= upper_bound)]
            filtered_df = filtered_df.dropna()
            filtered_df['Глубина'] = filtered_df[column_name]
            return filtered_df.reset_index(drop=True)
        
        # Фильтрация и объединение данных
        lower_bound, upper_bound, step = 12.7, 164.1, 0.1
        
        filtered_df_1 = filter_numeric_range(well_logs[['Глубина_ГК ', 'ГК ']], 
                                           'Глубина_ГК ', lower_bound, upper_bound, step)
        filtered_df_2 = filter_numeric_range(well_logs[['Глубина_ГГпК', 'ГГпК']], 
                                           'Глубина_ГГпК', lower_bound, upper_bound, step)
        filtered_df_3 = filter_numeric_range(well_logs[['Глубина_ПС', 'ПС']], 
                                           'Глубина_ПС', lower_bound, upper_bound, step)
        filtered_df_4 = filter_numeric_range(well_logs[['Глубина_КС', 'КС']], 
                                           'Глубина_КС', lower_bound, upper_bound, step)
        
        # Объединение данных
        result = pd.merge(filtered_df_1, filtered_df_2, on="Глубина", how='inner')
        result = pd.merge(result, filtered_df_3, on="Глубина", how='inner')
        result = pd.merge(result, filtered_df_4, on="Глубина", how='inner')
        
        # Удаление лишних столбцов
        columns_to_drop = [col_name for col_name in well_logs.columns if 'Глубина_' in col_name]
        result.drop(columns=columns_to_drop, inplace=True)
        
        well_logs_merged = result[['Глубина', 'ГК ', 'ГГпК', 'ПС', 'КС']]
        return well_logs_merged

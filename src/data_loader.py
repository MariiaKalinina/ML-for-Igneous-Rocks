import pandas as pd
from pathlib import Path
from config.paths import RAW_DATA_PATH

class DataLoader:
    def __init__(self):
        self.data = None
        self.lithology_data = None
    
    def load_well_logs(self):
        """Загрузка данных каротажа скважин"""
        data_initial = pd.read_excel(RAW_DATA_PATH, sheet_name='Well logging', skiprows=0)
        return data_initial.copy()
    
    def load_lithology_data(self):
        """Загрузка литологических данных"""
        data_initial_lithology = pd.read_excel(RAW_DATA_PATH, sheet_name='Lithology_full', skiprows=0)
        return data_initial_lithology.copy()

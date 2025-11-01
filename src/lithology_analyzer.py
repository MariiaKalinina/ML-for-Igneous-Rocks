import pandas as pd

class LithologyAnalyzer:
    def __init__(self):
        self.merged_data = None
    
    def assign_lithology(self, lithology, well_logs_merged):
        """Присвоение литологии данным каротажа"""
        corresponding_lit = pd.DataFrame(columns=['Глубина', 'Литология'])
        
        for index, row in well_logs_merged.iterrows():
            common_depth = row['Глубина']
            mask = (lithology['Кровля'] <= common_depth) & (lithology['Подошва'] >= common_depth)
            filtered_lithology = lithology[mask]
            
            for _, lit_row in filtered_lithology.iterrows():
                new_row = pd.DataFrame({
                    'Глубина': [common_depth],
                    'Литология': [lit_row['Литология']]
                })
                corresponding_lit = pd.concat([corresponding_lit, new_row], ignore_index=True)
        
        return corresponding_lit
    
    def merge_with_lithology(self, lithology_data, well_logs_merged):
        """Объединение данных каротажа с литологией"""
        lithology_assigned = self.assign_lithology(lithology_data, well_logs_merged)
        
        result_new = pd.merge(
            lithology_assigned,
            well_logs_merged,
            on='Глубина',
            how='inner'
        )
        
        self.merged_data = result_new
        return result_new

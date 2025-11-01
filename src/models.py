from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

class LithologyPredictor:
    def __init__(self):
        self.models = {
            'Random Forest': RandomForestClassifier(),
            'Logistic Regression': LogisticRegression(),
            'SVM': SVC()
        }
        self.results = {}
    
    def prepare_features(self, data):
        """Подготовка признаков для моделирования"""
        # Кодирование литологии
        lithology_encoded = pd.get_dummies(data['Литология'])
        
        # Объединение признаков
        features = pd.concat([data[['ГК ', 'ГГпК', 'ПС', 'КС']], lithology_encoded], axis=1)
        
        return features
    
    def train_models(self, X, y):
        """Обучение нескольких моделей"""
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=42, stratify=y
        )
        
        for name, model in self.models.items():
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            
            self.results[name] = {
                'model': model,
                'accuracy': accuracy,
                'predictions': y_pred,
                'true_values': y_test
            }
            
            print(f"{name} Accuracy: {accuracy:.4f}")
        
        return self.results

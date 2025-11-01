# Thermophysical Properties Prediction for Igneous Rocks

ML application for predicting thermal conductivity tenosr and volumetric heat capacity of igneous rocks using well logging data and core measurements.

## Technologies

- **R Programming**
- **ML Libraries**: Scikit-Learn, XGBoost/LightGBM/CatBoost
- **Data Processing**: dplyr, tidyr
- **Visualization**: ggplot2, plotly
- **Statistical Analysis**: stats, car

## Data Sources

### Input Features:
- **Well Logging Data**:
  - Gamma Ray (GR) - natural radioactivity
  - Gamma-Gamma Density Log (GGDL) - bulk density
  - Resistivity Log (RL) - electrical properties
  - Spontaneous Potential (SP) - electrochemical activity
- **Rock Type**: categorical geological classification

### Target Variables:
- Thermal Conductivity Tensor Conponents (W/m·K)
- Volumetric Heat Capacity (J/m³·K)

### 1. Data Preprocessing
- Resolution matching of logging data to core measurements
- Feature scaling and normalization
- Categorical encoding of rock types
- Handling of missing values and outliers

### 2. Machine Learning Methods
- **Random Forests** - robust ensemble method
- **Gradient Boosting** (XGBoost) - high predictive accuracy
- **Support Vector Machines** - for non-linear relationships
- **Linear Models** - baseline performance

### 3. Model Validation
- Cross-validation (k-fold)
- Performance metrics: RMSE, MAE, R²
- Feature importance analysis
- Residual analysis


import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

from crop_yield_model.config.core import config
from crop_yield_model.processing.features import Mapper
from crop_yield_model.processing.features import OutlierHandler, YearOneHotEncoder

crop_yield_pipe = Pipeline([

    ######### Imputation ###########

    ######### Mapper ###########
    # print(config.crop_config)
    ('crop_country', Mapper(variable = config.crop_config.crop_country_var, mappings = config.crop_config.crop_country_mappings)),
    
    ('crop_name', Mapper(variable = config.crop_config.crop_name_var, mappings = config.crop_config.crop_name_mappings)),
    
    
    ######## Handle outliers ########
    ('handle_outliers_pesticide', OutlierHandler(variable = config.crop_config.crop_pesticides_var)),
    ('handle_outliers_rain', OutlierHandler(variable = config.crop_config.country_rain_var)),
    ('handle_outliers_temp', OutlierHandler(variable = config.crop_config.country_temp_var)),

    ######## One-hot encoding ########
    ('encode_year', YearOneHotEncoder(variable = config.crop_config.crop_year_var)),

    # Scale features
    ('scaler', StandardScaler()),
    
    # Regressor
    ('model_rf', RandomForestRegressor(n_estimators = config.crop_config.n_estimators, 
                                       max_depth = config.crop_config.max_depth,
                                      random_state = config.crop_config.random_state))
    
    ])
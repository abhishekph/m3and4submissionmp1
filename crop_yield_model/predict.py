import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from typing import Union
import pandas as pd
import numpy as np

from crop_yield_model import __version__ as _version
from crop_yield_model.config.core import config
from crop_yield_model.processing.data_manager import load_pipeline
from crop_yield_model.processing.data_manager import pre_pipeline_preparation
from crop_yield_model.processing.validation import validate_inputs


pipeline_file_name = f"{config.app_config.pipeline_save_file}{_version}.pkl"
crop_yield_pipe = load_pipeline(file_name = pipeline_file_name)


def make_prediction(*, input_data: Union[pd.DataFrame, dict]) -> dict:
    """Make a prediction using a saved model """
    
    validated_data, errors = validate_inputs(input_df = pd.DataFrame(input_data))
    
    validated_data = validated_data.reindex(columns = config.crop_config.features)
    
    results = {"predictions": None, "version": _version, "errors": errors}
      
    if not errors:
        predictions = crop_yield_pipe.predict(validated_data)
        results = {"predictions": np.floor(predictions), "version": _version, "errors": errors}
        print(results)
    else:
        print(errors)

    return results



if __name__ == "__main__":

    # 114254
    data_in = {'Area': ['Pakistan'], 
               'Item': ['Sweet potatoes'], 
               'Year': [2009], 
               'average_rain_fall_mm_per_year': [494.0], 
               'pesticides_tonnes': [3957.61], 
               'avg_temp': [25.37]}
    make_prediction(input_data = data_in)
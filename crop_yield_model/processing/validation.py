import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from typing import List, Optional, Tuple, Union

from datetime import datetime
import numpy as np
import pandas as pd
from pydantic import BaseModel, ValidationError

from crop_yield_model.config.core import config
from crop_yield_model.processing.data_manager import pre_pipeline_preparation


def validate_inputs(*, input_df: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[dict]]:
    """Check model inputs for unprocessable values."""

    pre_processed = pre_pipeline_preparation(data_frame = input_df)
    validated_data = pre_processed[config.crop_config.features].copy()
    errors = None

    try:
        # replace numpy nans so that pydantic can validate
        MultipleDataInputs(
            inputs = validated_data.replace({np.nan: None}).to_dict(orient="records")
        )
    except ValidationError as error:
        errors = error.json()

    return validated_data, errors


class DataInputSchema(BaseModel):
    Area: Optional[str]
    Item: Optional[str]
    Year: Optional[int]
    average_rain_fall_mm_per_year: Optional[float]
    pesticides_tonnes: Optional[float]
    avg_temp: Optional[float]
    # data_in = {'Area': ['Pakistan'], 
    #            'Item': ['Wheat'], 
    #            'Year': [2009], 
    #            'average_rain_fall_mm_per_year': [494.0], 
    #            'pesticides_tonnes': [3957.61], 
    #            'avg_temp': [25.37]}


class MultipleDataInputs(BaseModel):
    inputs: List[DataInputSchema]
from typing import Any, List, Optional
import datetime

from pydantic import BaseModel
from crop_yield_model.processing.validation import DataInputSchema


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    #predictions: Optional[List[int]]
    predictions: Optional[int]


class MultipleDataInputs(BaseModel):
    inputs: List[DataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                        {'Area': ['Pakistan'], 
                        'Item': ['Wheat'], 
                        'Year': [2009], 
                        'average_rain_fall_mm_per_year': [494.0], 
                        'pesticides_tonnes': [3957.61], 
                        'avg_temp': [25.37]}
                ]
            }
        }
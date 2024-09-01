
"""
Note: These tests will fail if you have not first trained the model.
"""

import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import numpy as np
from crop_yield_model.config.core import config
from crop_yield_model.processing.features import Mapper, OutlierHandler, YearOneHotEncoder


def test_country_variable_mapper(sample_input_data):
    # # Given
    # mapper = Mapper(variable = config.crop_config.crop_country_var, 
    #                 mappings = config.crop_config.crop_country_mappings
    #                 )
    # assert sample_input_data[0].loc[2, 'Area'] == 'India'

    # # When
    # subject = mapper.fit(sample_input_data[0]).transform(sample_input_data[0])

    # # Then
    # assert subject.loc[2, 'Area'] == 42
    pass


def test_rainfall_variable_outlierhandler(sample_input_data):
    # # Given
    # encoder = OutlierHandler(variable = config.crop_config.country_rain_var)
    # q1, q3 = np.percentile(sample_input_data[0]['average_rain_fall_mm_per_year'], q=[500, 3000])
    # iqr = q3 - q1
    # assert sample_input_data[0].loc[0, 'average_rain_fall_mm_per_year'] > q3 + (1.5 * iqr)

    # # When
    # subject = encoder.fit(sample_input_data[0]).transform(sample_input_data[0])

    # # Then
    # assert subject.loc[0, 'average_rain_fall_mm_per_year'] <= q3 + (1.5 * iqr)
    pass

def test_year_variable_encoder(sample_input_data):
    # # Given
    # encoder = YearOneHotEncoder(variable = config.crop_config.crop_year_var)
    # assert sample_input_data[0].loc[2, 'Year'] == 1995

    # # When
    # subject = encoder.fit(sample_input_data[0]).transform(sample_input_data[0])

    # # Then
    # assert subject.loc[2, 'Year'] == 3
    pass
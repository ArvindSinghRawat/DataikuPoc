# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
GHG_Emissions_prepared = dataiku.Dataset("GHG_Emissions_prepared")
GHG_Emissions_prepared_df = GHG_Emissions_prepared.get_dataframe()
Input_prepared = dataiku.Dataset("Input_prepared")
Input_prepared_df = Input_prepared.get_dataframe()


# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

Output_df = ... # Compute a Pandas dataframe to write into Output


# Write recipe outputs
Output = dataiku.Dataset("Output")
Output.write_with_schema(Output_df)

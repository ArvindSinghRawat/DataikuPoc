# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
input = dataiku.Dataset("Processed_Input")
input_df = Processed_Input.get_dataframe()
ghg_emmissions = dataiku.Dataset("GHG_Emissions_processed")
ghg_emmissions_df = GHG_Emissions_processed.get_dataframe()


# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

labels = pd.Series(list(range(2020,2100)))
cash = input_df["Cash and cash equivalents"]

pd.


Output_df = ... # Compute a Pandas dataframe to write into Output


# Write recipe outputs
Output = dataiku.Dataset("Output")
Output.write_with_schema(Output_df)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
input = dataiku.Dataset("Processed_Input")
input_df = input.get_dataframe()
ghg_emmissions = dataiku.Dataset("GHG_Emissions_processed")
ghg_emmissions_df = ghg_emmissions.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
labels = pd.Series(list(range(2020,2100)))
cash = input_df["Cash and cash equivalents"]

Output_df = pd.concat(labels, cash)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
Output = dataiku.Dataset("Output")
Output.write_with_schema(Output_df)
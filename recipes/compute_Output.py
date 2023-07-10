# -------------------------------------------------------------------------------- NOTEBOOK-CELL: MARKDOWN
# # Processing

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: MARKDOWN
# ## Imports

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
print('Done Imports')

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: MARKDOWN
# ## Reading datasets

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
ghg_input = dataiku.Dataset("GHG_Emissions_prepared")
ghg_input_df = ghg_input.get_dataframe()
finance_input = dataiku.Dataset("Input_prepared")
finance_input_df = finance_input.get_dataframe()
print('Done Reading')

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: MARKDOWN
# ## Actual Processing
# 
# - Computes a range of years, and then extrapolates linearly till 2100

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
years = pd.Series(list(range(2021, 2100)))
revenue = finance_input_df["Revenue (All regions)"]
print('Done Extraction')

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
output_df = pd.concat({
    'year': years,
    "Revenue (All regions)": revenue
}, axis=1)
output_df
print('Done Extrapolation')

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
output_df = output_df.interpolate(method ='barycentric', limit_direction ='forward')
output_df
print('Done Dataframe generation')

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: MARKDOWN
# ## Saving data

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
Output = dataiku.Dataset("Output")
Output.write_with_schema(output_df)
print('Done Saving')
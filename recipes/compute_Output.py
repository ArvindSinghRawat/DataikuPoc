# -------------------------------------------------------------------------------- NOTEBOOK-CELL: MARKDOWN
# # Processing

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: MARKDOWN
# ## Imports

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: MARKDOWN
# ## Reading datasets

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
ghg_input = dataiku.Dataset("GHG_Emissions_prepared")
ghg_input_df = ghg_input.get_dataframe()
finance_input = dataiku.Dataset("Input_prepared")
finance_input_df = finance_input.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: MARKDOWN
# ## Actual Processing
# 
# - Computes a range of years, and then extrapolates linearly till 2100

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
years = pd.Series(list(range(2021, 2100)))
finance_input_df[]

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
years

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE

# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

Output_df = ... # Compute a Pandas dataframe to write into Output


# Write recipe outputs
Output = dataiku.Dataset("Output")
Output.write_with_schema(Output_df)
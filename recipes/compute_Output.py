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
# ## Reading Data

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
ghg_input = dataiku.Dataset("GHG_Emissions_prepared")
ghg_input_df = ghg_input.get_dataframe()
finance_input = dataiku.Dataset("Input_prepared")
finance_input_df = finance_input.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: MARKDOWN
# # Compute Logic

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
years = pd.Series(list(range(2021,2100)))
revenue = finance_input["Revenue (All regions)"]

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
output_df = pd.concat({
    'Year': years,
    "Revenue (All regions)": revenue
})

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: MARKDOWN
# ## Saving Logic

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
Output = dataiku.Dataset("Output")
Output.write_with_schema(output_df)
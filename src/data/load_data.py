# %%writefile_and_run src/data/load_data.py

#@title Fetch and Parse Data
import plotly.express as px

def load_data():
  return px.data.iris()

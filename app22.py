##import json
##import streamlit as st
##import pandas as pd  # type: ignore
##from pycaret.clustering import load_model, predict_model  # type: ignore
##import plotly.express as px  # type: ignore

MODEL_NAME = 'welcome_survey_clustering_pipeline_v2'

DATA = 'welcome_survey_simple_v2.csv'

CLUSTER_NAMES_AND_DESCRIPTIONS = 'welcome_survey_cluster_names_and_descriptions_v1.json'

print(DATA)
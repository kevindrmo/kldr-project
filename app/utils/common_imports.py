from pathlib import Path
import sys

# Define ROOT once
ROOT = Path(__file__).parent.parent


if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

# Commonly used libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Optionally:  helper functions
def load_data(path):
    return pd.read_csv(path)

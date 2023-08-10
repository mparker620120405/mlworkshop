# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 09:22:54 2022

@author: tgrae
"""

import streamlit as st
import pandas as pd

st.write("""
         # My first app
         Hello *world!*
         Hi world
         """)


df = pd.read_csv("data.csv")
st.line_chart(df)

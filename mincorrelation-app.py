# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 22:01:45 2021

@author: yaobv
"""
import pandas as pd
import numpy as np
import streamlit as st

players21 = pd.read_csv(r'https://github.com/yaobviously/minutesapp/blob/main/boxscoreappdata.csv?raw=true')

st.write("Minutes Correlation App") 

defaultteam = 'Toronto'

st.header("Select Team")

team = st.text_area('Team', defaultteam, height=100)

def teammincorr(team):
    
    mintable = players21.loc[(players21['Team'] == team) & (players21['MPG'] >=16) & (players21['MIN'] >= 15)][['GameID', 'Player', 'MIN']]
    pivottable = (mintable.pivot(index='GameID', columns='Player', values='MIN')).round(2)
    df = pivottable.corr().round(2)
    
    return df

X = teammincorr(team)

st.write(X)

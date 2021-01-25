# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 22:01:45 2021

@author: yaobv
"""
import pandas as pd
import streamlit as st

players21 = pd.read_csv(r'https://github.com/yaobviously/minutesapp/blob/main/boxscoreappdata.csv?raw=true')

st.write("Minutes Correlation App") 

defaultteam = 'Toronto'

team = st.text_area('Team', defaultteam, height=50)

def teammincorr(team):
    
    mintable = players21.loc[(players21['Team'] == team) & (players21['MPG'] >=16) & (players21['MIN'] >= 15)][['GameID', 'Player', 'MIN']]
    pivottable = (mintable.pivot(index='GameID', columns='Player', values='MIN')).round(2)
    df = pivottable.corr().round(2)
    
    return df 

X = teammincorr(team)

def color_negative_red(val):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, black otherwise.
    """
    color = 'red' if val < 0 else 'green'
    return 'color: %s' % color

X = X.style.applymap(color_negative_red)

st.write(X)

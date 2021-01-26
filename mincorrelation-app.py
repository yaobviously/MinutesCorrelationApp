# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 22:01:45 2021

@author: yaobv
"""
import pandas as pd
import streamlit as st
import numpy as np
import altair as alt
import datetime
from datetime import datetime, timedelta


pd.set_option('precision', 2)
players21 = pd.read_csv(r'https://github.com/yaobviously/minutesapp/blob/main/boxscoreappdata.csv?raw=true')
players21 = players21.sort_values(by='Team', ascending=True)
players21['Date'] = pd.to_datetime(players21['Date'])

st.write("Minutes Correlation App") 



teamlist = players21['Team'].unique().tolist()
team = st.selectbox('Team', teamlist)

today = pd.Timestamp(datetime.date.today())
earlier = pd.Timestamp(datetime.date.today() - timedelta(days=3))
                       
mask = (players21['Date'] > earlier) & (players21['Date'] < today) & (players21['Team'] == team)

plistdf = players21[mask]

playerlist = plistdf['Player'].unique().tolist()
                     
def teammincorr(team):
    
    mintable = players21.loc[(players21['Team'] == team) & (players21['MPG'] >=16) & (players21['MIN'] >= 2) & (players21['Player'].isin(playerlist))][['GameID', 'Player', 'MIN']]
    
    pivottable = (mintable.pivot(index='GameID', columns='Player', values='MIN')).round(2)
    df = pivottable.corr().round(2)
    
    return df 

X = teammincorr(team)

def color_negative_red(val):
   
    color = 'red' if val < 0 else 'green'
    return 'color: %s' % color

X = X.style.applymap(color_negative_red)

st.table(X)

st.write('Player Minutes Distributions')

def boxteam(team):
    df = players21.loc[(players21['Team'] == team) & (players21['MPG'] >= 16)][['Player', 'MIN', 'PlayerFP']]
    return df
    
boxteamdf = boxteam(team)
                                                                
                                                                 
                                                                
boxplot = alt.Chart(boxteamdf).mark_boxplot().encode(
    x='Player:O',
    y='MIN:Q'
).properties(width=750, height=400)
    

st.altair_chart(boxplot)


import streamlit as st
import streamlit.components.v1 as components
import requests

st.title('Chess Analyzer')  

components.iframe('https://www.chess.com/game/live/51637817329')
components.iframe('https://docs.streamlit.io/library/components/components-api', height = 600, scrolling = True)
import streamlit as st
import json

st.title("Watch Feed Tracker")

with open("data.json") as f:
    data = json.load(f)

for item in data:
    st.write(f"### [{item['title']}]({item['link']})")
    st.write(item['published'])

import pandas as pd
import numpy as np
import streamlit as st

df=pd.DataFrame({"Name" : ["Jane", "Jone", "Hook"],
                 "Age" : [25,23,59]})

data=st.dataframe(df)

options=st.sidebar.selectbox("option",["Show data"],index=None)

def main():
    if options:
        data

if __name__=="__main__":
    main()
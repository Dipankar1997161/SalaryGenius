import streamlit as st
from predict import predict_page
from explore import explore_page
from about import about_me_page
import warnings
from home import home_page
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

warnings.filterwarnings(action='ignore')

st.set_option('deprecation.showPyplotGlobalUse', False)
def main():
    st.set_page_config(initial_sidebar_state="collapsed", layout="wide")
    st.set_option('deprecation.showfileUploaderEncoding', False)
    page_bg_css = """
    <style>
        body {background-color: #ffffff;}
    </style>
    """

    # Display the CSS in the Streamlit app

        # Sidebar options
    title_html = """
    <div style="text-align: left;">
        <h1>
            <span style="font-weight: bold;">SalaryGenius:</span>
            <span style="font-size: 16px; font-family: Arial, sans-serif;">Know your Salary</span>
        </h1>
    </div>
    """
    with st.sidebar:
        st.image("https://e0.pxfuel.com/wallpapers/277/445/desktop-wallpaper-financial-financial-background-on-bat-finance-and-accounting.jpg")
        st.markdown(title_html, unsafe_allow_html = True)
            #st.markdown(page_bg_css, unsafe_allow_html=True)
        option = st.selectbox('Navigation', ["Home","About Me","Explore Data", "Predict"])
        st.caption('''App created by [**@dipankarnandi**](https://github.com/Dipankar1997161)''')
    if option == 'Home':
        home_page()
    elif option == 'About Me':
        about_me_page()
    elif option == "Explore Data":
        st.title("SalaryGenius")
        if st.button("Explore"):
            explore_page()
            if st.button("Reset"):
                home_page()
    elif option == "Predict":
        st.title("SalaryGenius")
        st.subheader("""Want to see your Salary??""")
        st.success(""" ## BINGO!! you are at the right place""")
        st.subheader('''***Additional features will be updated soon:***\n''')
        st.success(
    """- **Options:**.\n
    - **Education:** Select the Degree of your Choice.\n
    - **Country:** Select the Country to display the salary.\n
    - **Experience:** Slide the experience level - Max 30.\n"""
    )
        predict_page()
if __name__ == '__main__':
    main()
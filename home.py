import streamlit as st

#st.set_page_config(initial_sidebar_state="collapsed", layout="wide")
def home_page():
    st.title("SalaryGenius")
    st.image("img.jpg")
    st.success('''**A Salary Predictor App**. Trained on 2 years of combined data to estimate salary on a World-Wide Scale. With just 3 inputs, you see your **CASH**. The data used for this app is **2020-2022**
    The app also will also give you a quick analysis of the current salary market.''')
    st.subheader('''**The features of the app you will find on the sidebar menu on the left are:**\n''')
    st.markdown('''More Options will be added soon as this is just the Basic Version.''')
    st.success(
'''- **Home:** Appliction Info\n
- **About Me:** General Info About Developer \n
- **Explore:** Quick Analysis of the Data\n
- **Predict:** Salary Prediction\n''')
    st.caption('''App created by [**@dipankarnandi**](https://github.com/Dipankar1997161)''')
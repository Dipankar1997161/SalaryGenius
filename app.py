import streamlit as st
import warnings
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

warnings.filterwarnings(action='ignore')
st.set_option('deprecation.showPyplotGlobalUse', False)


def clear_country(category, threshold):
    category_map = {}
    for i in range(len(category)):
        if category.values[i] >= threshold:
            category_map[category.index[i]] = category.index[i]
        else:
            category_map[category.index[i]] = 'Other'
    return category_map


def experience(x):
    if x == 'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)


def clean_edu(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelors'
    if 'Master’s degree' in x:
        return 'Masters'
    if 'Professional degree' in x or 'Other doctoral' in x:
        return 'Postgrad'
    return 'Pre Bachelors'


#@st.cache_data
def load_data():
    df = pd.read_csv("survey_results_public.csv")
    df =df.rename(columns={'ConvertedCompYearly': 'Salary'})
    df = df[['EdLevel', 'Employment', 'Country', 'YearsCodePro', 'Salary']]
    df = df[df["Salary"].notnull()]
    df = df.dropna()
    df = df[df["Employment"] == "Employed full-time"]
    df = df.drop("Employment", axis=1)

    country_map = clear_country(df.Country.value_counts(), 400)
    df["Country"] = df["Country"].map(country_map)
    df = df[df["Salary"] <= 200000]
    df = df[df["Salary"] >= 10000]
    df = df[df["Country"] != "Other"]

    df["YearsCodePro"] = df["YearsCodePro"].apply(experience)
    df["EdLevel"] = df["EdLevel"].apply(clean_edu)
    #df = df.rename({"ConvertedComp": "Salary"}, axis=1)
    return df

df = load_data()

def explore_page():
    st.title("Explore Software Engineer Salaries")

    st.write(
        """
    ### Stack Overflow Developer Survey 2022
    """
    )
    st.write(
    """
    #### Transformed DataFrame
    """
)
    st.dataframe(df)
    data = df["Country"].value_counts()
    st.write(
    """
    #### Mean Salary Based On Country
    """
)
    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write(
        """
    #### Mean Salary Based On Experience
    """
    )

    data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data)
    """
    Encode the EdLevel
    """
    
    st.write(
        """
    #### Salary Distribution based on EducationLevel
    """
    )
    fig, ax = plt.subplots()
    sns.boxplot(x="EdLevel", y="Salary", data=df, ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")

    plt.tight_layout()

    # Save the figure to a file
    plt.savefig("box_plot.png")

    # Display the figure in Streamlit
    st.image("box_plot.png")

    st.write(
        """
    #### Max Salary in Country Wise
    """
    )
    data = df.groupby(["Country"])["Salary"].max().sort_values(ascending=True)
    st.bar_chart(data)
    st.write(
        """
    #### Minimum Salary in each country
    """
    )
    data = df.groupby(["Country"])["Salary"].min().sort_values(ascending=True)
    st.bar_chart(data)

def load_model():
    with open('./model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

model = load_model()

regressor = model["model"]
en_country = model["country"]
en_education = model["education"]
                 
                 
def predict_page():
          
    countries = (
    "United States of America",
    "India",
    "United Kingdom of Great Britain and Northern Ireland",
    "Germany",
    "Canada",
    "Brazil",
    "France",
    "Spain",
    "Australia",
    "Netherlands",
    "Poland",
    "Italy",
    "Russian Federation",
    "Sweden",
    "Israel",
      "Switzerland",
      "Norway"
    )
    education = (
        "Pre Bachelors",
        "Bachelors",
        "Masters",
        "Postgrad",
    )
    education = st.selectbox("Education", education)
    country = st.selectbox("Country", countries)
    experience = st.slider("Years of Coding Experience",0,30,2)
    ok = st.button("Predict Your Salary")
    if ok:
        X =np.array([[education, country, experience]])
        X[:, 0] = en_education.transform(X[:,0])
        X[:, 1] = en_country.transform(X[:,1])
        X = X.astype(float)
        salary = regressor.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")
#st.set_page_config(initial_sidebar_state="collapsed", layout="wide")
def home_page():
    st.title("SalaryGenius")
    st.image("https://e0.pxfuel.com/wallpapers/277/445/desktop-wallpaper-financial-financial-background-on-bat-finance-and-accounting.jpg")
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

def about_me_page():
    st.title("About Developer")
    st.header(" WELCOME to the ME Page :full_moon_with_face:")
    #st.image("https://e0.pxfuel.com/wallpapers/277/445/desktop-wallpaper-financial-financial-background-on-bat-finance-and-accounting.jpg")
    st.markdown('''##### **My name is Dipankar Nandi.**\n''')
    me = st.button("Where I am From? :smile:")
    passion = st.button("My Profession? :smile:")
    if me:
        st.markdown('''##### **I am from the land of Spices :flag-in:**\n''')
        st.markdown('''##### **Now I am in the land of Technology :flag-de:**\n''')
    if passion:
        st.markdown('''##### **I strive to become a Junior Developer in the Field of Machine Learning and AI. Then earn my spot to the Senior Position**\n''')
        st.markdown('''My relative field of Interest are listed below:''')
        st.success(
'''- **Natural Langauge Processing:** Natural Language can be hard to process by a machine and I take this as a challenge to develop more in this\n
- **Computer Vision:** This field has many advancements and I have worked in both 2D and 3D domains of Computer Vision\n
- **Data Science:** Tons of application ranging from Sentiment - Prediction - Time Series. All by iteself is fun to learn and grow\n''')
    st.caption('''My Github Repo [**@dipankarnandi**](https://github.com/Dipankar1997161)''')
    st.caption('''My Linkedln Profile [**@dipankarnandi**](https://www.linkedin.com/in/dipankarnandi1997/)''')

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
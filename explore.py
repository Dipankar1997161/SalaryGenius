import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

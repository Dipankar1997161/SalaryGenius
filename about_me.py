import streamlit as st

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




import streamlit as st
import pandas as pd
import pickle as pk

with open("salary.pickle", "rb")as f:
    model = pk.load(f)

st.title("Salary Prediction")
age = st.number_input("Age", 18, 65)
exp = st.slider("Years of Experience", 0, 40)
edu = st.selectbox("Education", ["Bachelor's", "Master's", "PHD"])
if st.button("Submit"):
    st.success("The form is Submitted Successfully")
    if edu == "Bachelor's":
        b = 1
        m = 0
        p = 0
    elif edu == "Master's":
        b = 0
        m = 1
        p = 0
    else:
        b = 0
        m = 0
        p = 1

    data = {"Age": [age], "Years of Experience": [exp],
            "Bachelor's": [b], "Master's": [m], "PhD": [p]}
    df = pd.DataFrame(data)
    result = round(model.predict(df)[0], 2)
    st.write(f'predicted salary : {result}')

# st.date_input("DOB")
# # st.radio("Gender", ["Male", "Female"])
# # st.text_input("Name")
# st.number_input("Age", 0, 100)
# st.selectbox("Pick one", ["Bachelor's", "Master's", "PHD"])
# st.text_input("Job Title")
# st.number_input("Years of Experience", 0, 100)
# st.number_input("Salary", 0, 1000000000)
# st.button("Click me")
# # st.download_button("Download file", data)
# # st.link_button("Go to gallery", url)
# # st.menu_button("Export", options=["CSV", "JSON", "PDF"])
# # st.page_link("app.py", label="Home")
# # st.data_editor("Edit data", data)
# st.checkbox("I agree")
# st.feedback("thumbs")
# # st.pills("Tags", ["Sports", "Politics"])

# # st.segmented_control("Filter", ["Open", "Closed"])
# # st.toggle("Enable")

# # st.multiselect("Buy", ["milk", "apples", "potatoes"])
# # st.slider("Pick a number", 0, 100)
# # st.select_slider("Pick a size", ["S", "M", "L"])


# # st.text_area("Text to translate")

# # st.datetime_input("Event date and time")
# # st.time_input("Meeting time")
# # st.file_uploader("Upload a CSV")
# # st.audio_input("Record a voice message")
# # st.camera_input("Take a picture")
# # st.color_picker("Pick a color")
# # st.pagination(10)

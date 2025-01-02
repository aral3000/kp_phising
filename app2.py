import streamlit as st
import numpy as np
import pickle
from convert import convertion
from feature import FeatureExtraction
import warnings

warnings.filterwarnings('ignore')

# Load the model
file = open("model.pkl", "rb")
gbc = pickle.load(file)
file.close()

# Streamlit app
st.title("Phishing Website Detection")

# Navigation menu
menu = ["Home", "Use Cases"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.subheader("Home")

    # Input URL
    url = st.text_input("Enter the URL to analyze:")

    if st.button("Analyze"):
        if url:
            obj = FeatureExtraction(url)
            x = np.array(obj.getFeaturesList()).reshape(1, 30)

            y_pred = gbc.predict(x)[0]
            name = convertion(url, int(y_pred))

            # Display result
            if y_pred == 1:
                st.success(f"The website is likely safe.")
            else:
                st.error(f"The website is likely unsafe.")
        else:
            st.warning("Please enter a URL.")

elif choice == "Use Cases":
    st.subheader("Use Cases")
    st.write("Here you can describe various use cases of your application.")

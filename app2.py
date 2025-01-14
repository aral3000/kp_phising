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

            # Predict probabilities
            y_prob = gbc.predict_proba(x)[0]  # Returns probabilities for each class
            y_pred = np.argmax(y_prob)  # Class with the highest probability
            name = convertion(url, int(y_pred))

            # Calculate percentages
            safe_prob = y_prob[1] * 100  # Probability of being safe
            phishing_prob = y_prob[0] * 100  # Probability of being phishing


            y_pred = gbc.predict(x)[0]
            name = convertion(url, int(y_pred))

             # Display result
            if y_pred == 1:
            st.success(f"The website is likely safe ({safe_prob:.2f}% safe).")
            else:
            st.error(f"The website is likely unsafe ({phishing_prob:.2f}% unsafe).")
        else:
            st.warning("Please enter a URL.")


elif choice == "Use Cases":
    st.subheader("Use Cases")
    st.write("The Streamlit application for phishing website detection has a wide range of use cases across various sectors. For the general public, it helps verify the safety of suspicious web links from emails, text messages, or social media, protecting them from phishing attacks. In corporate environments, IT teams can use the app to validate reported suspicious links, safeguard sensitive data, and support cybersecurity training. Educational institutions and government agencies can integrate the app into curricula or monitoring systems to educate students and protect digital infrastructure. Additionally, customer service teams, journalists, digital activists, and e-commerce users can utilize the app to ensure the safety of their digital interactions, prevent data breaches, and promote secure online transactions.")

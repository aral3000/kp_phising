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
    st.write("Streamlit applications for phishing website detection can serve various use cases in different domains. For general users, the app provides a straightforward tool to check the safety of web links they encounter in emails, text messages, or social media, empowering them to avoid phishing scams. Employees in government or private sectors can use the app to ensure the security of links, particularly when dealing with sensitive documents or emails. This helps mitigate cybersecurity risks within organizations.

In corporate environments, IT teams can leverage the app to validate suspicious links reported by employees or detected within internal networks, thereby protecting company data. It also serves as an educational tool for cybersecurity awareness and training, helping participants understand phishing characteristics and prevention techniques through practical simulations.

Educational institutions can integrate the app into their curriculum, providing students with hands-on experience in cybersecurity. Large organizations or government agencies can incorporate the app into their monitoring systems, automating the detection of malicious links from user reports or system logs to safeguard critical digital infrastructure.

Customer support teams can use the app to verify links submitted by clients, ensuring safe interactions and enhancing trust. Journalists and digital activists, often targeted by malicious actors, can utilize the app to verify link authenticity before accessing them, reducing the risk of cyberattacks.

For government cybersecurity efforts, the app can help assess web links reported by citizens, providing a quick response mechanism to address threats. Additionally, e-commerce users can validate lesser-known websites before making purchases, promoting safer online transactions and reducing the likelihood of data theft. These use cases highlight the versatility and importance of a Streamlit application in combating phishing threats across various sectors.")

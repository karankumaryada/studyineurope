import streamlit as st

# Page Title
st.set_page_config(page_title="Study in Europe - Free Consultancy", page_icon="🎓", layout="wide")

st.title("🌍 Study in Europe - Free Consultancy for Indian Students")

# Home Section
st.header("Welcome to Your Free Study Abroad Consultancy!")
st.write("We help Indian students achieve their dream of studying in Europe by providing free guidance on admissions, visas, and scholarships.")

# Why Study in Europe Section
st.subheader("🎓 Why Study in Europe?")
st.write("- World-class universities and research opportunities")
st.write("- Affordable education and scholarship options")
st.write("- Diverse culture and excellent career prospects")

# Services Section
st.subheader("🛠 Our Services")
st.write("✅ University selection and application guidance")
st.write("✅ Visa processing assistance")
st.write("✅ Scholarship and financial aid advice")
st.write("✅ Accommodation and travel support")

# Google Form for Booking Appointments
st.subheader("📅 Book a Free Consultancy Session")
st.write("Fill out the form below to schedule a session with us:")

google_form_url = "https://forms.gle/YOUR_FORM_LINK_HERE"  # Replace with your Google Form link
st.markdown(f"[👉 Click here to book an appointment]({google_form_url})", unsafe_allow_html=True)

# Contact Section
st.subheader("📞 Contact Us")
st.write("📧 Email: your_email@example.com")
st.write("📱 WhatsApp: +91XXXXXXXXXX")
st.write("🌐 Website: www.yourwebsite.com")

st.success("We look forward to helping you start your journey to Europe!")

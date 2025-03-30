import streamlit as st

# Page Title
st.set_page_config(page_title="Study in Europe - Consultancy", page_icon="🎓", layout="wide")

st.title("🌍 Study in Europe - Affordable Consultancy for Indian Students")

# Home Section
st.header("Welcome to Your Study Abroad Consultancy!")
st.image("home_image.jpeg", caption="Study in Europe", use_column_width=True)  # Placeholder for image
st.write("We help Indian students achieve their dream of studying in Europe by providing expert guidance on admissions, visas, and scholarships.")

# Why Study in Europe Section
st.subheader("🎓 Why Study in Europe?")
st.image("europe_image.jpeg", caption="Beautiful European Campuses", use_column_width=True)  # Placeholder for image
st.write("- World-class universities and research opportunities")
st.write("- Affordable education and scholarship options")
st.write("- Diverse culture and excellent career prospects")

# Services Section
st.subheader("🛠 Our Services")
st.write("✅ University selection and application guidance")
st.write("✅ Visa processing assistance")
st.write("✅ Scholarship and financial aid advice")
st.write("✅ Accommodation and travel support")

# Pricing Section
st.subheader("💰 Pricing for Our Consultancy Services")
st.write("We offer affordable consultancy services to help you study in Europe. Our pricing is as follows:")
st.write("- Basic Consultation (30 mins): ₹499")
st.write("- Full Admission Guidance: ₹4,999")
st.write("- Visa & Scholarship Assistance: ₹7,999")
st.write("*Prices are subject to change based on individual requirements.")

# Google Form for Booking Appointments
st.subheader("📅 Book a Consultancy Session")
st.write("Fill out the form below to schedule a session with us:")

google_form_url = "https://forms.gle/YOUR_FORM_LINK_HERE"  # Replace with your Google Form link
st.markdown(f"[👉 Click here to book an appointment]({google_form_url})", unsafe_allow_html=True)

# Contact Section
st.subheader("📞 Contact Us")
st.image("contact_image.jpg", caption="Get in Touch", use_column_width=True)  # Placeholder for image
st.write("📧 Email: karankumaryadav297@gmail.com")
st.write("📱 WhatsApp: +917689036040")

st.success("We look forward to helping you start your journey to Europe!")

import streamlit as st
from streamlit_extras.stylable_container import stylable_container

# 1. Page Configuration
st.set_page_config(page_title="Smart Clinic", layout="wide", initial_sidebar_state="expanded")

# 2. Custom CSS for UI Polish
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #F8F9FE;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: white;
        border-right: 1px solid #E6E9EF;
    }
    
    /* Typography */
    h1 {
        color: #1A202C;
        font-weight: 800;
        font-size: 3rem !important;
    }
    
    .subtitle {
        color: #4A5568;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }

    /* Custom Card Styling */
    .feature-card {
        background-color: white;
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        height: 100%;
    }
    
    /* Custom Button */
    div.stButton > button {
        background-color: #5E5CE6;
        color: white;
        border-radius: 10px;
        padding: 0.6rem 2rem;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Navigation
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/883/883360.png", width=50) # Placeholder Logo
    st.title("Smart Clinic")
    st.caption("Booking System")
    
    st.markdown("---")
    st.write("MENU")
    st.button("🏠 Home", use_container_width=True)
    st.button("👤 Add Doctor", use_container_width=True)
    st.button("📅 Book Appointment", use_container_width=True)
    st.button("📋 View Appointments", use_container_width=True)
    st.button("📊 Analytics", use_container_width=True)
    
    st.markdown("---")
    with stylable_container(
        key="help_box",
        css_styles="""
            {
                background-color: #EEF2FF;
                border-radius: 15px;
                padding: 15px;
            }
        """
    ):
        st.write("**Need Help?**")
        st.caption("We're here to help you")
        st.link_button("Contact Support →", "#", type="secondary")

# 4. Main Content Area
col_text, col_img = st.columns([1, 1.2], gap="large")

with col_text:
    st.write("🛡️ Trusted by thousands")
    st.markdown("<h1>Welcome to the <br><span style='color:#5E5CE6'>Smart Clinic</span> <br>Booking System</h1>", unsafe_allow_html=True)
    st.markdown("""
        <p class='subtitle'>
        Book appointments, manage schedules, and provide better 
        healthcare experiences for patients and doctors.
        </p>
    """, unsafe_allow_html=True)
    
    if st.button("View Doctors"):
        st.toast("Redirecting to Doctors list...")

with col_img:
    # Using a professional medical stock photo placeholder
    st.image("https://images.unsplash.com/photo-1576091160550-2173dba999ef?ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80", use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# 5. Bottom Feature Cards
card_cols = st.columns(4)

features = [
    {"icon": "📅", "title": "Book Appointments", "desc": "Schedule appointments with your preferred doctor easily and quickly."},
    {"icon": "👩‍⚕️", "title": "Expert Doctors", "desc": "Choose from a wide range of experienced and specialized doctors."},
    {"icon": "🔒", "title": "Secure & Safe", "desc": "Your data is protected with top-level security and privacy."},
    {"icon": "📈", "title": "Smart Analytics", "desc": "Track clinic performance and get real-time insights with smart reports."}
]

for i, col in enumerate(card_cols):
    with col:
        st.markdown(f"""
            <div class="feature-card">
                <div style="font-size: 2.5rem; margin-bottom: 1rem;">{features[i]['icon']}</div>
                <h3 style="font-size: 1.1rem; margin-bottom: 0.5rem;">{features[i]['title']}</h3>
                <p style="color: #718096; font-size: 0.9rem;">{features[i]['desc']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        
        
        
        
        
        #####APP
        import streamlit as st
import pandas as pd
import sqlite3
from datetime import date

# Database connection
conn = sqlite3.connect("clinic.db", check_same_thread=False)
cursor = conn.cursor()

st.set_page_config(page_title="Clinic Booking System", layout="wide")

# Title
st.title("🏥 Smart Clinic Booking System")

# Sidebar
menu = st.sidebar.selectbox(
    "Menu",
    ["Home", "Add Doctor", "Book Appointment", "View Appointments", "Analytics"]
)

# HOME PAGE

if menu == "Home":

    st.markdown("""
    <style>

    .stApp {
        background: linear-gradient(to right, #f5f3ff, #fff7fb);
    }

    .main-title {
        font-size: 65px;
        font-weight: 800;
        line-height: 1.1;
        color: #111827;
    }

    .highlight {
        color: #6d28d9;
    }

    .description {
        font-size: 22px;
        color: #4b5563;
        line-height: 1.7;
    }

    .feature-card {
        background: white;
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0px 5px 20px rgba(0,0,0,0.05);
    }

    </style>
    """, unsafe_allow_html=True)

    # HERO SECTION
    col1, col2 = st.columns([1.2, 1])

    with col1:

        st.markdown("""
        <p style="
        background:#ede9fe;
        display:inline-block;
        padding:10px 20px;
        border-radius:20px;
        color:#6d28d9;
        font-weight:600;
        ">
        Trusted by thousands
        </p>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="main-title">
            Welcome to the <br>
            <span class="highlight">
            Smart Clinic
            </span><br>
            Booking System
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="description">
        Book appointments, manage schedules,
        and provide better healthcare experiences
        for patients and doctors.
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        st.button("👩🏽‍⚕️ View Doctors")

    with col2:

        st.image(
            "https://images.unsplash.com/photo-1594824476967-48c8b964273f?q=80&w=1200&auto=format&fit=crop",
            use_container_width=True
        )

    st.write("")
    st.write("")

    # FEATURE CARDS
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class="feature-card">
        <h1>📅</h1>
        <h3>Book Appointments</h3>
        <p>Schedule appointments quickly and easily.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="feature-card">
        <h1>👩🏽‍⚕️</h1>
        <h3>Expert Doctors</h3>
        <p>Choose experienced and specialized doctors.</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="feature-card">
        <h1>🔒</h1>
        <h3>Secure & Safe</h3>
        <p>Your clinic data is protected and secure.</p>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="feature-card">
        <h1>📊</h1>
        <h3>Smart Analytics</h3>
        <p>Track clinic performance with insights.</p>
        </div>
        """, unsafe_allow_html=True)
# ADD DOCTOR PAGE
elif menu == "Add Doctor":

    st.subheader("➕ Add Doctor")

    col1, col2 = st.columns(2)

    with col1:
        doctor_name = st.text_input("Doctor Name")
        specialty = st.selectbox(
            "Specialty",
            [
                "General Practitioner",
                "Dentist",
                "Cardiologist",
                "Dermatologist",
                "Pediatrician",
                "Neurologist"
            ]
        )

    with col2:
        experience = st.number_input(
            "Years of Experience",
            min_value=1,
            max_value=50
        )

        phone = st.text_input("Phone Number")

    if st.button("Add Doctor"):

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS doctors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            specialty TEXT,
            experience INTEGER,
            phone TEXT
        )
        """)

        cursor.execute(
            """
            INSERT INTO doctors
            (name, specialty, experience, phone)
            VALUES (?, ?, ?, ?)
            """,
            (
                doctor_name,
                specialty,
                experience,
                phone
            )
        )

        conn.commit()

        st.success("Doctor added successfully!")

    st.divider()

    st.subheader("👨‍⚕️ Doctors List")

    doctors_df = pd.read_sql(
        "SELECT * FROM doctors",
        conn
    )

    st.dataframe(
        doctors_df,
        use_container_width=True
    )
    
    st.divider()

    st.subheader("🗑️ Delete Doctor")

    if not doctors_df.empty:
        doctor_to_delete = st.selectbox(
            "Select Doctor to Delete",
            doctors_df["name"]
        )

        if st.button("Delete Doctor"):
            cursor.execute(
                "DELETE FROM doctors WHERE name = ?",
                (doctor_to_delete,)
            )

            conn.commit()

            st.warning(
                f"{doctor_to_delete} deleted successfully!"
            )

            st.rerun()
    else:
        st.info("No doctors available to delete.")

# BOOK APPOINTMENT PAGE
elif menu == "Book Appointment":
    
    st.subheader("📅 Book Appointment")

    col1, col2 = st.columns(2)

    with col1:
        patient_name = st.text_input("Patient Name")

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=100
        )

        gender = st.selectbox(
            "Gender",
            ["Male", "Female", "Other"]
        )

    with col2:
        contact = st.text_input("Phone Number")

        appointment_date = st.date_input(
            "Appointment Date",
            min_value=date.today()
        )

        appointment_time = st.selectbox(
            "Appointment Time",
            [
                "09:00 AM",
                "10:00 AM",
                "11:00 AM",
                "02:00 PM",
                "03:00 PM"
            ]
        )

    doctors = pd.read_sql(
        "SELECT * FROM doctors",
        conn
    )

    if not doctors.empty:
        doctor = st.selectbox(
            "Select Doctor",
            doctors["name"]
        )

        symptoms = st.text_area(
            "Symptoms / Reason for Visit"
        )

        if st.button("Confirm Booking"):

            # Check if slot already booked
            cursor.execute(
                """
                SELECT * FROM appointments
                WHERE doctor_name = ?
                AND date = ?
                AND time = ?
                """,
                (
                    doctor,
                    str(appointment_date),
                    appointment_time
                )
            )

            existing_booking = cursor.fetchone()

            # If slot exists
            if existing_booking:

                st.error(
                    f"{doctor} already has an appointment at "
                    f"{appointment_time} on {appointment_date}"
                )

            else:

                # Save appointment
                cursor.execute(
                    """
                    INSERT INTO appointments
                    (
                        patient_name,
                        age,
                        gender,
                        contact,
                        doctor_name,
                        symptoms,
                        date,
                        time,
                        status
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        patient_name,
                        age,
                        gender,
                        contact,
                        doctor,
                        symptoms,
                        str(appointment_date),
                        appointment_time,
                        "Confirmed"
                    )
                )

                conn.commit()

                st.success(
                    f"Appointment booked successfully with Dr {doctor}"
                )
    else:
        st.warning("Please add doctors first.")

# VIEW APPOINTMENTS
elif menu == "View Appointments":
    st.subheader("📋 Appointment Records")

    appointments = pd.read_sql(
        "SELECT * FROM appointments",
        conn
    )

    if not appointments.empty:
        st.dataframe(
            appointments,
            use_container_width=True
        )
    else:
        st.info("No appointments found.")

# ANALYTICS
elif menu == "Analytics":
    st.subheader("📊 Clinic Analytics")

    appointments = pd.read_sql(
        "SELECT * FROM appointments",
        conn
    )

    if not appointments.empty:
        st.write("### Total Appointments")
        st.metric(
            "Bookings",
            len(appointments)
        )

        doctor_counts = (
            appointments["doctor_name"]
            .value_counts()
            .reset_index()
        )

        doctor_counts.columns = [
            "Doctor",
            "Bookings"
        ]

        st.write("### Doctor Performance")

        st.bar_chart(
            doctor_counts.set_index("Doctor")
        )

        st.write("### Appointment Status")

        status_counts = (
            appointments["status"]
            .value_counts()
        )

        st.write(status_counts)

    else:
        st.info("No analytics data available.")
    
    
    
    
    
    st.markdown("""
<style>

div.stButton > button {
    width: 100%;
    height: 64px;
    background-color: #6366F1;
    color: white;
    border: none;
    border-radius: 18px;
    font-size: 20px;
    font-weight: 500;
    text-align: left;
    padding-left: 22px;
    margin-bottom: 16px;
}

div.stButton > button:hover {
    background-color: #7C83FF;
    color: white;
}

</style>
""", unsafe_allow_html=True)
   
   
https://images.unsplash.com/photo-1594824476967-48c8b964273f?q=80&w=1200&auto=format&fit=crop
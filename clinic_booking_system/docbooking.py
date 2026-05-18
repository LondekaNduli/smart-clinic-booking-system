import streamlit as st
import pandas as pd
import sqlite3
from datetime import date
from streamlit_extras.stylable_container import stylable_container

# Database connection
conn = sqlite3.connect(
    "clinic.db",
    check_same_thread=False
)
cursor = conn.cursor()

# Page setup
st.set_page_config(
    page_title="Clinic Booking System",
    layout="wide"
)


st.markdown("""
<style>
img {
    border-radius: 25px;
}
</style>
""", unsafe_allow_html=True)


# SESSION STATE
if "menu" not in st.session_state:
    st.session_state.menu = "🏠 Home"


# ================= SIDEBAR =================
with st.sidebar:

    # Sidebar styling
    st.markdown("""
    <style>

    section[data-testid="stSidebar"] {
        background-color: #f8fafc;
    }

    div.stButton > button {
        width: 100%;
        height: 50px;
        background: linear-gradient(90deg,#6366F1,#5B5FEF);
        color: white;
        border: none;
        border-radius: 20px;
        font-size: 20px;
        font-weight: 500;
        text-align: left;
        padding-left: 22px;
        margin-bottom: 5px;
    }

    div.stButton > button:hover {
        background: linear-gradient(90deg,#7C83FF,#6366F1);
        color: white;
    }

    div.stButton > button:focus {
        border: none;
        box-shadow: none;
    }

    </style>
    """, unsafe_allow_html=True)

    # Logo
    st.image(
        "https://cdn-icons-png.flaticon.com/512/4320/4320371.png",
        width=70
    )

    # Title
    st.markdown("""
    <h2 style="
    margin-bottom:0;
    font-size:30px;
    font-weight:700;
    color:#111827;
    ">
    Smart Clinic
    </h2>
    """, unsafe_allow_html=True)

    st.write("")
    st.markdown("# MENU")
    st.write("")

    # MENU BUTTONS
    if st.button("🏠 Home", use_container_width=True):
        st.session_state.menu = "🏠 Home"

    if st.button("👩🏽‍⚕️ Add Doctor", use_container_width=True):
        st.session_state.menu = "👩🏽‍⚕️ Add Doctor"

    if st.button("📅 Book Appointment", use_container_width=True):
        st.session_state.menu = "📅 Book Appointment"

    if st.button("📋 View Appointments", use_container_width=True):
        st.session_state.menu = "📋 View Appointments"

    if st.button("📊 Analytics", use_container_width=True):
        st.session_state.menu = "📊 Analytics"

    st.write("")
    st.write("")

# Help box 
    st.info("""
      🎧 **Need Help?** 
      
    **Contact Support** 
      
     📞: +27 73 123 4567     
     📧:support@smartclinic.com
    """)

# ACTIVE MENU
menu = st.session_state.menu


# HOME PAGE
if menu == "🏠 Home":

    st.markdown("""
    <style>

    .stApp {
        background:
        linear-gradient(to right,
        #f6f3ff,
        #fff7fb);
    }

    .main-title{
        font-size:68px;
        font-weight:800;
        line-height:1.1;
        color:#111827;
    }

    .highlight{
        color:#6d28d9;
    }

    .description{
        font-size:22px;
        color:#4b5563;
        line-height:1.8;
    }

    .purple-button{
        background:#6d28d9;
        color:white;
        padding:16px 40px;
        border-radius:18px;
        border:none;
        font-size:22px;
        font-weight:600;
        width:260px;
    }

    .card{
        background:white;
        padding:35px;
        border-radius:28px;
        text-align:center;
        box-shadow:
        0 8px 30px rgba(0,0,0,0.05);
        min-height:250px;
    }

    </style>
    """, unsafe_allow_html=True)

    left, right = st.columns([1, 1.15])

    with left:

        st.markdown("""
        <div style="
        background:#ede9fe;
        color:#6d28d9;
        display:inline-block;
        padding:10px 20px;
        border-radius:20px;
        font-weight:600;
        ">
        🛡️ Trusted by thousands
        </div>
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

        if st.button("👩🏽‍⚕️ View Doctors", key="view_doctors_home"):
            st.session_state.menu = "👨‍⚕️ Doctors"
            st.rerun()
         
    with right:
        st.image(
        "pic1.png",
        width=550
    )

    st.write("")
    st.write("")
    
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


# VIEW DOCTORS PAGE
elif menu == "👨‍⚕️ Doctors":
    st.subheader("👨‍⚕️ Our Doctors")

    doctors_df = pd.read_sql(
        "SELECT name, specialty, experience FROM doctors",
        conn
    )

    if not doctors_df.empty:
        for _, doctor in doctors_df.iterrows():
           html = f"""
           <div style="
           background:white;
           padding:20px;
           border-radius:18px;
           margin-bottom:15px;
           box-shadow:0 4px 12px rgba(0,0,0,0.05);
        ">
        <h3 style="margin:0; color:#111827;">
        👩🏽‍⚕️ Dr. {doctor['name']}
        </h3>

        <p style="color:#6B7280; margin-top:8px; font-size:18px;">
        <strong>Specialty:</strong> {doctor['specialty']}
        </p>

    <p style="color:#6B7280; font-size:16px;">
        {doctor['experience']} years experience
    </p>
</div>
"""

    st.markdown(html, unsafe_allow_html=True)
 
else:
    st.info("No doctors available yet.")
        
# ADD DOCTOR PAGE
elif menu == "👩🏽‍⚕️ Add Doctor":

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
elif menu == "📅 Book Appointment":
    
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
elif menu == "📋 View Appointments":
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
elif menu == "📊 Analytics":
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
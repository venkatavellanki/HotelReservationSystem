import streamlit as st
import pandas as pd
from datetime import date, timedelta

# App title
st.title("🏨 Hotel Reservation System")

# Session state to store reservations
if "reservations" not in st.session_state:
    st.session_state.reservations = []

# Sidebar for navigation
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Make a Reservation", "View Reservations"])

# --- Reservation Page ---
if page == "Make a Reservation":
    st.header("📝 Make a Reservation")

    # Guest details
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")

    # Dates
    check_in = st.date_input("Check-in Date", min_value=date.today())
    check_out = st.date_input("Check-out Date", min_value=check_in + timedelta(days=1))

    # Room details
    room_type = st.selectbox("Room Type", ["Single", "Double", "Suite"])
    guests = st.slider("Number of Guests", 1, 5)

    # Submit button
    if st.button("Book Now"):
        if name and email and phone:
            reservation = {
                "Name": name,
                "Email": email,
                "Phone": phone,
                "Check-in": check_in,
                "Check-out": check_out,
                "Room Type": room_type,
                "Guests": guests
            }
            st.session_state.reservations.append(reservation)
            st.success("✅ Reservation successfully made!")
        else:
            st.error("❌ Please fill in all the details.")

# --- View Reservations Page ---
elif page == "View Reservations":
    st.header("📋 All Reservations")

    if st.session_state.reservations:
        df = pd.DataFrame(st.session_state.reservations)
        st.dataframe(df)
    else:
        st.info("No reservations made yet.")

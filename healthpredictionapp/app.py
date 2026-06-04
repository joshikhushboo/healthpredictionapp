import streamlit as st 
import sqlite3
import pandas as pd
from datetime import date
from ai_predictionn import predict_health 


st.title("Health Prediction Application")

name = st.text_input("Full Name")
dob = st.date_input("Date of Birth")
email = st.text_input("Email Address")

glucose = st.number_input("Glucose")
haemoglobin = st.number_input("Haemoglobin")
cholesterol = st.number_input("Cholesterol")

if st.button("Submit"):

    if name.strip() == "":
        st.error("Name cannot be empty")

    elif "@" not in email or "." not in email:
        st.error("Enter a valid email address")

    elif dob > date.today():
        st.error("Date of Birth cannot be in the future")

    else:

        conn = sqlite3.connect("patients.db")
        cursor = conn.cursor()
        remarks = predict_health(
    glucose,
    haemoglobin,
    cholesterol
)
#CREATE
        cursor.execute("""                                     
        INSERT INTO patients
        (full_name,dob,email,glucose,haemoglobin,cholesterol,remarks)
        VALUES(?,?,?,?,?,?,?)
        """, (
            name,
            str(dob),
            email,
            glucose,
            haemoglobin,
            cholesterol,
            remarks
        ))

        conn.commit()
        conn.close()

        st.success("Patient Record Saved Successfully!")
        
        #READ
    st.subheader("Patient Records")

conn = sqlite3.connect("patients.db")

df = pd.read_sql_query(
    "SELECT * FROM patients",
    conn
)

conn.close()

st.dataframe(df)
#DELETE
st.subheader("Delete Patient Record")

delete_id = st.number_input(
    "Enter Patient ID to Delete",
    min_value=1,
    step=1
)

if st.button("Delete Record"):

    conn = sqlite3.connect("patients.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM patients WHERE id=?",
        (delete_id,)
    )

    conn.commit()
    conn.close()

    st.success("Record Deleted Successfully!")

    #UPDATE
    st.subheader("Update Patient Record")

update_id = st.number_input(
    "Patient ID to Update",
    min_value=1,
    step=1,
    key="update_id"
)

new_glucose = st.number_input(
    "New Glucose",
    key="new_glucose"
)

new_haemoglobin = st.number_input(
    "New Haemoglobin",
    key="new_haemoglobin"
)

new_cholesterol = st.number_input(
    "New Cholesterol",
    key="new_cholesterol"
)

if st.button("Update Record"):

    conn = sqlite3.connect("patients.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE patients
        SET glucose=?,
            haemoglobin=?,
            cholesterol=?
        WHERE id=?
    """, (
        new_glucose,
        new_haemoglobin,
        new_cholesterol,
        update_id
    ))

    conn.commit()
    conn.close()

    st.success("Record Updated Successfully!")

   
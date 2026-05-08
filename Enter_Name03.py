import streamlit as st
import pandas as pd
import numpy as np

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Student Data Analysis",
    layout="wide"
)

# -----------------------------------
# TITLE
# -----------------------------------

st.title("General trend of student (grades vs absences)")

# -----------------------------------
# STUDENT DATA
# -----------------------------------

data = {
    "Name": [
        "Ali", "Sara", "Yacine", "Lina", "Amine",
        "Aya", "Nadia", "Karim", "Sofiane", "Meriem",
        "Imane", "Walid", "Rania", "Nour", "Samir",
        "Yasmine", "Khaled", "Amina", "Rayane", "Islam"
    ],

    "Grade": [
        15, 18, 9, 12, 14,
        17, 8, 11, 6, 16,
        13, 10, 19, 7, 5,
        18, 12, 14, 9, 20
    ],

    "Absences": [
        2, 1, 8, 5, 3,
        1, 10, 6, 12, 2,
        4, 7, 0, 11, 13,
        1, 5, 3, 8, 0
    ]
}

df = pd.DataFrame(data)

# -----------------------------------
# STUDENT INPUT
# -----------------------------------

student_name = st.text_input("Student's name")

# -----------------------------------
# SEARCH STUDENT
# -----------------------------------

if student_name:

    result = df[
        df["Name"].str.lower() == student_name.lower()
    ]

    if not result.empty:

        grade = result.iloc[0]["Grade"]
        absences = result.iloc[0]["Absences"]

        st.write(f"Your grade in the Python course is: {grade}")
        st.write(f"Your absences have exceeded {absences} times.")

        # -----------------------------------
        # FEEDBACK
        # -----------------------------------

        if grade >= 16:
            feedback = "Excellent work! Keep it up."

        elif grade >= 12:
            feedback = "Good job. Continue improving."

        elif grade >= 10:
            feedback = "Average performance. Study more."

        else:
            feedback = "Please review your lessons and attend classes regularly."

        st.success(feedback)

    else:
        st.error("Student not found.")

# -----------------------------------
# DATA ANALYSIS SECTION
# -----------------------------------

st.markdown("---")

st.title("📊 Data Analysis App")

st.write("Using student grades")

# -----------------------------------
# SHOW DATA
# -----------------------------------

st.subheader("Student Dataset")

st.dataframe(df)

# -----------------------------------
# CHART
# -----------------------------------

st.subheader("Relationship between Grades and Absences")

st.bar_chart(df.select_dtypes(include='number'))



# -----------------------------------
# CONCLUSION
# -----------------------------------

st.subheader("General Analysis")

st.write(
    "The chart shows that students with more absences "
    "generally tend to obtain lower grades in the Python course."
)
# streamlit run Enter_Name03.py
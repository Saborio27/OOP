
import streamlit as st
from student_class import StudentClass

st.title("Student Study & Grade Tracker")

st.write("Welcome to our Student Study & Grade Tracker!")

# Store classes during the session
if "classes" not in st.session_state:
    st.session_state.classes = []

# ADD CLASS
st.subheader("Add Class")

class_name = st.text_input("Enter Class Name:")

credits = st.number_input(
    "Enter Credit Hours:",
    min_value=1,
    max_value=6,
    value=3
)

if st.button("Add Class"):
    if class_name.strip() == "":
        st.error("Please enter a class name.")
    else:
        new_class = StudentClass(class_name, credits)
        st.session_state.classes.append(new_class)
        st.success("Class added successfully!")


# VIEW CLASSES
st.subheader("My Classes")

if len(st.session_state.classes) == 0:
    st.write("No classes added yet.")
else:
    for student_class in st.session_state.classes:
        st.write(
            student_class.name,
            "-",
            student_class.credits,
            "credits"
        )


# ENTER GRADES
st.subheader("Enter Grades")

if len(st.session_state.classes) == 0:
    st.warning("Please add a class first.")
else:
    class_names = [
        student_class.name
        for student_class in st.session_state.classes
    ]

    selected_index = st.selectbox(
        "Choose a Class:",
        range(len(class_names)),
        format_func=lambda i: class_names[i],
        key="enter_class"
    )

    grade = st.number_input(
        "Enter Grade:",
        min_value=0.0,
        max_value=100.0,
        value=0.0
    )

    if st.button("Save Grade"):
        st.session_state.classes[selected_index].add_grade(grade)
        st.success("Grade saved successfully!")


# VIEW GRADES
st.subheader("View Grades")

if len(st.session_state.classes) == 0:
    st.warning("No classes available.")
else:
    class_names = [
        student_class.name
        for student_class in st.session_state.classes
    ]

    view_index = st.selectbox(
        "Select a Class to View Grades:",
        range(len(class_names)),
        format_func=lambda i: class_names[i],
        key="view_class"
    )

    view_class = st.session_state.classes[view_index]

    if len(view_class.grades) == 0:
        st.info("No grades entered for this class.")
    else:
        st.write("Grades for", view_class.name)

        for grade in view_class.grades:
            st.write("Grade:", grade)

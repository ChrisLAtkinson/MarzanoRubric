import streamlit as st
import pandas as pd

# Title and Introduction
st.title("Interactive Principal Evaluation Rubric")
st.write("""
This tool evaluates principals based on the Marzano School Leadership Evaluation Model.
You can score domains, provide evidence, view detailed rubrics, and save or print the results.
""")

# Define Rubric Data
rubric_data = [
    {
        "Domain": "Domain 1: A Data-Driven Focus on Student Achievement",
        "Element": "Clear and measurable school-wide goals",
        "Rubric": [
            "**Innovating (4):** Ensures adjustments are made or new methods are utilized so that all stakeholders sufficiently understand the goals.",
            "**Applying (3):** Ensures clear, measurable goals with specific timelines focused on critical needs regarding improving student achievement are established and monitored.",
            "**Developing (2):** Ensures clear, measurable goals with specific timelines are established.",
            "**Beginning (1):** Attempts to establish clear, measurable goals but does not complete the task or does so partially.",
            "**Not Using (0):** Does not attempt to establish clear, measurable goals."
        ]
    },
    {
        "Domain": "Domain 2: Continuous Improvement of Instruction",
        "Element": "Clear and measurable individual student goals",
        "Rubric": [
            "**Innovating (4):** Ensures adjustments are made or new methods are utilized so that all faculty and students sufficiently understand goals.",
            "**Applying (3):** Ensures each student has written achievement goals that are clear, measurable, and monitored.",
            "**Developing (2):** Ensures each student has written achievement goals.",
            "**Beginning (1):** Attempts to ensure written goals but does so partially.",
            "**Not Using (0):** Does not attempt to ensure written achievement goals."
        ]
    },
    {
        "Domain": "Domain 3: A Guaranteed and Viable Curriculum",
        "Element": "Data analysis for school achievement",
        "Rubric": [
            "**Innovating (4):** Data are analyzed in a variety of ways to provide the most useful information.",
            "**Applying (3):** Data are available and regularly monitored.",
            "**Developing (2):** Data are available for tracking progress.",
            "**Beginning (1):** Attempts to ensure data are available but does so partially.",
            "**Not Using (0):** Does not attempt to ensure data availability."
        ]
    },
    {
        "Domain": "Domain 4: Cooperation and Collaboration",
        "Element": "Data analysis for individual student achievement",
        "Rubric": [
            "**Innovating (4):** Refines individual achievement goals or tracking processes based on data analysis.",
            "**Applying (3):** Ensures data are available and monitored for individual student achievement.",
            "**Developing (2):** Ensures data are available for individual student achievement.",
            "**Beginning (1):** Attempts to ensure data availability but does so partially.",
            "**Not Using (0):** Does not attempt to ensure data availability."
        ]
    },
    {
        "Domain": "Domain 5: School Climate",
        "Element": "Programs and practices for intervention",
        "Rubric": [
            "**Innovating (4):** Continually examines and expands intervention options.",
            "**Applying (3):** Ensures intervention programs are in place and monitored.",
            "**Developing (2):** Ensures intervention programs are in place.",
            "**Beginning (1):** Attempts to ensure programs but does so partially.",
            "**Not Using (0):** Does not attempt to ensure intervention programs."
        ]
    }
]

# Initialize Session State
if 'scores' not in st.session_state:
    st.session_state['scores'] = [0] * len(rubric_data)
if 'evidence' not in st.session_state:
    st.session_state['evidence'] = [''] * len(rubric_data)

# User Input for Each Domain
st.write("### Evaluation Criteria")
for i, item in enumerate(rubric_data):
    st.write(f"## {item['Domain']}")
    st.write(f"**Element:** {item['Element']}")
    
    # Display Rubric Table
    st.write("**Scoring Rubric:**")
    for level in item['Rubric']:
        st.markdown(f"- {level}")
    
    # Scoring Slider
    st.session_state['scores'][i] = st.slider(
        "Score (0-4)", 0, 4, st.session_state['scores'][i], key=f"score_{i}"
    )
    
    # Evidence Input
    st.session_state['evidence'][i] = st.text_area(
        "Evidence", value=st.session_state['evidence'][i], key=f"evidence_{i}"
    )

# Calculate Overall Score
total_score = sum(st.session_state['scores'])
max_score = len(rubric_data) * 4
average_score = total_score / len(rubric_data)

st.write("### Evaluation Summary")
st.write(f"**Total Score:** {total_score}/{max_score}")
st.write(f"**Average Score:** {average_score:.2f}")

# Evidence Summary
st.write("### Evidence Summary")
for i, item in enumerate(rubric_data):
    st.write(f"- **{item['Domain']} - {item['Element']}**: {st.session_state['evidence'][i]}")

# Save and Export
st.write("### Save & Print")
if st.button("Save Results"):
    results_df = pd.DataFrame({
        "Domain": [item['Domain'] for item in rubric_data],
        "Element": [item['Element'] for item in rubric_data],
        "Score": st.session_state['scores'],
        "Evidence": st.session_state['evidence']
    })
    results_df.to_csv('principal_evaluation_results.csv', index=False)
    st.success("Results saved as 'principal_evaluation_results.csv'.")

if st.button("Download Results"):
    st.download_button(
        label="Download CSV",
        data=results_df.to_csv(index=False).encode('utf-8'),
        file_name='principal_evaluation_results.csv',
        mime='text/csv'
    )

st.write("You can also press `Ctrl+P` or `Cmd+P` to print this page.")

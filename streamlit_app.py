import streamlit as st
import pandas as pd

# Title and introduction
st.title("Interactive Principal Evaluation Rubric")
st.write("""
This rubric evaluates a principal based on domains and elements derived from the Marzano School Leadership Evaluation Model.
You can add evidence, rate each criterion, and calculate an overall score. The results can be saved or printed.
""")

# Define rubric structure
rubric_data = {
    "Domain": [
        "Domain 1: A Data-Driven Focus on Student Achievement",
        "Domain 2: Continuous Improvement of Instruction",
        "Domain 3: A Guaranteed and Viable Curriculum",
        "Domain 4: Cooperation and Collaboration",
        "Domain 5: School Climate"
    ],
    "Elements": [
        "Clear and measurable school-wide goals",
        "Clear and measurable individual student goals",
        "Data analysis for school achievement",
        "Data analysis for individual student achievement",
        "Programs and practices for intervention"
    ],
    "Criteria": [
        """
        - Written goals are established as a percentage of students who will score at a proficient or higher level on state assessments.
        - School-wide achievement goals are posted and discussed regularly.
        - Faculty and staff can describe the school-wide achievement goals.
        """,
        """
        - Each student has written achievement goals.
        - Students keep data notebooks regarding their individual goals.
        - Parent-teacher conferences focus on individual student goals.
        """,
        """
        - Reports, graphs, and charts are available for overall student achievement.
        - School leadership teams regularly analyze school growth data.
        - Data briefings are conducted at faculty meetings.
        """,
        """
        - Individual student achievement is tracked through charts and graphs.
        - Teachers regularly analyze growth data for individual students.
        - Individual student reports are regularly updated.
        """,
        """
        - Extended school day and week programs are in place.
        - Tutorial programs are available.
        - Academic help is available during school hours.
        """
    ]
}

# Create DataFrame
df = pd.DataFrame(rubric_data)

# Initialize session state
if 'scores' not in st.session_state:
    st.session_state['scores'] = [0] * len(df)
if 'evidence' not in st.session_state:
    st.session_state['evidence'] = [''] * len(df)

# User input for each domain
st.write("### Evaluation Criteria")
for i, row in df.iterrows():
    st.write(f"## {row['Domain']}")
    st.write(f"**Element:** {row['Elements']}")
    st.write(f"**Criteria:** {row['Criteria']}")
    
    st.session_state['scores'][i] = st.slider(
        "Score (0-4)", 0, 4, st.session_state['scores'][i], key=f"score_{i}"
    )
    st.session_state['evidence'][i] = st.text_area(
        "Evidence", value=st.session_state['evidence'][i], key=f"evidence_{i}"
    )

# Calculate Overall Score
total_score = sum(st.session_state['scores'])
max_score = len(df) * 4
average_score = total_score / len(df)

st.write("### Evaluation Summary")
st.write(f"**Total Score:** {total_score}/{max_score}")
st.write(f"**Average Score:** {average_score:.2f}")

# Display evidence summary
st.write("### Evidence Summary")
for i, row in df.iterrows():
    st.write(f"- **{row['Domain']} - {row['Elements']}**: {st.session_state['evidence'][i]}")

# Save and Export
st.write("### Save & Print")
if st.button("Save Results"):
    results_df = pd.DataFrame({
        "Domain": df['Domain'],
        "Element": df['Elements'],
        "Criteria": df['Criteria'],
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

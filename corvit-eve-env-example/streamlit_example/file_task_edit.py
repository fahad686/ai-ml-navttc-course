import streamlit as st
import os

# Initialize session state
if "topics" not in st.session_state:
    st.session_state.topics = []  # list to store topics and essays

st.header('Enter 5 Topics with Essays')

# --------- Step 1: Add Topics and Essays ----------
if len(st.session_state.topics) < 5:
    with st.form(key=f"topic_form_{len(st.session_state.topics)}"):
        topic_name = st.text_input('Topic Name')
        essay_data = st.text_area('Essay')
        submitted = st.form_submit_button('Add Topic')

        if submitted:
            if topic_name and essay_data:
                # Save in file
                with open(f'{topic_name}.txt', 'w') as file:
                    file.write(essay_data)

                # Store in session
                st.session_state.topics.append({
                    "topic": topic_name,
                    "essay": essay_data
                })
                st.success(f"'{topic_name}' saved successfully!")
            else:
                st.warning('Please fill out both Topic and Essay fields')

else:
    st.success("You have added 5 topics successfully!")

# --------- Step 2: Update Old Topic with New One ----------
st.header("Update Existing Topic and Essay")

# Dropdown to select old topic
if st.session_state.topics:
    old_topic = st.selectbox(
        "Select a topic to update",
        [t["topic"] for t in st.session_state.topics]
    )

    # Get the essay for selected topic
    old_essay = next((t["essay"] for t in st.session_state.topics if t["topic"] == old_topic), "")
    st.write(f"**Old Topic Name:** {old_topic}")
    st.write(f"**Old Essay:** {old_essay}")

    # New topic and essay input
    with st.form(key="update_form"):
        new_topic = st.text_input('New Topic Name')
        new_essay = st.text_area('New Essay')
        update_submitted = st.form_submit_button('Update')

        if update_submitted:
            if new_topic and new_essay:
                # Update session state
                for t in st.session_state.topics:
                    if t["topic"] == old_topic:
                        t["topic"] = new_topic
                        t["essay"] = new_essay

                # Update file
                if os.path.exists(f'{old_topic}.txt'):
                    os.remove(f'{old_topic}.txt')  # remove old file

                with open(f'{new_topic}.txt', 'w') as file:
                    file.write(new_essay)

                st.success(f"'{old_topic}' successfully updated to '{new_topic}'!")
            else:
                st.warning('Please fill out both New Topic and New Essay fields.')


import streamlit as st

# Define pages
name_generator = st.Page("name_generator.py", title='Name Generator', icon='🎰')
concept_dissection = st.Page("ideas_generator.py", title='Ideas Generator', icon='🔪')
ideas_archive = st.Page("ideas_archive.py", title='Ideas Archive', icon='📘')
faq = st.Page("faq.py", title='FAQ', icon='🌐')

pg = st.navigation([name_generator, concept_dissection, ideas_archive, faq])

pg.run()
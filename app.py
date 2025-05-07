import streamlit as st

# Define pages
name_generator = st.Page("name_generator.py", title='Name Generator', icon='🎰')
words_archive = st.Page("words_archive.py", title='Words Archive', icon='📘')
concept_dissection = st.Page("ideas_generator.py", title='Ideas Generator', icon='🔪')
faq = st.Page("faq.py", title='FAQ', icon='🌐')

pg = st.navigation([name_generator, words_archive, concept_dissection, faq])

pg.run()
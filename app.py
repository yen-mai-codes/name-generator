import streamlit as st

# Define pages
name_generator = st.Page("name_generator.py", title='Name generator', icon='🎰')
words_archive = st.Page("words_archive.py", title='Words archive', icon='📘')

pg = st.navigation([name_generator, words_archive])

pg.run()
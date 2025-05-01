'''Page for managing words'''

import streamlit as st
from utils.utils import (
    manage_word,
    get_file,
    write_to_file
)

words_file_name = 'data/words.json'
words = get_file(words_file_name)

st.markdown('# Words Archive 📘')

def on_submit():    
    new_words = manage_word(st.session_state.action, st.session_state.word, words)
    write_to_file(words_file_name, new_words)

# ---Side bar
# Word Input
col1, col2 = st.columns(2)
st.sidebar.markdown('# Inputs')
st.sidebar.text_input('Word', key='word')
st.sidebar.selectbox('Action', ['Add', 'Remove'], key='action')
st.sidebar.button('Submit', on_click=on_submit)

# Main
# Word list
col1, col2, col3 = st.columns(3)
words_count = len(words['words'])

for word in words['words']:
    st.write(word)
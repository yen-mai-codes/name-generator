'''Page for managing words'''

import streamlit as st
import pandas as pd
from utils.utils import (
    manage_word,
    get_file,
    write_to_file
)

words_file_name = 'data/words.json'
words = get_file(words_file_name)

st.markdown('# Words Archive 📘')

def on_submit():    
    """
    Callback function when user submits word inputs.
    """
    # Change words json based on user's input action and word
    new_words = manage_word(st.session_state.action, st.session_state.word, words)

    # Write to words file the new words json
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
words_df = pd.DataFrame.from_records(words['words'], index='word').sort_values(by=['word', 'pos_tag'])
st.table(words_df)
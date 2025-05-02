'''Page for managing words'''

import streamlit as st
import pandas as pd
from utils.utils import (
    manage_word,
    get_file,
    write_to_file
)

pos_types_file_name = 'data/pos_types.json'
pos_types = get_file(pos_types_file_name)['pos_types']

words_file_name = 'data/words.json'
words = get_file(words_file_name)

st.markdown('# Words Archive 📘')

def on_submit(action: str):    
    """
    Callback function when user submits word inputs.
    """

    # Change words json based on user's input action and word
    new_words = manage_word(action, st.session_state.word, st.session_state.pos, words)

    # Write to words file the new words json
    write_to_file(words_file_name, new_words)

# ---Side bar
# Word Input
col1, col2 = st.columns(2)
st.markdown('# Inputs')
col1, col2 = st.columns([2,1], vertical_alignment='center')
with col1:
    st.text_input('Word', key='word', label_visibility='collapsed', placeholder='Enter cool word')
    st.multiselect('POS', pos_types, key='pos', label_visibility='collapsed', placeholder='Choose POS tags')

with col2:
    st.button('Add', on_click=on_submit, args=('Add',), icon='💏', use_container_width=True)
    st.button('Remove', on_click=on_submit, args=('Remove',), icon="🤮", use_container_width=True)

# Main
# Word list
words_df = pd.DataFrame.from_records(words['words'], index='word').sort_values(by=['word'])
st.table(words_df)
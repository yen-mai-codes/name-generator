'''Page for name generation'''

import streamlit as st
import nltk
import random
import pandas as pd
from utils.utils import get_file

pos_types_file_name = 'data/pos_types.json'
pos_types = get_file(pos_types_file_name)['pos_types']

words_file_name = 'data/words.json'
words = get_file(words_file_name)['words']

names_file_name = 'data/names.json'
names = get_file(names_file_name)

def on_submit():
    """
    Callback function when user submits name generation inputs.
    """
    names = set()
    first_word_candidates = []
    second_word_candidates = []
    first_pos = set(st.session_state.first_pos)
    second_pos = set(st.session_state.second_pos)

    # Loop through words to find candidates with input POS
    for word in words:
        if word['pos_tag'] in first_pos:
            first_word_candidates.append(word)
        if word['pos_tag'] in second_pos:
            second_word_candidates.append(word)

    # Generate names
    for _ in range(st.session_state.names_count):
        found = False
        while not found:
            first_word = random.choice(first_word_candidates)
            second_word = random.choice(second_word_candidates)
            name = f'{first_word['word']}{second_word['word']}'

            # Check if name has already been generated
            if name not in names:
                found = True
        names.add(name)
        
    st.session_state.names = names

st.markdown('# Name Generator 🎰')

# ---Side bar
# Word Input
st.sidebar.markdown('# Inputs')
st.sidebar.multiselect('First POS', pos_types, key='first_pos')
st.sidebar.multiselect('Second POS', pos_types, key='second_pos')
st.sidebar.number_input('Number of outputs', min_value=1, max_value=10, key='names_count')
st.sidebar.button('Submit', on_click=on_submit)

# ---Main
def change_state(edited_df):
    st.session_state['df'] = edited_df

# Names output
if 'names' in st.session_state:
    name_rankings = ['YES', 'Normal about it', "It's good, just not for me",'Hard pass']   
    names = list(st.session_state.names)
    df = pd.DataFrame({'Name': names})
    for ranking in name_rankings:
        df[ranking] = False
    if 'df' not in st.session_state:
        st.session_state.df = df
    edited_df = st.session_state['df']
    edited_df = st.data_editor(edited_df, on_change=change_state, args=(edited_df,))
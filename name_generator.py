'''Page for name generation'''

import streamlit as st
import nltk
import random
import pandas as pd
from utils.utils import get_file

words_file_name = 'data/words.json'
words_data = get_file(words_file_name)
pos_types = [x for x in words_data]

names_file_name = 'data/names.json'
names = get_file(names_file_name)

def get_word_candidates(pos_list: list):
    """
    Get a list of all word candidates that fall into any of `pos_list`.

    Inputs:
    --------
    pos_list (list): 
        List of pos.
    """
    candidates = set()
    for pos in pos_list:
        for word in words_data[pos]['words']:
            candidates.add(word)

    return list(candidates)

def on_submit_input():
    """
    Callback function when user submits name generation inputs.
    """
    names = set()
    first_pos = set(st.session_state.first_pos)
    second_pos = set(st.session_state.second_pos)

    first_word_candidates = get_word_candidates(first_pos)
    second_word_candidates = get_word_candidates(second_pos)

    # Generate names
    for _ in range(st.session_state.names_count):
        found = False
        while not found:
            first_word = random.choice(first_word_candidates)
            second_word = random.choice(second_word_candidates)
            if first_word == second_word:
                continue
            name = f'{first_word}{second_word}'

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
st.sidebar.button('Submit', on_click=on_submit_input)

# ---Main
def change_state(edited_df):
    st.session_state['df'] = edited_df

# Names output
if 'names' in st.session_state:
    name_rankings = ['YES', 'Normal about it', "It's good, just not for me",'Hard pass']   
    names = list(st.session_state.names)
    col1, col2, col3, col4, col5 = st.columns(5)
    for i in range(st.session_state.names_count):
        name = names[i]
        with col1:
            st.write(name, key={name})
        with col2:
            st.checkbox('YES', key=f'{name}_yes')
        with col3:
            st.checkbox('Normal', key=f'{name}_normal')
        with col4:
            st.checkbox('Maybe', key=f'{name}_not_for_me')
        with col5:
            st.checkbox('Pass', key=f'{name}_pass')
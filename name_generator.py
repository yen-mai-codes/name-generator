'''Page for name generation'''

import streamlit as st
import nltk
import random
import pandas as pd
from utils.utils import (
    manage_word,
    write_to_file,
    get_file
)

words_file_name = 'data/words.json'
words_data = get_file(words_file_name)
pos_types = [x for x in words_data]

names_file_name = 'data/names.json'
names = get_file(names_file_name)

# Sidebar
st.sidebar.markdown('# Words Archive 📘')

def on_submit_word_input(action: str):    
    """
    Callback function when user submits word inputs.
    """
    # Change words json based on user's input action and word
    new_data = manage_word(action, st.session_state.word, st.session_state.pos, words_data)
    # Write to words file the new words json
    write_to_file(words_file_name, new_data)

# ---Side bar
st.sidebar.text_input('Word', key='word', label_visibility='collapsed', placeholder='Enter cool word')
st.sidebar.multiselect('POS', pos_types, key='pos', label_visibility='collapsed', placeholder='Choose POS tags')
st.sidebar.button('Add', on_click=on_submit_word_input, args=('Add',), use_container_width=True)
st.sidebar.button('Remove', on_click=on_submit_word_input, args=('Remove',), use_container_width=True)
# st.write(words_data)

st.markdown('# Name Generator 🎰')


# ---Main
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

def on_submit_name_input():
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
# Word Input
col1, col2, col3 = st.columns([3,3,2])
with col1:
    st.multiselect('First POS', pos_types, key='first_pos')
with col2:
    st.multiselect('Second POS', pos_types, key='second_pos')
with col3:
    st.number_input('Outputs count', min_value=1, max_value=10, key='names_count')
st.button('Submit', on_click=on_submit_name_input, use_container_width=True)

def change_state(edited_df):
    st.session_state['df'] = edited_df

# Names output
if 'names' in st.session_state:
    name_rankings = ['YES', 'Normal about it', "It's good, just not for me",'Hard pass']   
    names = list(st.session_state.names)
    col1, col2, col3, col4, col5 = st.columns([3,1,1,1,1])
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
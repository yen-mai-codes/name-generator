import streamlit as st
import nltk
import random
from utils.utils import get_file

pos_types_file_name = 'data/pos_types.json'
pos_types = get_file(pos_types_file_name)['pos_types']

words_file_name = 'data/words.json'
words = get_file(words_file_name)['words']

def on_submit():
    names = set()
    first_word_candidates = []
    second_word_candidates = []
    first_pos = set(st.session_state.first_pos)
    second_pos = set(st.session_state.second_pos)

    for word in words:
        if word['pos_tag'] in first_pos:
            first_word_candidates.append(word)
        if word['pos_tag'] in second_pos:
            second_word_candidates.append(word)

    for _ in range(st.session_state.names_count):
        found = False
        while not found:
            first_word = random.choice(first_word_candidates)
            second_word = random.choice(second_word_candidates)
            name = f'{first_word['word']}{second_word['word']}'
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
st.sidebar.number_input('Number of outputs', min_value=1, max_value=5, key='names_count')
st.sidebar.button('Submit', on_click=on_submit)


# ---Main
# Names output
if 'names' in st.session_state:
    st.write(st.session_state.names)
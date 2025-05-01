'''Page for managing words'''

import json
import nltk
import streamlit as st
from pathlib import Path

words_file_name = 'words.json'
words_file = Path(words_file_name)
words_json = json.load(words_file)

#-------------------------------------------
def get_word_index(word: str) -> int:
    """
    Get word's index in words file.

    Inputs:
    --------
    word (str): 
        A word.

    Returns:
    --------
    int: 
        Index of word in words file, -1 otherwise.
    """
    words = words_json['words']
    for i in range(len(words_json['words'])):
        w = words[i]
        if w['word'] == word:
            return i
    return -1

#-------------------------------------------
def manage_word(action: str, word: str) -> dict:
    """
    Manage word with action input. Writes to words file.

    Inputs:
    --------
    action(str):
        An action for a word.
    word (str): 
        A word.
    """    
    word_index = get_word_index(word)
    if action == 'Add':
        # Word not found in words file
        if word_index == -1:
            words_json['words'].append({
                'word': word,
                'pos_tag': nltk.pos_tag(nltk.word_tokenize(word))
            })
    
    if action == 'Delete':
        # Word found in words file
        if word_index >= 0:
            words_json['words'].pop(word_index)
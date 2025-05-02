import json
import nltk
import streamlit as st

def get_file(file_name: str):
    with open(file_name) as f:
        words = json.load(f)
        return words
    
def write_to_file(file_name: str, new_data):
    with open(file_name, 'w') as f:
       json.dump(new_data, f)

#-------------------------------------------
def get_word_index(word: str, words_json: dict) -> int:
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
    for i in range(len(words)):
        w = words[i]
        if w['word'] == word:
            return i
    return -1

#-------------------------------------------
def manage_word(action: str, word: str, pos: list, words_json: dict) -> dict:
    """
    Manage word with action input. Writes to words file.

    Inputs:
    --------
    action(str):
        An action for a word.
    word (str): 
        A word.
    """    
    word_index = get_word_index(word, words_json)
    if action == 'Add':
        # Word not found in words file
        if word_index == -1:
            words_json['words'].append({
                'word': word,
                'pos_tag': pos
            })
    
    if action == 'Remove':
        # Word found in words file
        if word_index >= 0:
            words_json['words'].pop(word_index)

    return words_json

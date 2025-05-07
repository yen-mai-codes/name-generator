import json
import nltk
import streamlit as st

#-------------------------------------------
def get_file(file_name: str):
    with open(file_name) as f:
        words = json.load(f)
        return words
    
#-------------------------------------------
def write_to_file(file_name: str, new_data):
    with open(file_name, 'w', encoding='utf-8') as f:
       json.dump(new_data, f, ensure_ascii=False, indent=4)

#-------------------------------------------
def manage_word(action: str, word: str, word_types: list, data: dict) -> dict:
    """
    Add or remove word from json.

    Inputs:
    --------
    action(str):
        An action for a word.
    word (str): 
        A word.
    word_types (str):
        Word's types.
    data (dict):
        Json of words.
    """    
    for word_type in word_types:
        words_list = data[word_type]['words']
        if action == 'Add' and word not in words_list:
            words_list.append(word)
        
        if action == 'Remove' and word in words_list:
            words_list.remove(word)

    return data
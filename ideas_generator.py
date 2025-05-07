'''Page for Generating Ideas'''

import streamlit as st
import random
from utils.utils import (
    manage_idea_component,
    get_file,
    write_to_file
)

idea_components_file = 'data/idea_components.json'
idea_components = get_file(idea_components_file)
component_types = [x for x in idea_components]

def on_submit_component(action: str):
    """Callback function for add/remove components"""
    new_data = manage_idea_component(action, st.session_state.component, st.session_state.type, idea_components)
    write_to_file(idea_components_file, new_data)

def on_submit_generator():
    themes = ', '.join(random.sample(idea_components['theme'], k=st.session_state.themes_count))
    styles = ', '.join(random.sample(idea_components['style'], k=st.session_state.styles_count))
    activations = st.session_state.activations

    output = dict()
    for activation in activations:
        if activation == 'theme':
            component = themes
        elif activation == 'style':
            component = styles
        else:
            component = random.choice(idea_components[activation])
        output[activation] = component
    
    st.session_state.generator_output = output

# Sidebar for editing and displaying idea components
st.sidebar.markdown('### Input')
st.sidebar.text_input('Component', label_visibility='collapsed',placeholder='Type component here', key='component')
st.sidebar.selectbox('Select type', component_types, label_visibility='collapsed', key='type')
st.sidebar.button('Add', on_click=on_submit_component, args=('Add', ))
st.sidebar.button('Remove', on_click=on_submit_component, args=('Remove', ))
st.sidebar.markdown('### Components')
st.sidebar.write(idea_components)

# Main page for generating ideas
st.markdown('# Ideas Generator')
st.markdown('### Parameters')
st.multiselect("Activation", component_types, default=['medium', 'finish', 'theme', 'style'],placeholder='Choose parameters to activate', key='activations')
col1, col2 = st.columns(2)
with col1:
    st.number_input("Themes count", step=1, min_value=1, key='themes_count')
with col2:
    st.number_input("Styles count", step=1, min_value=1, key='styles_count')

st.button('Submit', on_click=on_submit_generator)
if 'generator_output' in st.session_state:
    st.write(st.session_state.generator_output)
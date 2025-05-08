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
sorted_parameters = ['genre', 'theme', 'finish', 'medium', 'style', 'vibe', 'size']

def on_submit_component(action: str):
    """Callback function for add/remove components"""
    new_data = manage_idea_component(action, st.session_state.component, st.session_state.type, idea_components)
    write_to_file(idea_components_file, new_data)

def on_submit_generator():
    parameters = st.session_state.parameters
    output = dict()

    for parameter in sorted_parameters:
        if parameter in parameters:
            key = f"{parameter}_count"
            parameter_count = st.session_state[key]
            output[parameter] = ', '.join(random.sample(idea_components[parameter], parameter_count))
    
    st.session_state.generator_output = output

def on_change_parameters():
    if 'parameters' in st.session_state:
        parameters = st.session_state.parameters
        if len(parameters) > 0:
            columns = st.columns(len(parameters))
            for i in range(len(parameters)):
                parameter = parameters[i]
                with columns[i]:
                    st.number_input(f"{parameter.capitalize()} count",min_value=1, step=1, key=f"{parameter}_count")

# Sidebar for editing and displaying idea components
st.sidebar.markdown('# Idea Components Archive')
st.sidebar.text_input('Component', label_visibility='collapsed',placeholder='Type component here', key='component')
st.sidebar.selectbox('Select type', component_types, label_visibility='collapsed', key='type')
st.sidebar.button('Add', on_click=on_submit_component, args=('Add', ), use_container_width=True)
st.sidebar.button('Remove', on_click=on_submit_component, args=('Remove', ), use_container_width=True)
st.sidebar.markdown('### Components')
st.sidebar.write(idea_components)

# Main page for generating ideas
st.markdown('# Ideas Generator')
st.multiselect("Parameters", component_types, on_change=on_change_parameters(), placeholder='Choose parameters to activate', key='parameters')
st.button('Submit', on_click=on_submit_generator, use_container_width=True)

if 'generator_output' in st.session_state:
    st.write(st.session_state.generator_output)
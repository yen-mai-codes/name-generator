'''Page for Archiving Ideas'''

import streamlit as st
from utils.utils import (
    manage_idea_component,
    get_file,
    write_to_file
)

idea_components_file = 'data/idea_components.json'
idea_components = get_file(idea_components_file)

ideas_file = 'data/ideas.json'
ideas = get_file(ideas_file)

sorted_parameters = ['genre', 'theme', 'finish', 'medium', 'style', 'vibe', 'size']

def on_submit_idea():
    idea = st.session_state.idea
    idea_obj = dict()
    idea_obj['idea'] = idea
    idea_obj['parameters'] = dict()
    new_data = idea_components
    for parameter in sorted_parameters:
        key = f"inp_{parameter}"
        inp_parameters = st.session_state[key]
        if inp_parameters == "":
            continue 
        inp_parameters = inp_parameters.split(', ')
        existing_inp_parameters = idea_components[parameter]
        for inp_parameter in inp_parameters:
            if inp_parameter not in existing_inp_parameters:
                new_data = manage_idea_component('Add', inp_parameter, parameter, idea_components)

        idea_obj['parameters'][parameter] = inp_parameters
    ideas['ideas'].append(idea_obj)
    write_to_file(ideas_file, ideas)
    write_to_file(idea_components_file, new_data)

# Sidebar for editing and displaying idea components
st.sidebar.markdown('# Ideas Input')
st.sidebar.text_area('Idea', label_visibility='collapsed',placeholder='Enter cool idea', key='idea')
for i in range(len(sorted_parameters)):
    parameter = sorted_parameters[i]
    st.sidebar.text_input(f'{parameter.capitalize()}', key=f"inp_{parameter}")

st.sidebar.button('Submit', on_click=on_submit_idea, use_container_width=True)
st.markdown('# Ideas Archive')
for idea in ideas['ideas']:
    parameters = idea['parameters']
    st.write('---------------------------------------------')
    st.text(idea['idea'])
    for parameter in parameters:
        value = parameters[parameter]
        if value:
            st.text(f'{parameter.capitalize()}: {', '.join(value)}')
'''Page for Generating Ideas'''

import streamlit as st
import configparser
import pytumblr
from utils.utils import (
    manage_word,
    get_file,
    write_to_file
)
from pathlib import Path
from pinterest.organic.boards import Board

idea_components_file = 'data/idea_components.json'
idea_components = get_file(idea_components_file)

# # Get tumblr api client
# config_file_name = '.env'
# config = configparser.ConfigParser()
# config.read(Path(config_file_name))
# tumblr_config = config['tumblr']

# client = pytumblr.TumblrRestClient(
#     tumblr_config['consumer_key'],
#     tumblr_config['consumer_secret'],
#     '<oauth_token>',
#     '<oauth_secret>',
# )

st.markdown('# Ideas Generator')


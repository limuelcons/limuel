from google.cloud import dialogflow_v2beta1 as dialogflow
import streamlit as st
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'lim.json'

project_id = "lim-dyxn"
session_id = '1234567'
language_code = 'en'

session_client = dialogflow.SessionsClient()

def detect_intext(text):
   session = session_client.session_path(project_id, session_id)
   text_input = dialogflow.TextInput(text=text,language_code=language_code)
   query_input = dialogflow.Query_input(text=text_input)

   response = session_client.detect_intent(request={'session': session, 'query_input': query_input})


   return response.query_result.fulfillment_text


st.title('CHATBOT')

if 'message' not in st.session_state:
	st.session_state.message = []

for message in st.session_state.mesages:
	display_input = st.chat_message(message['role'])
	display_input.write(message['content'])


prompt = st.chat_input('You ')

if prompt:
    st.chat_message('user').write(prompt)

    st.session_state.message.append({'role': 'user', 'content': bot_response})
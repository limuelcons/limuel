import streamlit as st

st.title('CHATBOT')

prompt = st. chat_input('user')
 
if "messages" not in st.session_state:
  st.session_state.message = []

for message in st.session_state.message:
  user_input = st.chat_message(message['role'])
  user_input.write(message['content'])

st.chat_message("user").write(prompt)

if prompt and prompt != '':
  st.session_state.message.append({'role': 'user', 'content':prompt})
   
if prompt == 'hello':
  st.chat_message('assitant').write("how are you")	
  st.session_state.message.append({'role':'asssistant', 'content': 'how are you'})
elif prompt == 'who are you?':
  st.chat_message('Assitant').write('I am your asssistant')
  st.session_state.message.append({'role': 'asssistant','content':  'I am your asssistant'})
elif prompt == 'Hi':
 st.chat_message('Assitant').write('hello!')
 st.session_state.message.append({'role': 'asssistant','content': 'hello'})
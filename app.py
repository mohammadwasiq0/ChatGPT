import streamlit as st
from langchain.llms import OpenAI
st.title('🦜🔗 Quickstart App')
st.write("## Connect me on Linkedin [Link](https://www.linkedin.com/in/mohammadwasiq0/)")
st.write("### [Get API Link](https://platform.openai.com/account/api-keys?ref=blog.streamlit.io)")
# openai_api_key = st.sidebar.text_input('OpenAI API Key')
openai_api_key = "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"
def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))
with st.form('my_form'):
  text = st.text_area('Enter text:', 'Tell me about Aligarh Muslim University')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)

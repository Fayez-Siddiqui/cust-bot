from typing import Optional

import streamlit as st
# from streamlit_drawable_canvas import st_canvas
from PIL import Image
from chatbot import chatbot_answer




def prompt_and_generate_button(material):
    st.write("Welcome "+st.session_state["name"]+"😎")
    if "messages" not in st.session_state.keys():
                st.session_state.messages = [{"role": "😇", "content": "How may I help you?"}]
                
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "😎", "content": prompt})
        with st.chat_message("😎"):
            st.write(prompt)
    if st.session_state.messages[-1]["role"] != "😇":
        with st.chat_message("😇"):
            with st.spinner("Thinking..."):
                inputs = {"question": prompt}
                ans=chatbot_answer(material,prompt)
                if len(ans)>0:
                    st.write(ans)
                else :
                    st.write("Please reach out to our supervisor this question is beyond my capabilities 😓") 
        message = {"role": "😇", "content": ans}
        st.session_state.messages.append(message)
    

    

    


def main():
    st.set_page_config(layout="wide")
    st.title("Customer service ChatBot")
    print("loading relevant information")
    print("lets start prompting")
    with open("info.txt","r",errors='ignore') as f:
        material=f.read()
    st.session_state["name"]="user"
    prompt_and_generate_button(material)
    

if __name__ == "__main__":
    main()
import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("Chef Chat (2 Start Michelin Exppeince)")

# Create the model 

def generate_content(prompt):
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages = [
            {"role":"system",
             "content":"""
                    You are a 2 michellin star chef who wants to help home cooks
                    improve their cooking skills. You may only answer home cooking
                    related questions.
                    If they ask about any nonsense outside of cooking, SCOLD THEM
             """
            },
            {'role':'user',
             'content':prompt}
        ],
        n=1,
        max_tokens=150
    )
    return response.choices[0].message.content

# Initialize the chat history 

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role":"assistant",
            "content":"How may I help you?"
        }
    ]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Process and store prompts and responses
def ai_function(prompt):
    response = generate_content(prompt)

    # Display the Assistant Message
    with st.chat_message("assistant"):
        st.markdown(response)

    # Stroring the User Message
    st.session_state.messages.append(
        {
            "role":"user",
            "content":prompt
        }
    )

    # Store the Assistant Message
    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":response
        }
    )
# test commints
# Accept user input 
prompt = st.chat_input("Ask me anything!")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
        
    ai_function(prompt)
import streamlit as st
import openai

st.set_page_config(page_title="JamesChatGPT")
st.title("🤖 Welcome to JamesChatGPT")
st.write("Ask anything — I'm here to help you!")

api_key = st.text_input("Enter your OpenAI API Key", type="password")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are JamesGPT, a helpful assistant built by James Vasanth."}]

prompt = st.text_input("You:", placeholder="Type your question and hit Enter")

if prompt and api_key:
    st.session_state.messages.append({"role": "user", "content": prompt})
    try:
        openai.api_key = api_key
        with st.spinner("Thinking..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=st.session_state.messages
            )
        reply = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.success("JamesGPT: " + reply)
    except Exception as e:
        st.error(f"Error: {e}")

st.subheader("Chat History")
for msg in st.session_state.messages[1:]:
    role = "You" if msg["role"] == "user" else "JamesGPT"
    st.markdown(f"**{role}:** {msg['content']}")

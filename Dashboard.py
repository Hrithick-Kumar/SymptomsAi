import streamlit as st
import requests 
st.header("Symptoms Ai")
def SymptomsAi(Symptoms):
  api_url="https://openrouter.ai/api/v1/chat/completions"
  api_key=st.secrets["SymptomsAi"]
  headers={
    "Authorization":f"Bearer {api_key}",
    "Content-Type":"application/json"
  }
  payload={
    "model":"openrouter/free",
    "messages":[{"role":"system","content":"you are an expert general doctor.you can analyze symptoms and show possibilities"},
                {"role":"user","content":Symptoms}]
  }
  response=requests.post(api_url,headers=headers,json=payload)
  result=response.json()
  if "choices" in result:
    return result["choices"][0]["message"]["content"]
Symptoms=st.chat_input("Ask Doctor")
if Symptoms:
  with st.chat_message("User"):
    st.write(Symptoms)
  with st.spinner("Analyzing"):
    answer=SymptomsAi(Symptoms)
    with st.chat_message("Assistant"):
      st.markdown(answer)



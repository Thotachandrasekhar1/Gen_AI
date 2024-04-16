from openai import OpenAI
import streamlit as st


st.title("Reviewing the Code")
ai_code = st.text_area("Please Enter your python code", height=200)


if st.button("Generate"):
    f=open(r"C:\\Users\\THOTA CHANDRASEKHAR\\Downloads\\Gen_AI\\keys\\key.txt")
    OPENAI_AI_KEY = f.read()
    client=OpenAI(api_key=OPENAI_AI_KEY)

    response = client.chat.completions.create(
                model = 'gpt-3.5-turbo-0125',
                messages = [
                    {"role":"system", "content": """You're a useful AI helper.
                                                    Accept user input in the form of code. Determine which code bugs exist and address them.
                                                    Make that the code is generated correctly.

                                                    The output needs to be in: {"Bugs":"review_on_code", "code":'''fixed code'''} """},
                    {"role":"user", "content": ai_code}],
                    temperature=0.5
    )
    
    rr=(response.choices[0].message.content)

    st.header("Code Review")
    st.write(rr)
    


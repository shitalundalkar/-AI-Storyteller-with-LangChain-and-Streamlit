import os
os.environ["OPENAI_API_KEY"] = ""
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import os
os.environ["OPENAI_API_KEY"] = ""
st.title("📖 AI Storyteller")
st.write("Generate amazing AI-driven stories! Just provide a prompt.")
prompt = st.text_input("Enter a story idea (e.g., 'A brave knight fights a dragon'): ")
if st.button("Generate Story"):
    if prompt:
        # LangChain Story Generation
        template = PromptTemplate(
            input_variables=["story_prompt"],
            template="Write a short creative story about: {story_prompt}"
        )
        
        llm = OpenAI(temperature=0.7)
        story = llm(template.format(story_prompt=prompt))
        
        # Display the generated story
        st.subheader("📜 Your AI-Generated Story:")
        st.write(story)
    else:
        st.warning("Please enter a prompt to generate a story.")
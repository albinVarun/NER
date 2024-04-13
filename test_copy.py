#NER libraries
import spacy 
from spacy import displacy 
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()
from pprint import pprint
from newspaper import Article 

#streamlit libraries
import streamlit as st
st.title("Name Entity Recognition")
url_input=st.text_input("Enter URL")
   

st.subheader("OR")

text_input=st.text_input("Enter the text")

if (st.button("Analyze")):
    if url_input !='':
        articled=Article(url_input)
        articled.download()
        articled.parse()
        #articled.text
        document=nlp(articled.text)
        ent_html = displacy.render(document, style="ent", jupyter=False)
        
        st.markdown(ent_html, unsafe_allow_html=True)
    elif text_input !="":
        documented=nlp(text_input)
        ent_html= displacy.render(documented,style="ent",jupyter=False)
        st.markdown(ent_html,unsafe_allow_html=True)
    else:
        st.warning("Please use a single field at a time")
#Source: https://stackoverflow.com/questions/69696035/typeerror-object-of-type-mappingproxy-is-not-json-serializable
import streamlit as st
import Processor as processor
import json

ecgProperty = processor.GetSourceProperty(r"C:\Users\100.dat")

st.write(type(ecgProperty))
st.write(ecgProperty)
jsonECGPropertyStr = json.dumps(ecgProperty.__dict__)
st.write(jsonECGPropertyStr)
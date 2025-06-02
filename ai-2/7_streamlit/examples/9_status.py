import streamlit as st
import time

progress_bar = st.progress(0)

progress_bar = st.progress(0)
    time.sleep(0.2)
    progress_bar.progress(percent)

with st.spinner('Wait for it...'):
    time.sleep(3)
    st.success('Done!')

st.ballons()

st.snow()

st.success('Success')

st.error('Error')

st.info('Info')

st.warning('Warning')

st.exception(Exception('Exception'))
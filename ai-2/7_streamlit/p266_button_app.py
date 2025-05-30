import streamlit as st

st.title('스트림릿에서의 버튼 입력 사용 예')

clicked = st.button('button 1')
st.write('Button 1 Status: ', clicked)

if clicked:
    st.write('Button 1 clicked')
else:
    st.write('Button 1 not clicked')

clicked = st.button('button 2')
st.write('Button 2 Status: ', clicked)

if clicked:
    st.write('Button 2 clicked')
else:
    st.write('Button 2 not clicked')
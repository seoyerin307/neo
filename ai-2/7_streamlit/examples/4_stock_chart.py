import streamlit as st 
import FinanceDataReader as fdr
import datetime

date = st.date_input(
    '조회 시작일을 선택해주세요',
    datetime.date(2025, 5, 1)
)

code = st.text_input(
    '종목 코드',
    value='',
    placeholder='종목 코드를 입력하세요'
)

if code and date:
    df = fdr.DataReader(code, date)
    data = df.sort_index(ascending=True).loc[:, 'Close']
    st.line_chart(data)


import streamlit as st
import random
import datetime

st.title(':sparkles 로또 생성기 :sparkles')

def generate_lotto():
    lotto = set()

    while len(lotto) < 6:
        number =random.randint(1, 46)
        lotto.add(number)

    lotto = list(lotto)
    lotto.sort()
    return lotto

buttion = st.button('로또 생성')

if buttion:
    for i in range(1, 6):
        st.subheader(f"{i}, 행운의 번호 : :green[{generate_lotto()}]")
    st.write(f'생성된 시간 : {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
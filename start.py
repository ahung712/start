import streamlit as st

st.title('간단한 계산기')

a = st.number_input('첫번째 숫자를 입력하세요:', value=10)
b = st.number_input('두번째 숫자를 입력하세요:', value=20)
result = a + b

st.write(f'결과: {result}')


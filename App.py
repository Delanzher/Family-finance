import streamlit as st

st.set_page_config(page_title="Мои финансы", page_icon="💰", layout="wide")

st.title("Мои финансы")
st.subheader("Семейный финансовый кабинет")

st.write("Управляем семейным бюджетом разумно.")

st.divider()

st.metric("Доходы за месяц", "0 ₽")
st.metric("Расходы за месяц", "0 ₽")
st.metric("Остаток", "0 ₽")

st.info("Добро пожаловать в ваш финансовый кабинет!")

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Мои финансы", page_icon="💰", layout="wide")

st.title("Мои финансы")
st.caption("Семейный финансовый кабинет")

if "operations" not in st.session_state:
    st.session_state.operations = []

st.subheader("Добавить операцию")

operation_type = st.selectbox("Тип операции", ["Расход", "Доход"])

income_categories = ["Моя зарплата", "Мой аванс", "Зарплата мужа", "Премия", "Дополнительный доход", "Инвестиционный доход"]

expense_categories = ["Продукты", "Жильё и коммунальные услуги", "Транспорт", "Здоровье", "Одежда и уход", "Кафе и развлечения", "Кошки", "Подписки", "Ипотека", "Прочее"]

categories = income_categories if operation_type == "Доход" else expense_categories

category = st.selectbox("Категория", categories)

operation_date = st.date_input("Дата операции")

amount = st.number_input("Сумма, рублей", min_value=0, step=100)

comment = st.text_input("Комментарий")

if st.button("Добавить операцию", type="primary"):
    if amount > 0:
        st.session_state.operations.append({
            "Дата": str(operation_date),
            "Тип": operation_type,
            "Категория": category,
            "Сумма": amount,
            "Комментарий": comment
        })
        st.success("Операция добавлена!")
    else:
        st.warning("Укажи сумму больше нуля.")

st.divider()

st.subheader("Финансовые итоги")

operations = st.session_state.operations

income = sum(item["Сумма"] for item in operations if item["Тип"] == "Доход")
expenses = sum(item["Сумма"] for item in operations if item["Тип"] == "Расход")
balance = income - expenses

col1, col2, col3 = st.columns(3)

col1.metric("Доходы", f"{income:,.0f} ₽")
col2.metric("Расходы", f"{expenses:,.0f} ₽")
col3.metric("Остаток", f"{balance:,.0f} ₽")

st.divider()

st.subheader("История операций")

if operations:
    table = pd.DataFrame(operations)
    st.dataframe(table, use_container_width=True)
else:
    st.info("Пока операций нет. Добавь первую запись!")

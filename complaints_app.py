import streamlit as st
import pandas as pd
from datetime import datetime

st.title("نظام إدارة الشكاوى 📋")

# إدخال البيانات
complaint_id = st.text_input("رقم الشكوى")
product = st.text_input("اسم المنتج")
severity = st.selectbox("درجة الخطورة", ["High", "Medium", "Low"])
details = st.text_area("تفاصيل الشكوى")

# زر الحفظ
if st.button("حفظ الشكوى"):
    new_data = {
        "Complaint ID": [complaint_id],
        "Product": [product],
        "Severity": [severity],
        "Details": [details],
        "Date": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    }
    new_df = pd.DataFrame(new_data)

    try:
        existing_df = pd.read_excel("complaints_database.xlsx")
        updated_df = pd.concat([existing_df, new_df], ignore_index=True)
    except FileNotFoundError:
        updated_df = new_df

    updated_df.to_excel("complaints_database.xlsx", index=False)
    st.success("تم حفظ الشكوى بنجاح!")

# زر لعرض الشكاوى
if st.button("عرض جميع الشكاوى"):
    try:
        df = pd.read_excel("complaints_database.xlsx")
        st.write(df)
    except:
        st.warning("لا توجد شكاوى لعرضها حاليًا.")

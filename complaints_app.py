import streamlit as st
import pandas as pd
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials

st.title("نظام إدارة الشكاوى 📋")

complaint_id = st.text_input("رقم الشكوى")
product = st.text_input("اسم المنتج")
severity = st.selectbox("درجة الخطورة", ["High", "Medium", "Low"])
details = st.text_area("تفاصيل الشكوى")

if st.button("حفظ الشكوى"):
    new_data = [
        complaint_id,
        product,
        severity,
        details,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ]

    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=scopes)
    client = gspread.authorize(creds)

    # افتحي الملف "Complaints Database" اللي عملتيه في Google Sheets
    sheet = client.open("Complaints Database").sheet1
    sheet.append_row(new_data)

    st.success("✅ تم حفظ الشكوى بنجاح في Google Sheets!")

if st.button("عرض كل الشكاوى"):
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=scopes)
    client = gspread.authorize(creds)
    
    sheet = client.open("Complaints Database").sheet1
    data = sheet.get_all_records()

    df = pd.DataFrame(data)
    st.write(df)

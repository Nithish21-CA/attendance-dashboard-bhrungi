import streamlit as st
import pandas as pd

st.title("Attendance Summary Dashboard")

uploaded_file = st.file_uploader("Upload Excel file (one sheet per employee)", type=["xlsx"])

if uploaded_file:
    xls = pd.ExcelFile(uploaded_file)
    summary = []

    for sheet in xls.sheet_names:
        df = xls.parse(sheet)
        df.columns = df.columns.str.strip()  # Clean up column names
        present_days = (df["In Time"] != "00:00").sum()
        absent_days = (df["In Time"] == "00:00").sum()
        summary.append({"Name": sheet, "Present Days": present_days, "Absent Days": absent_days})

    summary_df = pd.DataFrame(summary)
    st.dataframe(summary_df)

    st.download_button("Download Summary CSV", summary_df.to_csv(index=False), file_name="attendance_summary.csv")

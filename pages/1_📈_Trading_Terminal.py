import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Trading Terminal | APEX ROAST", layout="wide")

st.title("📈 Global Coffee Trading Terminal")
st.markdown("---")

# 模擬 ICO Indicator Prices 數據 (參考 2026-04 數據)
data = {
    'Date': ['01-Apr', '02-Apr', '03-Apr', '06-Apr', '07-Apr', '08-Apr', '09-Apr'],
    'I-CIP': [268.65, 267.06, 264.09, 265.59, 260.40, 264.58, 264.41],
    'Colombian Milds': [334.35, 332.90, 330.87, 333.26, 323.61, 330.37, 330.40],
    'Robustas': [167.50, 165.22, 163.91, 164.15, 160.13, 160.04, 159.55]
}
df = pd.DataFrame(data)
df.set_index('Date', inplace=True)

# 佈局：上方顯示走勢圖
st.subheader("ICO Indicator Prices - April 2026")
st.line_chart(df[['I-CIP', 'Colombian Milds', 'Robustas']])

# 佈局：下方顯示詳細表格
col1, col2 = st.columns([2, 1])
with col1:
    st.write("### Market Detail (US cents/lb)")
    st.table(df)

with col2:
    st.write("### Market Summary")
    avg_price = df['I-CIP'].mean()
    st.metric(label="Average I-CIP", value=f"{avg_price:.2f}", delta="-0.1%")
    st.info("數據來源：International Coffee Organization (ICO)")

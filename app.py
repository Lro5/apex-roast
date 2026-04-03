import streamlit as st

# 設定網頁標題
st.set_page_config(page_title="Apex Roast | Premium Coffee", page_icon="☕")

# 自定義風格
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏎️ APEX ROAST")
st.subheader("Where Precision Meets Caffeine.")

st.write("Driven by data, roasted by masters. Welcome to the future of coffee.")

# 產品展示
col1, col2 = st.columns(2)
with col1:
    st.write("**The GT3 Blend**")
    st.button("Order GT3")
with col2:
    st.write("**The Apex Light**")
    st.button("Order Apex")

st.divider()
st.write("📍 Based in Hong Kong")

import streamlit as st

# 設定網頁標題
st.set_page_config(page_title="Apex Roast | Premium Coffee", page_icon="☕")

# ⚠️ 請將下面改做你嘅 WhatsApp 電話 (例如 85263168336)
whatsapp_number = "852XXXXXXXX" 

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #25D366; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏎️ APEX ROAST")
st.subheader("Where Precision Meets Caffeine.")

st.write("Driven by data, roasted by masters. Welcome to the future of coffee.")

# 產品展示
col1, col2 = st.columns(2)

with col1:
    st.write("**The GT3 Blend**")
    st.link_button("Order GT3 via WhatsApp", f"https://wa.me/{whatsapp_number}?text=I'd%20like%20to%20order%20the%20GT3%20Blend")

with col2:
    st.write("**The Apex Light**")
    st.link_button("Order Apex via WhatsApp", f"https://wa.me/{whatsapp_number}?text=I'd%20like%20to%20order%20the%20Apex%20Light")

st.divider()
st.write("📍 Based in Hong Kong")

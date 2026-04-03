import streamlit as st

# 設定網頁標題及分頁圖示
st.set_page_config(page_title="Apex Roast | Premium Coffee", page_icon="☕", layout="wide")

# ⚠️ 注意：呢度已經改咗做 .png 嚟配合你啱啱上傳嘅檔案
wallpaper_url = "https://raw.githubusercontent.com/Lro5/apex-roast/main/apex-32.png"
whatsapp_number = "85263168336"

# CSS 樣式
st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.8)), url("{wallpaper_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .main-text {{
        color: white;
        text-shadow: 2px 2px 8px #000000;
    }}
    .stButton>button {{
        background-color: #25D366;
        color: white;
        border: none;
        padding: 18px;
        font-size: 20px;
        font-weight: bold;
        border-radius: 12px;
        transition: 0.3s;
    }}
    </style>
    """, unsafe_allow_html=True)

# 頁面內容
st.markdown('<h1 class="main-text" style="font-size: 60px;">🏎️ APEX ROAST</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="main-text" style="color: #FF4B4B;">32# Edition: Precision Roasted.</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown('<h3 class="main-text">🏁 The GT3 Blend</h3>', unsafe_allow_html=True)
    st.link_button("Order GT3 via WhatsApp", f"https://wa.me/{whatsapp_number}?text=I'd%20like%20to%20order%20the%20GT3%20Blend")

with col2:
    st.markdown('<h3 class="main-text">⏱️ The Apex Light</h3>', unsafe_allow_html=True)
    st.link_button("Order Apex via WhatsApp", f"https://wa.me/{whatsapp_number}?text=I'd%20like%20to%20order%20the%20Apex%20Light")

st.divider()
st.markdown('<p class="main-text" style="text-align: center;">📍 Based in Hong Kong | APEX ROAST © 2026</p>', unsafe_allow_html=True)

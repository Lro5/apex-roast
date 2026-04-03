import streamlit as st

# 設定網頁標題及分頁圖示
st.set_page_config(page_title="Apex Roast | Premium Coffee", page_icon="☕", layout="wide")

# 圖片網址 (指向你 GitHub 入面張 32 號車相片)
wallpaper_url = "https://raw.githubusercontent.com/Lro5/apex-roast/main/apex-32.jpg"
whatsapp_number = "85263168336"

# CSS 樣式：強化視覺規模感
st.markdown(f"""
    <style>
    /* 背景設定：半透明遮罩 + 固定背景 */
    .stApp {{
        background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.8)), url("{wallpaper_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* 字體樣式 */
    .main-text {{
        color: white;
        text-shadow: 2px 2px 8px #000000;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }}
    
    /* 按鈕樣式：高級綠色 + 懸停效果 */
    .stButton>button {{
        background-color: #25D366;
        color: white;
        border: none;
        padding: 18px;
        font-size: 20px;
        font-weight: bold;
        border-radius: 12px;
        transition: 0.3s;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }}
    .stButton>button:hover {{
        background-color: #128C7E;
        transform: scale(1.02);
    }}
    </style>
    """, unsafe_allow_html=True)

# 頁面內容
st.markdown('<h1 class="main-text" style="font-size: 60px; margin-bottom: 0;">🏎️ APEX ROAST</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="main-text" style="color: #FF4B4B;">Precision Roasted. Track Ready.</h2>', unsafe_allow_html=True)
st.markdown('<p class="main-text" style="font-size: 20px;">Driven by data, roasted by masters. From the apex of the track to the perfect cup.</p>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# 產品展示區
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div style="background: rgba(255,255,255,0.1); padding: 20px; border-radius: 15px; border-left: 5px solid #FF4B4B;">', unsafe_allow_html=True)
    st.markdown('<h3 class="main-text">🏁 The GT3 Blend</h3>', unsafe_allow_html=True)
    st.markdown('<p class="main-text">Dark Roast | Bold & Intense</p>', unsafe_allow_html=True)
    st.link_button("Order GT3 via WhatsApp", f"https://wa.me/{whatsapp_number}?text=I'd%20like%20to%20order%20the%20GT3%20Blend")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div style="background: rgba(255,255,255,0.1); padding: 20px; border-radius: 15px; border-left: 5px solid #FF4B4B;">', unsafe_allow_html=True)
    st.markdown('<h3 class="main-text">⏱️ The Apex Light</h3>', unsafe_allow_html=True)
    st.markdown('<p class="main-text">Light Roast | Floral & Precise</p>', unsafe_allow_html=True)
    st.link_button("Order Apex via WhatsApp", f"https://wa.me/{whatsapp_number}?text=I'd%20like%20to%20order%20the%20Apex%20Light")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()
st.markdown('<p class="main-text" style="text-align: center;">📍 Based in Hong Kong | APEX ROAST © 2026</p>', unsafe_allow_html=True)

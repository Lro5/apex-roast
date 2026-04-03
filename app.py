import streamlit as st

# 設定網頁標題
st.set_page_config(page_title="Apex Roast | Premium Coffee", page_icon="☕", layout="wide")

# 圖片與電話設定
wallpaper_url = "https://raw.githubusercontent.com/Lro5/apex-roast/main/apex-32.png"
whatsapp_number = "85263168336"

# CSS 樣式：大膽、清晰、中軸對齊
st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.85)), url("{wallpaper_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* 全域文字白色與陰影 */
    .white-text {{
        color: #FFFFFF !important;
        text-align: center;
        text-shadow: 0px 4px 15px rgba(0,0,0,0.9);
        font-family: 'Helvetica Neue', sans-serif;
    }}

    /* 產品卡片：磨砂玻璃效果 */
    .product-box {{
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(10px);
        padding: 40px 20px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        text-align: center;
        transition: 0.3s;
    }}
    
    .stButton>button {{
        background-color: #25D366;
        color: white !important;
        border: none;
        padding: 15px 30px;
        font-size: 20px;
        font-weight: 700;
        border-radius: 50px; /* 圓角按鈕更現代 */
        width: 80%;
    }}
    </style>
    """, unsafe_allow_html=True)

# 品牌中心區
st.markdown('<div style="padding: 100px 0 50px 0;">', unsafe_allow_html=True)
st.markdown('<h1 class="white-text" style="font-size: 100px; font-weight: 900; letter-spacing: 10px; margin-bottom: 0;">APEX ROAST</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="white-text" style="font-size: 30px; letter-spacing: 5px; color: #FF4B4B;">PRECISION ROASTED. TRACK READY.</h3>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 產品展示區
col1, col2, col3 = st.columns([1, 4, 4]) # 左右留白令中間更集中

with col2:
    st.markdown('<div class="product-box">', unsafe_allow_html=True)
    st.markdown('<h2 class="white-text" style="font-size: 36px;">The GT3 Blend</h2>', unsafe_allow_html=True)
    st.markdown('<p class="white-text" style="font-size: 18px; opacity: 0.8;">Bold • Intense • Powerful</p>', unsafe_allow_html=True)
    st.link_button("Order via WhatsApp", f"https://wa.me/{whatsapp_number}?text=I'd%20like%20to%20order%20the%20GT3%20Blend")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="product-box">', unsafe_allow_html=True)
    st.markdown('<h2 class="white-text" style="font-size: 36px;">The Apex Light</h2>', unsafe_allow_html=True)
    st.markdown('<p class="white-text" style="font-size: 18px; opacity: 0.8;">Floral • Precise • Elegant</p>', unsafe_allow_html=True)
    st.link_button("Order via WhatsApp", f"https://wa.me/{whatsapp_number}?text=I'd%20like%20to%20order%20the%20Apex%20Light")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br><br><br>", unsafe_allow_html=True)
st.divider()
st.markdown('<p class="white-text" style="font-size: 16px; opacity: 0.6;">📍 Based in Hong Kong | APEX ROAST © 2026</p>', unsafe_allow_html=True)

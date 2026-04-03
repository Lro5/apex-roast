import streamlit as st

# 設定網頁標題
st.set_page_config(page_title="Apex Roast | Premium Coffee", page_icon="☕", layout="wide")

# 圖片與電話設定
wallpaper_url = "https://raw.githubusercontent.com/Lro5/apex-roast/main/apex-32.png"
whatsapp_number = "85263168336"

# CSS 樣式：極致對齊與置中
st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.85)), url("{wallpaper_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    .center-container {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        color: #FFFFFF !important;
        font-family: 'Helvetica Neue', sans-serif;
    }}

    /* 產品框：縮窄寬度並置中 */
    .product-box {{
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(12px);
        padding: 35px 25px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        text-align: center;
        margin: 10px auto;
        max-width: 350px; /* 限制寬度令佢更置中 */
        min-height: 280px;
    }}
    
    .white-text {{
        color: #FFFFFF !important;
        text-shadow: 0px 4px 12px rgba(0,0,0,0.9);
    }}

    .stButton>button {{
        background-color: #25D366;
        color: white !important;
        border: none;
        padding: 12px 20px;
        font-size: 18px;
        font-weight: 700;
        border-radius: 50px;
        width: 100%;
        margin-top: 20px;
    }}
    </style>
    """, unsafe_allow_html=True)

# 品牌中心區
st.markdown('<div class="center-container" style="padding: 80px 0 40px 0;">', unsafe_allow_html=True)
st.markdown('<h1 class="white-text" style="font-size: clamp(40px, 8vw, 110px); font-weight: 900; letter-spacing: 15px; margin-bottom: 10px;">APEX ROAST</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="white-text" style="font-size: clamp(16px, 3vw, 28px); letter-spacing: 6px; color: #FF4B4B; font-weight: 300;">PRECISION ROASTED. TRACK READY.</h3>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 產品展示區：使用 5 格佈局將產品推向中間 (1:2:2:1)
col_space1, col1, col2, col_space2 = st.columns([1, 2, 2, 1])

with col1:
    st.markdown('<div class="product-box">', unsafe_allow_html=True)
    st.markdown('<h2 class="white-text" style="font-size: 30px; margin-bottom: 5px;">The GT3 Blend</h2>', unsafe_allow_html=True)

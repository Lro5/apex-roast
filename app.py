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
st.markdown('<h2 class="main-text" style="color: #FF4B4B;">Precision Roasted. Track

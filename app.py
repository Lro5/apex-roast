import streamlit as st

# 設定網頁標題
st.set_page_config(page_title="Apex Roast | Premium Selection", page_icon="☕", layout="wide")

# 基本設定
base_url = "https://raw.githubusercontent.com/Lro5/apex-roast/main/"
wallpaper_url = base_url + "apex-32.png"
whatsapp_number = "85263168336"

# 咖啡豆資料庫 (純文字，無 Icon)
beans = [
    {"name": "衣索匹亞 罕貝拉 可如蜜", "img": "bean1.png", "award": "非洲收穫祭水洗組第一名", "flavor": "橙汁、蜂蜜、花香"},
    {"name": "衣索匹亞 吉馬", "img": "bean2.png", "award": "非洲收穫祭蜜處理組第二名", "flavor": "柑橘、黑嘉倫子、黑糖"},
    {"name": "巴拿馬 翡翠莊園 拉米約", "img": "bean3.png", "award": "2025 水洗藝伎組冠軍", "flavor": "茉莉花、檸檬糖、果汁感"},
    {"name": "巴拿馬 翡翠莊園 坎納斯", "img": "bean4.png", "award": "2025 日曬藝伎組冠軍", "flavor": "白蘭花、荔枝、鳳梨"},
    {"name": "衣索匹亞 西達碼 邦娜", "img": "bean5.png", "award": "獲獎出口商精品豆", "flavor": "莉莉、杏脯、伯爵茶"}
]

# CSS 樣式：極致置中與高級感
st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.9)), url("{wallpaper_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* 強制所有文字置中 */
    .white-text {{ 
        color: #FFFFFF !important; 
        text-align: center !important; 
        width: 100%;
        display: block;
        font-family: 'Helvetica Neue', sans-serif;
    }}
    
    /* 咖啡豆卡片置中設定 */
    .bean-card {{
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(12px);
        padding: 25px 15px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        margin-bottom: 20px;
        display: flex;
        flex-direction: column;
        align-items: center; /* 內部元素水平置中 */
        justify-content: flex-start;
        transition: 0.3s;
        min-height: 450px;
    }}
    
    .bean-card img {{
        border-radius: 12px;
        margin-bottom: 15px;
    }}

    .stButton {{
        display: flex;
        justify-content: center;
        width: 100%;
    }}

    .stButton>button {{
        background-color: #25D366;
        color: white !important;
        border-radius: 50px;
        width: 100%;
        font-weight: bold;
        border: none;
    }}
    </style>
    """, unsafe_allow_html=True)

# 標題 (置中)
st.markdown('<div style="text-align: center; padding: 60px 0;">', unsafe_allow_html=True)
st.markdown('<h1 class="white-text" style="font-size: 80px; font-weight: 900; letter-spacing: 12px;">APEX ROAST</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="white-text" style="color: #FF4B4B; letter-spacing: 5px; font-weight: 300;">THE CHAMPION SELECTION</h3>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 顯示 5 欄 (置中佈局)
cols = st.columns(5)

for i, bean in enumerate(beans):
    with cols[i]:
        # 整個卡片包裹在一個置中 div 內
        st.markdown(f'<div class="bean-card">', unsafe_allow_html=True)
        
        # 顯示圖片
        st.image(base_url + bean["img"], use_container_width=True)
        
        # 文字內容
        st.markdown(f'<h3 class="white-text" style="font-size: 20px; min-height: 55px; margin-top: 10px;">{bean["name"]}</h3>', unsafe_allow_html=True)
        st.markdown(f'<p class="white-text" style="color: #FFD700 !important; font-size: 14px; font-weight: 500; min-height: 40px;">{bean["award"]}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="white-text" style="font-size: 15px; opacity: 0.8; font-weight: 300; min-height: 50px;">{bean["flavor"]}</p>', unsafe_allow_html=True)
        
        # WhatsApp 按鈕
        order_msg = f"你好，我想訂購：{bean['name']}"
        st.link_button("Order Now", f"https://wa.me/{whatsapp_number}?text={order_msg}")
        
        st.markdown('</div>', unsafe_allow_html=True)

st.divider()
st.markdown('<p class="white-text" style="opacity: 0.5; font-size: 14px;">📍 HONG KONG | APEX ROAST © 2026</p>', unsafe_allow_html=True)

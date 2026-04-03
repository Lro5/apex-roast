import streamlit as st

# 設定網頁標題
st.set_page_config(page_title="Apex Roast | Premium Selection", page_icon="☕", layout="wide")

# 基本設定
base_url = "https://raw.githubusercontent.com/Lro5/apex-roast/main/"
wallpaper_url = base_url + "apex-32.png"
whatsapp_number = "85263168336"

# 咖啡豆資料庫 (已完全移除 Emoji Icon)
beans = [
    {"name": "衣索匹亞 罕貝拉 可如蜜", "img": "bean1.png", "award": "非洲收穫祭水洗組第一名", "flavor": "橙汁、蜂蜜、花香"},
    {"name": "衣索匹亞 吉馬", "img": "bean2.png", "award": "非洲收穫祭蜜處理組第二名", "flavor": "柑橘、黑嘉倫子、黑糖"},
    {"name": "巴拿馬 翡翠莊園 拉米約", "img": "bean3.png", "award": "2025 水洗藝伎組冠軍", "flavor": "茉莉花、檸檬糖、果汁感"},
    {"name": "巴拿馬 翡翠莊園 坎納斯", "img": "bean4.png", "award": "2025 日曬藝伎組冠軍", "flavor": "白蘭花、荔枝、鳳梨"},
    {"name": "衣索匹亞 西達碼 邦娜", "img": "bean5.png", "award": "獲獎出口商精品豆", "flavor": "莉莉、杏脯、伯爵茶"}
]

# CSS 樣式：強調極簡與高級感
st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.9)), url("{wallpaper_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .white-text {{ color: #FFFFFF !important; text-align: center; font-family: 'Helvetica Neue', sans-serif; }}
    
    /* 咖啡豆卡片樣式：強化磨砂玻璃效果 */
    .bean-card {{
        background: rgba(255, 255, 255, 0.06);
        backdrop-filter: blur(15px);
        padding: 25px 15px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        margin-bottom: 20px;
        text-align: center;
        transition: 0.3s ease;
        min-height: 400px; /* 統一高度 */
    }}
    .bean-card:hover {{
        transform: translateY(-8px);
        border-color: #FF4B4B;
        background: rgba(255, 255, 255, 0.1);
    }}
    
    .stButton>button {{
        background-color: #25D366;
        color: white !important;
        border-radius: 50px;
        width: 100%;
        font-weight: bold;
        padding: 12px;
        border: none;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }}
    </style>
    """, unsafe_allow_html=True)

# 標題
st.markdown('<div style="text-align: center; padding: 60px 0 40px 0;">', unsafe_allow_html=True)
st.markdown('<h1 class="white-text" style="font-size: 85px; font-weight: 900; letter-spacing: 12px; margin-bottom: 0;">APEX ROAST</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="white-text" style="color: #FF4B4B; letter-spacing: 6px; font-weight: 300;">THE CHAMPION SELECTION</h3>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 顯示 5 款咖啡豆 (5 欄佈局)
cols = st.columns(5)

for i, bean in enumerate(beans):
    with cols[i]:
        st.markdown(f'<div class="bean-card">', unsafe_allow_html=True)
        # 顯示圖片 (指向你的 GitHub 相片)
        st.image(base_url + bean["img"], use_container_width=True)
        
        st.markdown(f'<h3 class="white-text" style="font-size: 20px; height: 50px; display: flex; align-items: center; justify-content: center; margin-top: 10px;">{bean["name"]}</h3>', unsafe_allow_html=True)
        st.markdown(f'<p style="color: #FFD700; font-size: 14px; font-weight: 500; height: 35px;">{bean["award"]}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="white-text" style="font-size: 15px; opacity: 0.8; font-weight: 300; height: 40px;">{bean["flavor"]}</p>', unsafe_allow_html=True)
        
        # WhatsApp 連結自動帶入豆名
        order_msg = f"你好，我想訂購：{bean['name']}"
        st.link_button("Order Now", f"https://wa.me/{whatsapp_number}?text={order_msg}")
        st.markdown('</div>', unsafe_allow_html=True)

st.divider()
st.markdown('<p class="white-text" style="text-align: center; opacity: 0.5; font-size: 14px; letter-spacing: 1px; padding: 20px 0;">📍 HONG KONG | APEX ROAST © 2026</p>', unsafe_allow_html=True)

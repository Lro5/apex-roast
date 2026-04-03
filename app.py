import streamlit as st

# 設定網頁標題
st.set_page_config(page_title="Apex Roast | Premium Selection", page_icon="☕", layout="wide")

# 基本設定
base_url = "https://raw.githubusercontent.com/Lro5/apex-roast/main/"
wallpaper_url = base_url + "apex-32.png"
whatsapp_number = "85263168336"

# 咖啡豆資料 (無 Icon 版)
beans = [
    {"name": "衣索匹亞 罕貝拉 可如蜜", "img": "bean1.png", "award": "非洲收穫祭水洗組第一名", "flavor": "橙汁、蜂蜜、花香"},
    {"name": "衣索匹亞 吉馬", "img": "bean2.png", "award": "非洲收穫祭蜜處理組第二名", "flavor": "柑橘、黑嘉倫子、黑糖"},
    {"name": "巴拿馬 翡翠莊園 拉米約", "img": "bean3.png", "award": "2025 水洗藝伎組冠軍", "flavor": "茉莉花、檸檬糖、果汁感"},
    {"name": "巴拿馬 翡翠莊園 坎納斯", "img": "bean4.png", "award": "2025 日曬藝伎組冠軍", "flavor": "白蘭花、荔枝、鳳梨"},
    {"name": "衣索匹亞 西達碼 邦娜", "img": "bean5.png", "award": "獲獎出口商精品豆", "flavor": "莉莉、杏脯、伯爵茶"}
]

# CSS 樣式：增加呼吸感與絕對置中
st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.9)), url("{wallpaper_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* 強制文字水平置中 */
    .white-text {{ 
        color: #FFFFFF !important; 
        text-align: center !important; 
        width: 100%;
        display: block;
        margin: 0 auto;
    }}
    
    /* 產品卡片：增加間距，防止密密麻麻 */
    .bean-card {{
        background: rgba(255, 255, 255, 0.07);
        backdrop-filter: blur(15px);
        padding: 40px 30px;
        border-radius: 30px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin: 20px auto;
        text-align: center;
        max-width: 400px;
        transition: 0.4s ease;
    }}
    
    .bean-card:hover {{
        border-color: #FF4B4B;
        background: rgba(255, 255, 255, 0.12);
    }}

    .stButton {{
        display: flex;
        justify-content: center;
    }}

    .stButton>button {{
        background-color: #25D366;
        color: white !important;
        border-radius: 50px;
        width: 80% !important;
        padding: 15px;
        font-size: 18px;
        border: none;
    }}
    </style>
    """, unsafe_allow_html=True)

# 標題 (大氣排版)
st.markdown('<div style="text-align: center; padding: 80px 0 60px 0;">', unsafe_allow_html=True)
st.markdown('<h1 class="white-text" style="font-size: 90px; font-weight: 900; letter-spacing: 15px;">APEX ROAST</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="white-text" style="color: #FF4B4B; letter-spacing: 8px; font-weight: 300;">THE CHAMPION SELECTION</h3>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 分行顯示：第一行 3 個，第二行 2 個 (置中佈局)
row1_cols = st.columns(3)
for i in range(3):
    with row1_cols[i]:
        bean = beans[i]
        st.markdown(f'<div class="bean-card">', unsafe_allow_html=True)
        st.image(base_url + bean["img"], use_container_width=True)
        st.markdown(f'<h2 class="white-text" style="font-size: 28px; margin-top: 20px;">{bean["name"]}</h2>', unsafe_allow_html=True)
        st.markdown(f'<p class="white-text" style="color: #FFD700 !important; font-size: 16px; font-weight: 600; letter-spacing: 1px;">{bean["award"]}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="white-text" style="font-size: 18px; opacity: 0.8; font-weight: 300; margin-bottom: 20px;">{bean["flavor"]}</p>', unsafe_allow_html=True)
        st.link_button("Order Now", f"https://wa.me/{whatsapp_number}?text=我想訂購：{bean['name']}")
        st.markdown('</div>', unsafe_allow_html=True)

row2_spacer1, row2_col1, row2_col2, row2_spacer2 = st.columns([0.5, 2, 2, 0.5])
for i in range(3, 5):
    target_col = row2_col1 if i == 3 else row2_col2
    with target_col:
        bean = beans[i]
        st.markdown(f'<div class="bean-card">', unsafe_allow_html=True)
        st.image(base_url + bean["img"], use_container_width=True)
        st.markdown(f'<h2 class="white-text" style="font-size: 28px; margin-top: 20px;">{bean["name"]}</h2>', unsafe_allow_html=True)
        st.markdown(f'<p class="white-text" style="color: #FFD700 !important; font-size: 16px; font-weight: 600; letter-spacing: 1px;">{bean["award"]}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="white-text" style="font-size: 18px; opacity: 0.8; font-weight: 300; margin-bottom: 20px;">{bean["flavor"]}</p>', unsafe_allow_html=True)
        st.link_button("Order Now", f"https://wa.me/{whatsapp_number}?text=我想訂購：{bean['name']}")
        st.markdown('</div>', unsafe_allow_html=True)

st.divider()
st.markdown('<p class="white-text" style="opacity: 0.5; letter-spacing: 2px; padding-bottom: 40px;">📍 HONG KONG | APEX ROAST © 2026</p>', unsafe_allow_html=True)

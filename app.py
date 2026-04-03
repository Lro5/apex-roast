import streamlit as st

# 設定網頁標題
st.set_page_config(page_title="Apex Roast | Premium Selection", page_icon="☕", layout="wide")

# 基本設定
base_url = "https://raw.githubusercontent.com/Lro5/apex-roast/main/"
wallpaper_url = base_url + "apex-32.png"
whatsapp_number = "85263168336"

# 咖啡豆資料 (純文字)
beans = [
    {"name": "衣索匹亞 罕貝拉 可如蜜", "img": "bean1.png", "award": "非洲收穫祭水洗組第一名", "flavor": "橙汁、蜂蜜、花香"},
    {"name": "衣索匹亞 吉馬", "img": "bean2.png", "award": "非洲收穫祭蜜處理組第二名", "flavor": "柑橘、黑嘉倫子、黑糖"},
    {"name": "巴拿馬 翡翠莊園 拉米約", "img": "bean3.png", "award": "2025 水洗藝伎組冠軍", "flavor": "茉莉花、檸檬糖、果汁感"},
    {"name": "巴拿馬 翡翠莊園 坎納斯", "img": "bean4.png", "award": "2025 日曬藝伎組冠軍", "flavor": "白蘭花、荔枝、鳳梨"},
    {"name": "衣索匹亞 西達碼 邦娜", "img": "bean5.png", "award": "獲獎出口商精品豆", "flavor": "莉莉、杏脯、伯爵茶"}
]

# CSS 樣式：解決置中與鋪排問題
st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.9)), url("{wallpaper_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* 強制全局文字置中 */
    .stMarkdown, .stText, h1, h2, h3, p {{
        text-align: center !important;
    }}

    .white-text {{ 
        color: #FFFFFF !important; 
        font-family: 'Helvetica Neue', sans-serif;
        display: block;
        width: 100%;
        text-shadow: 0 2px 10px rgba(0,0,0,0.8);
    }}
    
    /* 卡片容器：強制內部所有元素置中 */
    .bean-card {{
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(15px);
        padding: 30px 20px;
        border-radius: 25px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 20px;
        display: flex;
        flex-direction: column;
        align-items: center; /* 水平置中 */
        justify-content: space-between;
        min-height: 520px;
        transition: 0.4s ease;
    }}
    
    .bean-card:hover {{
        border-color: #FF4B4B;
        background: rgba(255, 255, 255, 0.12);
        transform: translateY(-5px);
    }}

    /* 圖片樣式 */
    .bean-img {{
        width: 100%;
        border-radius: 15px;
        margin-bottom: 20px;
    }}

    /* === 高級賽車版按鈕樣式 === */
    .stButton {{
        display: flex;
        justify-content: center;
        width: 100%;
        margin-top: 25px;
    }}
    
    .stButton>button {{
        /* 賽車紅高級漸變 */
        background: linear-gradient(135deg, #FF1E1E 0%, #333333 100%) !important;
        color: white !important;
        border-radius: 50px !important;
        border: none !important;
        padding: 15px 35px !important;
        font-size: 20px !important;
        font-weight: 900 !important;
        letter-spacing: 2px !important;
        width: 100% !important;
        text-transform: uppercase !important;
        box-shadow: 0 5px 20px rgba(0,0,0,0.5);
        transition: all 0.3s ease-in-out;
        position: relative;
        overflow: hidden;
    }}
    
    /* 懸停效果：霓虹光暈 */
    .stButton>button:hover {{
        background: linear-gradient(135deg, #FF4B4B 0%, #444444 100%) !important;
        transform: scale(1.05);
        box-shadow: 0 0 25px rgba(255, 75, 75, 0.7) !important;
        letter-spacing: 3px !important;
    }}
    
    /* 按鈕點擊效果 */
    .stButton>button:active {{
        transform: scale(0.98);
        box-shadow: 0 2px 10px rgba(255, 75, 75, 0.5) !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# 標題區
st.markdown('<div style="padding: 60px 0;">', unsafe_allow_html=True)
st.markdown('<h1 class="white-text" style="font-size: clamp(40px, 8vw, 90px); font-weight: 900; letter-spacing: 15px; margin: 0;">APEX ROAST</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="white-text" style="color: #FF4B4B; letter-spacing: 8px; font-weight: 300; font-size: clamp(14px, 2vw, 24px);">THE CHAMPION SELECTION</h3>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 顯示 5 欄
cols = st.columns(5)

for i, bean in enumerate(beans):
    with cols[i]:
        st.markdown(f'''
            <div class="bean-card">
                <img src="{base_url + bean["img"]}" class="bean-img">
                <div>
                    <h3 class="white-text" style="font-size: 20px; margin-bottom: 10px; font-weight: 800;">{bean["name"]}</h3>
                    <p style="color: #FFD700; font-size: 14px; font-weight: 600; margin-bottom: 10px; letter-spacing: 1px; text-transform: uppercase;">{bean["award"]}</p>
                    <p class="white-text" style="font-size: 15px; opacity: 0.8; font-weight: 300; letter-spacing: 0.5px;">{bean["flavor"]}</p>
                </div>
        ''', unsafe_allow_html=True)
        
        # WhatsApp 按鈕
        order_msg = f"你好，我想訂購：{bean['name']}"
        st.link_button("Order Now", f"https://wa.me/{whatsapp_number}?text={order_msg}")

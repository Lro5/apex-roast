import streamlit as st
import urllib.parse
import random # 用於模擬即時波動數據

# 設定網頁標題
st.set_page_config(page_title="APEX ROAST | TRADING TERMINAL", page_icon="📈", layout="wide")

# ==========================================
# 模擬即時數據函數 (讓網頁有生命感)
# ==========================================
def get_ticker_html():
    # 模擬全球咖啡期貨數據
    data = [
        ("ICE ARABICA", 224.15, +1.24),
        ("ICE ROBUSTA", 4120.00, -0.85),
        ("ICO COMPOSITE", 210.45, +0.32),
        ("PANAMA AUCTION", 850.00, +5.12),
        ("ETHIOPIA BENCHMARK", 185.20, -1.15)
    ]
    ticker_content = "  /  ".join([f"{name}: {price} <span style='color:{'#00ff00' if change > 0 else '#ff4b4b'}'>{'+' if change > 0 else ''}{change}%</span>" for name, price, change in data])
    return f"""
    <div style="background: #111; color: white; padding: 10px; border-bottom: 1px solid #FF4B4B; overflow: hidden; white-space: nowrap; font-family: 'Michroma'; font-size: 12px;">
        <marquee scrollamount="5">{ticker_content}  /  {ticker_content}</marquee>
    </div>
    """

# ==========================================
# 初始化購物車 (Session State)
# ==========================================
if 'cart' not in st.session_state:
    st.session_state.cart = {}

# ==========================================
# 基本設定
# ==========================================
base_url = "https://raw.githubusercontent.com/Lro5/apex-roast/main/"
wallpaper_url = base_url + "apex-endurance-32.png"
your_email = "hirosenno@gmail.com" 

beans = [
    {
        "name": "衣索匹亞 罕貝拉 可如蜜",
        "name_en": "Ethiopia Hambela Kurume",
        "img": "bean1.png",
        "origin": "ETHIOPIA HAMBELA",
        "price": 168,
        "yield": "LOW", # 增加交易所屬性：產量
        "volatility": "STABLE", # 增加交易所屬性：波動性
        "story_zh": "高海拔產區限量批次，其潔淨度如同市場指標，是極致平衡的資產選擇。",
        "flavor_zh": "橙汁感、白色花香、荔枝甜感",
        "weight": "200g"
    },
    {
        "name": "巴拿馬 翡翠莊園 拉米約",
        "name_en": "Panama Esmeralda Laramillo",
        "img": "bean3.png",
        "origin": "PANAMA ESME LARAMILLO",
        "price": 328,
        "yield": "CRITICAL LOW",
        "volatility": "HIGH",
        "story_zh": "藝伎界的藍籌股。拉米約地塊擁有完美的微型氣候，是收藏級的頂級標的。",
        "flavor_zh": "茉莉花香、檸檬糖、佛手柑",
        "weight": "100g"
    }
    # 其他豆子可按此格式類推...
]

# 插入頂部滾動條
st.markdown(get_ticker_html(), unsafe_allow_html=True)

# CSS 樣式升級 (加入更多終端機元素)
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Michroma&family=JetBrains+Mono:wght@400;700&display=swap');

    .stApp {{
        background: linear-gradient(90deg, rgba(0,0,0,1) 40%, rgba(0,0,0,0.5) 100%), url("{wallpaper_url}");
        background-size: cover;
        background-color: #000;
        font-family: 'JetBrains Mono', monospace;
    }}

    /* 交易所風格的邊框 */
    .detail-section {{
        background: rgba(10, 10, 10, 0.85);
        border: 1px solid rgba(255, 75, 75, 0.3);
        padding: 30px;
        margin-bottom: 25px;
        border-left: 5px solid #FF4B4B;
    }}

    .bean-title {{ color: #FFFFFF; font-family: 'Michroma'; font-size: 22px; }}
    .origin-label {{ color: #FF4B4B; font-family: 'Michroma'; letter-spacing: 2px; font-size: 12px; }}
    .price-text {{ color: #00ff00; font-family: 'Michroma'; font-size: 28px; }} /* 價格改用綠色表示獲利感 */
    
    .stButton>button {{
        background: transparent;
        border: 1px solid #FF4B4B !important;
        color: #FF4B4B !important;
        font-family: 'Michroma';
        transition: 0.3s;
    }}
    .stButton>button:hover {{
        background: #FF4B4B !important;
        color: black !important;
        box-shadow: 0 0 15px #FF4B4B;
    }}
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 主頁面：交易大廳
# ==========================================
col_main, col_spacer = st.columns([2, 1])

with col_main:
    st.markdown('<h1 style="color: white; font-family: \'Michroma\'; font-size: 40px;">TRADING TERMINAL</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color: #FF4B4B; font-family: \'Michroma\'; font-size: 12px;">SYSTEM STATUS: ONLINE | APEX SELECTION V2.0</p>', unsafe_allow_html=True)

    for i, bean in enumerate(beans):
        with st.container():
            st.markdown(f'''
            <div class="detail-section">
                <p class="origin-label">ASSET ID: {bean["origin"]}</p>
                <h2 class="bean-title">{bean["name"]}</h2>
                <div style="display: flex; gap: 20px; margin: 10px 0;">
                    <span style="background: #222; padding: 5px 10px; font-size: 10px; color: #aaa; border: 1px solid #444;">YIELD: {bean["yield"]}</span>
                    <span style="background: #222; padding: 5px 10px; font-size: 10px; color: #aaa; border: 1px solid #444;">VOLATILITY: {bean["volatility"]}</span>
                </div>
            </div>
            ''', unsafe_allow_html=True)
            
            c1, c2, c3 = st.columns([1, 1, 1])
            with c1:
                st.image(base_url + bean["img"], width=200)
            with c2:
                st.markdown(f'<p style="font-size: 14px; color: #ccc;">{bean["story_zh"]}</p>', unsafe_allow_html=True)
                st.markdown(f'<p style="color: #FFD700; font-size: 13px;">PROFILE: {bean["flavor_zh"]}</p>', unsafe_allow_html=True)
            with c3:
                st.markdown(f'<div class="price-text">${bean["price"]} <span style="font-size:12px; color:#666;">HKD/{bean["weight"]}</span></div>', unsafe_allow_html=True)
                qty = st.number_input("UNITS", 1, 10, 1, key=f"q_{i}")
                if st.button(f"EXECUTE BUY ORDER", key=f"b_{i}"):
                    st.session_state.cart[bean["name"]] = {"price": bean["price"], "qty": qty, "name_en": bean["name_en"]}
                    st.toast(f"ORDER EXECUTED: {bean['name']}")
                    st.rerun()

# 購物車與側邊欄邏輯保持不變（但樣式會繼承上面的終端風格）
# ... (其餘側邊欄代碼與你提供的一致)

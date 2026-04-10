import streamlit as st
import urllib.parse

# 設定網頁標題
st.set_page_config(page_title="Apex Roast | Private Selection", page_icon="☕", layout="wide")

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

# 深度資料庫
beans = [
    {
        "name": "衣索匹亞 罕貝拉 可如蜜",
        "name_en": "Ethiopia Hambela Kurume",
        "img": "bean1.png",
        "origin": "ETHIOPIA HAMBELA",
        "price": 168,
        "weight": "200g",
        "story_zh": "產自高海拔罕貝拉產區，可如蜜（Kurume）是當地原生種。這款豆在非洲收穫祭中脫穎而出，以極致的潔淨度與花香聞名。經過嚴格水洗處理，呈現出如精品香水般的層次。",
        "story_en": "Sourced from high-altitude Hambela, Kurume is a prized landrace known for exceptional clarity and floral elegance. Fully washed for sophisticated layers.",
        "award": "非洲收穫祭水洗組第一名 | 1st Place, African Harvest (Washed)",
        "flavor_zh": "橙汁感、白色花香、荔枝甜感、蜂蜜餘韻",
        "flavor_en": "Orange Juice, White Florals, Lychee Sweetness, Honey Finish"
    },
    {
        "name": "衣索匹亞 吉馬",
        "name_en": "Ethiopia Djimmah",
        "img": "bean2.png",
        "origin": "ETHIOPIA DJIMMAH",
        "price": 158,
        "weight": "200g",
        "story_zh": "吉馬產區是咖啡發源地。這批次採用特殊蜜處理技術，保留果肉糖分發酵，使得口感厚實，酸質圓潤且帶有豐富漿果氣息。",
        "story_en": "From the birthplace of coffee, this Honey Process lot achieves a bolder body and rounded acidity with rich berry notes.",
        "award": "非洲收穫祭蜜處理組第二名 | 2nd Place, African Harvest (Honey)",
        "flavor_zh": "柑橘、黑嘉倫子、成熟果實、黑糖甜感",
        "flavor_en": "Citrus, Blackcurrant, Ripe Stone Fruit, Brown Sugar"
    },
    {
        "name": "巴拿馬 翡翠莊園 拉米約",
        "name_en": "Panama Esmeralda Laramillo",
        "img": "bean3.png",
        "origin": "PANAMA ESME LARAMILLO",
        "price": 328,
        "weight": "100g",
        "story_zh": "傳奇的翡翠莊園。拉米約地塊擁有完美的微型氣候，這款水洗藝伎展現了最經典的貴族氣息，細緻且悠長。",
        "story_en": "The legendary Hacienda La Esmeralda. Laramillo plot Geisha epitomizes aristocratic elegance—refined and lingering.",
        "award": "2025 水洗藝伎組冠軍 | 2025 Washed Geisha Champion",
        "flavor_zh": "茉莉花香、檸檬糖、精緻果汁感、佛手柑",
        "flavor_en": "Jasmine, Lemon Candy, Refined Juice, Bergamot"
    },
    {
        "name": "巴拿馬 翡翠莊園 坎納斯",
        "name_en": "Panama Esmeralda Cañas Verdes",
        "img": "bean4.png",
        "origin": "PANAMA ESME CANAS",
        "price": 358,
        "weight": "100g",
        "story_zh": "坎納斯地塊的日曬處理法將藝伎的熱帶水果風味推向巔峰。賦予了咖啡更強烈的甜度與發酵酒香感。",
        "story_en": "Cañas Verdes plot pushes Geisha’s profile to its peak through Natural processing, offering intense sweetness.",
        "award": "2025 日曬藝伎組冠軍 | 2025 Natural Geisha Champion",
        "flavor_zh": "白蘭花、濃郁荔枝、鳳梨、熱帶水果風味",
        "flavor_en": "White Orchid, Intense Lychee, Pineapple, Tropical Fruit"
    },
    {
        "name": "衣索匹亞 西達碼 邦娜",
        "name_en": "Ethiopia Sidama Bonna",
        "img": "bean5.png",
        "origin": "ETHIOPIA SIDAMA BONNA",
        "price": 148,
        "weight": "200g",
        "story_zh": "西達碼邦娜合作社展現了特有的伯爵茶感，口感輕盈卻充滿記憶點，是極致優雅的代表作。",
        "story_en": "Sidama Bonna showcases signature Earl Grey tea-like character. Light on the palate yet deeply memorable.",
        "award": "獲獎出口商年度推薦 | Award-winning Exporter's Choice",
        "flavor_zh": "莉莉花香、杏脯、伯爵茶、清爽柑橘",
        "flavor_en": "Lily, Dried Apricot, Earl Grey Tea, Crisp Citrus"
    }
]

# CSS 樣式
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Michroma&family=Inter:wght@300;400;700&display=swap');

    .stApp {{
        background: linear-gradient(90deg, rgba(0,0,0,1) 40%, rgba(0,0,0,0.2) 100%), url("{wallpaper_url}");
        background-size: contain; 
        background-repeat: no-repeat;
        background-position: right center; 
        background-attachment: fixed;
        background-color: #000000; 
        font-family: 'Inter', sans-serif;
    }}

    [data-testid="stSidebar"] {{
        background-color: rgba(15, 15, 15, 0.95) !important;
        border-right: 1px solid rgba(255, 75, 75, 0.2);
    }}

    /* 輸入框深色設定 */
    div[data-baseweb="input"], 
    div[data-baseweb="textarea"], 
    div[data-baseweb="base-input"],
    .stNumberInput div {{
        background-color: rgba(30, 30, 30, 0.8) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
    }}

    input, textarea {{
        background-color: transparent !important;
        color: white !important;
        -webkit-text-fill-color: white !important;
    }}

    div[data-baseweb="input"]:focus-within, 
    div[data-baseweb="textarea"]:focus-within {{
        background-color: rgba(45, 45, 45, 0.9) !important;
        border-color: #FF4B4B !important;
    }}

    [data-testid="stMainViewContainer"] > section {{
        padding-left: 5% !important;
        padding-right: 35% !important; 
    }}
    
    .detail-section {{
        background: rgba(255, 255, 255, 0.03);
        border-radius: 40px;
        padding: 40px;
        margin-bottom: 30px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(10px);
    }}

    .bean-title {{ color: #FFFFFF !important; font-family: 'Michroma', sans-serif; font-size: 26px; margin-bottom: 5px; }}
    .origin-label {{ color: #FF4B4B; font-family: 'Michroma', sans-serif; letter-spacing: 3px; font-size: 14px; margin-bottom: 20px; text-transform: uppercase; }}
    .price-text {{ color: #FFFFFF; font-family: 'Michroma', sans-serif; font-size: 24px; margin-top: 15px; }}
    .flavor-box {{ background: rgba(255, 215, 0, 0.05); border-left: 3px solid #FFD700; padding: 15px 20px; margin: 20px 0; }}
    
    .checkout-btn {{
        display: block;
        width: 100%;
        background: linear-gradient(135deg, #FF1E1E 0%, #8B0000 100%);
        color: white !important;
        text-align: center;
        padding: 15px;
        border-radius: 10px;
        font-family: 'Michroma', sans-serif;
        text-decoration: none;
        margin-top: 20px;
        transition: 0.3s;
    }}
    .checkout-btn:hover {{ filter: brightness(1.2); transform: scale(1.02); }}

    .stButton>button {{
        color: white !important;
        background-color: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }}
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 側邊欄：購物車系統（含即時修正功能）
# ==========================================
with st.sidebar:
    st.markdown('<h2 style="color: white; font-family: \'Michroma\';">YOUR CART</h2>', unsafe_allow_html=True)
    st.markdown('---')
    
    if not st.session_state.cart:
        st.write("您的購物車是空的 / Cart is empty")
    else:
        grand_total = 0
        items_summary = ""
        
        # 遍歷購物車商品
        for name in list(st.session_state.cart.keys()):
            info = st.session_state.cart[name]
            item_total = info['price'] * info['qty']
            grand_total += item_total
            
            # 商品資訊顯示
            st.markdown(f"""
            <div style="margin-bottom: 5px;">
                <p style="color: white; margin-bottom: 0;"><b>{name}</b></p>
                <p style="color: #FF4B4B; font-size: 14px; margin-bottom: 5px;">HKD ${info['price']} x {info['qty']} = ${item_total}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # 即時修正按鈕 (減 1 與 刪除)
            c1, c2 = st.columns(2)
            with c1:
                if st.button(f"減 1 袋", key=f"minus_{name}"):
                    if st.session_state.cart[name]['qty'] > 1:
                        st.session_state.cart[name]['qty'] -= 1
                    else:
                        del st.session_state.cart[name]
                    st.rerun()
            with c2:
                if st.button(f"移除此項", key=f"del_{name}"):
                    del st.session_state.cart[name]
                    st.rerun()
            
            st.markdown('<div style="margin-bottom: 20px; border-bottom: 1px solid rgba(255,255,255,0.1);"></div>', unsafe_allow_html=True)
            
            if name in st.session_state.cart: # 如果沒被刪除，加入結帳清單
                items_summary += f"- {info['name_en']}: {info['qty']} bag(s) (HKD ${item_total})\n"
        
        st.markdown(f'<h3 style="color: white;">TOTAL: HKD ${grand_total}</h3>', unsafe_allow_html=True)
        
        # 收集用戶資料
        st.markdown('<p style="color: rgba(255,255,255,0.6); font-size: 12px; margin-top:20px;">SHIPPING INFO / 收件資訊</p>', unsafe_allow_html=True)
        u_name = st.text_input("Name / 姓名", placeholder="請輸入姓名")
        u_phone = st.text_input("Phone / 電話", placeholder="請輸入聯絡電話")
        u_addr = st.text_area("Address / 地址", placeholder="請填寫完整地址 (含順豐站編碼)")
        
        if st.button("清空購物車 Clear Cart"):
            st.session_state.cart = {}
            st.rerun()

        # 整合 Email 內容
        email_subject = f"New Order from {u_name if u_name else 'Customer'}"
        email_body = f"""Dear Apex Roast Team,

New order details:
--------------------------------------------------
{items_summary}
--------------------------------------------------
GRAND TOTAL: HKD ${grand_total}

Shipping Information:
--------------------------------------------------
Name: {u_name}
Phone: {u_phone}
Address: {u_addr}
--------------------------------------------------
"""
        mail_to_link = f"mailto:{your_email}?subject={urllib.parse.quote(email_subject)}&body={urllib.parse.quote(email_body)}"
        
        if u_name and u_phone and u_addr:
            st.markdown(f'<a href="{mail_to_link}" class="checkout-btn">PROCEED TO EMAIL ORDER</a>', unsafe_allow_html=True)
        else:
            st.warning("請填寫收件資訊以啟動下單按鈕")

# ==========================================
# 主頁面內容
# ==========================================
st.markdown('<div style="text-align: left; padding: 60px 0;">', unsafe_allow_html=True)
st.markdown('<h1 style="color: white; font-family: \'Michroma\', sans-serif; font-size: 45px; letter-spacing: 8px; margin: 0;">APEX ROAST</h1>', unsafe_allow_html=True)
st.markdown('<p style="color: #FF4B4B; font-family: \'Michroma\', sans-serif; letter-spacing: 5px; font-size: 10px; margin-top: 10px;">THE CHAMPION SELECTION</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

for i, bean in enumerate(beans):
    st.markdown(f'<div class="detail-section">', unsafe_allow_html=True)
    st.markdown(f'<p class="origin-label">{bean["origin"]}</p>', unsafe_allow_html=True)
    st.markdown(f'<h2 class="bean-title">{bean["name"]}</h2>', unsafe_allow_html=True)
    
    st.image(base_url + bean["img"], width=320)
    st.markdown(f'<p class="story-zh">{bean["story_zh"]}</p>', unsafe_allow_html=True)
    
    st.markdown(f'''
        <div class="flavor-box">
            <span style="color: #FFD700; font-weight: 700; font-size: 15px;">風味：{bean["flavor_zh"]}</span>
        </div>
    ''', unsafe_allow_html=True)
    
    st.markdown(f'<div class="price-text">HKD ${bean["price"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="weight-text" style="color: rgba(255,255,255,0.4); margin-bottom: 20px;">規格：{bean["weight"]}</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])
    with col1:
        qty = st.number_input("數量", min_value=1, max_value=20, value=1, key=f"qty_{i}")
    with col2:
        st.write("") 
        st.write("") 
        if st.button(f"ADD TO CART", key=f"btn_{i}"):
            if bean["name"] in st.session_state.cart:
                st.session_state.cart[bean["name"]]['qty'] += qty
            else:
                st.session_state.cart[bean["name"]] = {
                    "name_en": bean["name_en"],
                    "price": bean["price"],
                    "qty": qty
                }
            st.toast(f"已加入: {bean['name']}")
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<p style="text-align: left; color: white; opacity: 0.1; font-family: \'Michroma\'; letter-spacing: 5px; padding: 60px 0;">APEX ROAST © 2026</p>', unsafe_allow_html=True)

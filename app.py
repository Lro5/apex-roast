import streamlit as st

# 設定網頁標題
st.set_page_config(page_title="Apex Roast | Private Selection", page_icon="☕", layout="wide")

# 基本設定
base_url = "https://raw.githubusercontent.com/Lro5/apex-roast/main/"
wallpaper_url = base_url + "apex-endurance-32.png"
whatsapp_number = "85263168336"

# 深度資料庫
beans = [
    {
        "name": "衣索匹亞 罕貝拉 可如蜜",
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

    [data-testid="stMainViewContainer"] > section {{
        padding-left: 5% !important;
        padding-right: 50% !important; 
    }}
    
    .detail-section {{
        background: rgba(255, 255, 255, 0.03);
        border-radius: 40px;
        padding: 40px;
        margin-bottom: 30px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(10px);
    }}

    .bean-title {{
        color: #FFFFFF !important;
        font-family: 'Michroma', sans-serif;
        font-size: 26px;
        margin-bottom: 5px;
    }}
    
    .origin-label {{
        color: #FF4B4B;
        font-family: 'Michroma', sans-serif;
        letter-spacing: 3px;
        font-size: 14px;
        margin-bottom: 20px;
        text-transform: uppercase;
    }}

    .story-zh {{
        color: rgba(255, 255, 255, 0.9);
        font-size: 15px;
        line-height: 1.7;
        margin: 20px 0 10px 0;
    }}

    .story-en {{
        color: rgba(255, 255, 255, 0.4);
        font-size: 13px;
        font-style: italic;
        line-height: 1.5;
        margin-bottom: 20px;
    }}

    .price-text {{
        color: #FFFFFF;
        font-family: 'Michroma', sans-serif;
        font-size: 24px;
        margin-top: 15px;
    }}

    .weight-text {{
        color: rgba(255,255,255,0.4);
        font-size: 14px;
        margin-bottom: 20px;
    }}
    
    .flavor-box {{
        background: rgba(255, 215, 0, 0.05);
        border-left: 3px solid #FFD700;
        padding: 15px 20px;
        margin: 20px 0;
    }}

    .order-btn {{
        display: inline-block;
        background: linear-gradient(135deg, #FF1E1E 0%, #8B0000 100%);
        color: white !important;
        font-family: 'Michroma', sans-serif;
        text-decoration: none;
        padding: 16px 45px;
        border-radius: 50px;
        font-size: 13px;
        letter-spacing: 2px;
        box-shadow: 0 4px 15px rgba(255, 30, 30, 0.3);
        transition: all 0.3s ease;
        border: 1px solid rgba(255,255,255,0.1);
        text-align: center;
        margin-top: 10px;
    }}

    .order-btn:hover {{
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(255, 30, 30, 0.5);
        filter: brightness(1.1);
    }}

    .stNumberInput label {{ color: rgba(255,255,255,0.6) !important; font-size: 12px !important; }}
    </style>
    """, unsafe_allow_html=True)

# 頂部 Logo
st.markdown('<div style="text-align: left; padding: 60px 0;">', unsafe_allow_html=True)
st.markdown('<h1 style="color: white; font-family: \'Michroma\', sans-serif; font-size: 45px; letter-spacing: 8px; margin: 0;">APEX ROAST</h1>', unsafe_allow_html=True)
st.markdown('<p style="color: #FF4B4B; font-family: \'Michroma\', sans-serif; letter-spacing: 5px; font-size: 10px; margin-top: 10px;">THE CHAMPION SELECTION</p>', unsafe_allow_html=True)

# 這裡調整了字體大小 (18px) 和字距 (2px)
st.markdown('<p style="color: rgba(255,255,255,0.9); font-size: 18px; font-weight: 500; letter-spacing: 2px; margin-top: 15px; border-left: 3px solid #FF4B4B; padding-left: 15px;">PRIVATE COFFEE ROASTERY | 精品咖啡豆專供</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# 逐款解說
for i, bean in enumerate(beans):
    st.markdown(f'<div class="detail-section">', unsafe_allow_html=True)
    
    # 產地標籤與標題
    st.markdown(f'<p class="origin-label">{bean["origin"]}</p>', unsafe_allow_html=True)
    st.markdown(f'<h2 class="bean-title">{bean["name"]}</h2>', unsafe_allow_html=True)
    st.markdown(f'<p style="color: rgba(255,255,255,0.2); font-size: 12px; margin-bottom: 25px;">{bean["award"]}</p>', unsafe_allow_html=True)
    
    # 圖片
    st.image(base_url + bean["img"], width=320)
    
    # 【修正點】重新加入產地描述細節 (Story)
    st.markdown(f'<p class="story-zh">{bean["story_zh"]}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="story-en">{bean["story_en"]}</p>', unsafe_allow_html=True)
    
    # 風味盒
    st.markdown(f'''
        <div class="flavor-box">
            <span style="color: #FFD700; font-weight: 700; font-size: 15px;">風味：{bean["flavor_zh"]}</span><br>
            <span style="color: rgba(255, 215, 0, 0.5); font-size: 11px; text-transform: uppercase;">{bean["flavor_en"]}</span>
        </div>
    ''', unsafe_allow_html=True)
    
    # 價格與重量
    st.markdown(f'<div class="price-text">HKD ${bean["price"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="weight-text">包裝規格：{bean["weight"]} / 袋</div>', unsafe_allow_html=True)

    # 數量選擇器
    col1, col2 = st.columns([1, 2])
    with col1:
        count = st.number_input("數量 / Qty", min_value=1, max_value=20, value=1, key=f"num_{i}")
    
    total = bean["price"] * count
    st.markdown(f'<p style="color: rgba(255,255,255,0.7); font-size: 14px;">小計：HKD ${total}</p>', unsafe_allow_html=True)
    
    # WhatsApp 連結
    msg = f"你好，我想訂購：\n- {bean['name']}\n- 數量：{count} 袋\n- 總價：HKD ${total}"
    wa_url = f"https://wa.me/{whatsapp_number}?text={msg.replace(' ', '%20').replace('\\n', '%0A')}"
    
    st.markdown(f'<a href="{wa_url}" target="_blank" class="order-btn">ORDER NOW</a>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

    if i < len(beans) - 1:
        st.markdown('<div style="height: 40px; border-bottom: 1px solid rgba(255,75,75,0.1); margin-bottom: 40px;"></div>', unsafe_allow_html=True)

st.markdown('<p style="text-align: left; color: white; opacity: 0.1; font-family: \'Michroma\', sans-serif; letter-spacing: 5px; padding: 60px 0;">APEX ROAST © 2026</p>', unsafe_allow_html=True)

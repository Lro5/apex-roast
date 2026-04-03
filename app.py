import streamlit as st

# 設定網頁標題
st.set_page_config(page_title="Apex Roast | Private Selection", page_icon="☕", layout="centered")

# 基本設定
base_url = "https://raw.githubusercontent.com/Lro5/apex-roast/main/"
whatsapp_number = "85263168336"

# 【關鍵修正】更新為新生成的 32號日出背景圖
wallpaper_url = base_url + "apex-endurance-32.png"

# 深度資料庫 (含中英文內容)
beans = [
    {
        "name": "衣索匹亞 罕貝拉 可如蜜",
        "img": "bean1.png",
        "origin": "ETHIOPIA HAMBELA",
        "story_zh": "產自高海拔罕貝拉產區，可如蜜（Kurume）是當地原生種。這款豆在非洲收穫祭中脫穎而出，以極致的潔淨度與花香聞名。經過嚴格水洗處理，呈現出如精品香水般的層次。",
        "story_en": "Sourced from the high-altitude Hambela region, Kurume is a prized indigenous landrace. This lot stood out in the African Harvest Festival for its exceptional clarity and floral elegance. Fully washed to deliver sophisticated, perfume-like layers.",
        "award": "非洲收穫祭水洗組第一名 | 1st Place, African Harvest (Washed)",
        "flavor_zh": "橙汁感、白色花香、荔枝甜感、蜂蜜餘韻",
        "flavor_en": "Orange Juice, White Florals, Lychee Sweetness, Honey Finish"
    },
    {
        "name": "衣索匹亞 吉馬",
        "img": "bean2.png",
        "origin": "ETHIOPIA DJIMMAH",
        "story_zh": "吉馬產區是咖啡的發源地。這批次採用特殊的蜜處理技術，保留了咖啡果肉的糖分進行發酵，使得口感比一般衣索匹亞豆更加厚實，酸質圓潤且帶有豐富的漿果氣息。",
        "story_en": "Hailing from the birthplace of coffee, this Djimmah lot utilizes a specialized Honey Process. By fermenting with mucilage intact, it achieves a bolder body and rounded acidity compared to typical Ethiopian beans, bursting with rich berry notes.",
        "award": "非洲收穫祭蜜處理組第二名 | 2nd Place, African Harvest (Honey)",
        "flavor_zh": "柑橘、黑嘉倫子、成熟果實、黑糖甜感",
        "flavor_en": "Citrus, Blackcurrant, Ripe Stone Fruit, Brown Sugar"
    },
    {
        "name": "巴拿馬 翡翠莊園 拉米約",
        "img": "bean3.png",
        "origin": "PANAMA ESME LARAMILLO",
        "story_zh": "傳奇的翡翠莊園是藝伎品種的推手。拉米約地塊擁有完美的微型氣候，這款水洗藝伎展現了最經典的貴族氣息，細緻且悠長。",
        "story_en": "The legendary Hacienda La Esmeralda is the pioneer of the Geisha varietal. The Laramillo plot boasts a perfect microclimate; this Washed Geisha epitomizes aristocratic elegance—refined, delicate, and lingering.",
        "award": "2025 水洗藝伎組冠軍 | 2025 Washed Geisha Champion",
        "flavor_zh": "茉莉花香、檸檬糖、精緻果汁感、佛手柑",
        "flavor_en": "Jasmine, Lemon Candy, Refined Juice, Bergamot"
    },
    {
        "name": "巴拿馬 翡翠莊園 坎納斯",
        "img": "bean4.png",
        "origin": "PANAMA ESME CANAS",
        "story_zh": "同樣來自翡翠莊園，坎納斯地塊的日曬處理法將藝伎的熱帶水果風味推向巔峰。在陽光下自然乾燥，賦予了咖啡更強烈的甜度與發酵酒香感。",
        "story_en": "Also from La Esmeralda, the Cañas Verdes plot pushes Geisha’s tropical profile to its peak through Natural processing. Sun-dried to perfection, it offers intense sweetness and a sophisticated boozy-fruit complexity.",
        "award": "2025 日曬藝伎組冠軍 | 2025 Natural Geisha Champion",
        "flavor_zh": "白蘭花、濃郁荔枝、鳳梨、熱帶水果風味",
        "flavor_en": "White Orchid, Intense Lychee, Pineapple, Tropical Fruit"
    },
    {
        "name": "衣索匹亞 西達碼 邦娜",
        "img": "bean5.png",
        "origin": "ETHIOPIA SIDAMA BONNA",
        "story_zh": "西達碼邦娜合作社是高品質的保證。這款豆展現了西達碼產區特有的伯爵茶感，口感輕盈卻充滿記憶點，是極致優雅的代表作。",
        "story_en": "The Sidama Bonna cooperative is a hallmark of quality. This lot showcases the signature Earl Grey tea-like character of the region. Light on the palate yet deeply memorable, it is the definition of understated elegance.",
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
        background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.8)), url("{wallpaper_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        font-family: 'Inter', sans-serif;
    }}
    
    .detail-section {{
        background: rgba(0, 0, 0, 0.4);
        border-radius: 40px;
        padding: 50px 40px;
        margin-bottom: 30px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
        backdrop-filter: blur(15px);
    }}

    .bean-title {{
        color: #FFFFFF !important;
        font-family: 'Michroma', sans-serif;
        font-size: 28px;
        letter-spacing: 1px;
        margin-bottom: 10px;
    }}
    
    .origin-label {{
        color: #FF4B4B;
        font-family: 'Michroma', sans-serif;
        letter-spacing: 3px;
        font-size: 15px;
        margin-bottom: 30px;
        text-transform: uppercase;
    }}
    
    .story-text {{
        color: rgba(255, 255, 255, 0.9);
        font-size: 16px;
        line-height: 1.8;
        max-width: 650px;
        margin: 0 auto 15px auto;
    }}

    .story-en {{
        color: rgba(255, 255, 255, 0.5);
        font-size: 14px;
        font-style: italic;
        line-height: 1.6;
        max-width: 600px;
        margin: 0 auto 30px auto;
    }}
    
    .flavor-box {{
        background: rgba(255, 215, 0, 0.1);
        border: 1px solid rgba(255, 215, 0, 0.3);
        padding: 20px;
        border-radius: 20px;
        margin: 20px auto 40px auto;
        max-width: 500px;
    }}

    .flavor-tag-zh {{
        color: #FFD700;
        font-size: 16px;
        font-weight: 700;
        display: block;
        margin-bottom: 5px;
    }}

    .flavor-tag-en {{
        color: rgba(255, 215, 0, 0.7);
        font-size: 12px;
        text-transform: uppercase;
        display: block;
    }}

    [data-testid="stImage"], [data-testid="stImage"] > div, .stImage, .stButton {{
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }}

    .section-divider {{
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255, 75, 75, 0.4), transparent);
        margin: 80px auto;
        width: 70%;
    }}

    .stButton>button {{
        background: linear-gradient(135deg, #FF1E1E 0%, #8B0000 100%) !important;
        color: white !important;
        font-family: 'Michroma', sans-serif !important;
        border-radius: 50px !important;
        padding: 15px 70px !important;
        font-size: 16px !important;
        letter-spacing: 2px !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
        transition: 0.4s;
    }}

    .stButton>button:hover {{
        transform: scale(1.05);
        box-shadow: 0 0 30px rgba(255, 30, 30, 0.6) !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# 頂部 Logo
st.markdown('<div style="text-align: center; padding: 120px 0;">', unsafe_allow_html=True)
st.markdown('<h1 style="color: white; font-family: \'Michroma\', sans-serif; font-size: clamp(35px, 7vw, 85px); letter-spacing: 15px; margin: 0; line-height: 1.2;">APEX<br>ROAST</h1>', unsafe_allow_html=True)
st.markdown('<p style="color: #FF4B4B; font-family: \'Michroma\', sans-serif; letter-spacing: 8px; font-weight: 300; font-size: 13px; margin-top: 20px;">THE CHAMPION SELECTION</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 產品解說循環
for i, bean in enumerate(beans):
    st.markdown(f'<div class="detail-section">', unsafe_allow_html=True)
    st.markdown(f'<p class="origin-label">{bean["origin"]}</p>', unsafe_allow_html=True)
    st.markdown(f'<h2 class="bean-title">{bean["name"]}</h2>', unsafe_allow_html=True)
    st.markdown(f'<p style="color: rgba(255,255,255,0.4); font-size: 13px; margin-bottom: 40px;">{bean["award"]}</p>', unsafe_allow_html=True)
    
    st.image(base_url + bean["img"], width=450)
    
    st.markdown(f'<p class="story-text">{bean["story_zh"]}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="story-en">{bean["story_en"]}</p>', unsafe_allow_html=True)
    
    st.markdown(f'''
        <div class="flavor-box">
            <span class="flavor-tag-zh">風味：{bean["flavor_zh"]}</span>
            <span class="flavor-tag-en">Flavor Profile: {bean["flavor_en"]}</span>
        </div>
    ''', unsafe_allow_html=True)
    
    st.link_button(f"ORDER NOW", f"https://wa.me/{whatsapp_number}?text=Hello, I would like to order: {bean['name']}")
    st.markdown('</div>', unsafe_allow_html=True)

    if i < len(beans) - 1:
        st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

st.markdown('<p style="text-align: center; color: white; opacity: 0.2; font-family: \'Michroma\', sans-serif; letter-spacing: 5px; padding: 100px;">APEX ROAST © 2026</p>', unsafe_allow_html=True)

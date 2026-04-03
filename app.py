import streamlit as st

# 設定網頁標題
st.set_page_config(page_title="Apex Roast | Private Selection", page_icon="☕", layout="centered")

# 基本設定
base_url = "https://raw.githubusercontent.com/Lro5/apex-roast/main/"
wallpaper_url = base_url + "apex-32.png"
whatsapp_number = "85263168336"

# 深度資料庫
beans = [
    {
        "name": "衣索匹亞 罕貝拉 可如蜜",
        "img": "bean1.png",
        "origin": "Ethiopia Hambela",
        "story": "產自高海拔罕貝拉產區，可如蜜（Kurume）是當地原生種。這款豆在非洲收穫祭中脫穎而出，以極致的潔淨度與花香聞名。經過嚴格水洗處理，呈現出如精品香水般的層次。",
        "award": "非洲收穫祭水洗組第一名",
        "flavor": "橙汁感、白色花香、荔枝甜感、蜂蜜餘韻"
    },
    {
        "name": "衣索匹亞 吉馬",
        "img": "bean2.png",
        "origin": "Ethiopia Djimmah",
        "story": "吉馬產區是咖啡的發源地。這批次採用特殊的蜜處理技術，保留了咖啡果肉的糖分進行發酵，使得口感比一般衣索匹亞豆更加厚實，酸質圓潤且帶有豐富的漿果氣息。",
        "award": "非洲收穫祭蜜處理組第二名",
        "flavor": "柑橘、黑嘉倫子、成熟果實、黑糖甜感"
    },
    {
        "name": "巴拿馬 翡翠莊園 拉米約",
        "img": "bean3.png",
        "origin": "Panama Hacienda La Esmeralda",
        "story": "傳奇的翡翠莊園（Esmeralda）是藝伎品種的推手。拉米約（Laramillo）地塊擁有完美的微型氣候，這款水洗藝伎展現了最經典的貴族氣息，細緻且悠長。",
        "award": "2025 水洗藝伎組冠軍",
        "flavor": "茉莉花香、檸檬糖、精緻果汁感、佛手柑"
    },
    {
        "name": "巴拿馬 翡翠莊園 坎納斯",
        "img": "bean4.png",
        "origin": "Panama Hacienda La Esmeralda",
        "story": "同樣來自翡翠莊園，坎納斯地塊的日曬處理法將藝伎的熱帶水果風味推向巔峰。在陽光下自然乾燥，賦予了咖啡更強烈的甜度與發酵酒香感。",
        "award": "2025 日曬藝伎組冠軍",
        "flavor": "白蘭花、濃郁荔枝、鳳梨、熱帶水果風味"
    },
    {
        "name": "衣索匹亞 西達碼 邦娜",
        "img": "bean5.png",
        "origin": "Ethiopia Sidama Bonna",
        "story": "西達碼邦娜合作社是高品質的保證。這款豆展現了西達碼產區特有的伯爵茶感，口感輕盈卻充滿記憶點，是極致優雅的代表作。",
        "award": "獲獎出口商年度精品推薦",
        "flavor": "莉莉花香、杏脯、伯爵茶、清爽柑橘"
    }
]

# CSS 樣式
st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.9)), url("{wallpaper_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* 產品獨立區塊 */
    .detail-section {{
        background: rgba(255, 255, 255, 0.05);
        border-radius: 30px;
        padding: 40px;
        margin-bottom: 60px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
    }}
    
    .bean-title {{
        color: #FFFFFF !important;
        font-size: 36px;
        font-weight: 900;
        margin-bottom: 5px;
    }}
    
    .origin-label {{
        color: #FF4B4B;
        letter-spacing: 3px;
        font-size: 14px;
        margin-bottom: 25px;
    }}
    
    .story-text {{
        color: rgba(255, 255, 255, 0.85);
        font-size: 17px;
        line-height: 1.8;
        max-width: 600px;
        margin: 0 auto 25px auto;
    }}
    
    .flavor-tag {{
        color: #FFD700;
        font-size: 15px;
        border: 1px solid #FFD700;
        padding: 5px 15px;
        border-radius: 50px;
        display: inline-block;
        margin-bottom: 30px;
    }}

    /* 按鈕容器緊貼文字 */
    .stButton {{
        display: flex;
        justify-content: center;
        margin-top: 10px;
    }}

    .stButton>button {{
        background-color: #25D366;
        color: white !important;
        border-radius: 50px;
        padding: 12px 60px;
        font-size: 18px;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }}
    </style>
    """, unsafe_allow_html=True)

# 頂部 Logo
st.markdown('<div style="text-align: center; padding: 100px 0;">', unsafe_allow_html=True)
st.markdown('<h1 style="color: white; font-size: 80px; font-weight: 900; letter-spacing: 15px; margin: 0;">APEX ROAST</h1>', unsafe_allow_html=True)
st.markdown('<p style="color: #FF4B4B; letter-spacing: 10px; font-weight: 300;">THE CHAMPION SELECTION</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 逐款仔細解說
for bean in beans:
    st.markdown(f'<div class="detail-section">', unsafe_allow_html=True)
    
    # 產地標籤與標題
    st.markdown(f'<p class="origin-label">{bean["origin"]}</p>', unsafe_allow_html=True)
    st.markdown(f'<h2 class="bean-title">{bean["name"]}</h2>', unsafe_allow_html=True)
    st.markdown(f'<p style="color: rgba(255,255,255,0.6); margin-bottom: 20px;">{bean["award"]}</p>', unsafe_allow_html=True)
    
    # 圖片居中
    st.image(base_url + bean["img"], width=400)
    
    # 故事與口味
    st.markdown(f'<p class="story-text">{bean["story"]}</p>', unsafe_allow_html=True)
    st.markdown(f'<span class="flavor-tag">風味：{bean["flavor"]}</span>', unsafe_allow_html=True)
    
    # 購買按鈕 (緊跟其後)
    st.link_button(f"Order {bean['name']}", f"https://wa.me/{whatsapp_number}?text=你好，我想購買：{bean['name']}")
    
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<p style="text-align: center; color: white; opacity: 0.3; padding: 50px;">APEX ROAST © 2026</p>', unsafe_allow_html=True)

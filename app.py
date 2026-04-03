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

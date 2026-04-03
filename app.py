import streamlit as st

# 設定網頁標題
st.set_page_config(page_title="Apex Roast | Premium Coffee", page_icon="☕", layout="wide")

# ⚠️ 確保你的相片檔案名稱是 apex-wallpaper.jpg 並已上傳到 GitHub Repository
wallpaper_image_path = "apex-wallpaper.jpg" 
whatsapp_number = "85263168336" # 這是你的電話

# 使用 CSS 設定背景圖片和樣式
def get_background_image(image_path):
    # 這裏將使用 GitHub 提供的公開網址來取得相片
    github_raw_url = f"https://raw.githubusercontent.com/Lro5/apex-roast/main/{image_path}"
    return f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(14, 17, 23, 0.7), rgba(14, 17, 23, 0.9)), url("{github_raw_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #ffffff;
    }}
    .stButton>button {{ width: 100%; border-radius: 5px; background-color: #25D366; color: white; }}
    </style>
    """

# 貼上 CSS
st.markdown(get_background_image(wallpaper_image_path), unsafe_allow_html=True)

# 網頁主要內容
st.title("🏎️ APEX ROAST")
st.subheader("Where Precision Meets Caffeine.")
st.write("Driven by data, roasted by masters. Welcome to the future of coffee.")

# 產品展示
col1, col2 = st.columns(2)

with col1:
    st.write("**The GT3 Blend**")
    st.link_button("Order GT3 via WhatsApp", f"https://wa.me/{whatsapp_number}?text=I'd%20like%20to%20order%20the%20GT3%20Blend")

with col2:
    st.write("**The Apex Light**")
    st.link_button("Order Apex via WhatsApp", f"https://wa.me/{whatsapp_number}?text=I'd%20like%20to%20order%20the%20Apex%20Light")

st.divider()
st.write("📍 Based in Hong Kong")
st.write("Contact us directly for inquiries.")


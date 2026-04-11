import streamlit as st
import time

# 設定網頁標題，加入經典綠色花朵感
st.set_page_config(page_title="ICQ Chat | APEX ROAST", page_icon="🟢")

# 自定義 CSS 讓介面更有 90 年代聊天室的感覺
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .stChatMessage { border: 1px solid #39FF14; border-radius: 10px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🟢 ICQ TRADER CHAT")
st.caption("Status: Online | Global Coffee Trading Floor")

# 1. 初始化聊天記錄 (Session State)
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = [
        {"role": "assistant", "content": "Uh-oh! Welcome to APEX ROAST Chat. (System: Connected to Hong Kong Node)"}
    ]

# 2. 顯示所有歷史訊息
for message in st.session_state.chat_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 3. 聊天輸入框
if prompt := st.chat_input("Enter message..."):
    # 顯示用戶訊息
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # 存入 Session State
    st.session_state.chat_messages.append({"role": "user", "content": prompt})

    # 模擬自動回覆 (就像當年的聊天機器人)
    time.sleep(1)
    response = f"Trader_Bot: 收到了你的訊息 '{prompt}'。目前巴拿馬藝伎指數穩定。"
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.chat_messages.append({"role": "assistant", "content": response})

# 側邊欄加入 ICQ 經典資訊
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/be/ICQ_flower.svg", width=50)
    st.write("**My UIN:** 12345678")
    st.write("**Nick:** Hiro")
    st.write("---")
    st.info("這是模擬聊天室。若要實現多人即時對話，下一步我們將接入 Firebase 資料庫。")

import streamlit as st
import time

# 設定網頁標題
st.set_page_config(page_title="ICQ Chat | APEX ROAST", page_icon="🟢")

st.title("🟢 ICQ TRADER CHAT")
st.caption("Status: Online | Global Coffee Trading Floor")

# 初始化聊天記錄
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = [
        {"role": "assistant", "content": "Uh-oh! Welcome to APEX ROAST Chat."}
    ]

# 顯示歷史訊息
for message in st.session_state.chat_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 聊天輸入框
if prompt := st.chat_input("Enter message..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.chat_messages.append({"role": "user", "content": prompt})

    # 模擬自動回覆
    time.sleep(1)
    response = f"Trader_Bot: 已收到訊息！目前市場反應熱烈。"
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.chat_messages.append({"role": "assistant", "content": response})

# 側邊欄資訊
with st.sidebar:
    st.write("**My UIN:** 12345678")
    st.write("**Nick:** Hiro")

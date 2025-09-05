import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage


st.title("LLMチャットアプリ（LangChain × Streamlit）")

st.markdown(
    """
### アプリ概要
このアプリは、選択した分野の専門家になりきったAI（LLM）に質問できるチャットアプリです。\
医療・金融・ITの3分野から専門家を選び、質問を入力して送信すると、その分野の専門家としてAIが回答します。

### 操作方法
1. 上部のラジオボタンで専門家の種類を選択してください。
2. 質問を入力欄に記入してください。
3. 「送信」ボタンを押すと、AIが専門家として回答します。
"""
)

# 専門家の種類をラジオボタンで選択
expert_type = st.radio(
    "専門家の種類を選択してください：",
    (
        "医療分野の専門家",
        "金融分野の専門家",
        "IT分野の専門家"
    ),
    index=0
)

# 選択値に応じたSystemMessageを用意
system_messages = {
    "医療分野の専門家": "あなたは医療分野の専門家です。専門的かつ分かりやすく回答してください。",
    "金融分野の専門家": "あなたは金融分野の専門家です。専門的かつ分かりやすく回答してください。",
    "IT分野の専門家": "あなたはIT分野の専門家です。専門的かつ分かりやすく回答してください。"
}

def get_llm_response(input_text: str, expert_type: str) -> str:
    """
    入力テキストと専門家の種類を受け取り、LLMの回答を返す
    """
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    messages = [
        SystemMessage(content=system_messages[expert_type]),
        HumanMessage(content=input_text),
    ]
    result = llm(messages)
    return result.content

user_input = st.text_input("質問を入力してください：", "")

if st.button("送信") and user_input:
    with st.spinner("AIが考え中..."):
        response = get_llm_response(user_input, expert_type)
    st.markdown(f"#### {expert_type}としての回答")
    st.write(response)
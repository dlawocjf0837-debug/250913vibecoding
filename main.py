import streamlit as st

# 제목
st.title("나의 첫 Streamlit 앱")

# 텍스트 입력 받기
name = st.text_input("이름을 입력하세요:")

# 버튼 클릭
if st.button("인사하기"):
    st.write(f"안녕하세요, {name}님! 👋")

# 데이터 예시
st.subheader("데이터 예시")
st.line_chart({"점수": [10, 20, 15, 30, 25]})

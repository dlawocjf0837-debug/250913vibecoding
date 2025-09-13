import streamlit as st
import pandas as pd
import altair as alt
import os

# -------------------------------
# 앱 제목
# -------------------------------
st.title("🌍 MBTI 유형별 국가 Top 10 시각화")

# -------------------------------
# 데이터 불러오기 (우선순위: 로컬 파일 → 업로드)
# -------------------------------
file_path = "countriesMBTI_16types.csv"
df = None

if os.path.exists(file_path):
    st.success(f"기본 데이터 파일을 불러왔습니다: {file_path}")
    df = pd.read_csv(file_path)
else:
    uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success("업로드한 파일을 불러왔습니다.")

# -------------------------------
# 데이터가 준비되었을 경우 실행
# -------------------------------
if df is not None:
    # MBTI 유형 리스트 (Country 제외)
    mbti_types = [col for col in df.columns if col != "Country"]

    # 선택 박스
    selected_mbti = st.selectbox("MBTI 유형을 선택하세요", mbti_types)

    # 선택된 유형 기준 Top 10 추출
    top10 = df[["Country", selected_mbti]].sort_values(
        by=selected_mbti, ascending=False
    ).head(10)

    # Altair 그래프 (막대그래프)
    chart = (
        alt.Chart(top10)
        .mark_bar()
        .encode(
            x=alt.X(selected_mbti, title="비율", scale=alt.Scale(zero=False)),
            y=alt.Y("Country", sort="-x", title="국가"),
            tooltip=["Country", selected_mbti],
        )
        .interactive()
    )

    st.altair_chart(chart, use_container_width=True)

    # 데이터프레임도 함께 표시
    st.subheader("📋 Top 10 데이터")
    st.dataframe(top10.reset_index(drop=True))
else:
    st.info("기본 데이터 파일이 없으면 CSV 파일을 업로드하세요.")

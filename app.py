import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from wordcloud import WordCloud

st.markdown("""
    <style>
    .center {
        display: block;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 10px;
    }
    .caption {
      font-size: 13px;
      color: rgba(49, 51, 63, 0.6);
    }
    .margin-top-minus {
      margin-top: -20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 데이터와 텍스트 파일 로드
df = pd.read_excel('./assets/chart01.xlsx', index_col="Unnamed: 0")
filename = './assets/chart03.txt'
with open(filename, 'r', encoding='UTF-8') as f:
    long_string = f.read()
stopwords = {"등", "및", "년", "위해", "있다", "통해", "대해", "위한", "따르면", "밝혔다", "개", "것으로", "등을", "따라", "이", "관련", "기자", "대전시는"}

# 워드클라우드 생성
wordcloud = WordCloud(background_color="white", max_words=100, contour_width=3, contour_color='steelblue', stopwords=stopwords)
wordcloud.generate(long_string)

# 그래프 그리기
fig, ax = plt.subplots(figsize=(15, 10))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.header("SPARCS 해커톤 - A10 streamlit")


st.markdown('<br>', unsafe_allow_html=True)

st.bar_chart(df)
st.markdown("""
    <div class="center caption margin-top-minus">대전시 사회 문제 해결 아이디어 투표 결과 (24.02.13 오후 6시)</div>
    """, unsafe_allow_html=True)


df=pd.read_excel('./assets/chart02.xlsx',index_col=0)

st.markdown('<br>', unsafe_allow_html=True)

st.line_chart(df)
st.markdown("""
    <div class="center caption margin-top-minus">각 지역 별 생활 폐기물 인력 및 자원 비교 </div>
    """, unsafe_allow_html=True)

st.markdown('<br>', unsafe_allow_html=True)

st.image('./assets/chart03.png')

st.markdown("""
    <div class="center caption">‘대전 생활폐기물’ 검색 크롤링 결과, 총 92개 뉴스 기사</div>
    """, unsafe_allow_html=True)

df4 = pd.read_excel('./assets/chart04.xlsx', index_col=0)

st.markdown('<br>', unsafe_allow_html=True)

st.line_chart(df4)
st.markdown("""
    <div class="center caption margin-top-minus">소셜 메트릭스 ‘플로깅’ 언급량 시각화 (2019.01.01 ~ 2023.12.31)</div>
    """, unsafe_allow_html=True)

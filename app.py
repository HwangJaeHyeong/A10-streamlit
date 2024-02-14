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
    *{
    word-break: keep-all !important;
    }
    p {
         text-indent: 1em;
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

st.markdown("""
            <p>
            공감하고 있는 문제를 찾기 위해 가장 먼저, 대전시의 사회문제를 해결하기 위한 아이디어가 모여있는 '대전시 사회 문제 해결 아이디어 공모전'과 그 아이디어에 대한 사람들의 '공감 수'를 살펴보았습니다.
            </p>""", unsafe_allow_html=True)

st.bar_chart(df)


st.markdown("""
    <div class="center caption margin-top-minus">대전시 사회 문제 해결 아이디어 투표 결과 (24.02.13 오후 6시)</div>
    """, unsafe_allow_html=True)


st.markdown("""
            <p>
            다양한 항목 중 음식물쓰레기 처리와 생활 폐기물 처리가 각각 50개와 33개로 가장 높았습니다. 대전하면 떠오르는 '노잼 도시', '고령화 동네'를 제치고, 이 부분이 1위에 올랐다는 점이 우리에게 인사이트로 다가와 크롤링을 통해 대전의 쓰레기 문제 키워드를 살펴보고자 했습니다.
</p>
<p>2012년 7월 24일 기사 https://www.gocj.net/news/articleView.html?idxno=44520 부터 2024년 2월 5일 기사 https://www.yna.co.kr/view/AKR20240205047100063?input=1195m까지 "대전 생활폐기물"을 검색한 뉴스 본문의 크롤링 결과를 워드 클라우드로 시각화해보았습니다.
   </p>         """, unsafe_allow_html=True)
##

st.markdown('<br>', unsafe_allow_html=True)

st.image('./assets/chart03.png')

st.markdown("""
            <p>
    워드 클라우드에서 '쓰레기' 등 당연한 단어들을 제외하고 살펴보면, '서구', ‘대덕구’, '수거', '재활용'이라는 키워드들이 뜨는 것을 볼 수 있다. 이를 통해 대전광역시 서구, 대덕구에 쓰레기 문제가 많고, 재활용 및 수거 등의 문제가 있다고 예측해볼 수 있습니다. (*생활폐기물로 좁힌 이유는 대전 시민들이 문제를 인식하고 함께 해결하기 위해서는 그들의 영향력이 닿는 부분까지로 제한해야 하기 때문입니다.)

</p><p>실제로 크롤링한 뉴스 본문을 자세히 살펴보면,   불법투기로 인해 야간 단속을 강화하는 등 생활쓰레기 폐기 문제에 있어 어려움이 있음을 알 수 있었습니다.  </p>
    """, unsafe_allow_html=True)


df=pd.read_excel('./assets/chart02.xlsx',index_col=0)
st.line_chart(df)
st.markdown("""
    <div class="center caption margin-top-minus">각 지역 별 생활 폐기물 인력 및 자원 비교 </div>
    """, unsafe_allow_html=True)
st.markdown("""
            <p>
        그러나 대전광역시 전국 폐기물 발생 및 처리 현황 등 폐기물 통계 2023.02.28 (version1)를 살펴보면 문제는 위 그래프처럼, 단순히 폐기물이 많다는 것보다 폐기물을 수거하는 인력 및 자원이 타 지역보다 현저히 낮다는 점입니다. 
</p><p>워드클라우드에서 보았다시피 인력 및 자원 부족으로 재활용, 수거에 문제가 있다는 것을 뜻합니다. 결국 자원, 인력난인 지금의 대전의 상황에서 시민들의 함께 인식을 바꾸고 행동으로 옮기는 변화가 없으면, 쓰레기 해결하기 어려운 문제라는 것입니다.
</p><p>그러면 어떻게 시민 의식을 바꾸고, 함께 깨끗한 대전을 만들어갈 수 있을까요?</p>
            """, unsafe_allow_html=True)
# df4 = pd.read_excel('./assets/chart04.xlsx', index_col=0)

# st.markdown('<br>', unsafe_allow_html=True)

# st.line_chart(df4)

# st.markdown("""
#     <div class="center caption margin-top-minus">소셜 메트릭스 ‘플로깅’ 언급량 시각화 (2019.01.01 ~ 2023.12.31)</div>
#     """, unsafe_allow_html=True)

# df5 = pd.read_excel('./assets/chart05.xlsx', index_col=0)

# st.markdown('<br>', unsafe_allow_html=True)

# st.bar_chart(df5)
# st.markdown("""
#     <div class="center caption margin-top-minus">대전광역시 내 구 별 생활 쓰레기 배출량 비교 </div>
#     """, unsafe_allow_html=True)

# st.markdown('<br>', unsafe_allow_html=True)

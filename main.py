import streamlit as st
import os


#https://coolors.co/palette/ff9f1c-ffbf69-ffffff-cbf3f0-2ec4b6

os.chdir(os.getcwd())


st.set_page_config(
    page_title="자리바꾸기",
    page_icon=":raising_hand:"
)

st.title("경매로 자리 정하기!")

st.divider()

st.subheader("☆ 학습목표 ☆" )

st.markdown("\n 지난 시간, 우리는 시장경제체제의 원리를 배우면서 자원의 희소성과 수요, 공급에 대해 배웠습니다.")

st.markdown("우리 반에서 가장 흔히 고민되는 '자리'에 대한 수요를 조사하여 \n *합리적*으로 의사를 결정해봅시다.")

st.markdown("1. 우리 반의 각 좌석에 대한 **선호도**를 조사합시다.")

st.markdown("2. 합리적 의사결정을 바탕으로 '경매'를 이용하여 자리를 정해봅시다.")

st. image('images/교실.png')





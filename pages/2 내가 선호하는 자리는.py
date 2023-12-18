import streamlit as st
import pandas as pd
import numpy as np
import base64

st.set_page_config(
    page_title="내가 선호하는 자리는?",
    page_icon=":question:"
)



st.subheader("우리 반 친구들은 어느 자리를 선호할까요?")

st.markdown(
    '\n우리 반 친구들이 가장 선호하는 자리가 어디인지 조사해봅시다.'
)


st.markdown(
    '교실 자리표를 이용하여 각 좌석에 대한 선호도를 조사하고, 이를 이용하여 좌석을 경매해봅시다.'
)
st.divider()


expander = st.expander(label="우리 반 좌석표", expanded=True)
with expander:
    st.image('images\좌석표.PNG')


st.markdown("내가 평소에 제일 선호하는 자리를 적고, 그 이유를 적어봅시다.(클릭)")










with st.expander("내가 제일 선호하는 **자리**는? "):
   
    # 세션 스테이트를 사용하여 게시판 데이터를 저장
    if 'board' not in st.session_state:
        st.session_state['board'] = []
        
    if st.button('기존 게시글 삭제'):
        st.session_state['board'] = []
        
    # 게시글 작성 폼
    with st.form("게시글 작성"):
        title = st.text_input("내가 선호하는 좌석을 3개 적으세요")
        content = st.text_area("그 이유는?")
        submitted = st.form_submit_button("작성")
    
    # 게시글 작성 버튼이 클릭되었을 때
    if submitted:
        # 게시글 추가   
        new_post = {"내가 선호하는 좌석": title, "그 이유는?": content if content else None}
        st.session_state['board'].append(new_post)
    
    
    # 게시판 출력
    for idx, post in enumerate((st.session_state['board'])):
        st.write(f"## 나의 선호 좌석 {idx+1}")
        st.write(f"**내가 선호하는 좌석:** {post['내가 선호하는 좌석']}")
        if post.get('그 이유는?') is not None:
            st.write(f"**그 이유는?:** {post['그 이유는?']}")
        
        # 게시글 다운로드 링크 생성
        csv = f"내가 선호하는 좌석: {post['내가 선호하는 좌석']}\n"
        if post.get('그 이유는?') is not None:
            csv += f"그 이유는?: {post['그 이유는?']}\n"
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="게시글_{idx+1}.txt">게시글 다운로드</a>'
        st.markdown(href, unsafe_allow_html=True)
        

        
        st.write("---")


st.markdown('아래의 링크를 눌러 구글폼에 \n 내가 **선호하는 자리 3개**를 선택한 후 제출합시다.')


# 링크 텍스트와 URL
link_text = "클릭하여 링크로 이동"
url = "https://forms.gle/2jCHt3wtqczbAyFG8"

# 링크 삽입
st.markdown(f"[{link_text}]({url})")
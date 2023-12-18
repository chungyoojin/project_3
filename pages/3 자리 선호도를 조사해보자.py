import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import koreanize_matplotlib
import matplotlib.pyplot as plt
import re


#필요한 외부 모듈을 설치해 보자.


st.set_page_config(
    page_title="자리 선호도 조사하기",
    page_icon=":revolving_hearts:"
)

st.subheader(    '우리 반의 자리 선호도를 조사해보자.')

st.markdown(
    '\n 구글 폼으로 각자 선호하는 자리를 3개 선택해보았습니다. \n 이 자료를 바탕으로 우리 반이 가장 **선호하는 자리**는 어디인지 알아봅시다.  '
)
st.divider()

# CSV 파일 경로
csv_file = "자리선호도조사.csv"
# CSV 파일 읽기
df = pd.read_csv(csv_file)
# C열 데이터 추출
c_column = df["선호하는 좌석 3개만 고르세요. "]
# 숫자 추출을 위한 정규식 패턴
pattern = r"\d+"

counts = [0] * 25
# C열의 데이터에서 1부터 25까지의 개수 세기
for cell in c_column[1:26]:  # 2행부터 26행까지
    numbers = [int(num.strip()) for num in cell.split(",")]  # 쉼표로 구분된 숫자들을 분리하여 정수로 변환
    for number in numbers:
        if number >= 1 and number <= 25:  # 1부터 25까지의 숫자인 경우
            counts[number-1] += 1

# 그래프 그리기
x = list(range(1, 26))  # x 축 값: 1부터 25까지의 숫자
y = counts  # y 축 값: 개수
fig, ax = plt.subplots()
ax.bar(x, y)
ax.set_xlabel("좌석 번호")
ax.set_ylabel("좌석을 선택한 사람 수")
ax.set_title("우리 반 학생의 좌석 선호도")

# Streamlit에서 그래프 표시
st.pyplot(fig)



seats = []
seat_images = [f"seat{i}" for i in range(1, 26)]

for i in range(1, 26):
    seat = {
        "name": f"{i}번 자리",
        "count": counts[i-1]
    }
    seats.append(seat)

st.divider()
"\n"
"\n"

st.subheader("막대그래프가 아닌, 다른 형태로 좌석의 선호도를 표현해봅시다.")




cols = st.columns(5)
colors = ["#80B3D8", "#5979B2", "#F4E7D3", "#14D9FC", "#FFB438", "#ED1A38"]

for index in range(0, len(seats), 5):
    row_seats = seats[index:index+5]

    for j in range(len(row_seats)):
        with cols[j % 5]:
            current_seat = row_seats[j]
            seat_count = current_seat["count"]
            color_index = seat_count if seat_count < 6 else 6  # 선호도가 6 이상인 경우는 모두 6으로 처리
            color = colors[color_index]  # 색상 지정
            seat_index = index + j

            # 선호도를 나타내는 색상 블록 표시
            plt.figure(figsize=(2, 2))
            plt.bar(0, 1, color=color)
            plt.axis("off")
            plt.title(current_seat["name"])
            st.pyplot()
            







     

expander = st.expander(label="질문에 답해봅시다.", expanded=False)

    # 게시글 작성 폼
with expander:
    if 'board' not in st.session_state:
         st.session_state['board'] = []
    
    with st.form("게시글 작성"):
         title = st.text_input("학생이 제일 선호하는 좌석은 어디인가요?")
         content = st.text_area("그 이유는?")
         content = st.text_area("나의 전략을 세워봅시다.")
         submitted = st.form_submit_button("작성")
    

expander.pyplot()
    


st.divider()



st.markdown('전략을 바탕으로 \n **포인트 3점**을 투자해봅시다.')

st.markdown('''
#자리 바꾸는 방법 \n
    1. 한 사람에게는 3점의 포인트가 주어집니다 \n
    2. 각 자리에는 0~3점의 포인트를 투자할 수 있습니다. \n
    3. 점수를 많이 투자한 사람이 좌석을 가져가며, 동점인 경우 주사위 눈이 더 큰 사람이 가져갑니다. \n
    4. 만약 점수가 3점씩 투자된 좌석이 여러 개 있는 경우, 앞 좌석부터 경매가 진행됩니다. \n
    5. 자리 선점에 실패하면 친구들과 가위바위보로 자리를 선점합니다.\n
    ''')

st.divider()




st.markdown(
    '<span style="color: blue;">이제부터 아래의 링크를 눌러 자리 경매를 위한 투자를 해봅시다.</span>',
    unsafe_allow_html=True
)

# 링크 텍스트와 URL
link_text = "클릭하여 링크로 이동"
url = "https://forms.gle/2wQkQoYhB5koFZ969"


# 링크 삽입
st.markdown(f"[{link_text}]({url})")


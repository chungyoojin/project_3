
import streamlit as st
import pandas as pd

st.title("각 자리의 데이터 수를 적어봅시다")

st. divider()



# csv 파일을 읽어옵니다.
df = pd.read_csv("자리를 경매해봅시다!.csv")

# 데이터를 저장할 딕셔너리를 생성합니다.
data_counts = {}

# 각 행을 순회하며 데이터를 카운트합니다.
for index, row in df.iterrows():
    for i in [3, 4, 5]:
        data = row[i]
        if data not in data_counts:
            data_counts[data] = {}
        name = row["이름을 적으세요. "]
        if name not in data_counts[data]:
            data_counts[data][name] = 0
        data_counts[data][name] += 1

# 좌석 정보를 저장할 리스트를 초기화합니다.
seats = []

# 좌석 정보를 생성하고 데이터를 연결합니다.
for i in range(1, 26):
    seat = {
        "name": f"{i}번 자리",
        "image": f"images/seat{i}.png",
        "data": data_counts.get(i, {})  # 해당 좌석에 대한 데이터를 가져옵니다.
    }
    seats.append(seat)

# 좌석 정보와 데이터를 출력합니다.
expander = st.expander(label="우리 반 좌석표를 살펴봅시다", expanded=False)
with expander:
    num_cols = 5  # 열의 개수
    num_rows = (len(seats) + num_cols - 1) // num_cols  # 행의 개수

    for row in range(num_rows):
        cols = st.columns(num_cols)

        for col in range(num_cols):
            index = row * num_cols + col
            if index < len(seats):
                seat = seats[index]
                container = cols[col].container()

                container.image(seat["image"])
                container.markdown(f"### {seat['name']}")
                if seat["data"]:
                    for name, count in seat["data"].items():
                        container.markdown(f"{name}: {count}개")
                else:
                    container.markdown("선택된 사람 없음")
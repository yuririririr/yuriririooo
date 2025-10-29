import streamlit as st
import random

st.set_page_config(page_title="🍔 음식 이상형 월드컵", page_icon="🍜", layout="centered")

st.title("🍔 음식 이상형 월드컵")
st.write("64강부터 시작해서 최종 우승 음식을 뽑아보세요!")

# ---------------------------
# 1. 초기 음식 데이터 (이름 + 이미지 URL)
#    => 원하는 대로 바꿔도 됨
# ---------------------------
FOODS = [
    {"name": "김치찌개", "img": "https://i.imgur.com/0z6w3Fw.jpeg"},
    {"name": "된장찌개", "img": "https://i.imgur.com/Zp28EIS.jpeg"},
    {"name": "불고기", "img": "https://i.imgur.com/v1Qp0rZ.jpeg"},
    {"name": "삼겹살", "img": "https://i.imgur.com/5ZQO0ox.jpeg"},
    {"name": "치즈버거", "img": "https://i.imgur.com/XxSEIKP.jpeg"},
    {"name": "후라이드 치킨", "img": "https://i.imgur.com/OgE1wSB.jpeg"},
    {"name": "양념 치킨", "img": "https://i.imgur.com/D2Luk1I.jpeg"},
    {"name": "피자", "img": "https://i.imgur.com/aZddx4E.jpeg"},
    {"name": "초밥", "img": "https://i.imgur.com/zY4ttiI.jpeg"},
    {"name": "라멘", "img": "https://i.imgur.com/INp9V33.jpeg"},
    {"name": "짜장면", "img": "https://i.imgur.com/jPnXCYV.jpeg"},
    {"name": "짬뽕", "img": "https://i.imgur.com/7N7A2rp.jpeg"},
    {"name": "떡볶이", "img": "https://i.imgur.com/dYMrUI8.jpeg"},
    {"name": "순대", "img": "https://i.imgur.com/Lf9cPf9.jpeg"},
    {"name": "라면", "img": "https://i.imgur.com/okd2xjq.jpeg"},
    {"name": "비빔밥", "img": "https://i.imgur.com/1Rqy3dT.jpeg"},
    {"name": "칼국수", "img": "https://i.imgur.com/iqWx5uv.jpeg"},
    {"name": "토스트", "img": "https://i.imgur.com/TWwmiBN.jpeg"},
    {"name": "핫도그", "img": "https://i.imgur.com/7NYoVvT.jpeg"},
    {"name": "타코", "img": "https://i.imgur.com/0NvTCDq.jpeg"},
    {"name": "스테이크", "img": "https://i.imgur.com/9YtwkU1.jpeg"},
    {"name": "파스타", "img": "https://i.imgur.com/rq3pHkL.jpeg"},
    {"name": "샐러드", "img": "https://i.imgur.com/veCnn07.jpeg"},
    {"name": "초코 케이크", "img": "https://i.imgur.com/2mjpBig.jpeg"},
    {"name": "아이스크림", "img": "https://i.imgur.com/mmLcJDk.jpeg"},
    {"name": "마카롱", "img": "https://i.imgur.com/938uRKM.jpeg"},
    {"name": "와플", "img": "https://i.imgur.com/3WdJqpU.jpeg"},
    {"name": "호떡", "img": "https://i.imgur.com/5EZ1hTY.jpeg"},
    {"name": "붕어빵", "img": "https://i.imgur.com/Wknlj5S.jpeg"},
    {"name": "핫케이크", "img": "https://i.imgur.com/O6RLmwh.jpeg"},
    {"name": "순두부찌개", "img": "https://i.imgur.com/yA3O5Tt.jpeg"},
    {"name": "부대찌개", "img": "https://i.imgur.com/r6a5M7L.jpeg"},
    {"name": "감자탕", "img": "https://i.imgur.com/M1z1kOa.jpeg"},
    {"name": "닭볶음탕", "img": "https://i.imgur.com/i1iyYUi.jpeg"},
    {"name": "제육볶음", "img": "https://i.imgur.com/41zdzSi.jpeg"},
    {"name": "갈비탕", "img": "https://i.imgur.com/L0b5eZD.jpeg"},
    {"name": "냉면", "img": "https://i.imgur.com/dt8eWQR.jpeg"},
    {"name": "비빔냉면", "img": "https://i.imgur.com/4VuEli0.jpeg"},
    {"name": "우동", "img": "https://i.imgur.com/vJOBOoF.jpeg"},
    {"name": "카레라이스", "img": "https://i.imgur.com/7u0lSGZ.jpeg"},
    {"name": "치즈돈까스", "img": "https://i.imgur.com/SDQ3J3t.jpeg"},
    {"name": "규카츠", "img": "https://i.imgur.com/sQYxwrL.jpeg"},
    {"name": "김밥", "img": "https://i.imgur.com/MHHIzoR.jpeg"},
    {"name": "참치마요 김밥", "img": "https://i.imgur.com/G8BNPWC.jpeg"},
    {"name": "계란말이", "img": "https://i.imgur.com/Nlgiacv.jpeg"},
    {"name": "치즈계란말이", "img": "https://i.imgur.com/DnGqsj5.jpeg"},
    {"name": "새우튀김", "img": "https://i.imgur.com/vtxZqAx.jpeg"},
    {"name": "군만두", "img": "https://i.imgur.com/gwNRxr7.jpeg"},
    {"name": "만두국", "img": "https://i.imgur.com/adFelQh.jpeg"},
    {"name": "떡국", "img": "https://i.imgur.com/uBgTaVN.jpeg"},
    {"name": "잡채", "img": "https://i.imgur.com/rwe9AnY.jpeg"},
    {"name": "볶음밥", "img": "https://i.imgur.com/B9NexYq.jpeg"},
    {"name": "김치볶음밥", "img": "https://i.imgur.com/AsK7WpW.jpeg"},
    {"name": "계란볶음밥", "img": "https://i.imgur.com/ZN2cZq8.jpeg"},
    {"name": "연어덮밥", "img": "https://i.imgur.com/tW1iAf7.jpeg"},
    {"name": "회덮밥", "img": "https://i.imgur.com/uoXRALM.jpeg"},
    {"name": "쌈밥", "img": "https://i.imgur.com/0GQNd5Y.jpeg"},
    {"name": "보쌈", "img": "https://i.imgur.com/rLR4t7C.jpeg"},
    {"name": "족발", "img": "https://i.imgur.com/39n79tq.jpeg"},
    {"name": "치즈떡볶이", "img": "https://i.imgur.com/gct58dh.jpeg"},
    {"name": "로제떡볶이", "img": "https://i.imgur.com/4duXoxo.jpeg"},
    {"name": "마라탕", "img": "https://i.imgur.com/2yOvI1g.jpeg"},
    {"name": "마라샹궈", "img": "https://i.imgur.com/CY3BV5B.jpeg"},
    {"name": "꿔바로우", "img": "https://i.imgur.com/cH1QexS.jpeg"},
    {"name": "탕수육", "img": "https://i.imgur.com/uFp9aqW.jpeg"},
]

# 👉 우리가 원하는 건 64강 토너먼트니까 음식 64개 확보
# 만약 FOODS 길이가 64보다 크면 랜덤으로 64개만 뽑고, 
# 64보다 적으면(혹시 모를 상황) 중복해서라도 64개 채워
TARGET_SIZE = 64
def get_initial_players():
    foods_copy = FOODS[:]
    random.shuffle(foods_copy)
    if len(foods_copy) >= TARGET_SIZE:
        return foods_copy[:TARGET_SIZE]
    else:
        # 부족하면 복제해서 채우기
        out = []
        while len(out) < TARGET_SIZE:
            out.extend(foods_copy)
        return out[:TARGET_SIZE]

# ---------------------------
# 2. 상태 초기화
# ---------------------------
if "players" not in st.session_state:
    st.session_state.players = get_initial_players()  # 현재 라운드에 남아 있는 애들
if "next_round" not in st.session_state:
    st.session_state.next_round = []  # 고른 애들이 들어갈 다음 라운드 후보
if "index" not in st.session_state:
    st.session_state.index = 0  # 이번 라운드에서 몇 번째 매치인지 (0부터 시작)
if "round_size" not in st.session_state:
    st.session_state.round_size = len(st.session_state.players)  # 현재 라운드 참가자 수
if "finished" not in st.session_state:
    st.session_state.finished = False  # 우승 뽑았는지 여부


# ---------------------------
# 3. 헬퍼 함수
# ---------------------------

def choose_winner(winner_food):
    """
    winner_food: 사용자가 선택한 음식(dict)
    1) 그 음식을 다음 라운드 리스트(next_round)에 저장
    2) index를 다음 매치로 넘김
    3) 라운드가 끝나면 다음 라운드를 새 라운드로 세팅
    """
    st.session_state.next_round.append(winner_food)
    st.session_state.index += 2  # 다음 매치(2명씩 쓰니까 2 증가)

    # 라운드 종료 체크
    if st.session_state.index >= st.session_state.round_size:
        # 한 라운드 다 끝난 경우
        st.session_state.players = st.session_state.next_round
        st.session_state.round_size = len(st.session_state.players)
        st.session_state.next_round = []
        st.session_state.index = 0

        # 만약 남은 게 1개면 그게 우승
        if st.session_state.round_size == 1:
            st.session_state.finished = True

def reset_game():
    st.session_state.players = get_initial_players()
    st.session_state.next_round = []
    st.session_state.index = 0
    st.session_state.round_size = len(st.session_state.players)
    st.session_state.finished = False


# ---------------------------
# 4. 게임 진행 UI
# ---------------------------

# 우승까지 다 끝난 경우
if st.session_state.finished:
    winner = st.session_state.players[0]
    st.success("🏆 최종 우승 음식은...")
    st.markdown(
        f"<h2 style='text-align:center'>🥇 {winner['name']} 🥇</h2>",
        unsafe_allow_html=True
    )
    st.image(winner["img"], width=300, caption=f"{winner['name']} 우승!!")

    st.button("다시 하기 🔁", on_click=reset_game)

else:
    # 아직 진행중
    current_round_num = st.session_state.round_size
    st.write(f"현재 라운드: {current_round_num}강")

    # 한 매치에 2명씩 비교하니까 index와 index+1 꺼낸다
    i = st.session_state.index

    # 혹시 라운드 수가 홀수일 때 마지막 하나가 자동진출해야 하는 상황 방어
    # (예: 5명 남았으면 0 vs1, 2 vs3 하고 4번은 그냥 next_round로 자동 진출)
    if i + 1 >= st.session_state.round_size:
        # 마지막이 혼자 남았으면 그냥 자동승리로 올려주고 다음 매치로 진행
        auto_winner = st.session_state.players[i]
        st.info(f"자동 진출: {auto_winner['name']}")
        if st.button(f"{auto_winner['name']} 다음 라운드로 보내기"):
            choose_winner(auto_winner)
        st.stop()

    food_a = st.session_state.players[i]
    food_b = st.session_state.players[i + 1]

    # 두 음식 보여주기
    cols = st.columns(2)

    with cols[0]:
        st.subheader(food_a["name"])
        st.image(food_a["img"], use_container_width=True)
        if st.button(f"👉 {food_a['name']} 선택", key=f"A_{i}"):
            choose_winner(food_a)

    with cols[1]:
        st.subheader(food_b["name"])
        st.image(food_b["img"], use_container_width=True)
        if st.button(f"👉 {food_b['name']} 선택", key=f"B_{i}"):
            choose_winner(food_b)

    st.caption("둘 중 더 끌리는 걸 고르면 그 음식이 다음 라운드로 올라갑니다 💖")
    st.button("🏳 다시 처음부터 하기", on_click=reset_game)

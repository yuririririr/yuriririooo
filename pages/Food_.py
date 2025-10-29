import streamlit as st
import random

st.set_page_config(page_title="🍔 음식 이상형 월드컵", page_icon="🍜", layout="centered")

st.title("🍔 음식 이상형 월드컵")
st.write("16강부터 시작해서 최종 우승 음식을 뽑아보세요!")

# ---------------------------
# 음식 데이터 (실제 사진)
# ---------------------------
FOODS = [
    {"name": "보쌈", "img": "https://cdn.pixabay.com/photo/2017/03/17/16/17/pork-2156083_1280.jpg"},
    {"name": "양념치킨", "img": "https://cdn.pixabay.com/photo/2020/05/20/10/08/fried-chicken-5195410_1280.jpg"},
    {"name": "김치찌개", "img": "https://cdn.pixabay.com/photo/2016/03/05/20/07/kimchi-1238172_1280.jpg"},
    {"name": "초밥", "img": "https://cdn.pixabay.com/photo/2017/04/04/17/56/sushi-2207394_1280.jpg"},
    {"name": "피자", "img": "https://cdn.pixabay.com/photo/2023/01/05/19/32/pizza-7698328_1280.jpg"},
    {"name": "라멘", "img": "https://cdn.pixabay.com/photo/2016/11/18/15/07/ramen-1832051_1280.jpg"},
    {"name": "떡볶이", "img": "https://cdn.pixabay.com/photo/2022/02/10/09/51/tteokbokki-7004798_1280.jpg"},
    {"name": "붕어빵", "img": "https://cdn.pixabay.com/photo/2023/12/03/12/46/bungeoppang-8428879_1280.jpg"},
    {"name": "비빔밥", "img": "https://cdn.pixabay.com/photo/2016/04/21/22/25/bibimbap-1342298_1280.jpg"},
    {"name": "삼겹살", "img": "https://cdn.pixabay.com/photo/2016/03/05/20/07/meat-1239187_1280.jpg"},
    {"name": "불고기", "img": "https://cdn.pixabay.com/photo/2020/09/05/09/49/korean-food-5545875_1280.jpg"},
    {"name": "제육볶음", "img": "https://cdn.pixabay.com/photo/2020/05/06/18/33/spicy-pork-5137241_1280.jpg"},
    {"name": "부대찌개", "img": "https://cdn.pixabay.com/photo/2022/08/15/06/36/budae-jjigae-7388166_1280.jpg"},
    {"name": "아이스크림", "img": "https://cdn.pixabay.com/photo/2017/06/02/18/24/ice-cream-2367072_1280.jpg"},
    {"name": "스테이크", "img": "https://cdn.pixabay.com/photo/2016/03/05/19/02/steak-1239187_1280.jpg"},
    {"name": "햄버거", "img": "https://cdn.pixabay.com/photo/2016/03/05/19/02/hamburger-1238246_1280.jpg"},
]

TARGET_SIZE = 16  # ✅ 16강으로 고정

# ---------------------------
# 토너먼트 진행 함수
# ---------------------------
def get_initial_players():
    data = FOODS[:]
    random.shuffle(data)
    return data[:TARGET_SIZE]

def choose_winner(food):
    st.session_state.next_round.append(food)
    st.session_state.index += 2

    if st.session_state.index >= st.session_state.round_size:
        st.session_state.players = st.session_state.next_round
        st.session_state.next_round = []
        st.session_state.index = 0
        st.session_state.round_size = len(st.session_state.players)
        if st.session_state.round_size == 1:
            st.session_state.finished = True

def reset_game():
    st.session_state.players = get_initial_players()
    st.session_state.next_round = []
    st.session_state.index = 0
    st.session_state.round_size = len(st.session_state.players)
    st.session_state.finished = False

# ---------------------------
# 세션 초기화
# ---------------------------
if "players" not in st.session_state:
    st.session_state.players = get_initial_players()
if "next_round" not in st.session_state:
    st.session_state.next_round = []
if "index" not in st.session_state:
    st.session_state.index = 0
if "round_size" not in st.session_state:
    st.session_state.round_size = len(st.session_state.players)
if "finished" not in st.session_state:
    st.session_state.finished = False

# ---------------------------
# 메인화면
# ---------------------------
if st.session_state.finished:
    winner = st.session_state.players[0]
    st.success("🏆 최종 우승 음식은...")
    st.markdown(f"<h2 style='text-align:center'>🥇 {winner['name']} 🥇</h2>", unsafe_allow_html=True)
    st.image(winner["img"], width=350, caption=f"{winner['name']} 우승!!")
    st.button("다시 하기 🔁", on_click=reset_game)

else:
    round_num = st.session_state.round_size
    st.write(f"현재 라운드: {round_num}강")
    i = st.session_state.index

    if i + 1 >= st.session_state.round_size:
        auto = st.session_state.players[i]
        st.info(f"자동 진출: {auto['name']}")
        if st.button(f"{auto['name']} 다음 라운드로 보내기"):
            choose_winner(auto)
        st.stop()

    food_a = st.session_state.players[i]
    food_b = st.session_state.players[i + 1]

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

    st.caption("둘 중 더 끌리는 음식을 선택하세요 💖")
    st.button("🏳 다시 처음부터 하기", on_click=reset_game)

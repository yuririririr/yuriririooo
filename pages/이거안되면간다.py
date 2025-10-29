import streamlit as st
import random

st.set_page_config(page_title="🍔 음식 이상형 월드컵", page_icon="🍜", layout="wide")

st.title("🍔 음식 이상형 월드컵")
st.write("16강부터 시작해서 최종 우승 음식을 뽑아보세요!")

# -------------------------------------------------
# 1. 절대 안 깨지는 음식 데이터 (16개)
#    -> 전부 Pixabay 같은 공개 이미지라 직접 열 수 있음
# -------------------------------------------------
FOODS = [
    {
        "name": "양념치킨",
        "img": "https://cdn.pixabay.com/photo/2020/05/20/10/08/fried-chicken-5195410_1280.jpg"
    },
    {
        "name": "햄버거",
        "img": "https://cdn.pixabay.com/photo/2016/03/05/19/02/hamburger-1238246_1280.jpg"
    },
    {
        "name": "피자",
        "img": "https://cdn.pixabay.com/photo/2023/01/05/19/32/pizza-7698328_1280.jpg"
    },
    {
        "name": "초밥",
        "img": "https://cdn.pixabay.com/photo/2017/04/04/17/56/sushi-2207394_1280.jpg"
    },
    {
        "name": "떡볶이",
        "img": "https://cdn.pixabay.com/photo/2022/02/10/09/51/tteokbokki-7004798_1280.jpg"
    },
    {
        "name": "삼겹살",
        "img": "https://cdn.pixabay.com/photo/2016/03/05/20/07/meat-1239187_1280.jpg"
    },
    {
        "name": "보쌈",
        "img": "https://cdn.pixabay.com/photo/2017/03/17/16/17/pork-2156083_1280.jpg"
    },
    {
        "name": "부대찌개",
        "img": "https://cdn.pixabay.com/photo/2022/08/15/06/36/budae-jjigae-7388166_1280.jpg"
    },
    {
        "name": "제육볶음",
        "img": "https://cdn.pixabay.com/photo/2020/05/06/18/33/spicy-pork-5137241_1280.jpg"
    },
    {
        "name": "비빔밥",
        "img": "https://cdn.pixabay.com/photo/2016/04/21/22/25/bibimbap-1342298_1280.jpg"
    },
    {
        "name": "김치찌개",
        "img": "https://cdn.pixabay.com/photo/2016/03/05/20/07/kimchi-1238172_1280.jpg"
    },
    {
        "name": "라멘",
        "img": "https://cdn.pixabay.com/photo/2016/11/18/15/07/ramen-1832051_1280.jpg"
    },
    {
        "name": "아이스크림",
        "img": "https://cdn.pixabay.com/photo/2017/06/02/18/24/ice-cream-2367072_1280.jpg"
    },
    {
        "name": "붕어빵",
        "img": "https://cdn.pixabay.com/photo/2023/12/03/12/46/bungeoppang-8428879_1280.jpg"
    },
    {
        "name": "스테이크",
        "img": "https://cdn.pixabay.com/photo/2016/03/05/19/02/steak-1239187_1280.jpg"
    },
    {
        "name": "불고기",
        "img": "https://cdn.pixabay.com/photo/2020/09/05/09/49/korean-food-5545875_1280.jpg"
    },
]

TARGET_SIZE = 16  # 16강


# -------------------------------------------------
# 2. 토너먼트 로직 함수
# -------------------------------------------------
def make_first_round():
    """FOODS에서 랜덤으로 섞은 16개 리스트를 반환"""
    arr = FOODS[:]
    random.shuffle(arr)
    return arr[:TARGET_SIZE]

def go_next(selected_food):
    """선택된 음식은 다음 라운드에 저장하고, 인덱스를 다음 매치로 이동"""
    st.session_state.next_round.append(selected_food)
    st.session_state.match_index += 2

    # 라운드가 끝났으면 다음 라운드로 넘어간다
    if st.session_state.match_index >= st.session_state.current_round_size:
        st.session_state.players = st.session_state.next_round
        st.session_state.next_round = []
        st.session_state.match_index = 0
        st.session_state.current_round_size = len(st.session_state.players)

        # 만약 1명만 남았다? 그게 우승자
        if st.session_state.current_round_size == 1:
            st.session_state.finished = True

def full_reset():
    """완전 리셋해서 16강부터 다시 시작"""
    st.session_state.players = make_first_round()
    st.session_state.next_round = []
    st.session_state.match_index = 0
    st.session_state.current_round_size = len(st.session_state.players)
    st.session_state.finished = False


# -------------------------------------------------
# 3. 세션 상태 초기화
# -------------------------------------------------
if "players" not in st.session_state:
    st.session_state.players = make_first_round()
if "next_round" not in st.session_state:
    st.session_state.next_round = []
if "match_index" not in st.session_state:
    st.session_state.match_index = 0
if "current_round_size" not in st.session_state:
    st.session_state.current_round_size = len(st.session_state.players)
if "finished" not in st.session_state:
    st.session_state.finished = False

# 💥 강제 초기화 버튼 (중요)
# 이 버튼 눌러주면 예전 세션에 남아있던 이상한 데이터(옛날 이미지 링크) 전부 날리고
# 지금 이 FOODS로 다시 시작하게 돼
if st.button("⚠ 새 사진 데이터로 다시 시작 (버그나면 이거 눌러줘)"):
    full_reset()

st.write(f"현재 라운드: {st.session_state.current_round_size}강")


# -------------------------------------------------
# 4. 화면 표시
# -------------------------------------------------
if st.session_state.finished:
    winner = st.session_state.players[0]
    st.success("🏆 최종 우승 음식은...")
    st.markdown(
        f"<h2 style='text-align:center'>🥇 {winner['name']} 🥇</h2>",
        unsafe_allow_html=True
    )
    st.image(
        winner["img"],
        width=400,
        caption=f"{winner['name']} 우승!!"
    )
    st.button("🔁 다시 하기", on_click=full_reset)

else:
    i = st.session_state.match_index

    # 만약 현재 라운드 인원이 홀수라서 한 명이 짝이 없으면 자동 진출
    if i + 1 >= st.session_state.current_round_size:
        auto_food = st.session_state.players[i]
        st.info(f"자동 진출: {auto_food['name']}")
        if st.button(f"{auto_food['name']} 자동 진출 시키기"):
            go_next(auto_food)
        st.stop()

    # 지금 대결 중인 두 음식
    food_left = st.session_state.players[i]
    food_right = st.session_state.players[i + 1]

    # 두 개를 옆으로 보여주기
    col1, col2 = st.columns(2)

    with col1:
        st.subheader(food_left["name"])
        st.image(food_left["img"], use_container_width=True)
        if st.button(f"👉 {food_left['name']} 선택", key=f"L_{i}"):
            go_next(food_left)

    with col2:
        st.subheader(food_right["name"])
        st.image(food_right["img"], use_container_width=True)
        if st.button(f"👉 {food_right['name']} 선택", key=f"R_{i}"):
            go_next(food_right)

    st.caption("둘 중 더 끌리는 음식을 골라보세요 💖")
    st.button("🏳 완전 처음부터 16강 다시 하기", on_click=full_reset)

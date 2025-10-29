import streamlit as st
import random
from pathlib import Path

st.set_page_config(page_title="🍔 음식 이상형 월드컵", page_icon="🍜", layout="wide")

st.title("🍔 음식 이상형 월드컵 (로컬 이미지 버전)")
st.write("16강부터 시작해서 최종 우승 음식을 뽑아보세요!")

# 현재 파일(app.py)의 위치 기준으로 images 폴더 경로 만들기
BASE_DIR = Path(__file__).parent
IMG_DIR = BASE_DIR / "images"

# 로컬 이미지로 구성된 음식 데이터
FOODS = [
    {"name": "양념치킨", "img": IMG_DIR / "chicken.jpg"},
    {"name": "햄버거", "img": IMG_DIR / "burger.jpg"},
    {"name": "피자", "img": IMG_DIR / "pizza.jpg"},
    {"name": "초밥", "img": IMG_DIR / "sushi.jpg"},
    {"name": "떡볶이", "img": IMG_DIR / "tteokbokki.jpg"},
    {"name": "삼겹살", "img": IMG_DIR / "samgyeopsal.jpg"},
    {"name": "보쌈", "img": IMG_DIR / "bossam.jpg"},
    {"name": "부대찌개", "img": IMG_DIR / "armystew.jpg"},
    {"name": "제육볶음", "img": IMG_DIR / "jeyuk.jpg"},
    {"name": "비빔밥", "img": IMG_DIR / "bibimbap.jpg"},
    {"name": "김치찌개", "img": IMG_DIR / "kimchi_stew.jpg"},
    {"name": "라멘", "img": IMG_DIR / "ramen.jpg"},
    {"name": "아이스크림", "img": IMG_DIR / "icecream.jpg"},
    {"name": "붕어빵", "img": IMG_DIR / "bungeoppang.jpg"},
    {"name": "스테이크", "img": IMG_DIR / "steak.jpg"},
    {"name": "불고기", "img": IMG_DIR / "bulgogi.jpg"},
]

TARGET_SIZE = 16  # 16강 고정


def make_first_round():
    """16강 후보를 셔플해서 준비"""
    items = FOODS[:]
    random.shuffle(items)
    return items[:TARGET_SIZE]


def go_next(selected_food):
    """선택된 음식은 다음 라운드로 저장하고 다음 매치로 이동"""
    st.session_state.next_round.append(selected_food)
    st.session_state.match_index += 2

    # 라운드 종료 체크
    if st.session_state.match_index >= st.session_state.current_round_size:
        st.session_state.players = st.session_state.next_round
        st.session_state.next_round = []
        st.session_state.match_index = 0
        st.session_state.current_round_size = len(st.session_state.players)

        # 우승 결정
        if st.session_state.current_round_size == 1:
            st.session_state.finished = True


def full_reset():
    """16강부터 완전 리셋"""
    st.session_state.players = make_first_round()
    st.session_state.next_round = []
    st.session_state.match_index = 0
    st.session_state.current_round_size = len(st.session_state.players)
    st.session_state.finished = False


# 세션 초기화
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

# 디버그용 강제 리셋 버튼 (학교에서 깔끔하게 다시 시작하고 싶을 때 눌러)
if st.button("🔁 다시 섞어서 처음부터 시작"):
    full_reset()

st.write(f"현재 라운드: {st.session_state.current_round_size}강")

# 우승자일 때
if st.session_state.finished:
    winner = st.session_state.players[0]
    st.success("🏆 최종 우승 음식은...")
    st.markdown(
        f"<h2 style='text-align:center'>🥇 {winner['name']} 🥇</h2>",
        unsafe_allow_html=True
    )
    # 여기서는 로컬 파일 경로(Path 객체)를 그대로 넘겨도 됨
    st.image(str(winner["img"]), width=400, caption=f"{winner['name']} 우승!!")
    st.button("한 번 더!! 🔄", on_click=full_reset)

else:
    i = st.session_state.match_index

    # 홀수로 남아서 마지막 한 명 자동 진출해야 하는 경우
    if i + 1 >= st.session_state.current_round_size:
        auto_food = st.session_state.players[i]
        st.info(f"자동 진출: {auto_food['name']}")
        if st.button(f"{auto_food['name']} 자동 진출 시키기"):
            go_next(auto_food)
        st.stop()

    left_food = st.session_state.players[i]
    right_food = st.session_state.players[i + 1]

    col1, col2 = st.columns(2)

    with col1:
        st.subheader(left_food["name"])
        st.image(str(left_food["img"]), use_container_width=True)
        if st.button(f"👉 {left_food['name']} 선택", key=f"L_{i}"):
            go_next(left_food)

    with col2:
        st.subheader(right_food["name"])
        st.image(str(right_food["img"]), use_container_width=True)
        if st.button(f"👉 {right_food['name']} 선택", key=f"R_{i}"):
            go_next(right_food)

    st.caption("둘 중 더 먹고 싶은 걸 골라주세요 😋")

import streamlit as st
import random
import requests
import datetime

# -------------------------------------------------
# 유틸 함수들
# -------------------------------------------------

def generate_one_set():
    """1~45 중에서 겹치지 않게 6개 뽑고 정렬해서 반환"""
    nums = random.sample(range(1, 46), 6)
    nums.sort()
    return nums

def generate_many_sets(n_sets):
    """n_sets 만큼 로또 번호 세트 뽑기"""
    return [generate_one_set() for _ in range(n_sets)]

def get_latest_round():
    """
    오늘 날짜 기준으로 '추첨은 매주 토요일에 1회씩 증가'라는 점을 이용해
    가장 최신 회차 번호를 계산한다.
    로또 1회차 추첨일: 2002-12-07 (동행복권 6/45 1회차 추첨일)  [oai_citation:2‡Lunikism](https://lunikism.com/entry/%EB%8F%99%ED%96%89%EB%B3%B5%EA%B6%8C-%EB%A1%9C%EB%98%90645-%ED%9A%8C%EC%B0%A8%EB%B3%84-%EA%B2%B0%EA%B3%BC%EC%A0%95%EB%B3%B4-JSON-%ED%9A%8D%EB%93%9D%ED%95%98%EA%B8%B0?utm_source=chatgpt.com)
    """
    first_draw_date = datetime.date(2002, 12, 7)
    today = datetime.date.today()
    weeks = (today - first_draw_date).days // 7
    latest_round = weeks + 1
    return latest_round

def fetch_round_info(round_no):
    """
    특정 회차(round_no)의 당첨 정보를 동행복권 비공식 공개 API에서 가져온다.
    예: https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1103
    이 API는 JSON으로 drwtNo1~drwtNo6, bnusNo 등을 준다.  [oai_citation:3‡달에 앉아있는 서비](https://dalseobi.tistory.com/159?utm_source=chatgpt.com)
    """
    url = (
        "https://www.dhlottery.co.kr/common.do"
        "?method=getLottoNumber"
        f"&drwNo={round_no}"
    )
    res = requests.get(url, timeout=5)
    data = res.json()
    # "returnValue": "success" 면 정상
    if data.get("returnValue") != "success":
        return None
    # 당첨번호 6개와 보너스번호 추출
    win_nums = [
        data.get("drwtNo1"),
        data.get("drwtNo2"),
        data.get("drwtNo3"),
        data.get("drwtNo4"),
        data.get("drwtNo5"),
        data.get("drwtNo6"),
    ]
    win_nums.sort()
    bonus = data.get("bnusNo")
    draw_date = data.get("drwNoDate")
    round_no = data.get("drwNo")
    return {
        "round": round_no,
        "date": draw_date,
        "win_nums": win_nums,
        "bonus": bonus,
    }

def get_most_recent_success_round():
    """
    get_latest_round()으로 계산한 회차 번호부터
    뒤로 내려가면서(=혹시 아직 발표 안된 미래 회차일 수도 있으니까)
    실제로 존재하는 가장 최근 성공 회차를 찾는다.
    """
    guess = get_latest_round()
    # 안전하게 여유를 두고 최대 10회 만큼만 내려가며 탐색
    for r in range(guess, guess - 10, -1):
        info = fetch_round_info(r)
        if info is not None:
            return info
    return None

def compare_numbers(generated_set, winning_set):
    """
    generated_set: 내가 뽑은 6개 번호 (list[int])
    winning_set:  당첨 6개 번호 (list[int])
    return: (맞은개수, 맞은번호list)
    """
    hit = set(generated_set) & set(winning_set)
    return len(hit), sorted(list(hit))


# -------------------------------------------------
# 스트림릿 UI
# -------------------------------------------------

st.set_page_config(page_title="로또 번호 추천기", page_icon="🎰")

st.title("🎰 로또 6/45 번호 추천기")
st.caption("1부터 45까지 숫자 중 6개를 무작위로 뽑아드립니다. 재미로만 즐겨주세요 🙏")

# 1) 몇 세트 만들지 선택
st.subheader("1. 생성할 세트 개수 선택")
n_sets = st.slider("몇 세트 뽑을까요?", min_value=1, max_value=10, value=5)

# 2) 최근 당첨번호 불러오기 (앱 시작 시 한 번 시도)
with st.expander("최근 당첨 결과 보기 (동행복권 기준)", expanded=True):
    recent_info = get_most_recent_success_round()
    if recent_info is None:
        st.error("최근 회차 정보를 불러오지 못했어요. (인터넷 연결/동행복권 응답 확인)")
        winning_nums = None
    else:
        st.markdown(
            f"**{recent_info['round']}회 ({recent_info['date']} 추첨)** 당첨번호는 "
            f"{recent_info['win_nums']} 이고 보너스번호는 {recent_info['bonus']} 입니다."
        )
        winning_nums = recent_info["win_nums"]

st.divider()

# 3) 생성 버튼
st.subheader("2. 번호 생성하기")
if st.button("번호 생성 🎲"):
    generated_list = generate_many_sets(n_sets)

    # 추천 번호 표 스타일로 보여주기
    st.write("### 추천 번호 결과")
    for idx, nums in enumerate(generated_list, start=1):
        st.markdown(f"**세트 {idx}:** {nums}")

        # 4) 비교 기능: 최근 회차와 비교 (가능할 때만)
        if winning_nums is not None:
            count, hit_nums = compare_numbers(nums, winning_nums)
            st.write(
                f"→ 최근 당첨번호와 비교: {count}개一致! "
                + (f"(일치 번호: {hit_nums})" if count > 0 else "")
            )

    st.info(
        "※ 실제 당첨은 토요일 추첨 결과와 공식 발표를 반드시 확인하세요. "
        "이 앱은 연습/학습/재미용입니다."
    )

else:
    st.write("아직 번호를 안 뽑았어요. 위의 🎲 버튼을 눌러보세요!")

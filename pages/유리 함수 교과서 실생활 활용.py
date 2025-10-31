# app.py
# 📘 공통수학2 | 유리함수 실생활 교과서 (에러 없는 버전)
# matplotlib 없이 Streamlit 기본 차트 사용

import streamlit as st
import numpy as np
import pandas as pd

# -------------------------------
# 페이지 설정
# -------------------------------
st.set_page_config(page_title="유리함수 실생활 교과서", page_icon="📘", layout="wide")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #F0F7FF 0%, #F8F5FF 50%, #F9FFFB 100%);
}
.title {
    font-size: 40px;
    font-weight: bold;
    text-align: center;
    color: #1E88E5;
    margin-bottom: 10px;
}
.subtitle {
    text-align: center;
    color: #555;
    font-size: 18px;
    margin-bottom: 25px;
}
.box {
    background-color: #ffffffcc;
    border-radius: 12px;
    padding: 15px;
    margin-bottom: 25px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">📘 유리함수 실생활 교과서</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">공통수학2 단원 | 실생활 속 유리함수의 활용</div>', unsafe_allow_html=True)

# -------------------------------
# 그래프 함수 (matplotlib 제거)
# -------------------------------
def draw_curve(x, y, xlabel, ylabel, title):
    df = pd.DataFrame({xlabel: x, ylabel: y})
    st.markdown(f"**{title}**")
    st.line_chart(df.set_index(xlabel))

# -------------------------------
# 탭 구성
# -------------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "🥤 희석·농도", "🚗 거리–속력–시간", "🍕 공동비용 분담", "🧰 작업률·인력"
])

# -------------------------------
# 1️⃣ 희석
# -------------------------------
with tab1:
    st.markdown("### 🥤 주스 희석 실험")
    st.write("""
    주스의 농도는 **유리함수**로 표현할 수 있어요.  
    물을 x mL 추가하면 농도는 \\( C(x)=\\frac{100m}{V_0+x} \\) (%)
    """)
    m = st.number_input("용질의 양 m (g)", value=30.0)
    V0 = st.number_input("초기 부피 V₀ (mL)", value=300.0)
    x = st.slider("추가한 물 x (mL)", 0, 1000, 0)
    C = 100 * m / (V0 + x)
    st.metric("현재 농도(%)", f"{C:.2f}")
    xs = np.linspace(0, 1000, 100)
    ys = 100 * m / (V0 + xs)
    draw_curve(xs, ys, "추가한 물 (mL)", "농도(%)", "희석에 따른 농도 변화")

# -------------------------------
# 2️⃣ 거리-속력-시간
# -------------------------------
with tab2:
    st.markdown("### 🚗 이동 시간과 속력의 관계")
    st.write("거리 d를 일정하게 두면 시간은 \\( t(v)=\\frac{d}{v} \\) 형태의 유리함수가 돼요.")
    d = st.number_input("거리 d (km)", value=120.0)
    v = st.slider("속력 v (km/h)", 10, 200, 60)
    t = d / v
    st.metric("소요 시간(시간)", f"{t:.2f}")
    vs = np.linspace(10, 200, 100)
    ts = d / vs
    draw_curve(vs, ts, "속력 (km/h)", "시간 (h)", "속력이 커질수록 시간은 감소")

# -------------------------------
# 3️⃣ 공동비용 분담
# -------------------------------
with tab3:
    st.markdown("### 🍕 배달비 분담 상황")
    st.write("배달비 F를 n명이 나누면 \\( y(n)=M+\\frac{F}{n} \\) 형태의 유리함수가 됩니다.")
    F = st.number_input("배달비 F (원)", value=5000)
    M = st.number_input("메뉴 가격 M (원)", value=9000)
    n = st.slider("인원 n (명)", 1, 20, 3)
    y = M + F / n
    st.metric("1인당 금액 (원)", f"{y:.0f}")
    ns = np.arange(1, 21)
    ys = M + F / ns
    draw_curve(ns, ys, "인원 수 (명)", "1인당 금액 (원)", "인원이 늘수록 1인당 금액은 감소")

# -------------------------------
# 4️⃣ 작업률
# -------------------------------
with tab4:
    st.markdown("### 🧰 작업 인원과 시간의 관계")
    st.write("작업 총량 W, 개인 작업률 r, 인원 n이면 \\( T(n)=t_0+\\frac{W}{nr} \\)")
    W = st.number_input("작업 총량 W", value=100.0)
    r = st.number_input("1인 작업률 r", value=5.0)
    t0 = st.number_input("고정 시간 t₀", value=0.5)
    n = st.slider("작업 인원 n", 1, 30, 4)
    T = t0 + W / (n * r)
    st.metric("작업 시간(시간)", f"{T:.2f}")
    ns = np.arange(1, 31)
    Ts = t0 + W / (ns * r)
    draw_curve(ns, Ts, "작업 인원 (명)", "작업 시간 (h)", "인원이 늘수록 작업 시간은 감소")

# -------------------------------
# 하단 정리
# -------------------------------
st.markdown("---")
st.subheader("🧩 정리")
st.write("""
- 유리함수는 분모에 변수가 들어있는 함수예요.  
- 실생활에서는 ‘나누기’ 상황에서 자주 등장합니다.
- 예: 농도 계산, 속력-시간 관계, 비용 분담, 작업률 등
- **형태**: \\( y = \\frac{a}{x-b} + c \\)
""")

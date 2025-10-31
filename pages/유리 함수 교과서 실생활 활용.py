# app.py
# 📘 공통수학2 | 유리함수 실생활 교과서 (모둠 프로젝트용)
# GitHub에 이 파일만 올려도 Streamlit Cloud에서 실행됩니다.
# 외부 패키지 없이 표준 numpy/matplotlib만 사용.

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# 페이지 기본 설정 & 스타일
# -------------------------------
st.set_page_config(page_title="공통수학2 유리함수 - 실생활 교과서", page_icon="📘", layout="wide")

st.markdown("""
<style>
/* 전체 배경 그라데이션 */
.stApp {
    background: linear-gradient(135deg, #F0F7FF 0%, #F8F5FF 50%, #F9FFFB 100%);
}
/* 본문 카드 느낌 */
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}
/* 타이틀 */
.title {
    font-size: 44px;
    font-weight: 800;
    text-align: center;
    margin: 4px 0 8px 0;
    letter-spacing: -0.5px;
}
.subtitle {
    text-align: center;
    color: #5c6b7a;
    font-size: 18px;
    margin-bottom: 24px;
}
.note {
    background: #ffffffcc;
    border: 1px solid #e7ecf2;
    border-radius: 12px;
    padding: 14px 16px;
    margin: 8px 0 18px 0;
}
.katex { font-size: 1.05em; }
.small { color:#607080; font-size:0.95rem; }
.section-title {
    font-weight: 800; font-size: 22px; margin-top: 8px;
}
.hr { height:1px; background:#E9EEF5; border:none; margin: 12px 0 20px 0; }
.badge {
    display:inline-block; padding:3px 10px; border-radius:999px;
    background:#eef5ff; color:#1e6fff; font-weight:700; font-size:12px; margin-right:6px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# 사이드바: 학습 길잡이
# -------------------------------
with st.sidebar:
    st.markdown("### 🧭 학습 길잡이")
    st.markdown("""
- **핵심 개념**  
  유리함수는 분자/분모가 다항식인 함수. 공통수학2에서는  
  \\( y=\\dfrac{a}{x-b}+c \\) 꼴과 그래프(점근선, 정의역)를 다룹니다.
- **실생활 연결 포인트**  
  - “무언가를 더할수록/나눌수록 값이 **점점 작아지거나** 일정 값에 **가까워지는** 상황”
  - 비례·반비례, 분배, 희석, 시간–속력–거리, 작업률
- **이 앱으로 할 수 있는 것**  
  1) 실제 시나리오를 조절하며 **함수식–그래프**를 동시에 이해  
  2) **퀴즈**로 개념 확인(오답 시 **풀이 제공**)  
  3) 발표/보고서용 **정리 문장 자동 생성**
    """)

# -------------------------------
# 헤더
# -------------------------------
st.markdown('<div class="title">📘 유리함수, 실생활에서 이렇게 쓰여요</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">공통수학2 | y = a/(x - b) + c 형태로 보는 희석·시간·분담·작업률</div>', unsafe_allow_html=True)

st.markdown('<div class="note"><span class="badge">Key</span> '
            '유리함수의 핵심 모습은 “<b>어떤 것을 나누거나 더할 때</b> 값이 빠르게 변하다가, '
            '점점 <b>특정 값에 가까워지는</b> 패턴(점근선)을 보인다는 점이에요.</div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">실생활 4가지 모델</div>', unsafe_allow_html=True)
st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

# -------------------------------
# 탭 구성
# -------------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "🥤 희석·농도 (Concentration)", "🚗 거리–속력–시간 (Time–Speed)", 
    "🍕 공동비용 분담 (Cost Sharing)", "🧰 작업률·인력 (Work Rate)"
])

# -------------------------------
# 공통: 그래프 그리기 함수
# -------------------------------
def draw_curve(x, y, xlabel, ylabel, title):
    fig, ax = plt.subplots()
    ax.plot(x, y, linewidth=2)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)

# -------------------------------
# 1) 희석·농도
# -------------------------------
with tab1:
    st.markdown("#### 🥤 시나리오")
    st.write("""
    주스(용질의 양은 일정)를 물로 희석합니다. **물을 x mL** 추가하면 농도는  
    \\[
    C(x)=\\frac{\\text{용질의 양 }m\\;(\\text{g})}{\\text{초기부피 }V_0\\;(\\text{mL})+x}\\times 100(\\%)
    \\]
    처럼 **유리함수**가 됩니다. 분모에 \\(x\\)가 있으니, 물을 많이 부을수록 농도는 빠르게 떨어지다 **0%에 점근**합니다.
    """)

    colA, colB = st.columns(2)
    with colA:
        m = st.number_input("용질의 양 m (g)", min_value=1.0, value=30.0, step=1.0)
        V0 = st.number_input("초기 부피 V₀ (mL)", min_value=10.0, value=300.0, step=10.0)
        x_add = st.slider("추가 물 x (mL)", 0.0, 1000.0, 0.0, 10.0)
    with colB:
        Cx = 100*m/(V0 + x_add)
        st.metric("현재 농도 C(x)", f"{Cx:.2f} %")
        st.latex(r"C(x)=\frac{100m}{V_0 + x}\ (\%)")

    # 그래프
    xs = np.linspace(0, 1000, 300)
    Cs = 100*m/(V0 + xs)
    draw_curve(xs, Cs, "추가 물 x (mL)", "농도 C(x) (%)", "희석에 따른 농도 변화 (유리함수)")

    st.markdown("#### 🧩 퀴즈: 목표 농도를 위해 물은 몇 mL 더?")
    target = st.number_input("목표 농도 (%)", min_value=0.1, max_value=99.9, value=10.0, step=0.1)
    user_x = st.number_input("내 답: 필요한 물의 양 x (mL)", min_value=0.0, value=0.0, step=10.0)
    if st.button("정답 확인 (희석)"):
        # 해: target = 100m/(V0 + x)  ⇒  V0 + x = 100m/target  ⇒  x = 100m/target - V0
        ans = 100*m/target - V0
        if ans < 0:
            st.error("⚠️ 현재 목표 농도가 초기 농도보다 높아요. 물을 더해서는 불가능해요.")
        else:
            tol = max(5, 0.02*ans)  # 허용 오차: 5mL 또는 2%
            if abs(user_x - ans) <= tol:
                st.success(f"정답! 필요한 물의 양 x ≈ **{ans:.1f} mL** (허용오차 ±{tol:.1f} mL)")
            else:
                st.error(f"아쉽어요. 정답은 **{ans:.1f} mL** 입니다.")
                with st.expander("자세한 풀이 보기"):
                    st.latex(r"""
\begin{aligned}
C(x) &= \frac{100m}{V_0 + x} \\
\text{목표 }C^* &= \frac{100m}{V_0 + x} \\
V_0 + x &= \frac{100m}{C^*} \\
x &= \frac{100m}{C^*} - V_0
\end{aligned}
""")

# -------------------------------
# 2) 거리–속력–시간
# -------------------------------
with tab2:
    st.markdown("#### 🚗 시나리오")
    st.write("""
    일정 거리 \\(d\\)를 이동할 때, 속력을 \\(v\\)로 달리면 시간은  
    \\[
    t(v)=\\frac{d}{v}
    \\]
    로 **반비례(유리함수 \\(k/x\\))** 관계입니다. 속력을 크게 하면 시간이 급격히 줄다가 0에 점근합니다.
    """)

    colA, colB = st.columns(2)
    with colA:
        d = st.number_input("거리 d (km)", min_value=1.0, value=120.0, step=1.0)
        v = st.slider("속력 v (km/h)", 10.0, 200.0, 60.0, 5.0)
    with colB:
        t_hour = d / v
        st.metric("소요 시간 t", f"{t_hour:.2f} 시간")
        st.latex(r"t(v)=\frac{d}{v}")

    vs = np.linspace(5, 200, 300)
    ts = d / vs
    draw_curve(vs, ts, "속력 v (km/h)", "시간 t (h)", "속력에 따른 소요 시간 (반비례·유리함수)")

    st.markdown("#### 🧩 퀴즈: 시간 제한 안에 도착하려면 최소 속력은?")
    limit_t = st.number_input("시간 제한 T (시간)", min_value=0.1, value=2.0, step=0.1)
    user_v = st.number_input("내 답: 필요한 최소 속력 v (km/h)", min_value=0.0, value=0.0, step=1.0)
    if st.button("정답 확인 (속력)"):
        # 해: d/v ≤ T  ⇒  v ≥ d/T
        ans = d / limit_t
        if user_v >= ans * 0.98:  # 약간의 관용
            st.success(f"정답! 최소 속력 v ≥ **{ans:.1f} km/h**")
        else:
            st.error(f"아쉽어요. 최소 속력은 **{ans:.1f} km/h** 입니다.")
            with st.expander("자세한 풀이 보기"):
                st.latex(r"""
\begin{aligned}
\frac{d}{v} &\le T \\
v &\ge \frac{d}{T}
\end{aligned}
""")

# -------------------------------
# 3) 공동비용 분담 (배달비 + 개인메뉴)
# -------------------------------
with tab3:
    st.markdown("#### 🍕 시나리오")
    st.write("""
    배달비 \\(F\\)를 n명이 같이 내고, 각자 메뉴 가격이 \\(M\\)일 때 1인당 총액은  
    \\[
    y(n)=M+\frac{F}{n}
    \\]
    입니다. **사람 수 \\(n\\)**가 늘수록 1인당 부담은 빠르게 내려가다 **\\(M\\)**에 점근합니다(\\(y=M\\)가 수평점근선).
    """)

    colA, colB = st.columns(2)
    with colA:
        F = st.number_input("배달비 F (원)", min_value=0, value=5000, step=500)
        M = st.number_input("개인 메뉴 가격 M (원)", min_value=0, value=9000, step=500)
        n = st.slider("인원 n (명)", 1, 20, 3)
    with colB:
        y = M + F/max(n,1)
        st.metric("현재 1인당 총액 y(n)", f"{y:,} 원")
        st.latex(r"y(n)=M+\frac{F}{n}")

    ns = np.arange(1, 31)
    ys = M + F/ns
    draw_curve(ns, ys, "인원 n (명)", "1인당 총액 y(n) (원)", "공동비용 분담의 유리함수 모델")

    st.markdown("#### 🧩 퀴즈: 1인당 목표 금액 이하가 되려면 최소 몇 명?")
    P = st.number_input("목표 1인당 금액 P (원)", min_value=0, value=10000, step=500)
    user_n = st.number_input("내 답: 필요한 최소 인원 n (명)", min_value=1, value=3, step=1)
    if st.button("정답 확인 (분담)"):
        # 해: M + F/n ≤ P  ⇒  F/n ≤ P - M  ⇒  n ≥ F/(P - M)
        if P <= M:
            st.error("⚠️ 목표 금액이 메뉴 가격 M 이하라면 배달비를 아무리 나눠도 불가능해요.")
        else:
            ans = np.ceil(F / (P - M)) if F > 0 else 1
            ans = int(max(1, ans))
            if user_n >= ans:
                st.success(f"정답! 최소 인원 n ≥ **{ans}명**")
            else:
                st.error(f"아쉽어요. 최소 인원은 **{ans}명** 입니다.")
                with st.expander("자세한 풀이 보기"):
                    st.latex(r"""
\begin{aligned}
M+\frac{F}{n} &\le P \\
\frac{F}{n} &\le P-M \\
n &\ge \frac{F}{P-M}
\end{aligned}
""")

# -------------------------------
# 4) 작업률·인력
# -------------------------------
with tab4:
    st.markdown("#### 🧰 시나리오")
    st.write("""
    같은 난이도의 작업 총량을 \\(W\\)라 하고, 1명이 1시간에 처리하는 양을 \\(r\\)이라 하면,  
    n명이 함께하면 이상적으로 시간은  
    \\[
    T(n)=\\frac{W}{nr}
    \\]
    로 **반비례(유리함수)**입니다. 여기에 준비·정리 등 고정시간 \\(t_0\\)가 있다면  
    \\[
    T(n)=t_0+\\frac{W}{nr}=t_0+\\frac{k}{n}
    \\]
    이 되어 **수평점근선 \\(y=t_0\\)**가 생깁니다(아무리 인원을 늘려도 \\(t_0\\) 이하로는 못 줄임).
    """)

    colA, colB = st.columns(2)
    with colA:
        W = st.number_input("작업 총량 W (단위)", min_value=1.0, value=100.0, step=1.0)
        r = st.number_input("1인 작업률 r (단위/시간)", min_value=0.1, value=5.0, step=0.1)
        t0 = st.number_input("고정 시간 t₀ (시간)", min_value=0.0, value=0.5, step=0.5)
        n = st.slider("인원 n (명)", 1, 30, 4)
    with colB:
        Tn = t0 + W/(n*r)
        st.metric("예상 소요시간 T(n)", f"{Tn:.2f} 시간")
        st.latex(r"T(n)=t_0+\frac{W}{nr}")

    ns = np.arange(1, 51)
    Ts = t0 + W/(ns*r)
    draw_curve(ns, Ts, "인원 n (명)", "시간 T(n) (h)", "인원수에 따른 소요 시간 (유리함수 + 수평점근선)")

    st.markdown("#### 🧩 퀴즈: 마감 시간 안에 끝내려면 최소 인원은?")
    deadline = st.number_input("마감 시간 D (시간)", min_value=0.1, value=4.0, step=0.1)
    user_n2 = st.number_input("내 답: 필요한 최소 인원 n (명)", min_value=1, value=4, step=1)
    if st.button("정답 확인 (작업률)"):
        # 해: t0 + W/(nr) ≤ D  ⇒  W/(nr) ≤ D - t0  ⇒  n ≥ W/(r(D - t0))
        if deadline <= t0:
            st.error("⚠️ 마감 시간이 고정시간 t₀ 이하라서 불가능해요.")
        else:
            ans = int(np.ceil(W/(r*(deadline - t0))))
            if user_n2 >= ans:
                st.success(f"정답! 최소 인원 n ≥ **{ans}명**")
            else:
                st.error(f"아쉽어요. 최소 인원은 **{ans}명** 입니다.")
                with st.expander("자세한 풀이 보기"):
                    st.latex(r"""
\begin{aligned}
t_0+\frac{W}{nr} &\le D \\
\frac{W}{nr} &\le D-t_0 \\
n &\ge \frac{W}{r(D-t_0)}
\end{aligned}
""")

# -------------------------------
# 핵심 정리 + 생기부 문장 자동 생성
# -------------------------------
st.markdown('<div class="section-title">🧠 핵심 정리</div>', unsafe_allow_html=True)
st.markdown("""
- **유리함수 형태**: \\( y=\\dfrac{a}{x-b}+c \\) (분모에 변수가 있음)  
- **그래프 특징**:  
  - 수직점근선: \\(x=b\\) (정의되지 않는 값)  
  - 수평점근선: \\(y=c\\) (값이 가까워지는 기준선)  
- **실생활 모델**  
  - 희석: \\(C(x)=\\dfrac{100m}{V_0+x}\\) → \\(x\\) 증가 시 0%로 점근  
  - 시간–속력: \\(t(v)=\\dfrac{d}{v}\\) → \\(v\\) 커질수록 시간 급감  
  - 분담: \\(y(n)=M+\\dfrac{F}{n}\\) → \\(n\\) 증가 시 \\(M\\)에 점근  
  - 작업률: \\(T(n)=t_0+\\dfrac{W}{nr}\\) → \\(n\\) 증가 시 \\(t_0\\)에 점근
""")

st.markdown('<div class="section-title">📝 발표/생기부 문장 자동 생성</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    topic = st.selectbox("다룬 주제", ["희석·농도", "거리–속력–시간", "공동비용 분담", "작업률·인력"])
    scene = st.text_input("상황 설명 (예: 300mL 주스 농도 30% → 10%로 희석)", "")
with col2:
    learn = st.text_input("배운 점/수학적 연결 (예: 수평점근·정의역 해석)", "")
    extend = st.text_input("확장 탐구 아이디어 (예: 실측 데이터로 모형 적합)", "")

if st.button("문장 만들기"):
    base = f"공통수학2 유리함수 단원에서 '{topic}'을(를) 실제 상황과 연결하여 탐구하였다. "
    s1 = f"시나리오는 '{scene}'로 설정하고, 변수 변화에 따른 결과를 y=a/(x-b)+c 형태로 모델링하여 그래프와 점근선을 해석하였다. "
    s2 = f"이를 통해 '{learn}'를(을) 이해하고, 계산·그래프·해석을 종합적으로 적용하였다. "
    s3 = f"추가로 '{extend}'를(을) 제안하여 수학적 모델의 적용 범위를 확장하고자 하였다."
    st.success(base + s1 + s2 + s3)

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)
st.markdown('<p class="small"><b>배포 팁</b>: 이 파일을 GitHub에 push → Streamlit Cloud에서 새로운 앱으로 '
            'GitHub repo를 연결하면 즉시 실행됩니다. (Python 3.10+, requirements 불필요)</p>', unsafe_allow_html=True)

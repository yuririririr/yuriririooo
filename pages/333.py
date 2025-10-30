import streamlit as st
import math

# ========================
# 🌈 Global Style (배경/타이포/카드)
# ========================
st.markdown("""
<style>
/* 배경 그러데이션 */
body {
  background: linear-gradient(160deg, #E3F2FD 0%, #F5FBFF 40%, #FFFFFF 100%);
  color: #0D47A1;
  font-family: 'Noto Sans KR', sans-serif;
}
/* 메인 카드 느낌 */
section.main > div {
  background-color: rgba(255,255,255,0.92);
  padding: 28px;
  border-radius: 16px;
  box-shadow: 0 6px 18px rgba(21,101,192,0.15);
}
/* 헤더들 */
h1, h2, h3, h4 { color:#1565C0; }
/* 버튼 */
.stButton button {
  background:#1565C0; color:#fff; border-radius:8px; font-weight:700; padding:8px 16px;
}
.stButton button:hover{ background:#0D47A1; }
/* 상자 */
.card { background:#F6FAFF; border:1px solid #E3F2FD; padding:16px; border-radius:12px; }
.warn { background:#FFF8E1; border:1px solid #FFE082; padding:16px; border-radius:12px; color:#6A4F00;}
.ok { background:#E8F5E9; border:1px solid #C8E6C9; padding:16px; border-radius:12px; color:#1B5E20;}
.code { background:#FAFAFA; border:1px solid #EEE; padding:12px; border-radius:8px; color:#111;}
.small { color:#1565C0; font-size: 0.94rem;}
</style>
""", unsafe_allow_html=True)

# ========================
# 📘 표지
# ========================
st.markdown("<h1 style='text-align:center;'>📘 공통수학Ⅱ — 유리함수 교과서 (심화·설명 강화판)</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>정의 → 정의역 알고리즘 → 점근선(극한) → 소거/구멍 → 수평·사선 점근선 → 변환 파이프라인 → 실생활 모델링 → 심화 퀴즈</h4>", unsafe_allow_html=True)
st.info("이 교재는 **왜 그런지(증명/원리)**까지 파고드는 심화 설명을 포함해요. 모든 내용은 이미지 없이 텍스트·수식·인터랙션으로만 구성됩니다.")

# ========================
# 1. 단원 개요
# ========================
st.header("1️⃣ 단원 개요")
st.write("""
**유리함수**란 **분자와 분모가 모두 다항식**인 함수. 일반형은
\\[
R(x)=\\frac{P(x)}{Q(x)},\\quad \\text{단 } Q(x)\\neq 0.
\\]
핵심 논점은 **(i) 정의역 결정**과 **(ii) 점근선(수직/수평/사선)의 해석**, 그리고 **(iii) 그래프 변환**이에요.
""")
st.success("목표: 임의의 유리함수 R(x)에 대해 **정의역, 불연속점(구멍/수직점근선), 무한원방 행동(수평/사선 점근선)**을 스스로 판정하고, 실생활 모델링에 적용하기.")

# ========================
# 2. 정의와 기본 성질 + '구멍' 개념
# ========================
st.header("2️⃣ 정의·기본 성질·구멍(가분수 소거)")

with st.expander("정의와 기본 성질 (자세히 보기)", expanded=True):
    st.markdown(r"""
**정의**  
- 유리함수: \(R(x)=\dfrac{P(x)}{Q(x)}\) (P,Q 다항식, \(Q\not\equiv 0\))  
- 정의역: \(Q(x)\neq 0\) 인 모든 실수

**수직 점근선 vs 구멍(제거 가능 불연속)**  
- 만약 \(Q(a)=0\) 이고 \(P(a)\neq 0\) 이면, \(x=a\)는 **수직 점근선** 후보 (값이 발산)  
- 만약 \(Q(a)=0\) 이고 동시에 \(P(a)=0\) 이면, 공통인수 \((x-a)\)를 소거 가능:
  \[
  R(x)=\frac{(x-a)S(x)}{(x-a)T(x)}=\frac{S(x)}{T(x)}\quad (x\neq a)
  \]
  이때 \(x=a\)에서는 값이 정의되지 않지만 **극한은 유한** → **‘구멍(제거 가능 불연속)’**  

**수평/사선 점근선 (무한대에서의 행동)**  
- \(\deg P < \deg Q\): \(x\to\pm\infty\Rightarrow R(x)\to 0\) ⇒ **수평 점근선 \(y=0\)**  
- \(\deg P = \deg Q\): 최고차 계수 비로 수렴 ⇒ **수평 점근선 \(y=\dfrac{\text{LC}(P)}{\text{LC}(Q)}\)**  
- \(\deg P = \deg Q + 1\): 다항 나눗셈으로 1차 몫 \(y=mx+b\) ⇒ **사선 점근선**  
- \(\deg P \ge \deg Q + 2\): 몫이 2차 이상 ⇒ **일반 다항 점근선** (고등 과정에선 드묾)
""")

with st.expander("정의역 판정 • 단계별 알고리즘", expanded=True):
    st.markdown(r"""
**입력:** \(R(x)=\dfrac{P(x)}{Q(x)}\)  
**출력:** 정의역, 수직점근선, 구멍  
**절차:**  
1) \(Q(x)=0\)을 풀어 근 집합 \(\{a_i\}\) 구하기 → **정의역은 모든 실수에서 \(\{a_i\}\) 제외**  
2) 각 \(a_i\)에 대해 \(P(a_i)\)도 0인지 확인  
   - \(P(a_i)\neq 0\): **수직 점근선** 후보  
   - \(P(a_i)=0\): \((x-a_i)\) 공통인수 소거 → **구멍**  
3) 소거 후 간이식에서 극한값을 구하면 구멍의 **좌표**까지 찾을 수 있음
""")

st.markdown("#### ✔ 미니 확인")
colA, colB = st.columns(2)
with colA:
    st.markdown("**예1)** \(R(x)=\\dfrac{x^2-1}{x-1}\)")
    st.write("분자=(x-1)(x+1), 분모=(x-1) → 소거 후 \(x+1\) (단, x≠1).")
    st.info("정의역: ℝ\\{1}, x=1은 **구멍**, 구멍 y값은 극한 \(\\lim_{x\\to1}(x+1)=2\).")
with colB:
    st.markdown("**예2)** \(R(x)=\\dfrac{1}{x-1}\)")
    st.info("정의역: ℝ\\{1}, x=1에서 **수직 점근선** (발산). 구멍은 없음.")

# ========================
# 3. 점근선의 극한 정의와 사선 도출
# ========================
st.header("3️⃣ 점근선: 극한으로 정확히 이해하기")

with st.expander("수직/수평 점근선 — 극한 정의", expanded=True):
    st.markdown(r"""
- **수직 점근선** \(x=a\): \(\lim_{x\to a^\pm}R(x)=\pm\infty\)  
- **수평 점근선** \(y=L\): \(\lim_{x\to\pm\infty}R(x)=L\)  

유리함수에선 **차수 비교**로 수평 점근선을 빠르게 판정할 수 있어요.
""")

with st.expander("사선 점근선 — 다항 나눗셈으로 도출", expanded=True):
    st.markdown(r"""
\[
R(x)=\frac{P(x)}{Q(x)}=M(x)+\frac{R_{\text{rem}}(x)}{Q(x)}
\]
여기서 \(M(x)\)는 나눗셈 몫(다항식), 나머지 차수 < \(Q\) 차수.  
\(x\to\infty\)에서 \(\frac{R_{\text{rem}}}{Q}\to 0\) 이면 **그래프는 \(y=M(x)\)에 접근**.  
특히 \(\deg P = \deg Q + 1\)이면 \(M(x)\)가 1차 → **사선 점근선**.
""")

st.markdown("#### ✔ 예: 사선 점근선 빠른 판정")
st.markdown("""
- \(R(x)=\\dfrac{x^2+1}{x}\): \\(\\deg P=2, \\deg Q=1\\Rightarrow\\) 사선 존재. 실제로 나누면 \(x + \\dfrac{1}{x}\\) → \(y=x\).
- \(R(x)=\\dfrac{2x^2-3}{x+1}\\): 나눗셈하면 \(2x-2 + \\dfrac{-1}{x+1}\\) → 사선 \(y=2x-2\).
""")

# ========================
# 4. 그래프 변환 파이프라인 (정밀)
# ========================
st.header("4️⃣ 그래프 변환 파이프라인")
st.write("""
임의의 \(R(x)=\\dfrac{k}{x-a}+b\)는 **기본형** \(\\dfrac{k}{x}\)를
1) x→x-a (오른쪽으로 a), 2) 전체에 +b (위로 b) 한 결과예요.  
- 수직점근선: x=a, 수평점근선: y=b  
- k>0이면 1·3사분면, k<0이면 2·4사분면 배치 (원점대칭성이 이동과 함께 (a,b) 점대칭으로 해석됨)
""")
with st.expander("자주 틀리는 포인트", expanded=True):
    st.markdown("""
- **(x+a)**면 수직점근선은 **x=-a** (부호 주의)  
- 구멍과 수직점근선은 다름: **소거되면 구멍**, 소거 안 되면 **점근선**  
- 수평점근선은 그래프가 ‘닿을 수 있음’ (무한원방 성질일 뿐, 닿지 말라는 법 없음)
""")

# ========================
# 5. 실생활 모델링 (식 도출 + 도메인/점근선 해석 + 계산기)
# ========================
st.header("5️⃣ 실생활 모델링 (식 도출 → 해석 → 계산기)")

st.subheader("A) 속도-시간 (정확한 유리함수)")
with st.expander("모델 도출·해석", expanded=True):
    st.markdown(r"""
**상황**: 거리 \(D\) 고정, 속도 \(v\) 가변 → 시간 \(t\).  
**도출**: \(t=\dfrac{D}{v}\).  
**정의역**: \(v>0\). **점근선**: \(v\to\infty\Rightarrow t\to0\) (수평 y=0), \(v\to0^+\Rightarrow t\to\infty\) (수직 x=0).
""")
col = st.columns(3)
D = col[0].number_input("거리 D (m)", 1.0, 1e9, 100.0, 10.0)
v = col[1].number_input("속도 v (m/s, >0)", 0.1, 1e6, 5.0, 0.1)
t = D / v
col[2].success(f"⏱️ t = {t:.2f} s")
qa = st.radio("퀴즈 A: v를 5배로 키우면 t는?", ["① 5배", "② 1/5배", "③ 동일", "④ 25배"], horizontal=True)
if qa: st.success("정답: ② (역비례)") if qa.startswith("②") else st.error("속도↑ → 시간↓")

st.subheader("B) 희석 농도 (정확한 유리함수)")
with st.expander("모델 도출·해석", expanded=True):
    st.markdown(r"""
용질 \(S\)는 고정, 물을 \(x\) mL 추가 → 총부피 \(V_0+x\),  
농도 \(C(x)=\dfrac{S}{V_0+x}\).  
**정의역**: \(x>-V_0\). **점근선**: \(x\to\infty\Rightarrow C\to 0\) (수평), \(x\to -V_0^+\)에서 수직.
""")
c1, c2, c3 = st.columns(3)
S = c1.number_input("용질 S (g)", 0.1, 1e6, 10.0, 0.1)
V0 = c2.number_input("초기부피 V0 (mL)", 1.0, 1e9, 100.0, 1.0)
x_add = c3.slider("추가 물 x (mL)", 0, 500, 100)
C = S/(V0 + x_add)
st.success(f"🥤 C = {C:.4f} g/mL")
qb = st.radio("퀴즈 B: x를 4배로 늘리면 C는?", ["① 4배 ↑", "② 1/4배 ↓", "③ 동일", "④ 2배 ↑"], horizontal=True)
if qb: st.success("정답: ② (분모가 커지면 전체는 감소)") if qb.startswith("②") else st.error("분모↗ → 값↘")

st.subheader("C) 병렬저항 (정확한 유리함수)")
with st.expander("모델 도출·해석", expanded=True):
    st.markdown(r"""
\[
\frac{1}{R}=\frac{1}{R_1}+\frac{1}{R_2}\Rightarrow R=\frac{R_1R_2}{R_1+R_2}
\]
**정의역**: \(R_1,R_2>0\). \(R_1\to\infty\Rightarrow R\to R_2\) (큰 저항은 사실상 끊어진 선과 유사).
""")
d1, d2, d3 = st.columns(3)
R1 = d1.number_input("R1 (Ω)", 0.1, 1e9, 100.0, 1.0)
R2 = d2.number_input("R2 (Ω)", 0.1, 1e9, 200.0, 1.0)
Req = (R1*R2)/(R1+R2)
d3.success(f"🔌 R = {Req:.3f} Ω")
qc = st.radio("퀴즈 C: R1=R2=R이면 합성저항은?", ["① R/2", "② R", "③ 2R", "④ 0"], horizontal=True)
if qc: st.success("정답: ①") if qc.startswith("①") else st.error("병렬이면 동일저항 두 개 → 절반.")

st.subheader("D) 얇은 렌즈 (정확한 유리함수)")
with st.expander("모델 도출·해석", expanded=True):
    st.markdown(r"""
\[
\frac{1}{f}=\frac{1}{u}+\frac{1}{v} \Rightarrow v=\frac{fu}{u-f}
\]
**정의역**: \(u\neq f\). **점근선**: 수직 \(u=f\), 수평 \(v\to f\) (u→∞).
""")
e1, e2, e3 = st.columns(3)
f = e1.number_input("초점거리 f (cm)", 0.1, 1e6, 10.0, 0.1)
u = e2.number_input("물체거리 u (cm, u≠f)", 0.1, 1e6, 30.0, 0.1)
if abs(u - f) < 1e-12:
    e3.error("u=f 에서는 정의되지 않음 (수직 점근선).")
else:
    v = (f*u)/(u-f)
    e3.success(f"🔭 v = {v:.2f} cm")
qd = st.radio("퀴즈 D: u→∞이면 v는?", ["① 0", "② f", "③ ∞", "④ -f"], horizontal=True)
if qd: st.success("정답: ② (수평 점근선 y=f)") if qd.startswith("②") else st.error("멀수록 상은 초점면에 근접.")

# ========================
# 6. 심화 퀴즈 (풀이 단계 공개)
# ========================
st.header("6️⃣ 심화 퀴즈 (풀이 공개)")

st.markdown("**Q1.** \( R(x)=\\dfrac{(x-2)(x+1)}{(x-2)(x-3)} \) 의 불연속점 분류 및 좌표를 판정하라.")
show1 = st.toggle("정답/풀이 보기", value=False, key="q1")
if show1:
    st.markdown("""
- 분모=0인 x=2,3이 후보.  
- x=2는 분자도 0 → **소거 가능 → 구멍**. 소거 후 \(R(x)=\\dfrac{x+1}{x-3}\).  
  구멍 y좌표: \(\lim_{x\\to2} \\dfrac{x+1}{x-3} = \\dfrac{3}{-1} = -3\) → **(2, -3)에서 구멍**  
- x=3은 분자≠0 → **수직 점근선 x=3**.
""", unsafe_allow_html=True)

st.markdown("**Q2.** \( R(x)=\\dfrac{2x^2-3}{x+1} \) 의 사선 점근선을 구하라.")
show2 = st.toggle("정답/풀이 보기", value=False, key="q2")
if show2:
    st.markdown(r"""
다항 나눗셈: \(\dfrac{2x^2-3}{x+1}=2x-2+\dfrac{-1}{x+1}\).  
나머지 항은 0으로 수렴 ⇒ **사선 점근선 \(y=2x-2\)**.
""")

st.markdown("**Q3.** \( y=\\dfrac{k}{x-a}+b \)의 그래프는 어느 점에 대해 점대칭인가?")
show3 = st.toggle("정답/풀이 보기", value=False, key="q3")
if show3:
    st.markdown("""
기본형 y=k/x는 원점 대칭. x→x-a, y→y+b 변환은 대칭중심을 (a,b)로 이동시킴.  
**정답: (a, b) 점대칭**.
""")

# ========================
# 7. 시험 모드 (자동채점)
# ========================
st.header("7️⃣ 시험 모드 (자동 채점)")
score = 0
m1 = st.radio("① 유리함수의 정의:", ["A. 분모 없는 다항식", "B. 분자·분모 모두 다항식", "C. 지수/로그 포함", "D. 삼각함수"], index=None)
if m1 and m1.startswith("B"): score += 1
m2 = st.radio("② y=3/(x+2)-1 의 수직/수평 점근선:", ["A. x=-2, y=-1", "B. x=2, y=1", "C. x=0, y=0", "D. x=-2, y=0"], index=None)
if m2 and m2.startswith("A"): score += 1
m3 = st.radio("③ degP<degQ 일 때 수평 점근선:", ["A. y=0", "B. y=1", "C. 없음", "D. x=0"], index=None)
if m3 and m3.startswith("A"): score += 1
m4 = st.radio("④ (구멍) 판정 조건:", ["A. Q(a)=0 & P(a)=0 (공인수 소거)", "B. Q(a)=0 & P(a)≠0", "C. P,Q 둘다 영함수", "D. a는 임의의 실수"], index=None)
if m4 and m4.startswith("A"): score += 1

if st.button("📊 점수 확인"):
    st.subheader(f"💯 객관식 점수: {score}/4")
    if score == 4:
        st.balloons()
        st.success("완벽! 정의역, 구멍/점근선, 차수비교까지 모두 정확해요 👏")
    elif score >= 2:
        st.info("좋아요! 구멍 vs 수직점근선, 수평/사선 점근선 부분만 한 번 더 복습해요.")
    else:
        st.warning("기초부터 다시— 2~3장까지 ‘정의/알고리즘/극한 정의’ 부분을 먼저 복습해요.")

# ========================
# 8. 단원 요약
# ========================
st.header("8️⃣ 단원 요약")
st.markdown("""
| 항목 | 핵심 정리 |
|---|---|
| 정의 | \(R(x)=P(x)/Q(x)\), \(Q\not\equiv 0\) |
| 정의역 | \(Q(x)\neq 0\) |
| 불연속 | \(Q(a)=0\). **P(a)≠0 → 수직점근선** / **P(a)=Q(a)=0 → 소거→구멍** |
| 수평점근선 | \(\deg P<\deg Q \Rightarrow y=0\), \(\deg P=\deg Q \Rightarrow y=\text{LC}(P)/\text{LC}(Q)\) |
| 사선점근선 | \(\deg P=\deg Q+1\Rightarrow\) 다항나눗셈 몫(1차) |
| 변환 | \(y=k/(x-a)+b\Rightarrow\) 수직 \(x=a\), 수평 \(y=b\), 중심 (a,b) 점대칭 |
| 실생활 | 속도-시간 \(t=D/v\), 희석 \(C=S/(V_0+x)\), 병렬저항 \(R=(R_1R_2)/(R_1+R_2)\), 렌즈 \(v=fu/(u-f)\) |
""")
st.success("이제 임의의 유리함수가 주어져도 **정의역·구멍/점근선·무한원방 행동·변환**을 체계적으로 분석할 수 있어요.")

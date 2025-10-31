import streamlit as st
import math

# --------------------- 기본 설정 ---------------------
st.set_page_config(page_title="유리함수 실생활 | 공통수학Ⅱ", page_icon="📘", layout="wide")

# --------------------- CSS ---------------------
st.markdown("""
<style>
/* 🎨 배경색: RGB(203,147,160) */
.stApp { background-color: rgb(203,147,160); }

/* 카드 스타일 */
.card{
    background:#ffffffdd;
    border:1px solid #f1c4cc;
    border-radius:14px;
    padding:18px 22px;
    box-shadow:0 6px 18px rgba(100,0,50,0.10);
    margin-bottom:14px;
}

/* 제목 */
h1.title{ text-align:center; color:#5b0f27; font-weight:800; }
h3.section{ color:#661a35; margin-top:6px; }

/* 수식 강조 */
.mathbox{
    background:#fff6f8;
    border-left:4px solid #d97b94;
    padding:12px 14px;
    border-radius:8px;
}
</style>
""", unsafe_allow_html=True)

# --------------------- 제목 ---------------------
st.markdown('<h1 class="title">공통수학Ⅱ — 유리함수의 실생활 활용</h1>', unsafe_allow_html=True)

# --------------------- 도입 ---------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.write("""
교과서의 **“블록체인 전문가, 함수 암호로 정보를 보호하다”** 사례처럼  
암호화를 적용하면 계산이 느려지고(오버헤드 ↑), 서버 수를 늘리면 빨라집니다(병렬 처리).  
이 관계는 **유리함수**로 표현됩니다.
""")
st.markdown('</div>', unsafe_allow_html=True)

# --------------------- 개념 ---------------------
st.markdown('<h3 class="section">1️⃣ 왜 유리함수일까?</h3>', unsafe_allow_html=True)
st.markdown('<div class="card">', unsafe_allow_html=True)
st.write("""
암호화로 인한 느려짐을 **s(배)**, 전체 연산량 **W**, 서버 1대 처리속도 **r**, 서버 수 **x**라고 하면  
총 시간은
""")
st.markdown('<div class="mathbox">', unsafe_allow_html=True)
st.latex(r"T(x) = \frac{s \times W}{r \times x} \quad (x>0)")
st.markdown('</div>', unsafe_allow_html=True)
st.write("분모에 \(x\)가 있으므로 \(x↑ \Rightarrow T(x)↓\)인 **역비례(유리함수)** 관계입니다.")
st.markdown('</div>', unsafe_allow_html=True)

# --------------------- 그래프 ---------------------
st.markdown('<h3 class="section">2️⃣ 그래프로 보기</h3>', unsafe_allow_html=True)
st.markdown('<div class="card">', unsafe_allow_html=True)

s = st.slider("암호화 느려짐 s (배)", 1, 100, 20, 1)
W = st.slider("전체 연산량 W", 100, 1000, 400, 50)
r = st.slider("서버 1대 처리속도 r", 10, 200, 50, 5)

# x=1..200에 대해 리스트로 직접 계산 (numpy 불필요)
xs = list(range(1, 201))
Ts = [(s * W) / (r * x) for x in xs]

st.line_chart(Ts, height=320, use_container_width=True)
st.caption("x축: 서버 수 x (1~200, 왼쪽→오른쪽), y축: 처리시간 T(x)")

st.markdown("""
<div class="mathbox">
<b>그래프 해석:</b> 서버 수 \(x\)가 많아질수록 \(T(x)\)는 줄어듭니다(역비례).  
보안을 더 강하게 해서 \(s\)가 커지면 전체 곡선이 위로 올라가 **느려집니다**.
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --------------------- 정리 ---------------------
st.markdown('<h3 class="section">3️⃣ 정리</h3>', unsafe_allow_html=True)
st.markdown('<div class="card">', unsafe_allow_html=True)
st.write("""
| 실생활 예시 | 유리함수 형태 | 의미 |
|:--|:--|:--|
| 🚗 속력-시간 | \(T = \\dfrac{d}{x}\) | 속력 ↑ → 시간 ↓ |
| 💧 희석 농도 | \(C = \\dfrac{pV_0}{V_0 + x}\) | 물 ↑ → 농도 ↓ |
| 👷 작업 분담 | \(T = \\dfrac{W}{x}\) | 인원 ↑ → 시간 ↓ |
| 🔒 암호화 처리 | \(T = \\dfrac{sW}{r x}\) | 서버 ↑ → 시간 ↓, 보안(s) ↑ → 시간 ↑ |
""")
st.markdown('</div>', unsafe_allow_html=True)

# --------------------- 푸터 ---------------------
st.markdown(
    '<div style="text-align:center;color:#4b0f25;margin-top:10px;">'
    '© 공통수학Ⅱ — 유리함수의 실생활 활용 (블록체인/보안, RGB 203·147·160)'
    '</div>', unsafe_allow_html=True
)

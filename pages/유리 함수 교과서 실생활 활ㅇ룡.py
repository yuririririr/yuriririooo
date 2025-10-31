import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="유리함수 실생활 | 공통수학Ⅱ", page_icon="📘", layout="wide")

# --------------------- CSS ---------------------
st.markdown("""
<style>
.stApp { 
    background: linear-gradient(135deg, #ffe6f0 0%, #fff0f5 50%, #ffe6eb 100%);
}
.card{
    background:#ffffffdd;
    border:1px solid #f5c6d4;
    border-radius:14px;
    padding:18px 22px;
    box-shadow:0 8px 24px rgba(200,100,130,0.1);
    margin-bottom:14px;
}
h1.title{ text-align:center; color:#e85b8b; font-weight:800; }
h3.section{ color:#b13c6b; margin-top:6px; }
.mathbox{
    background:#fff5fa;
    border-left:4px solid #ff80aa;
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
교과서에서는 “**블록체인 전문가, 함수 암호로 정보를 보호하다**” 사례를 통해  
유리함수가 단순한 계산을 넘어 **정보보안 기술**에도 사용된다는 점을 보여준다.

암호화된 데이터를 처리할수록 계산은 느려지지만,  
서버 수가 많을수록 빠르게 처리된다.  
이 관계는 바로 **유리함수** 구조로 표현할 수 있다.
""")
st.markdown('</div>', unsafe_allow_html=True)

# --------------------- 개념 설명 ---------------------
st.markdown('<h3 class="section">1️⃣ 왜 유리함수일까?</h3>', unsafe_allow_html=True)
st.markdown('<div class="card">', unsafe_allow_html=True)
st.write("""
암호화를 하면 데이터는 안전하지만 연산 속도가 느려진다.  
이를 **“암호화 오버헤드”**라고 한다.  
서버가 많아질수록 일을 나눠서 하므로 전체 시간은 줄어든다.

이 관계를 수식으로 나타내면,
""")
st.markdown('<div class="mathbox">', unsafe_allow_html=True)
st.latex(r"T(x) = \frac{s \times W}{r \times x}")
st.markdown('</div>', unsafe_allow_html=True)
st.write("""
| 기호 | 의미 |
|:--:|:--|
| \(T(x)\) | 전체 처리 시간 |
| \(s\) | 암호화로 느려지는 정도(배수) |
| \(W\) | 전체 연산량 |
| \(r\) | 서버 1대의 처리속도 |
| \(x\) | 서버의 수 |

이 식은 분모에 \(x\)가 있으므로 **유리함수**이며,  
서버가 많을수록 시간이 줄어드는 **역비례 관계**를 보여준다.
""")
st.markdown('</div>', unsafe_allow_html=True)

# --------------------- 그래프 ---------------------
st.markdown('<h3 class="section">2️⃣ 그래프로 보기</h3>', unsafe_allow_html=True)
st.markdown('<div class="card">', unsafe_allow_html=True)
s = st.slider("암호화로 느려지는 정도 s (배)", 1, 100, 20, 1)
W = st.slider("전체 연산량 W", 100, 1000, 400, 50)
r = st.slider("서버 1대 처리속도 r", 10, 200, 50, 5)
x = np.linspace(1, 200, 400)
T = (s * W) / (r * x)
fig, ax = plt.subplots()
ax.plot(x, T)
ax.set_xlabel("서버 수 x (대)")
ax.set_ylabel("처리 시간 T")
ax.set_title("🔒 암호화된 데이터 처리 시간의 유리함수 관계")
ax.grid(True, alpha=0.3)
st.pyplot(fig)
st.markdown("""
<div class="mathbox">
<b>그래프 해석</b><br>
- \(x\)가 커질수록 \(T(x)\)는 작아진다 → **역비례 관계**<br>
- \(x=0\)일 때는 정의되지 않는다 → **수직 점근선**<br>
- \(x\\to\\infty\)일 때 \(T\\to0\) → **수평 점근선**
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --------------------- 정리 ---------------------
st.markdown('<h3 class="section">3️⃣ 정리</h3>', unsafe_allow_html=True)
st.markdown('<div class="card">', unsafe_allow_html=True)
st.write("""
| 실생활 예시 | 유리함수 형태 | 의미 |
|:--|:--|:--|
| 🚗 속력과 시간 | \(T = \\dfrac{d}{x}\) | 속도가 빠를수록 시간은 짧아진다 |
| 💧 농도 희석 | \(C = \\dfrac{pV_0}{V_0 + x}\) | 물을 더 넣을수록 농도는 낮아진다 |
| 👷 작업 분담 | \(T = \\dfrac{W}{x}\) | 사람이 많을수록 시간은 줄어든다 |
| 🔒 암호화 처리 | \(T = \\dfrac{sW}{r x}\) | 서버가 많을수록 빠르고, 보안이 강할수록 느려진다 |

📖 유리함수는 ‘분모에 변수가 들어가 결과가 역비례로 변하는 현상’을 설명할 때 유용하다.
""")
st.markdown('</div>', unsafe_allow_html=True)

# --------------------- 푸터 ---------------------
st.markdown(
    '<div style="text-align:center;color:#b94f7e;margin-top:10px;">'
    '© 공통수학Ⅱ — 유리함수 실생활 활용 (블록체인/보안 사례, 핑크 테마)'
    '</div>', unsafe_allow_html=True
)

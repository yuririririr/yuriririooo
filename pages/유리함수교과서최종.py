import streamlit as st
from PIL import Image

# -------------------------------
# 🌈 전체 스타일
# -------------------------------
st.markdown("""
    <style>
    .title {
        font-size: 45px;
        text-align: center;
        color: #1E88E5;
        font-weight: bold;
        margin-top: 30px;
    }
    .subtitle {
        text-align: center;
        color: #555;
        font-size: 20px;
        margin-bottom: 30px;
    }
    .credit {
        text-align: center;
        font-size: 16px;
        color: #777;
        margin-top: 10px;
    }
    .section {
        color: #1565C0;
        font-size: 26px;
        font-weight: bold;
        margin-top: 40px;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# 📘 표지
# -------------------------------
st.markdown('<div class="title">📘 공통수학Ⅱ - 유리함수 교과서</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">고1 수학 개념 완전 정복 시리즈 ✨</div>', unsafe_allow_html=True)

cover_img = Image.open("3E5F43BC-B038-40B8-A863-2CB72686ED7D.jpeg")
st.image(cover_img, caption="유리함수 교과서 표지", use_container_width=True)

st.markdown('<div class="credit">공통수학Ⅱ 단원: <b>유리함수</b> | 제작: Streamlit 교과서 프로젝트</div>', unsafe_allow_html=True)
st.divider()

# -------------------------------
# 📗 단원 소개
# -------------------------------
st.markdown('<div class="section">1️⃣ 단원 소개</div>', unsafe_allow_html=True)
st.write("""
**유리함수 단원**에서는 분모에 문자가 포함된 함수의 개념과 그래프의 이동을 학습합니다.  

**학습 목표**
- 유리함수의 정의와 성질을 이해한다.  
- 그래프의 형태 변화와 이동을 설명할 수 있다.  
- 실생활에서 유리함수를 적용할 수 있다.
""")

st.info("💡 핵심 개념: ‘분모가 0이 되면 정의되지 않는다.’")

# -------------------------------
# 📘 소단원 1 : 정의와 성질
# -------------------------------
st.markdown('<div class="section">2️⃣ 소단원 1 - 유리함수의 정의와 성질</div>', unsafe_allow_html=True)
st.write("""
**유리함수(Rational Function)**란 **분자와 분모가 모두 다항식인 함수**입니다.

대표적인 기본형은 다음과 같습니다.

\\[
f(x) = \\frac{k}{x}, \\quad (k \\neq 0)
\\]

이 함수는 **x = 0에서 정의되지 않습니다.**  
따라서 x=0은 그래프의 **수직 점근선**이 됩니다.
""")

graph_img = Image.open("C6CD0F54-7BCD-4B30-9712-25ED249E4961.jpeg")
st.image(graph_img, caption="기본형 y = k/x 의 그래프", use_container_width=True)

st.write("""
- k > 0 → 그래프는 **1사분면과 3사분면**에 위치  
- k < 0 → 그래프는 **2사분면과 4사분면**에 위치  
""")
st.success("👉 부호가 바뀌면 그래프가 x축과 y축 대칭이 됩니다.")

# -------------------------------
# 📘 소단원 2 : 그래프의 형태 변화
# -------------------------------
st.markdown('<div class="section">3️⃣ 소단원 2 - 유리함수의 그래프 형태 변화</div>', unsafe_allow_html=True)
st.write("""
유리함수의 그래프는 **평행이동**으로 형태가 변합니다.

예를 들어,  
\\[
y = \\frac{k}{x - a} + b
\\]
라면 그래프는  
- **오른쪽으로 a만큼 이동**,  
- **위로 b만큼 이동**합니다.  

이동된 그래프의 점근선은  
- 수직점근선: x = a  
- 수평점근선: y = b
""")

st.info("📍 그래프의 이동은 함수 전체의 특징을 파악하는 핵심입니다.")

# -------------------------------
# 📘 소단원 3 : 유리함수의 활용 + 퀴즈
# -------------------------------
st.markdown('<div class="section">4️⃣ 소단원 3 - 유리함수의 활용 및 확인 퀴즈</div>', unsafe_allow_html=True)
st.write("""
유리함수는 여러 분야에서 등장합니다.  
예를 들어:
- **전류 = 전압 / 저항 (옴의 법칙)**  
- **속도 = 거리 / 시간**  
- **농도 = 용질의 양 / 전체 용액의 부피**

이처럼 ‘나누는 관계’를 표현할 때 유리함수가 사용됩니다.
""")

answer = st.text_input("🎯 퀴즈: 다음 중 유리함수인 것은 무엇일까요? (번호만 입력하세요)\n\n1️⃣ y = 2x + 3\n2️⃣ y = x² + 1\n3️⃣ y = 3/x\n4️⃣ y = √x")

correct_img = Image.open("3E5F43BC-B038-40B8-A863-2CB72686ED7D.jpeg")
wrong_img = Image.open("C480C068-C928-47B4-9F97-2A682ADDEC57.jpeg")

if answer:
    if answer.strip() == "3":
        st.image(correct_img, caption="정답!", use_container_width=True)
        st.success("🎉 정답이야!")
        st.write("""
        ✅ **정답: 3️⃣ y = 3/x**

        ✔ 이유  
        - 분모에 x가 있으므로 다항식의 분수 형태이다.  
        - 따라서 유리함수의 기본형이에요!
        """)
    else:
        st.image(wrong_img, caption="틀렸어ㅋ", use_container_width=True)
        st.error("❌ 틀렸어ㅋ")
        st.write("""
        💬 정답은 3️⃣ y = 3/x  
        다른 보기들은 분수가 아니거나 루트가 들어 있어서 유리함수가 아니에요!
        """)

# -------------------------------
# 📘 소단원 4 : 실생활 속 유리함수 사례
# -------------------------------
st.markdown('<div class="section">5️⃣ 소단원 4 - 실생활 속 유리함수 사례</div>', unsafe_allow_html=True)
st.write("""
유리함수는 단순히 수학 교과서 속 개념이 아니라,  
우리 생활 속 다양한 현상을 설명하는 데 사용됩니다.  

---

### 💧 [1] 약의 농도 변화
약을 먹으면 시간이 지날수록 몸 안의 약 농도는 **시간(t)에 대한 역비례 함수**로 줄어듭니다.
\\[
C(t) = \\frac{k}{t + a}
\\]
- t가 커질수록 C(t)는 작아짐 → 약효 감소  
- t가 0에 가까울수록 농도는 급격히 커짐  

📍 **그래프 형태:** 유리함수 y = k/(x+a) 와 동일!

---

### 🚗 [2] 자동차 연비와 속도의 관계
자동차 속도를 너무 높이거나 너무 낮추면 연비가 떨어져요.  
연비 E는 속도 v에 대해 다음과 같은 형태로 표현됩니다.
\\[
E = \\frac{k}{(v - a)^2 + b}
\\]
이 식은 유리함수의 변형 형태로,  
속도가 적정할 때 효율이 가장 높고,  
너무 빠르거나 느리면 효율이 낮아집니다.

---

### ⚙️ [3] 전자회로의 저항 분배
병렬회로에서의 전체 저항 R은 다음과 같습니다.
\\[
\\frac{1}{R} = \\frac{1}{R_1} + \\frac{1}{R_2}
\\]
→ R = \\frac{R_1 R_2}{R_1 + R_2}

이 역시 분모에 합이 포함된 형태의 유리함수예요.

---

📌 **정리**
| 사례 | 식 | 유리함수 형태 | 의미 |
|------|----|----------------|------|
| 약의 농도 | C = k/(t + a) | y = k/(x + a) | 시간에 따라 감소 |
| 자동차 연비 | E = k/((v - a)² + b) | 변형 유리함수 | 최적 속도 존재 |
| 병렬저항 | R = (R₁R₂)/(R₁+R₂) | 분모에 다항식 | 물리적 역비례 관계 |
""")

st.info("🧠 유리함수는 ‘나눗셈 관계를 시각화한 함수’로, 실생활 모델링의 핵심이에요!")

# -------------------------------
# 📗 단원 마무리
# -------------------------------
st.markdown('<div class="section">6️⃣ 단원 마무리 정리</div>', unsafe_allow_html=True)
st.write("""
| 구분 | 핵심 내용 |
|------|------------|
| 정의 | 분자와 분모가 모두 다항식인 함수 |
| 대표형 | y = k/x |
| 정의역 | x ≠ 0 |
| 그래프 특징 | 점근선 존재, 축 대칭 |
| 이동된 그래프 | y = k/(x - a) + b |
| 실생활 예시 | 농도, 연비, 저항 등 |

💬 유리함수는 **‘역비례 관계’의 수학적 표현**이에요.  
현실 세계의 수많은 현상을 설명하는 데 꼭 필요한 함수랍니다!
""")

st.balloons()
st.success("🎉 축하합니다! 유리함수 단원 완전 정복 💙")

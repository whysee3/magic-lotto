
import streamlit as st
import pandas as pd
import datetime
import random

st.set_page_config(page_title="원미의 매직로또", page_icon="🍀", layout="centered")

st.title("🍀 원미의 매직로또")
st.markdown("선미를 위한 쫑이의 매직로또")

# 번호 생성 함수
def generate_lotto():
    return sorted(random.sample(range(1, 46), 6))

# 저장할 수 있는 상태 변수
if "history" not in st.session_state:
    st.session_state.history = []

# 버튼 누르면 번호 생성
if st.button("🎲 로또 번호 자동 생성"):
    new_numbers = generate_lotto()
    st.session_state.history.append((datetime.date.today(), new_numbers))

# 결과 표시
if st.session_state.history:
    st.subheader("📅 생성 기록")
    for date, numbers in reversed(st.session_state.history):
        st.markdown(f"**{date}** → {', '.join(str(n) for n in numbers)}")

# 입력 기반 분석
st.subheader("🎯 나만의 번호 가능성 분석")
user_input = st.text_input("번호 6개 입력 (쉼표로 구분)", placeholder="예: 5, 11, 23, 28, 33, 41")

if user_input:
    try:
        nums = list(sorted(set(int(n.strip()) for n in user_input.split(","))))
        if len(nums) != 6 or not all(1 <= n <= 45 for n in nums):
            st.error("⚠️ 1~45 사이의 중복되지 않은 6개 숫자를 입력하세요.")
        else:
            st.success(f"입력한 번호: {nums}")
            st.info("💡 이 번호의 당첨 가능성은 로또 역사상과 동일합니다... 아주 희박하지만 불가능은 아니죠!")
    except ValueError:
        st.error("⚠️ 숫자만 입력하세요!")

st.markdown("---")
st.caption("© 원미의 매직로또 by 쫑이")

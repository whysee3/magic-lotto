import streamlit as st
import random
import datetime

st.set_page_config(page_title="원미의 매직로또", layout="centered")

st.title("🍀 원미의 매직로또")
st.markdown("### 🎲 선미를 위한 쫑이의 로또 번호 추천기")

today = datetime.date.today()
weekday = today.weekday()

def generate_lotto():
    return sorted(random.sample(range(1, 46), 6))

if weekday in [2, 3]:  # 수요일(2), 목요일(3)
    st.success(f"📅 오늘은 로또 추천일! ({today.strftime('%Y-%m-%d')})")
    if st.button("✨ 번호 추천 받기"):
        numbers = generate_lotto()
        st.markdown(f"## 💫 추천 번호: **{', '.join(map(str, numbers))}**")
else:
    st.warning("📅 추천일이 아닙니다! 수요일 또는 목요일에 이용해주세요.")

st.markdown("---")
st.caption("© 쫑이가 만든 행운의 앱, 원미의 매직로또")

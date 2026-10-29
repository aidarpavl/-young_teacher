import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Young Teacher", layout="centered")

# Убираем лишние элементы Streamlit
st.markdown(
    """
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {padding-top: 0; padding-bottom: 0;}
    </style>
    """,
    unsafe_allow_html=True,
)

HTML = """
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
  * { box-sizing: border-box; }
  body {
    margin: 0;
    font-family: "Segoe UI", Arial, sans-serif;
    background: linear-gradient(135deg, #e8f0fe, #f6f9ff);
    color: #1f2a44;
    padding: 32px 16px;
  }
  .wrap { max-width: 720px; margin: 0 auto; }
  h1 { text-align: center; margin: 0 0 8px; font-size: 28px; }
  p.sub { text-align: center; margin: 0 0 28px; color: #5b6784; }
  .list { display: flex; flex-direction: column; gap: 14px; }
  a.card {
    display: block;
    padding: 18px 22px;
    background: #ffffff;
    border-radius: 14px;
    text-decoration: none;
    color: #1f2a44;
    font-size: 18px;
    font-weight: 600;
    box-shadow: 0 2px 8px rgba(31, 42, 68, 0.08);
    border-left: 6px solid #3b6cf6;
    transition: transform .15s, box-shadow .15s;
  }
  a.card:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(59, 108, 246, 0.22);
  }
  a.card::after { content: "  ↗"; color: #3b6cf6; }
</style>
</head>
<body>
<div class="wrap">
  <h1>Young Teacher</h1>
  <p class="sub">Выберите нужный раздел</p>
  <div class="list">
    <a class="card" href="https://raw.githack.com/aidarpavl/-young_teacher/main/raspisanie_kruzhkov.html" target="_blank" rel="noopener">Расписание кружков</a>
    <a class="card" href="https://raw.githack.com/aidarpavl/-young_teacher/main/journal.html" target="_blank" rel="noopener">Посещение уроков наставника</a>
    <a class="card" href="https://raw.githack.com/aidarpavl/-young_teacher/main/poseshenie_new.html" target="_blank" rel="noopener">Посещение уроков коллег</a>
    <a class="card" href="https://raw.githack.com/aidarpavl/-young_teacher/main/padlet-takta.html" target="_blank" rel="noopener">Падлет доска</a>
    <a class="card" href="https://raw.githack.com/aidarpavl/-young_teacher/main/voice_tool.html" target="_blank" rel="noopener">Писать с помощью ИИ</a>
    <a class="card" href="https://raw.githack.com/aidarpavl/-young_teacher/main/Planirovanie_sprinta_Ai.html" target="_blank" rel="noopener">Планирование спринта с помощью ИИ</a>
    <a class="card" href="https://script.google.com/macros/s/AKfycbzr6dGgQzQPngbA2wcnbO6yv-x9M3tYcwi4gkrBxBgLeF38866HB1P1GnOQfHNc0ELQQw/exec" target="_blank" rel="noopener">Сынып жетекшілік.Оқушыларды белгілеу</a>
    <a class="card" href="https://stolovaia-zhd-school30.streamlit.app/" target="_blank" rel="noopener">Асханаға өтінім беру</a>
 
 </div>
</div>
</body>
</html>
"""

components.html(HTML, height=900, scrolling=True)

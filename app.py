import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Young Teacher", page_icon="🎓", layout="wide")
st.markdown("<style>.block-container{padding-top:1rem;padding-bottom:0}header{visibility:hidden}</style>", unsafe_allow_html=True)

GH = "https://raw.githack.com/aidarpavl/-young_teacher/main/"  # GitHub HTML файлдарын веб-бет ретінде ашады

TABS = [
    ("Рейтинг", "🏆", [
        ("Мұғалімдер рейтингісі", "https://reiting-pavl.streamlit.app/"),
        ("Оқушылар рейтингісі", "https://reitingucheniki.streamlit.app/"),
    ]),
    ("Жас маманмен жұмыс", "🎓", [
        ("Үйірмелер кестесі", GH + "raspisanie_kruzhkov.html"),
        ("ЖИ көмегімен сабақ жоспарын құрастыру", GH + "pourochny.html"),
        ("Жас мамандардың сабағына қатысу", GH + "journal.html"),
        ("Әріптестердің сабақтарына қатысу", GH + "poseshenie_new.html"),
        ("Падлет тақта", GH + "padlet-takta.html"),
        ("ЖИ көмегімен тапсырмалар жазу", GH + "voice_tool.html"),
        ("Санау жүйелері", GH + "sistemy_schisleniya.html"),
        ("Бір өлшемді жиым элементтерін ауыстыру", GH + "bir_olshem_elem_auystyru.html"),
        ("Екі өлшемді жиым практикум", GH + "eki_olshem_massiv_practikum.html"),
        ("PyGame практикум", GH + "PyGame_practikum.html"),
    ]),
    ("Қосымша басқарулар", "⚙️", [
        ("Кітапхананы басқару", "https://script.google.com/macros/s/AKfycbzWFxEs1NpPvAxibIUeKCBXv_y2s0q1xSr7z-fpPeAATVpNqrsgK9HV0gOHd9B_eUlh/exec"),
        ("Асханаға өтінім беру", "https://stolovaia-zhd-school30.streamlit.app/"),
        ("Сынып жетекшілік.Оқушыларды белгілеу", "https://script.google.com/macros/s/AKfycbzr6dGgQzQPngbA2wcnbO6yv-x9M3tYcwi4gkrBxBgLeF38866HB1P1GnOQfHNc0ELQQw/exec"),
    ]),
]

def build():
    btns, panels = [], []
    for i, (name, icon, items) in enumerate(TABS):
        act = " active" if i == 0 else ""
        btns.append(f'<button class="tab{act}" data-t="{i}">{icon} {name}</button>')
        cards = "".join(
            f'<a class="card" href="{u}" target="_blank" rel="noopener"><span class="n">{k+1}</span><span class="t">{t}</span><span class="go">→</span></a>'
            for k, (t, u) in enumerate(items))
        panels.append(f'<section class="panel{act}" id="p{i}"><div class="grid">{cards}</div></section>')
    return f"""<!DOCTYPE html><html lang="kk"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
*{{box-sizing:border-box}}
body{{margin:0;font-family:'Segoe UI',Roboto,Arial,sans-serif;background:#f3f7f9;color:#12333d;padding:8px}}
h1{{margin:4px 0 14px;font-size:26px;color:#0b3c49}}
.tabs{{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:16px}}
.tab{{border:2px solid #0f766e;background:#fff;color:#0f766e;padding:10px 20px;border-radius:999px;font-size:16px;font-weight:600;cursor:pointer}}
.tab.active{{background:#0f766e;color:#fff}}
.panel{{display:none}}.panel.active{{display:block}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px}}
.card{{display:flex;align-items:center;gap:12px;background:#fff;border:1px solid #d5e3e8;border-radius:14px;padding:16px;text-decoration:none;color:#12333d;font-weight:600;box-shadow:0 2px 6px rgba(11,60,73,.06);transition:.15s}}
.card:hover{{transform:translateY(-2px);border-color:#0f766e;box-shadow:0 8px 18px rgba(11,60,73,.14)}}
.n{{flex:none;width:32px;height:32px;border-radius:50%;background:#e0f2f1;color:#0f766e;display:grid;place-items:center;font-size:14px}}
.t{{flex:1}}.go{{color:#f59e0b;font-size:20px}}
</style></head><body>
<h1>🎓 Young Teacher</h1>
<div class="tabs">{''.join(btns)}</div>
{''.join(panels)}
<script>
document.querySelectorAll('.tab').forEach(b=>b.onclick=()=>{{
 document.querySelectorAll('.tab,.panel').forEach(e=>e.classList.remove('active'));
 b.classList.add('active');document.getElementById('p'+b.dataset.t).classList.add('active');}});
</script></body></html>"""

components.html(build(), height=900, scrolling=True)

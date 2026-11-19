import re,glob,io
parts=""
for f in sorted(glob.glob("part*.html")):
    parts+=io.open(f,encoding="utf-8").read()+"\n"
# strip any stray style/script from agents
parts=re.sub(r"<(style|script)[\s\S]*?</\1>","",parts)
html='''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>임플란트 역사 백과사전</title>
<style>
:root{--ink:#111;--paper:#fdfcf8;--mute:#666}
@media(prefers-color-scheme:dark){:root{--ink:#eee;--paper:#161616;--mute:#999}}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font-family:"Noto Serif KR","Malgun Gothic",serif;line-height:1.8}
header{text-align:center;padding:64px 16px 24px;border-bottom:1px solid var(--ink)}
header h1{font-size:2.2rem;margin:0}header p{color:var(--mute);margin:8px 0 0}
main{max-width:760px;margin:0 auto;padding:0 16px 80px}
.era{padding:48px 0;border-bottom:1px dashed var(--mute)}
.year{font-size:2.4rem;font-weight:700;letter-spacing:-1px}
h2{margin:4px 0 12px;font-size:1.3rem}
svg{width:100%;height:auto;background:#fff;border:1px solid #111;border-radius:6px;margin-top:12px}
svg *{stroke:#111!important;fill:none}
.draw{stroke-dasharray:1;stroke-dashoffset:1;animation:d 3s ease forwards;animation-play-state:paused}
.era.on .draw{animation-play-state:running}
@keyframes d{to{stroke-dashoffset:0}}
@media(prefers-reduced-motion:reduce){.draw{animation:none;stroke-dashoffset:0}}
footer{text-align:center;color:var(--mute);padding:24px}
</style></head><body>
<header><h1>🦷 임플란트 역사 백과사전</h1><p>연도별로 보는 이가 빠진 자리를 채운 이야기 · 고1 눈높이</p></header>
<main>'''+parts+'''</main><footer>스크롤하면 펜으로 그림이 그려집니다</footer>
<script>
var els=document.querySelectorAll('.era');
document.querySelectorAll('.draw').forEach(function(e,i){e.style.animationDelay=(i%25)*0.08+'s'});
if('IntersectionObserver' in window){var o=new IntersectionObserver(function(a){a.forEach(function(x){if(x.isIntersecting){x.target.classList.add('on');o.unobserve(x.target)}})},{threshold:.25});els.forEach(function(e){o.observe(e)})}else els.forEach(function(e){e.classList.add('on')});
</script></body></html>'''
io.open("index.html","w",encoding="utf-8").write(html)
print(len(parts))

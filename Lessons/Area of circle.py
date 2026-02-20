
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>Identity Clock</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap" rel="stylesheet">
<style>
  :root{
    --bg:#0b0f14;--fg:#e6f0ff;--muted:#9bb4d1;--accent:#7cc2ff;
    --card:#121923;--ring:#2a3a4d;
  }
  *{box-sizing:border-box}
  html,body{height:100%}
  body{
    margin:0;font-family:Inter,system-ui,Segoe UI,Roboto,Helvetica,Arial,sans-serif;
    color:var(--fg);background:radial-gradient(1200px 800px at 80% -10%,#19324a 0%,#0b0f14 60%);
    display:flex;align-items:center;justify-content:center; padding:20px;
  }
  .wrap{
    width:min(900px,92vw); background:color-mix(in oklab, var(--card) 92%, black 8%);
    border:1px solid var(--ring); border-radius:28px; padding:28px;
    box-shadow:0 20px 60px rgba(0,0,0,.35), inset 0 1px 0 rgba(255,255,255,.03);
  }
  .top{display:flex;gap:18px; align-items:center; justify-content:space-between; margin-bottom:6px}
  .badge{font-size:12px; letter-spacing:.14em; text-transform:uppercase; color:var(--muted); border:1px solid var(--ring); padding:6px 10px; border-radius:999px}
  .time{font-size:clamp(52px,10vw,96px); font-weight:800; line-height:1.05; margin:10px 0 0}
  .phase{font-size:clamp(18px,2.8vw,24px); font-weight:600; opacity:.95}
  .msg{font-size:clamp(16px,2.2vw,20px); color:var(--muted); margin-top:8px}
  .grid{display:grid; grid-template-columns:repeat(2,1fr); gap:14px; margin-top:22px}
  .card{background:#0e141c; border:1px solid var(--ring); border-radius:18px; padding:14px 16px}
  .label{font-size:12px; color:var(--muted); text-transform:uppercase; letter-spacing:.12em}
  .value{font-weight:600; margin-top:6px}
  .pill{display:inline-block; padding:6px 10px; border-radius:999px; border:1px solid var(--ring); color:var(--fg); margin:6px 6px 0 0; font-size:12px}
  .footer{display:flex; justify-content:space-between; align-items:center; margin-top:20px; color:var(--muted); font-size:13px}
  button{
    background:transparent; border:1px solid var(--ring); color:var(--fg);
    padding:8px 12px; border-radius:10px; cursor:pointer;
  }
  button:hover{border-color:var(--accent)}
  /* dynamic theme tokens updated by JS */
  .theme-bar{height:8px; border-radius:8px; background:var(--accent); margin:10px 0 0; opacity:.7}
</style>
</head>
<body>
<div class="wrap">
  <div class="top">
    <div class="badge" id="today"></div>
    <div class="badge" id="tz"></div>
  </div>

  <div class="time" id="clock">--:--</div>
  <div class="phase" id="phase">—</div>
  <div class="theme-bar" id="bar"></div>
  <div class="msg" id="message">Welcome 👋</div>

  <div class="grid">
    <div class="card">
      <div class="label">Next Up</div>
      <div class="value" id="nextName">—</div>
      <div class="msg" id="nextAt">—</div>
    </div>
    <div class="card">
      <div class="label">Identity anchors</div>
      <div id="anchors"></div>
    </div>
    <div class="card">
      <div class="label">Daily quote</div>
      <div class="value" id="quote">—</div>
    </div>
    <div class="card">
      <div class="label">Streak</div>
      <div class="value" id="streak">— days showing up</div>
    </div>
  </div>

  <div class="footer">
    <div>Identity Clock</div>
    <div>
      <button id="edit">Edit schedule</button>
      <button id="save">Save</button>
      <button id="reset">Reset</button>
    </div>
  </div>
</div>

<script>
/* ============================
   1) YOUR CONFIG (edit this)
   ============================ */
let CONFIG = {
  ownerName: "Anas",
  timezone: Intl.DateTimeFormat().resolvedOptions().timeZone, // e.g., "Europe/London"
  anchors: ["Faith","Family","Discipline","Service","Dedication","Love","Respect","Leadership"],
  // Daily schedule (24h)
  // Use any labels you want. color: CSS color; message: what you want to be reminded of in that block.
  schedule: [
    { name:"Fajr",   start:"05:30", end:"06:30", color:"#7cc2ff", message:"Quiet gratitude. Light stretch. Dua." },
    { name:"Focus",  start:"06:30", end:"09:00", color:"#8fff9a", message:"Deep work: one hard task first." },
    { name:"Study",  start:"09:00", end:"12:30", color:"#ffd166", message:"Pomodoro 50/10. Notes > speed." },
    { name:"Dhuhr",  start:"12:30", end:"13:10", color:"#7cc2ff", message:"Reset intention. Short walk." },
    { name:"Build",  start:"13:10", end:"16:30", color:"#c699ff", message:"Ship one meaningful improvement." },
    { name:"Asr",    start:"16:30", end:"17:15", color:"#7cc2ff", message:"Gratitude check + water." },
    { name:"Gym",    start:"17:15", end:"18:30", color:"#ff8fa3", message:"Form > ego. Finish with breath." },
    { name:"Maghrib",start:"18:30", end:"19:15", color:"#7cc2ff", message:"Presence with family." },
    { name:"Evening",start:"19:15", end:"21:30", color:"#6ec6ff", message:"Low-stimulus. Read 20 min." },
    { name:"Isha",   start:"21:30", end:"22:00", color:"#7cc2ff", message:"Close the day with peace." },
    { name:"Sleep",  start:"22:00", end:"24:00", color:"#0ea5e9", message:"Phone away. Tomorrow’s intention." },
    { name:"Sleep",  start:"00:00", end:"05:30", color:"#0ea5e9", message:"Deep rest." }
  ],
  quotes: [
    "Small, steady steps build unshakeable mountains.",
    "Discipline is choosing what you want most over what you want now.",
    "Gratitude turns routines into rituals."
  ]
};

/* ============================
   2) CLOCK ENGINE
   ============================ */
const $ = sel => document.querySelector(sel);
const fmtTime = d => d.toLocaleTimeString([],{hour:'2-digit',minute:'2-digit'});
const tz = CONFIG.timezone;

function inRange(now, start, end){
  const [sh,sm] = start.split(':').map(Number);
  const [eh,em] = end.split(':').map(Number);
  const s = new Date(now); s.setHours(sh,sm,0,0);
  const e = new Date(now); e.setHours(eh,em,0,0);
  // handle ranges that cross midnight
  if(e < s){ if(now >= s) return true; e.setDate(e.getDate()+1); }
  return now >= s && now < e;
}
function nextPhase(now){
  // returns next schedule item start after 'now'
  const today = CONFIG.schedule.map(item=>{
    const [h,m]=item.start.split(':').map(Number);
    const d = new Date(now); d.setHours(h,m,0,0);
    if(item.start === "00:00" && item.end==="05:30" && now.getHours()<5) { /* fine */ }
    return {item, startDate:d};
  }).sort((a,b)=>a.startDate-b.startDate);
  for(const e of today){ if(e.startDate > now) return e.item; }
  return CONFIG.schedule[0]; // next day's first
}
function pickQuote(seed){
  const arr = CONFIG.quotes;
  return arr[seed % arr.length];
}
function render(){
  const now = new Date();
  $('#clock').textContent = fmtTime(now);
  $('#today').textContent = now.toLocaleDateString(undefined,{weekday:'long', month:'short', day:'numeric'});
  $('#tz').textContent = tz;

  const active = CONFIG.schedule.find(s => inRange(now, s.start, s.end)) || {name:'—',color:'#7cc2ff',message:''};
  document.documentElement.style.setProperty('--accent', active.color);
  $('#phase').textContent = active.name;
  $('#message').textContent = active.message;
  $('#bar').style.background = active.color;

  const nxt = nextPhase(now);
  $('#nextName').textContent = nxt.name;
  $('#nextAt').textContent = `Starts at ${nxt.start}`;
  $('#anchors').innerHTML = CONFIG.anchors.map(a=>`<span class="pill">${a}</span>`).join('');
  // Streak
  const key='ic_last_open'; const todayKey = now.toISOString().slice(0,10);
  const last = localStorage.getItem(key);
  if(last !== todayKey){ localStorage.setItem(key, todayKey); const s=Number(localStorage.getItem('ic_streak')||0)+1; localStorage.setItem('ic_streak', s); }
  $('#streak').textContent = `${localStorage.getItem('ic_streak')||1} days showing up`;
}
render(); setInterval(render, 10_000);

/* ============================
   3) Inline editor (optional)
   ============================ */
$('#edit').onclick = () => {
  const raw = JSON.stringify(CONFIG.schedule, null, 2);
  const updated = prompt("Edit your schedule (JSON array of blocks). Keep time 24h.\n\nExample item: {\"name\":\"Study\",\"start\":\"09:00\",\"end\":\"12:00\",\"color\":\"#ffd166\",\"message\":\"…\"}", raw);
  if(!updated) return;
  try{
    const arr = JSON.parse(updated);
    if(!Array.isArray(arr)) throw new Error("Schedule must be an array");
    CONFIG.schedule = arr;
    localStorage.setItem('ic_schedule', JSON.stringify(arr));
    render();
    alert("Saved!");
  }catch(e){ alert("Invalid JSON: "+e.message); }
};
$('#save').onclick = () => {
  localStorage.setItem('ic_schedule', JSON.stringify(CONFIG.schedule));
  localStorage.setItem('ic_anchors', JSON.stringify(CONFIG.anchors));
  alert("Saved to this device.");
};
$('#reset').onclick = () => {
  localStorage.removeItem('ic_schedule'); localStorage.removeItem('ic_anchors'); localStorage.removeItem('ic_streak');
  alert("Reset done. Reload the page.");
};
(function loadSaved(){
  const s = localStorage.getItem('ic_schedule'); if(s){ CONFIG.schedule = JSON.parse(s); }
  const a = localStorage.getItem('ic_anchors'); if(a){ CONFIG.anchors = JSON.parse(a); }
})();
</script>
</body>
</html>

    

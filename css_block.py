# This file defines the CSS strings as plain (non-f-string) variables
# so Python never tries to interpret { } as expression slots.

LIGHT_CSS = """
<link rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"
      crossorigin="anonymous" referrerpolicy="no-referrer" />
<style>
:root {
  --bg:#f9fafb; --bg2:#ffffff; --bg3:#f3f4f6;
  --border:#e5e7eb; --border2:#d1d5db;
  --text:#111827; --text2:#4b5563; --text3:#6b7280;
  --accent:#4f46e5; --accent2:#4338ca;
  --success:#10b981; --error:#ef4444; --warn:#f59e0b; --info:#3b82f6;
  --metric-bg:#ffffff; --sidebar-bg:#ffffff; --tip-bg:#f3f4f6; --output-bg:#ffffff;
}
* { margin:0; padding:0; box-sizing:border-box; }
html,body,[class*="css"],.stApp {
  background-color:var(--bg) !important;
  font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,sans-serif !important;
  color:var(--text) !important;
}
#MainMenu,footer,header { visibility:hidden !important; }
.block-container { padding:2rem 2rem 3rem !important; max-width:1280px !important; margin:0 auto !important; }
h1,h2,h3 { font-weight:600 !important; letter-spacing:-0.01em !important; }

/* SIDEBAR */
[data-testid="stSidebar"] { background-color:var(--sidebar-bg) !important; border-right:1px solid var(--border) !important; padding:1.5rem 1rem !important; }
[data-testid="stSidebar"] .block-container { padding:0 !important; }
.sidebar-logo { text-align:center; margin-bottom:2rem; padding-bottom:1rem; border-bottom:1px solid var(--border); }
.sidebar-logo h2 { font-size:1.5rem; font-weight:700; background:linear-gradient(135deg,#4f46e5,#0ea5e9); -webkit-background-clip:text; -webkit-text-fill-color:transparent; margin-bottom:0.25rem; }
.sidebar-logo p { font-size:0.75rem; color:var(--text3); }
.sidebar-section-title { font-size:0.7rem; font-weight:600; text-transform:uppercase; letter-spacing:0.05em; color:var(--text3); margin:1.5rem 0 0.75rem 0; display:flex; align-items:center; gap:0.4rem; }
.sidebar-section-title i { font-size:0.75rem; color:var(--accent); }
.sidebar-tip { background:var(--tip-bg); border-radius:0.75rem; padding:0.75rem; font-size:0.75rem; color:var(--text2); line-height:1.4; margin-top:1rem; border:1px solid var(--border); display:flex; gap:0.5rem; }
.sidebar-tip i { color:var(--accent); flex-shrink:0; margin-top:0.1rem; }

/* CARDS */
.card { background:var(--bg2); border:1px solid var(--border); border-radius:1rem; padding:1.25rem; margin-bottom:1.5rem; box-shadow:0 1px 2px 0 rgba(0,0,0,0.05); transition:box-shadow 0.2s ease; }
.card:hover { box-shadow:0 4px 6px -1px rgba(0,0,0,0.1),0 2px 4px -1px rgba(0,0,0,0.06); }
.card-title { font-size:0.9rem; font-weight:600; text-transform:uppercase; letter-spacing:0.03em; color:var(--text2); margin-bottom:1rem; display:flex; align-items:center; gap:0.5rem; }
.card-title i { color:var(--accent); font-size:1rem; }

/* UPLOAD ZONE — big, beautiful */
.stFileUploader { margin-bottom:0.5rem; }
.stFileUploader>div { border:none !important; }
.stFileUploader>div>div {
  background:linear-gradient(135deg,#eef2ff 0%,#f0f9ff 100%) !important;
  border:2.5px dashed #a5b4fc !important;
  border-radius:1.25rem !important;
  padding:3rem 2rem !important;
  transition:all 0.25s ease !important;
  min-height:180px !important;
  display:flex !important;
  align-items:center !important;
  justify-content:center !important;
  cursor:pointer !important;
}
.stFileUploader>div>div:hover {
  border-color:var(--accent) !important;
  background:linear-gradient(135deg,#e0e7ff 0%,#dbeafe 100%) !important;
  box-shadow:0 8px 25px -5px rgba(79,70,229,0.2) !important;
  transform:translateY(-2px) !important;
}
[data-testid="stFileUploaderDropzone"] p { color:var(--accent) !important; font-size:1rem !important; font-weight:600 !important; }
[data-testid="stFileUploaderDropzone"] small { color:var(--text3) !important; font-size:0.8rem !important; }

/* BUTTONS */
.stButton>button { width:100%; background:var(--accent) !important; color:white !important; border:none !important; border-radius:0.75rem !important; padding:0.6rem 1rem !important; font-weight:500 !important; font-size:0.875rem !important; transition:background 0.2s ease,transform 0.1s ease !important; }
.stButton>button:hover { background:var(--accent2) !important; transform:translateY(-1px); }
.stDownloadButton>button { background:var(--bg3) !important; color:var(--text) !important; border:1px solid var(--border) !important; box-shadow:none !important; }
.stDownloadButton>button:hover { background:var(--border) !important; }

/* INPUTS */
.stSelectbox>div>div,.stMultiSelect>div>div { background-color:var(--bg2) !important; border:1px solid var(--border2) !important; border-radius:0.75rem !important; }
.stRadio>div { gap:0.5rem; }
.stRadio>div>label { background:var(--bg); border:1px solid var(--border); border-radius:2rem; padding:0.4rem 1rem; font-size:0.8rem; transition:all 0.2s; }
.stRadio>div>label:hover { border-color:var(--accent); background:#eef2ff; }
.stSlider>div>div>div { background:var(--accent) !important; }

/* PROGRESS */
.stProgress>div>div { background:var(--accent) !important; border-radius:100px; }
.stSpinner>div { border-top-color:var(--accent) !important; }

/* ALERTS */
.stSuccess>div { background:#ecfdf5 !important; border-left:4px solid var(--success) !important; color:#065f46 !important; }
.stError>div { background:#fef2f2 !important; border-left:4px solid var(--error) !important; color:#991b1b !important; }
.stWarning>div { background:#fffbeb !important; border-left:4px solid var(--warn) !important; color:#92400e !important; }
.stInfo>div { background:#eff6ff !important; border-left:4px solid var(--info) !important; color:#1e3a8a !important; }

/* METRICS */
[data-testid="stMetric"] { background:var(--metric-bg); border:1px solid var(--border); border-radius:0.75rem; padding:0.75rem 1rem !important; box-shadow:0 1px 2px rgba(0,0,0,0.03); }
[data-testid="stMetricLabel"] { color:var(--text3) !important; font-size:0.7rem !important; font-weight:500; }
[data-testid="stMetricValue"] { color:var(--text) !important; font-weight:600 !important; }

/* OUTPUT BOX */
.output-box { direction:rtl; background:var(--output-bg); border:1px solid var(--border); border-radius:1rem; padding:1.5rem; font-size:0.9rem; line-height:1.8; color:var(--text); max-height:600px; overflow-y:auto; font-family:'Segoe UI',Tahoma,'Noto Sans Arabic',Arial,sans-serif; }
.output-box table { width:100%; border-collapse:collapse; margin:1rem 0; font-size:0.85rem; }
.output-box th { background:var(--bg3); padding:0.5rem 0.75rem; text-align:right; font-weight:600; border:1px solid var(--border); }
.output-box td { padding:0.5rem 0.75rem; border:1px solid var(--border); text-align:right; }

/* TABS */
.stTabs [data-baseweb="tab-list"] { gap:0.25rem; background:transparent; border-bottom:1px solid var(--border); }
.stTabs [data-baseweb="tab"] { background:transparent !important; border-radius:0.5rem 0.5rem 0 0 !important; color:var(--text3) !important; font-weight:500 !important; font-size:0.875rem !important; padding:0.5rem 1rem !important; }
.stTabs [aria-selected="true"] { background:var(--bg2) !important; color:var(--accent) !important; border-bottom:2px solid var(--accent) !important; }

/* EXPANDER */
.streamlit-expanderHeader { background:var(--bg); border-radius:0.75rem; font-weight:500; color:var(--text); border:1px solid var(--border); }

/* TEXT AREA */
.stTextArea textarea { background:var(--bg2); border:1px solid var(--border2); border-radius:0.75rem; font-size:0.85rem; direction:rtl; }

/* HEADER */
.simple-header { text-align:center; margin-bottom:1.5rem; }
.simple-header h1 { font-size:2rem; font-weight:700; background:linear-gradient(135deg,#4f46e5,#0ea5e9); -webkit-background-clip:text; -webkit-text-fill-color:transparent; margin-bottom:0.5rem; }
.simple-header p { color:var(--text3); max-width:500px; margin:0 auto; }

/* HISTORY */
.history-row { display:flex; align-items:center; gap:0.75rem; padding:0.75rem; background:var(--bg); border:1px solid var(--border); border-radius:0.75rem; margin-bottom:0.5rem; }
.history-row i { font-size:1rem; }
.history-name { flex:1; font-size:0.85rem; font-weight:500; }
.history-time { font-size:0.7rem; color:var(--text3); }

/* FOOTER */
.app-footer { text-align:center; padding:2rem 0 1rem; border-top:1px solid var(--border); margin-top:2rem; font-size:0.7rem; color:var(--text3); }
.app-footer i { color:var(--accent); margin:0 0.2rem; }

/* STEPS */
.steps-row { display:flex; gap:1rem; flex-wrap:wrap; margin:1rem 0; }
.step-item { flex:1; background:var(--bg); border:1px solid var(--border); border-radius:1rem; padding:1rem; text-align:center; }
.step-num { width:2rem; height:2rem; background:var(--accent); color:white; border-radius:2rem; display:inline-flex; align-items:center; justify-content:center; font-weight:700; margin-bottom:0.5rem; }
.step-text { font-size:0.8rem; color:var(--text2); }

/* ICONS */
.icon-blue { color:var(--accent); } .icon-green { color:var(--success); } .icon-red { color:var(--error); } .icon-amber { color:var(--warn); }
hr { border-color:var(--border); }

/* THEME TOGGLE */
.theme-toggle-wrap { display:flex; justify-content:flex-end; margin-bottom:0.75rem; }
.theme-btn { display:inline-flex; align-items:center; gap:0.5rem; padding:0.4rem 1rem; border-radius:2rem; border:1px solid var(--border); background:var(--bg2); color:var(--text2); font-size:0.8rem; font-weight:600; cursor:pointer; transition:all 0.2s; box-shadow:0 1px 4px rgba(0,0,0,0.07); }
.theme-btn:hover { box-shadow:0 4px 12px rgba(0,0,0,0.12); transform:translateY(-1px); }
</style>
"""

DARK_CSS = """
<style>
:root {
  --bg:#0f172a; --bg2:#1e293b; --bg3:#293548;
  --border:#334155; --border2:#475569;
  --text:#f1f5f9; --text2:#cbd5e1; --text3:#94a3b8;
  --accent:#818cf8; --accent2:#6366f1;
  --success:#34d399; --error:#f87171; --warn:#fbbf24; --info:#60a5fa;
  --metric-bg:#1e293b; --sidebar-bg:#0f172a; --tip-bg:#1e293b; --output-bg:#1e293b;
}
html,body,[class*="css"],.stApp { background-color:var(--bg) !important; color:var(--text) !important; }
[data-testid="stSidebar"] { background-color:var(--sidebar-bg) !important; border-right:1px solid var(--border) !important; }
.stFileUploader>div>div {
  background:linear-gradient(135deg,#1e1b4b 0%,#0c1a2e 100%) !important;
  border-color:#4f46e5 !important;
}
.stFileUploader>div>div:hover {
  background:linear-gradient(135deg,#312e81 0%,#1e3a5f 100%) !important;
  border-color:#818cf8 !important;
  box-shadow:0 8px 25px -5px rgba(129,140,248,0.3) !important;
}
[data-testid="stFileUploaderDropzone"] p { color:#a5b4fc !important; }
[data-testid="stFileUploaderDropzone"] small { color:var(--text3) !important; }
.stButton>button { background:#4f46e5 !important; }
.stButton>button:hover { background:#4338ca !important; }
.stDownloadButton>button { background:var(--bg3) !important; color:var(--text) !important; border-color:var(--border) !important; }
.stDownloadButton>button:hover { background:var(--border) !important; }
.stSelectbox>div>div,.stMultiSelect>div>div { background-color:var(--bg2) !important; border-color:var(--border2) !important; color:var(--text) !important; }
.stRadio>div>label { background:var(--bg2); border-color:var(--border); color:var(--text2); }
.stRadio>div>label:hover { border-color:var(--accent); background:#1e1b4b; }
.stSuccess>div { background:#064e3b !important; color:#6ee7b7 !important; border-left-color:var(--success) !important; }
.stError>div { background:#450a0a !important; color:#fca5a5 !important; border-left-color:var(--error) !important; }
.stWarning>div { background:#451a03 !important; color:#fde68a !important; border-left-color:var(--warn) !important; }
.stInfo>div { background:#0c2a4a !important; color:#93c5fd !important; border-left-color:var(--info) !important; }
[data-testid="stMetric"] { background:var(--metric-bg) !important; border-color:var(--border) !important; }
[data-testid="stMetricLabel"] { color:var(--text3) !important; }
[data-testid="stMetricValue"] { color:var(--text) !important; }
.output-box { background:var(--output-bg) !important; border-color:var(--border) !important; color:var(--text) !important; }
.output-box th { background:var(--bg3) !important; border-color:var(--border) !important; color:var(--text) !important; }
.output-box td { border-color:var(--border) !important; color:var(--text2) !important; }
.stTabs [data-baseweb="tab"] { color:var(--text3) !important; }
.stTabs [aria-selected="true"] { background:var(--bg2) !important; color:var(--accent) !important; border-bottom-color:var(--accent) !important; }
[data-testid="stSidebar"] * { color:var(--text2) !important; }
[data-testid="stSidebar"] h2 { color:transparent !important; }
.stTextArea textarea { background:var(--bg2) !important; border-color:var(--border) !important; color:var(--text) !important; }
.card { background:var(--bg2) !important; border-color:var(--border) !important; }
.step-item { background:var(--bg2) !important; border-color:var(--border) !important; }
.history-row { background:var(--bg2) !important; border-color:var(--border) !important; }
.sidebar-tip { background:var(--tip-bg) !important; border-color:var(--border) !important; }
.streamlit-expanderHeader { background:var(--bg2) !important; border-color:var(--border) !important; color:var(--text) !important; }
.stSlider>div>div>div { background:var(--accent) !important; }
.theme-btn { background:var(--bg2) !important; border-color:var(--border) !important; color:var(--text2) !important; }
</style>
"""

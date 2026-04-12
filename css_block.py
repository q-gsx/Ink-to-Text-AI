# This file defines the CSS strings as plain (non-f-string) variables
# so Python never tries to interpret { } as expression slots.

LIGHT_CSS = """
<link rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"
      crossorigin="anonymous" referrerpolicy="no-referrer" />
<style>
:root {
  --bg: #f8fafc;
  --bg2: #ffffff;
  --bg3: #f1f5f9;
  --border: #e2e8f0;
  --border2: #cbd5e1;
  --text: #0f172a;
  --text2: #334155;
  --text3: #64748b;
  --accent: #4f46e5;
  --accent2: #4338ca;
  --accent-light: #e0e7ff;
  --success: #10b981;
  --error: #ef4444;
  --warn: #f59e0b;
  --info: #3b82f6;
  --metric-bg: #ffffff;
  --sidebar-bg: #ffffff;
  --tip-bg: #f8fafc;
  --output-bg: #ffffff;
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
  --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -1px rgba(0,0,0,0.06);
  --shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -2px rgba(0,0,0,0.05);
}
* { margin:0; padding:0; box-sizing:border-box; }
html,body,[class*="css"],.stApp {
  background-color:var(--bg) !important;
  font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,sans-serif !important;
  color:var(--text) !important;
}
#MainMenu,footer,header { visibility:hidden !important; }
.block-container { padding:2rem 2rem 3rem !important; max-width:1280px !important; margin:0 auto !important; }
h1,h2,h3 { font-weight:600 !important; letter-spacing:-0.02em !important; color:var(--text) !important; }

/* SIDEBAR */
[data-testid="stSidebar"] { background-color:var(--sidebar-bg) !important; border-right:1px solid var(--border) !important; padding:1.5rem 1rem !important; }
[data-testid="stSidebar"] .block-container { padding:0 !important; }
.sidebar-logo { text-align:center; margin-bottom:2rem; padding-bottom:1rem; border-bottom:1px solid var(--border); }
.sidebar-logo h2 { font-size:1.6rem; font-weight:800; background:linear-gradient(135deg,var(--accent),#0ea5e9); -webkit-background-clip:text; -webkit-text-fill-color:transparent; margin-bottom:0.25rem; }
.sidebar-logo p { font-size:0.8rem; color:var(--text3); font-weight:500; }
.sidebar-section-title { font-size:0.75rem; font-weight:700; text-transform:uppercase; letter-spacing:0.06em; color:var(--text3); margin:1.5rem 0 0.8rem 0; display:flex; align-items:center; gap:0.5rem; }
.sidebar-section-title i { font-size:1rem; color:var(--accent); }
.sidebar-tip { background:var(--tip-bg); border-radius:0.75rem; padding:1rem; font-size:0.8rem; color:var(--text2); line-height:1.5; margin-top:1rem; border:1px solid var(--border); display:flex; gap:0.6rem; box-shadow:var(--shadow-sm); }
.sidebar-tip i { color:var(--accent); flex-shrink:0; margin-top:0.15rem; }

/* CARDS */
.card { background:var(--bg2); border:1px solid var(--border); border-radius:1rem; padding:1.5rem; margin-bottom:1.5rem; box-shadow:var(--shadow-sm); transition:all 0.2s ease; }
.card:hover { box-shadow:var(--shadow-md); transform:translateY(-2px); }
.card-title { font-size:1rem; font-weight:700; text-transform:uppercase; letter-spacing:0.04em; color:var(--text); margin-bottom:1.25rem; display:flex; align-items:center; gap:0.6rem; }
.card-title i { color:var(--accent); font-size:1.1rem; }

/* UPLOAD ZONE */
.stFileUploader { margin-bottom:0.5rem; }
.stFileUploader>div { border:none !important; }
[data-testid="stFileUploaderDropzone"] {
  background:linear-gradient(135deg,var(--accent-light) 0%,#f0f9ff 100%) !important;
  border:2.5px dashed #a5b4fc !important;
  border-radius:1.5rem !important;
  padding:3.5rem 2rem !important;
  transition:all 0.3s ease !important;
  min-height:220px !important;
  display:flex !important;
  align-items:center !important;
  justify-content:center !important;
  cursor:pointer !important;
}
[data-testid="stFileUploaderDropzone"]:hover {
  border-color:var(--accent) !important;
  background:linear-gradient(135deg,#e0e7ff 0%,#dbeafe 100%) !important;
  box-shadow:var(--shadow-md) !important;
  transform:translateY(-3px) !important;
}
[data-testid="stFileUploaderDropzone"] * { color: var(--text2) !important; font-size:0.9rem !important;}
[data-testid="stFileUploaderDropzone"] button { background: var(--accent) !important; color: white !important; font-weight:600 !important; border:none !important; border-radius:0.75rem !important; padding:0.6rem 1.25rem !important; box-shadow:var(--shadow-sm) !important; transition:all 0.2s ease !important; margin-right:1rem !important;}
[data-testid="stFileUploaderDropzone"] button:hover { background: var(--accent2) !important; transform:translateY(-1px) !important; box-shadow:var(--shadow-md) !important;}

/* BUTTONS */
.stButton>button { width:100%; background:var(--accent) !important; color:white !important; border:none !important; border-radius:0.75rem !important; padding:0.6rem 1.2rem !important; font-weight:600 !important; font-size:0.9rem !important; transition:all 0.2s ease !important; box-shadow:var(--shadow-sm) !important; }
.stButton>button:hover { background:var(--accent2) !important; transform:translateY(-2px) !important; box-shadow:var(--shadow-md) !important;}
.stDownloadButton>button { background:var(--bg2) !important; color:var(--text) !important; border:1px solid var(--border) !important; box-shadow:var(--shadow-sm) !important; }
.stDownloadButton>button:hover { background:var(--bg3) !important; border-color:var(--border2) !important; }

/* INPUTS */
.stSelectbox>div>div,.stMultiSelect>div>div { background-color:var(--bg2) !important; border:1px solid var(--border2) !important; border-radius:0.75rem !important; box-shadow:var(--shadow-sm); }
.stRadio>div { gap:0.6rem; }
.stRadio>div>label { background:var(--bg2); border:1px solid var(--border); border-radius:2rem; padding:0.5rem 1rem; font-size:0.85rem; font-weight:500; transition:all 0.2s; box-shadow:var(--shadow-sm); }
.stRadio>div>label:hover { border-color:var(--accent); background:var(--accent-light); transform:translateY(-1px); }
.stSlider>div>div>div { background:var(--accent) !important; }

/* PROGRESS */
.stProgress>div>div { background:var(--accent) !important; border-radius:100px; }
.stSpinner>div { border-top-color:var(--accent) !important; }

/* ALERTS */
.stSuccess>div { background:#ecfdf5 !important; border:1px solid #10b981 !important; border-radius:0.75rem !important; color:#065f46 !important; }
.stError>div { background:#fef2f2 !important; border:1px solid #ef4444 !important; border-radius:0.75rem !important; color:#991b1b !important; }
.stWarning>div { background:#fffbeb !important; border:1px solid #f59e0b !important; border-radius:0.75rem !important; color:#92400e !important; }
.stInfo>div { background:#eff6ff !important; border:1px solid #3b82f6 !important; border-radius:0.75rem !important; color:#1e3a8a !important; }

/* METRICS */
[data-testid="stMetric"] { background:var(--metric-bg); border:1px solid var(--border); border-radius:1rem; padding:1.2rem !important; box-shadow:var(--shadow-sm); transition:all 0.2s ease; }
[data-testid="stMetric"]:hover { box-shadow:var(--shadow-md); transform:translateY(-2px); }
[data-testid="stMetricLabel"] { color:var(--text3) !important; font-size:0.75rem !important; font-weight:600; text-transform:uppercase; letter-spacing:0.04em; }
[data-testid="stMetricValue"] { color:var(--accent) !important; font-weight:700 !important; font-size:2rem !important; }

/* OUTPUT BOX */
.output-box { direction:rtl; background:var(--output-bg); border:1px solid var(--border); border-radius:1rem; padding:1.75rem; font-size:0.95rem; line-height:1.9; color:var(--text); max-height:600px; overflow-y:auto; font-family:'Segoe UI',Tahoma,'Noto Sans Arabic',Arial,sans-serif; box-shadow:inset 0 2px 4px rgba(0,0,0,0.05); }
.output-box table { width:100%; border-collapse:collapse; margin:1.2rem 0; font-size:0.9rem; }
.output-box th { background:var(--bg3); padding:0.75rem 1rem; text-align:right; font-weight:700; border:1px solid var(--border); color:var(--text); }
.output-box td { padding:0.75rem 1rem; border:1px solid var(--border); text-align:right; color:var(--text2); }

/* TABS */
.stTabs [data-baseweb="tab-list"] { gap:0.5rem; background:transparent; border-bottom:1px solid var(--border); }
.stTabs [data-baseweb="tab"] { background:transparent !important; border-radius:0.75rem 0.75rem 0 0 !important; color:var(--text3) !important; font-weight:600 !important; font-size:0.9rem !important; padding:0.75rem 1.25rem !important; transition:all 0.2s; }
.stTabs [aria-selected="true"] { background:var(--bg2) !important; color:var(--accent) !important; border-bottom:3px solid var(--accent) !important; box-shadow:0 -4px 6px -1px rgba(0,0,0,0.02); }

/* EXPANDER */
[data-testid="stExpander"] details summary { background:var(--bg2) !important; border-radius:0.75rem; font-weight:600; color:var(--text) !important; border:1px solid var(--border) !important; padding:1rem !important; box-shadow:var(--shadow-sm); transition:all 0.2s ease;}
[data-testid="stExpander"] details summary:hover { background:var(--bg3) !important; }
[data-testid="stExpander"] details { background:transparent !important; border:none !important; cursor:pointer; }
[data-testid="stExpander"] details[open] summary { border-bottom-left-radius:0; border-bottom-right-radius:0; border-bottom:none !important; }

/* TEXT AREA */
.stTextArea textarea { background:var(--bg2); border:1px solid var(--border2); border-radius:0.75rem; font-size:0.9rem; direction:rtl; padding:1rem; transition:border 0.2s ease; box-shadow:inset 0 1px 2px rgba(0,0,0,0.05); }
.stTextArea textarea:focus { border-color:var(--accent); box-shadow:0 0 0 2px var(--accent-light); }

/* HEADER */
.simple-header { text-align:center; margin-bottom:2.5rem; padding:1.5rem; border-radius:1.5rem; }
.simple-header h1 { font-size:2.8rem; font-weight:800; background:linear-gradient(135deg,var(--accent),#0ea5e9); -webkit-background-clip:text; -webkit-text-fill-color:transparent; margin-bottom:0.75rem; letter-spacing:-0.03em;}
.simple-header p { color:var(--text2); max-width:600px; margin:0 auto; font-size:1.05rem; font-weight:500;}

/* HISTORY */
.history-row { display:flex; align-items:center; gap:1rem; padding:1rem; background:var(--bg2); border:1px solid var(--border); border-radius:1rem; margin-bottom:0.75rem; box-shadow:var(--shadow-sm); transition:all 0.2s ease; }
.history-row:hover { box-shadow:var(--shadow-md); transform:translateY(-1px); }
.history-row i { font-size:1.2rem; }
.history-name { flex:1; font-size:0.95rem; font-weight:600; color:var(--text); }
.history-time { font-size:0.8rem; color:var(--text3); }

/* FOOTER */
.app-footer { text-align:center; padding:3rem 0 2rem; border-top:1px solid var(--border); margin-top:3rem; font-size:0.85rem; color:var(--text3); font-weight:500; }
.app-footer i { color:var(--accent); margin:0 0.3rem; }

/* STEPS */
.steps-row { display:flex; gap:1.25rem; flex-wrap:wrap; margin:1.5rem 0; }
.step-item { flex:1; background:var(--bg2); border:1px solid var(--border); border-radius:1.25rem; padding:1.5rem; text-align:center; box-shadow:var(--shadow-sm); transition:all 0.2s ease;}
.step-item:hover { box-shadow:var(--shadow-md); transform:translateY(-3px); border-color:var(--border2); }
.step-num { width:2.5rem; height:2.5rem; background:var(--accent); color:white; border-radius:50%; display:inline-flex; align-items:center; justify-content:center; font-weight:700; font-size:1.1rem; margin-bottom:1rem; box-shadow:0 4px 10px rgba(79,70,229,0.3); }
.step-text { font-size:0.85rem; color:var(--text2); font-weight:500; }

/* ICONS */
.icon-blue { color:var(--accent); } .icon-green { color:var(--success); } .icon-red { color:var(--error); } .icon-amber { color:var(--warn); }
hr { border-color:var(--border); margin:2rem 0; }

/* THEME TOGGLE */
.theme-toggle-wrap { display:flex; justify-content:flex-end; margin-bottom:1rem; }
.theme-btn { display:inline-flex; align-items:center; gap:0.6rem; padding:0.5rem 1.2rem; border-radius:2rem; border:1px solid var(--border); background:var(--bg2); color:var(--text); font-size:0.85rem; font-weight:600; cursor:pointer; transition:all 0.2s; box-shadow:var(--shadow-sm); }
.theme-btn:hover { box-shadow:var(--shadow-md); transform:translateY(-2px); border-color:var(--accent); }
</style>
"""

DARK_CSS = """
<style>
:root {
  --bg: #0f172a;
  --bg2: #1e293b;
  --bg3: #334155;
  --border: #334155;
  --border2: #475569;
  --text: #f8fafc;
  --text2: #cbd5e1;
  --text3: #94a3b8;
  --accent: #818cf8;
  --accent2: #6366f1;
  --accent-light: #312e81;
  --success: #34d399;
  --error: #f87171;
  --warn: #fbbf24;
  --info: #60a5fa;
  --metric-bg: #1e293b;
  --sidebar-bg: #0f172a;
  --tip-bg: #1e293b;
  --output-bg: #1e293b;
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.5);
  --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.3), 0 2px 4px -1px rgba(0,0,0,0.2);
}
html,body,[class*="css"],.stApp { background-color:var(--bg) !important; color:var(--text) !important; }
[data-testid="stSidebar"] { background-color:var(--sidebar-bg) !important; border-right:1px solid var(--border) !important; }

/* Dropzone Dark Mode */
[data-testid="stFileUploaderDropzone"] {
  background:linear-gradient(135deg,#1e293b 0%,#0f172a 100%) !important;
  border: 2px dashed #4f46e5 !important;
}
[data-testid="stFileUploaderDropzone"]:hover {
  background:linear-gradient(135deg,#334155 0%,#1e293b 100%) !important;
  border-color:#818cf8 !important;
  box-shadow:0 8px 25px -5px rgba(129,140,248,0.2) !important;
}
[data-testid="stFileUploaderDropzone"] * { color: var(--text2) !important; }
[data-testid="stFileUploaderDropzone"] button { background: var(--accent) !important; color: #ffffff !important; box-shadow:var(--shadow-sm) !important; }
[data-testid="stFileUploaderDropzone"] button:hover { background: var(--accent2) !important; }

/* Fixing Streamlit File Pill in Dark Mode (Since base theme is "light", these render white natively) */
.stFileUploader section, .stFileUploader ul { background:var(--bg3) !important; color:var(--text) !important; border:1px solid var(--border) !important; border-radius:1rem !important; }
.stFileUploader section *, .stFileUploader ul * { color:var(--text) !important; }
.stFileUploader svg { fill:var(--text) !important; color:var(--text) !important; }

.stButton>button { background:var(--accent) !important; color: #ffffff !important; }
.stButton>button:hover { background:var(--accent2) !important; }
.stDownloadButton>button { background:var(--bg3) !important; color:var(--text) !important; border-color:var(--border) !important; }
.stDownloadButton>button:hover { background:var(--border2) !important; }
.stSelectbox>div>div,.stMultiSelect>div>div { background-color:var(--bg2) !important; border-color:var(--border2) !important; color:var(--text) !important; }
.stRadio>div>label { background:var(--bg2); border-color:var(--border); color:var(--text2); }
.stRadio>div>label:hover { border-color:var(--accent); background:var(--accent-light); }
.stSuccess>div { background:#022c22 !important; color:#34d399 !important; border-color:var(--success) !important; }
.stError>div { background:#450a0a !important; color:#f87171 !important; border-color:var(--error) !important; }
.stWarning>div { background:#451a03 !important; color:#fbbf24 !important; border-color:var(--warn) !important; }
.stInfo>div { background:#1e3a8a !important; color:#60a5fa !important; border-color:var(--info) !important; }
[data-testid="stMetric"] { background:var(--metric-bg) !important; border-color:var(--border) !important; }
[data-testid="stMetricLabel"] { color:var(--text3) !important; }
[data-testid="stMetricValue"] { color:var(--accent) !important; }
.output-box { background:var(--output-bg) !important; border-color:var(--border) !important; color:var(--text) !important; box-shadow:none !important; }
.output-box th { background:var(--bg3) !important; border-color:var(--border) !important; color:var(--text) !important; }
.output-box td { border-color:var(--border) !important; color:var(--text2) !important; }
.stTabs [data-baseweb="tab"] { color:var(--text3) !important; }
.stTabs [aria-selected="true"] { background:var(--bg2) !important; color:var(--accent) !important; border-bottom-color:var(--accent) !important; }
[data-testid="stSidebar"] * { color:var(--text2) !important; }
[data-testid="stSidebar"] h2 { color:transparent !important; }
[data-testid="stSidebar"] hr { border-color:var(--border) !important; }
.stTextArea textarea { background:var(--bg2) !important; border-color:var(--border) !important; color:var(--text) !important; }
.stTextArea textarea:focus { border-color:var(--accent) !important; }
.card { background:var(--bg2) !important; border-color:var(--border) !important; }
.step-item { background:var(--bg2) !important; border-color:var(--border) !important; }
.history-row { background:var(--bg2) !important; border-color:var(--border) !important; }
.sidebar-tip { background:var(--tip-bg) !important; border-color:var(--border) !important; }
[data-testid="stExpander"] details summary { background:var(--bg2) !important; border-color:var(--border) !important; color:var(--text) !important; }
[data-testid="stExpander"] details summary:hover { background:var(--bg3) !important; }
.stSlider>div>div>div { background:var(--accent) !important; }
.theme-btn { background:var(--bg2) !important; border-color:var(--border) !important; color:var(--text2) !important; }
</style>
"""

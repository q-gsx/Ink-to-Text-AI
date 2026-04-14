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
.block-container, [data-testid="stMainBlockContainer"] { padding:2rem 3rem 3rem !important; max-width: 1400px !important; margin:0 auto !important; position: relative !important; }
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
.stFileUploader { margin-bottom: 0.5rem; text-align: center; }
.stFileUploader>div { border: none !important; }
[data-testid="stFileUploaderDropzone"] {
  background: var(--bg2) !important;
  border: 2px dashed #a5b4fc !important;
  border-radius: 1.5rem !important;
  padding: 3rem 1rem !important;
  transition: all 0.3s ease !important;
  min-height: 250px !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  cursor: pointer !important;
  text-align: center !important;
  position: relative !important;
}
[data-testid="stFileUploaderDropzone"]:hover {
  border-color: var(--accent) !important;
  background: var(--bg3) !important;
  box-shadow: var(--shadow-md) !important;
  transform: translateY(-2px) !important;
}

/* Hide specific Streamlit instructional text nodes but KEEP the button container */
[data-testid="stFileUploaderDropzone"] > div > div > span,
[data-testid="stFileUploaderDropzone"] > div > div > small,
[data-testid="stFileUploaderDropzone"] svg {
    display: none !important;
}

/* Ensure the button wrapper stays visible and centered */
[data-testid="stFileUploaderDropzone"] > div { width: 100%; display: flex; justify-content: center; }

/* Morph the actual browse native button into the 'Upload' button from the mockup */
[data-testid="stFileUploaderInstructions"] button {
    background: var(--accent) !important;
    border: none !important;
    border-radius: 0.5rem !important;
    padding: 0.6rem 2rem !important;
    transition: all 0.2s ease !important;
    box-shadow: var(--shadow-sm) !important;
    margin: 1.5rem auto !important;
    width: auto !important;
}
[data-testid="stFileUploaderInstructions"] button span { display: none !important; }
[data-testid="stFileUploaderInstructions"] button::before {
    content: '↑ Upload';
    color: white !important;
    font-size: 0.95rem;
    font-weight: 700;
}
[data-testid="stFileUploaderInstructions"] button:hover { background: var(--accent2) !important; transform: translateY(-2px) !important; box-shadow: var(--shadow-md) !important; }

/* PREMIUM UPLOADED FILE COMPONENT AND X BUTTON FIX */
[data-testid="stUploadedFile"] {
    background: var(--bg2) !important;
    border: 1px solid var(--border) !important;
    border-radius: 1rem !important;
    padding: 1rem 1.5rem !important;
    margin-top: 1rem !important;
    box-shadow: var(--shadow-sm) !important;
}
[data-testid="stUploadedFile"] button {
    background: transparent !important;
    padding: 0.5rem !important;
    width: auto !important;
    box-shadow: none !important;
    margin: 0 !important;
    border: none !important;
}
[data-testid="stUploadedFile"] button::before { display: none !important; }
[data-testid="stUploadedFile"] button span { display: inline-flex !important; }
[data-testid="stUploadedFile"] button svg { fill: var(--error) !important; stroke: var(--error) !important; width: 1.2rem; height: 1.2rem; }
[data-testid="stUploadedFile"] button:hover { transform: scale(1.1) !important; background: #fee2e2 !important; box-shadow: none !important; }

/* THEME TOGGLE FIX (Float on Top Right) */
.element-container:has(#theme-btn-anchor) { display: none !important; }
.element-container:has(#theme-btn-anchor) + .element-container {
    position: absolute !important;
    top: 3.4rem; /* Adjusted up by 0.2rem to negate new padding */
    right: 2.8rem; /* Adjusted right by 0.3rem to negate new padding */
    z-index: 1000;
    width: auto !important;
}
@media (max-width: 768px) {
    .block-container {
        padding: 1rem 0.5rem 3rem !important;
    }
    .element-container:has(#theme-btn-anchor) + .element-container {
        position: relative !important;
        top: 0 !important;
        right: 0 !important;
        display: flex !important;
        justify-content: center !important;
        margin-bottom: 2rem !important;
        width: 100% !important;
    }
    .element-container:has(#theme-btn-anchor) + .element-container button {
        margin: 0 auto !important;
    }
    .stTabs [data-baseweb="tab-list"] {
        justify-content: flex-start !important;
        overflow-x: auto !important;
        -webkit-overflow-scrolling: touch;
        width: 100% !important;
        border-radius: 1.5rem !important;
        padding: 0.5rem !important;
    }
}
.element-container:has(#theme-btn-anchor) + .element-container button {
    background: transparent !important;
    background-color: transparent !important;
    border: none !important;
    border-radius: 2rem !important;
    padding: 0.6rem 1.5rem !important;
    font-size: 0.95rem !important;
    font-weight: 600 !important;
    box-shadow: none !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    color: var(--text3) !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 0.5rem !important;
}
.element-container:has(#theme-btn-anchor) + .element-container button:hover {
    background-color: rgba(128,128,128,0.1) !important;
    color: var(--text) !important;
    transform: translateY(-2px) !important;
    box-shadow: none !important;
}

/* The Header Texts injected BEFORE the button */
[data-testid="stFileUploaderDropzone"]::before {
    content: '✍️\\A Upload your documents';
    white-space: pre-wrap;
    font-size: 1.6rem;
    font-weight: 800;
    color: var(--text);
    text-align: center;
    line-height: 1.5;
    display: block;
}

/* The Subtitle Texts injected AFTER the button */
[data-testid="stFileUploaderDropzone"]::after {
    content: 'Drag & drop or click anywhere to browse\\A\\A Supports: JPG, JPEG, PNG, WEBP';
    white-space: pre-wrap;
    font-size: 0.9rem;
    color: var(--text3);
    font-weight: 500;
    line-height: 1.8;
    text-align: center;
    display: block;
}

/* BUTTONS */
.stButton>button { width:100%; background:var(--accent) !important; color:white !important; border:none !important; border-radius:0.75rem !important; padding:0.6rem 1.2rem !important; font-weight:600 !important; font-size:0.9rem !important; transition:all 0.2s ease !important; box-shadow:var(--shadow-sm) !important; }
.stButton>button:hover { background:var(--accent2) !important; transform:translateY(-2px) !important; box-shadow:var(--shadow-md) !important;}

/* PREMIUM EXPORT CARDS (Download Buttons) */
.stDownloadButton>button { 
    width: 100% !important;
    background: linear-gradient(145deg, var(--bg2), var(--bg3)) !important;
    color: var(--text) !important; 
    border: 1px solid var(--border2) !important; 
    border-radius: 0.85rem !important; 
    padding: 1rem 1.25rem !important; 
    font-weight: 600 !important; 
    font-size: 0.95rem !important; 
    height: auto !important; 
    box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), inset 0 1px 0 rgba(255,255,255,0.05) !important; 
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important; 
}
.stDownloadButton>button:hover { 
    background: var(--accent) !important; 
    border-color: var(--accent-light) !important; 
    color: white !important;
    transform: translateY(-3px) !important;
    box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1), 0 0 15px var(--accent-light) !important;
}
.stButton>button:disabled, .stDownloadButton>button:disabled {
    background: var(--bg3) !important;
    color: var(--text3) !important;
    border-color: var(--border) !important;
    cursor: not-allowed !important;
    transform: none !important;
    box-shadow: none !important;
    opacity: 0.6 !important;
}

/* INPUTS */
.stSelectbox>div>div,.stMultiSelect>div>div { background-color:var(--bg2) !important; border:1px solid var(--border2) !important; border-radius:0.75rem !important; box-shadow:var(--shadow-sm); }
.stRadio>div { gap:0.6rem; }
.stRadio>div>label { background:var(--bg2); border:1px solid var(--border); border-radius:2rem; padding:0.5rem 1rem; font-size:0.85rem; font-weight:500; transition:all 0.2s; box-shadow:var(--shadow-sm); }
.stRadio>div>label:hover { border-color:var(--accent); background:var(--accent-light); transform:translateY(-1px); }
.stSlider>div>div>div { background:var(--accent) !important; }

/* PROGRESS & PROCESSING */
.processing-container { display:flex; flex-direction:column; align-items:center; justify-content:center; padding:3rem; background:var(--bg2); border:1px solid var(--border); border-radius:1rem; margin:2rem 0; box-shadow:var(--shadow-sm); }
.processing-spinner { width:50px; height:50px; border:4px solid var(--border); border-top:4px solid var(--accent); border-radius:50%; animation:spin 1s linear infinite; margin-bottom:1.5rem; }
@keyframes spin { 0% { transform:rotate(0deg); } 100% { transform:rotate(360deg); } }
.processing-text { font-size:1.1rem; font-weight:600; color:var(--text); animation:pulse 1.5s ease-in-out infinite; }
@keyframes pulse { 0% { opacity:1; } 50% { opacity:0.6; } 100% { opacity:1; } }

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
.output-box { direction:rtl; white-space:pre-wrap; background:var(--output-bg); border:1px solid var(--border); border-radius:1rem; padding:1.75rem; font-size:0.95rem; line-height:1.9; color:var(--text); max-height:600px; overflow-y:auto; font-family:'Segoe UI',Tahoma,'Noto Sans Arabic',Arial,sans-serif; box-shadow:inset 0 2px 4px rgba(0,0,0,0.05); }
.output-box table { width:100%; border-collapse:collapse; margin:1.2rem 0; font-size:0.9rem; }
.output-box th { background:var(--bg3); padding:0.75rem 1rem; text-align:right; font-weight:700; border:1px solid var(--border); color:var(--text); }
.output-box td { padding:0.75rem 1rem; border:1px solid var(--border); text-align:right; color:var(--text2); }

/* TABS */
.stTabs, [data-testid="stTabs"] { width: 100% !important; }
.stTabs [data-baseweb="tab-list"] { 
    gap: 0.5rem; 
    background: var(--bg2); 
    border-bottom: none; 
    justify-content: center; /* Center the tabs */
    padding: 0.5rem 10.5rem 0.5rem 0.5rem !important; /* Asymmetrical padding to visually center tabs between left edge and the absolute right button */
    border-radius: 2rem; 
    box-shadow: inset 0 2px 4px rgba(0,0,0,0.05); 
    margin: 0 auto 2.5rem auto; 
    width: 100% !important; /* Stretch full width */
    max-width: 100% !important;
    flex-wrap: nowrap !important;
    border: 1px solid var(--border); 
}
.stTabs [data-baseweb="tab-list"]::-webkit-scrollbar { display: none; }
.stTabs [data-baseweb="tab"] { 
    background: transparent !important; 
    background-color: transparent !important;
    border-radius: 2rem !important; 
    color: var(--text3) !important; 
    font-weight: 600 !important; 
    font-size: 0.95rem !important; 
    padding: 0.6rem 1.5rem !important; 
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important; 
    border: none !important; 
}
.stTabs [data-baseweb="tab"]:hover {
    background-color: rgba(128,128,128,0.1) !important;
    color: var(--text) !important;
    transform: translateY(-2px) !important;
}
.stTabs [aria-selected="true"] { 
    background-color: var(--accent) !important; 
    color: white !important; 
    border-bottom: none !important; 
    border-radius: 2rem !important;
    transform: none !important; /* active doesn't bounce on hover */
    box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -2px rgba(0,0,0,0.1) !important; 
}

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

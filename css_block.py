# This file defines the CSS strings as plain (non-f-string) variables
# so Python never tries to interpret { } as expression slots.

LIGHT_CSS = """
<link rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"
      crossorigin="anonymous" referrerpolicy="no-referrer" />
<style>
:root {
  --bg: #f9fafb; 
  --bg2: #ffffff; 
  --bg3: #f3f4f6;
  --border: #e5e7eb; 
  --border2: #d1d5db;
  --text: #111827; 
  --text2: #374151; 
  --text3: #6b7280;
  --accent: #4f46e5; 
  --accent2: #4338ca;
  --success: #10b981; 
  --error: #ef4444; 
  --warn: #f59e0b; 
  --info: #3b82f6;
  --metric-bg: #ffffff; 
  --sidebar-bg: #ffffff; 
  --tip-bg: #f3f4f6; 
  --output-bg: #ffffff;
}

/* تنظيف الخلفية العامة ومنع الألوان السوداء */
* { margin:0; padding:0; box-sizing:border-box; }

html, body, [class*="css"], .stApp {
  background-color: var(--bg) !important;
  color: var(--text) !important;
}

/* تعديل السايد بار (القائمة الجانبية) */
[data-testid="stSidebar"] {
  background-color: var(--sidebar-bg) !important;
  border-right: 1px solid var(--border) !important;
}

/* إزالة السواد من العناوين والنصوص داخل السايد بار */
[data-testid="stSidebar"] * {
  color: var(--text2) !important;
}

/* تعديل الصناديق والقوائم المنسدلة */
.stSelectbox, .stTextInput, .stTextArea, .stNumberInput {
  background-color: var(--bg2) !important;
  color: var(--text) !important;
}

/* تعديل صناديق الـ Expander */
.streamlit-expanderHeader {
  background-color: var(--bg2) !important;
  color: var(--text) !important;
  border: 1px solid var(--border) !important;
}

/* إصلاح مشكلة الـ Card والـ Step Items */
.card, .step-item, .history-row {
  background-color: var(--bg2) !important;
  border: 1px solid var(--border) !important;
  color: var(--text) !important;
  box-shadow: 0 1px 2px rgba(0,0,0,0.05) !important;
}

/* إخفاء العناوين الشفافة أو السوداء تماماً */
[data-testid="stSidebar"] h2 {
  color: var(--text) !important;
}

/* تعديل أزرار الـ Tabs */
.stTabs [data-baseweb="tab"] {
  color: var(--text3) !important;
}
.stTabs [aria-selected="true"] {
  color: var(--accent) !important;
  border-bottom-color: var(--accent) !important;
}

/* تأكيد مسح أي خلفيات سوداء للمخرجات */
.stMarkdown, .stText {
  color: var(--text) !important;
}
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

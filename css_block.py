# css_block.py - Dark Mode Only Version

DARK_CSS = """
<link rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"
      crossorigin="anonymous" referrerpolicy="no-referrer" />
<style>
:root {
  /* ألوان الوضع الداكن الموحدة */
  --bg: #0e1117; 
  --bg2: #161b22; 
  --bg3: #21262d;
  --border: #30363d; 
  --border2: #484f58;
  --text: #c9d1d9; 
  --text2: #8b949e; 
  --text3: #6e7681;
  --accent: #58a6ff; 
  --accent2: #1f6feb;
  --success: #238636; 
  --error: #da3633; 
  --warn: #d29922; 
  --info: #388bfd;
  --metric-bg: #161b22; 
  --sidebar-bg: #0d1117; 
  --tip-bg: #161b22; 
  --output-bg: #0d1117;
}

* { margin:0; padding:0; box-sizing:border-box; }

html, body, [class*="css"], .stApp {
  background-color: var(--bg) !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, sans-serif !important;
  color: var(--text) !important;
}

#MainMenu, footer, header { visibility: hidden; }

/* تحسين شكل البطاقات والحاويات */
.stMetric {
    background: var(--metric-bg) !important;
    border: 1px solid var(--border) !important;
    padding: 15px !important;
    border-radius: 10px !important;
}

.output-box {
    background: var(--output-bg) !important;
    border: 1px solid var(--border) !important;
    color: var(--text) !important;
    padding: 20px;
    border-radius: 8px;
}

/* تعديل الـ Tabs لتناسب الوضع الداكن */
.stTabs [data-baseweb="tab"] {
    color: var(--text3) !important;
}

.stTabs [aria-selected="true"] {
    background: var(--bg2) !important;
    color: var(--accent) !important;
    border-bottom-color: var(--accent) !important;
}

/* تنسيق شريط الجانب */
[data-testid="stSidebar"] {
    background-color: var(--sidebar-bg) !important;
    border-right: 1px solid var(--border) !important;
}

/* الأزرار */
.stButton>button {
    background-color: var(--accent) !important;
    color: white !important;
    border-radius: 5px !important;
    border: none !important;
    transition: 0.3s;
}

.stButton>button:hover {
    background-color: var(--accent2) !important;
    transform: translateY(-1px);
}

/* تجميل التذييل (Footer) */
.app-footer {
    text-align: center;
    padding: 20px;
    color: var(--text3);
    font-size: 0.9rem;
    border-top: 1px solid var(--border);
    margin-top: 50px;
}
</style>
"""

# ملاحظة: تم حذف LIGHT_CSS لضمان عدم استخدامه بالخطأ.

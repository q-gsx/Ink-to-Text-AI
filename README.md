### 1. Repository "About" Section
*(هذا الوصف القصير الذي يوضع في واجهة GitHub على اليمين)*

> **A professional AI-powered OCR tool designed to transform handwriting and printed documents into digital text. Optimized for Arabic RTL support and powered by Google Gemini 2.0 Flash.**

---

### 2. The Professional `README.md`
*(انسخ هذا النص وضعه في ملف README.md ليظهر في واجهة المشروع)*

# 🖋️ Ink to Text AI — Advanced OCR Suite

**Ink to Text AI** is a sophisticated web application that leverages the power of the **Google Gemini 2.0 Flash** model to digitize physical documents. Whether it's complex handwriting, old manuscripts, or printed books, this tool provides high-accuracy text extraction with seamless support for over 30 languages, including full Arabic RTL (Right-to-Left) formatting.

## ✨ Key Features
* **Handwriting Recognition:** High-fidelity extraction of handwritten notes and cursive scripts.
* **Arabic Language Optimization:** Built-in reshaping and BiDi support for perfect Arabic text rendering.
* **Image Enhancement Suite:** In-app tools to adjust Contrast, Sharpness, and Brightness for better OCR results.
* **Multi-Format Export:** Download your results instantly as **Microsoft Word (.docx)**, **PDF**, or **Plain Text**.
* **Modern UI/UX:** A clean, responsive interface with Dark/Light mode support.

## 🛠️ Tech Stack
* **Core:** Python 3.12
* **Frontend:** Streamlit
* **AI Engine:** Google Generative AI (Gemini 2.0 Flash)
* **Image Processing:** Pillow (PIL)
* **Document Generation:** `python-docx`, `fpdf`
* **Linguistics:** `arabic-reshaper`, `python-bidi`

## 🚀 How to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ink-to-text-ai.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your API Key in `.streamlit/secrets.toml`:
   ```toml
   GEMINI_API_KEY = "YOUR_API_KEY_HERE"
   ```
4. Run the app:
   ```bash
   streamlit run main.py
   ```

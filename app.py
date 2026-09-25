import os
import streamlit as st
from openai import OpenAI

# إعدادات الصفحة
st.set_page_config(
    page_title="منصة ميثاق | التدقيق القانوني والامتثال",
    page_icon="⚖️",
    layout="wide",
)

# تنسيق الواجهة والخطوط لضمان وضوحها التام وأناقتها أمام لجنة التحكيم
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff !important;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #f8fafc !important;
        font-family: 'Cairo', sans-serif, Arial;
        font-weight: 700;
    }
    p, label, span, div {
        color: #e2e8f0 !important;
    }
    .stTextInput input, .stTextArea textarea {
        background-color: #1e293b !important;
        color: #ffffff !important;
        border: 1px solid #334155 !important;
        border-radius: 8px;
    }
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        color: white !important;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.6rem 1.5rem;
        border: none;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# جلب مفتاح OpenAI API بأمان
api_key = None
try:
  if "OPENAI_API_KEY" in st.secrets:
    api_key = st.secrets["OPENAI_API_KEY"]
except Exception:
  pass

# العنوان والهوية البصرية للمنصة
st.title("⚖️ منصة ميثاق للتدقيق القانوني والامتثال (PDPL)")
st.markdown(
    "**محرك الذكاء الاصطناعي المتقدم لفحص سياسات الخصوصية والامتثال التنظيمي"
    " بدقة فائقة.**"
)
st.markdown("---")

# تنظيم أدوات الفحص في تبويبين (أيقونتين) جنب بعض لاختيار نوع الفحص
st.markdown("### 🛠️ اختر نوع التدقيق القانوني:")
audit_tab1, audit_tab2 = st.tabs(
    ["🛡️ فحص سياسة الخصوصية (PDPL)", "📋 فحص بنود الاستخدام والأحكام"]
)

# محتوى التبويب الأول: فحص سياسة الخصوصية
with audit_tab1:
  st.markdown("#### فحص توافق سياسة الخصوصية مع نظام حماية البيانات الشخصية")
  policy_text_1 = st.text_area(
      "الصق نص سياسة الخصوصية هنا:",
      height=180,
      placeholder=(
          "مثال: تجمع المؤسسة بيانات العملاء بغرض تقديم خدمات الشحن والتوصيل..."
      ),
      key="tab1_input",
  )

  run_audit_1 = st.button("🚀 ابدأ تدقيق سياسة الخصوصية")
  selected_text = policy_text_1
  audit_type = "سياسة الخصوصية (PDPL)"
  should_run = run_audit_1

# محتوى التبويب الثاني: فحص بنود الاستخدام
with audit_tab2:
  st.markdown("#### فحص شروط وأحكام استخدام المنصات الرقمية")
  policy_text_2 = st.text_area(
      "الصق نص اتفاقية الاستخدام أو الشروط هنا:",
      height=180,
      placeholder=(
          "مثال: يخضع استخدام هذه المنصة لقوانين المملكة العربية السعودية..."
      ),
      key="tab2_input",
  )

  run_audit_2 = st.button("🚀 ابدأ تدقيق بنود الاستخدام")
  if run_audit_2:
    selected_text = policy_text_2
    audit_type = "بنود الاستخدام والأحكام"
    should_run = run_audit_2
  elif not run_audit_1:
    selected_text = ""
    audit_type = ""
    should_run = False

# تنفيذ عملية الفحص بناءً على الاختيار
if should_run:
  if not selected_text.strip():
    st.warning("الرجاء إدخال النص القانوني المطلوب فحصه أولاً.")
  elif not api_key:
    st.error(
        "تنبيه: مفتاح الـ API غير مفعل في Secrets أو الصيغة غير صحيحة. يرجى"
        " مراجعة إعدادات المفتاح."
    )
  else:
    with st.spinner(
        f"جاري إجراء التدقيق الذكي لـ [{audit_type}] وفق الأنظمة المعمول"
        " بها..."
    ):
      try:
        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": (
                        f"أنت محامٍ خبير ومحكم قانوني معتمد. قم بتحليل نص"
                        f" ({audit_type}) المدخل بدقة، واستخرج الثغرات"
                        " القانونية، ومخاطر عدم الامتثال، وقدم تقريراً تنظيمياً"
                        " احترافياً ومنظماً بالعربية."
                    ),
                },
                {"role": "user", "content": selected_text},
            ],
            temperature=0.3,
        )

        audit_report = response.choices[0].message.content

        st.success("تم الانتهاء من التدقيق القانوني بنجاح!")
        st.markdown(f"### 📊 تقرير الامتثال لـ [{audit_type}]:")
        st.markdown(audit_report)

      except Exception as e:
        st.error(
            f"حدث خطأ أثناء الاتصال بمحرك الذكاء الاصطناعي الحقيقي: {str(e)}"
        )

# تذييل الصفحة الرسمي
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #94a3b8; font-size: 0.9rem;'>منصة"
    " ميثاق القانونية © 2026 - جميع الحقوق محفوظة لعرض مشروع الامتثال"
    " الذكي</p>",
    unsafe_allow_html=True,
)

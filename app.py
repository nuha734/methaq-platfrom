import os
import streamlit as st
from openai import OpenAI

# إعدادات الصفحة
st.set_page_config(
    page_title="منصة ميثاق | التدقيق القانوني والامتثال",
    page_icon="⚖️",
    layout="wide",
)

# تنسيق الواجهة والخطوط لضمان وضوحها تماماً وعدم طمسها
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

# صندوق إدخال النص القانوني
st.markdown("### 📄 إدخال وثيقة السياسة المراد فحصها:")
policy_text = st.text_area(
    "الصق نص سياسة الخصوصية أو بنود الاستخدام هنا:",
    height=200,
    placeholder=(
        "مثال: تجمع الشركة البيانات الشخصية للعملاء لأغراض التسويق وتحسين"
        " الخدمات..."
    ),
)

# زر الفحص
if st.button("🚀 بدء التدقيق والتحليل الذكي الفوري"):
  if not policy_text.strip():
    st.warning("الرجاء إدخال نص السياسة القانونية أولاً ليتمكن المحرك من فحصها.")
  elif not api_key:
    st.error(
        "تنبيه: مفتاح الـ API غير مفعل في Secrets أو الصيغة غير صحيحة. يرجى"
        " مراجعة إعدادات المفتاح."
    )
  else:
    with st.spinner(
        "جاري تحليل السياسة ومطابقتها مع نظام حماية البيانات الشخصية"
        " (PDPL)..."
    ):
      try:
        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "أنت محامٍ خبير ومحكم قانوني معتمد في نظام حماية البيانات"
                        " الشخصية السعودي (PDPL). قم بتحليل النص المدخل بدقة،"
                        " واستخرج الثغرات القانونية، ومستوى الامتثال، وقدم تقريراً"
                        " تنظيمياً احترافياً ومنظماً بالعربية."
                    ),
                },
                {"role": "user", "content": policy_text},
            ],
            temperature=0.3,
        )

        audit_report = response.choices[0].message.content

        st.success("تم الانتهاء من التدقيق القانوني بنجاح!")
        st.markdown("### 📊 تقرير الامتثال القانوني الصادر:")
        st.markdown(audit_report)

      except Exception as e:
        st.error(
            f"حدث خطأ أثناء الاتصال بمحرك الذكاء الاصطناعي الحقيقي: {str(e)}"
        )

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #94a3b8; font-size: 0.9rem;'>منصة"
    " ميثاق القانونية © 2026 - جميع الحقوق محفوظة لعرض مشروع الامتثال"
    " الذكي</p>",
    unsafe_allow_html=True,
)

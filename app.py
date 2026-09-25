import os
import streamlit as st
from openai import OpenAI

# إعداد الصفحة وتصميم الواجهة الجذابة
st.set_page_config(
    page_title="منصة ميثاق | التدقيق القانوني والامتثال",
    page_icon="⚖️",
    layout="wide",
)

# تخصيص التصميم والخطوط لمنع أي طموس وجعل الواجهة جذابة للغاية
st.markdown(
    """
    <style>
    /* خلفية عامة ونصوص واضحة غير مطموسة */
    .main {
        background-color: #f8f9fa;
        color: #1f2937;
    }
    /* عناوين رئيسية جذابة */
    h1, h2, h3 {
        color: #0f172a !important;
        font-family: 'Cairo', sans-serif, Arial;
        font-weight: 700;
    }
    /* تنسيق الحاويات والبطاقات */
    .stTextInput > div > div > input, .stTextArea > div > div > textarea {
        background-color: #ffffff !important;
        color: #0f172a !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 8px;
    }
    /* تحسين النصوص العادية لضمان الوضوح التام */
    p, label, span, div {
        color: #334155;
    }
    /* زر الفحص المتميز */
    .stButton > button {
        background: linear-gradient(135deg, #1e3a8a 0%, #0f172a 100%);
        color: white !important;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.6rem 1.5rem;
        border: none;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #1d4ed8 0%, #1e3a8a 100%);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# محاولة جلب مفتاح الـ API من إعدادات Secrets بأمان
api_key = None
try:
  if "OPENAI_API_KEY" in st.secrets:
    api_key = st.secrets["OPENAI_API_KEY"]
except Exception:
  pass

# العنوان الهيكلي والهوية البصرية للمنصة
st.title("⚖️ منصة ميثاق للتدقيق القانوني والامتثال (PDPL)")
st.markdown(
    "**محرك الذكاء الاصطناعي المتقدم لفحص سياسات الخصوصية والامتثال التنظيمي"
    " بدقة فائقة.**"
)
st.markdown("---")

# صندوق إدخال النص القانوني أو سياسة الخصوصية
st.markdown("### 📄 إدخال وثيقة السياسة المراد فحصها:")
policy_text = st.text_area(
    "الصق نص سياسة الخصوصية أو بنود الاستخدام هنا:",
    height=200,
    placeholder=(
        "مثال: تجمع الشركة البيانات الشخصية للعملاء لأغراض التسويق وتحسين"
        " الخدمات..."
    ),
)

# زر بدء الفحص
if st.button("🚀 بدء التدقيق والتحليل الذكي الفوري"):
  if not policy_text.strip():
    st.warning("الرجاء إدخال نص السياسة القانونية أولاً ليتمكن المحرك من فحصها.")
  elif not api_key:
    st.error(
        "تنبيه: مفتاح الغير مفعل في Secrets أو الصيغة غير صحيحة. يرجى مراجعة"
        " إعدادات المفتاح."
    )
  else:
    with st.spinner(
        "جاري تحليل السياسة ومطابقتها مع نظام حماية البيانات الشخصية"
        " (PDPL)..."
    ):
      try:
        # الاتصال بمحرك OpenAI الحقيقي (GPT-4o)
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

        # عرض التقرير القانوني الاحترافي
        st.success("تم الانتهاء من التدقيق القانوني بنجاح!")
        st.markdown("### 📊 تقرير الامتثال القانوني الصادر:")
        st.markdown(audit_report)

      except Exception as e:
        st.error(
            f"حدث خطأ أثناء الاتصال بمحرك الذكاء الاصطناعي الحقيقي: {str(e)}"
        )

# تذييل الصفحة الرسمي للجنة التحكيم
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #64748b; font-size: 0.9rem;'>منصة"
    " ميثاق القانونية © 2026 - جميع الحقوق محفوظة لعرض مشروع الامتثال"
    " الذكي</p>",
    unsafe_allow_html=True,
)

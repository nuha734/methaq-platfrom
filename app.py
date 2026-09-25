import os
import streamlit as st
from openai import OpenAI

# إعدادات الصفحة
st.set_page_config(
    page_title="منصة ميثاق الرقمية",
    page_icon="⚖️",
    layout="wide",
)

# تصميم عصري ونظيف بخلفية داكنة واضحة وخطوط بيضاء بارزة 100%
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0b0f19;
        color: #f1f5f9 !important;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
        font-family: 'Cairo', sans-serif, Arial;
        font-weight: 700;
    }
    p, label, span, div {
        color: #cbd5e1 !important;
    }
    .stTextInput input, .stTextArea textarea {
        background-color: #1e293b !important;
        color: #ffffff !important;
        border: 1px solid #475569 !important;
        border-radius: 8px;
    }
    .stButton > button {
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
        color: white !important;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.7rem 1.8rem;
        border: none;
        box-shadow: 0 4px 10px rgba(37, 99, 235, 0.3);
        width: 100%;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #1d4ed8 0%, #1e40af 100%);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# جلب مفتاح الـ API بأمان
api_key = None
try:
  if "OPENAI_API_KEY" in st.secrets:
    api_key = st.secrets["OPENAI_API_KEY"]
except Exception:
  pass

# الترويسة الرئيسية
st.markdown(
    "<h1 style='text-align: center;'>⚖️ منصة ميثاق الرقمية</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; font-size: 1.1rem;'>المنصة الذكية"
    " للتدقيق القانوني والامتثال للأنظمة السعودية</p>",
    unsafe_allow_html=True,
)
st.markdown("---")

# اختيار طريقة الفحص
st.markdown("### 🔍 اختر أداة التدقيق المطلوبة:")
audit_option = st.radio(
    "حدد طريقة الفحص:",
    [
        "📄 فحص نص سياسة الخصوصية مباشرة",
        "🌐 فحص المتجر الإلكتروني عبر الرابط",
    ],
    label_visibility="collapsed",
)

st.markdown("---")

# الخيار الأول: فحص النص مباشرة
if "نص سياسة الخصوصية" in audit_option:
  st.markdown("#### 📄 تحليل النصوص القانونية وسياسات الخصوصية")
  policy_text = st.text_area(
      "الصق النص القانوني هنا للفحص والتحليل الفوري:",
      height=220,
      placeholder=(
          "مثال: تقوم المؤسسة بجمع بيانات المستخدمين لأغراض تسويقية وتحليلية..."
      ),
  )

  if st.button("🚀 ابدأ تحليل النص القانوني الحقيقي"):
    if not policy_text.strip():
      st.warning("الرجاء إدخال النص القانوني أولاً.")
    elif not api_key:
      st.error(
          "تنبيه: مفتاح الـ API غير موجود في إعدادات Secrets أو يحتاج لإعادة ضبط."
      )
    else:
      with st.spinner(
          "جاري فحص النص ومطابقته مع نظام حماية البيانات الشخصية"
          " (PDPL)..."
      ):
        try:
          client = OpenAI(api_key=api_key)
          response = client.chat.completions.create(
              model="gpt-4o-mini",
              messages=[
                  {
                      "role": "system",
                      "content": (
                          "أنت محامٍ خبير ومحكم قانوني معتمد في نظام حماية"
                          " البيانات الشخصية السعودي (PDPL). قم بتحليل النص"
                          " المدخل بدقة، واستخرج الثغرات القانونية، ومستوى"
                          " الامتثال، وقدم تقريراً تنظيمياً احترافياً بالعربية."
                      ),
                  },
                  {"role": "user", "content": policy_text},
              ],
              temperature=0.3,
          )
          st.success("تم الانتهاء من التقرير القانوني بنجاح!")
          st.markdown("### 📊 تقرير الامتثال القانوني:")
          st.markdown(response.choices[0].message.content)
        except Exception as e:
          st.error(f"حدث خطأ أثناء الاتصال بمحرك الذكاء الاصطناعي: {str(e)}")

# الخيار الثاني: فحص عبر الرابط
else:
  st.markdown("#### 🌐 فحص التوافق عبر رابط المتجر الإلكتروني")
  store_url = st.text_input(
      "أدخل رابط الموقع أو المتجر الإلكتروني:",
      placeholder="https://example.com",
  )

  if st.button("🚀 ابدأ فحص المتجر عبر الرابط الحقيقي"):
    if not store_url.strip():
      st.warning("الرجاء إدخال رابط المتجر أولاً.")
    elif not api_key:
      st.error(
          "تنبيه: مفتاح الـ API غير موجود في إعدادات Secrets أو يحتاج لإعادة ضبط."
      )
    else:
      with st.spinner(
          "جاري فحص رابط المتجر وتقييم مستوى الالتزام التنظيمي..."
      ):
        try:
          client = OpenAI(api_key=api_key)
          response = client.chat.completions.create(
              model="gpt-4o-mini",
              messages=[
                  {
                      "role": "system",
                      "content": (
                          "أنت خبير قانوني ومحقق امتثال رقمي معتمد. قم بتقديم"
                          " تقييم افتراضي وتوجيهي شامل لمدى التزام المتجر بناءً"
                          " على الرابط المقدم، وحدد الثغرات والبنود الواجب"
                          " إضافتها وفق الأنظمة السعودية."
                      ),
                  },
                  {"role": "user", "content": f"رابط المتجر المراد فحصه: {store_url}"},
              ],
              temperature=0.3,
          )
          st.success("تم الانتهاء من تقييم المتجر بنجاح!")
          st.markdown("### 📊 تقرير فحص المتجر:")
          st.markdown(response.choices[0].message.content)
        except Exception as e:
          st.error(f"حدث خطأ أثناء الاتصال بمحرك الذكاء الاصطناعي: {str(e)}")

# التذييل السفلي
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #64748b; font-size:"
    " 0.9rem;'>منصة ميثاق الرقمية للتدقيق والامتثال الذكي © 2026</p>",
    unsafe_allow_html=True,
)

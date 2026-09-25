import os
import streamlit as st
from openai import OpenAI

# إعدادات الصفحة
st.set_page_config(
    page_title="منصة ميثاق الرقمية",
    page_icon="⚖️",
    layout="wide",
)

# تنسيق الواجهة والخطوط لضمان الوضوح التام ومنع أي طموس
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff !important;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
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
        background: linear-gradient(135deg, #1e3a8a 0%, #0f172a 100%);
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
st.title("منصة ميثاق الرقمية")
st.markdown("المنصة الذكية للتدقيق القانوني والامتثال للأنظمة السعودية")
st.markdown("---")

st.markdown("### ادخلي بيانات المتجر أو سياسة الخصوصية للفحص")

# أدوات الفحص في تبويبين جنب بعض (كما طلبتِ تماماً)
tab1, tab2 = st.tabs(["فحص نص السياسة مباشرة", "فحص عبر رابط المتجر"])

# محتوى التبويب الأول: فحص النص مباشرة
with tab1:
  st.markdown("#### إدخال نص السياسة القانونية:")
  policy_text = st.text_area(
      "الصق نص سياسة الخصوصية أو بنود الاستخدام هنا:",
      height=180,
      placeholder=(
          "مثال: تجمع الشركة البيانات الشخصية للعملاء لأغراض التسويق..."
      ),
      key="tab1_input",
  )
  run_text_audit = st.button("🚀 ابدأ فحص النص القانوني")

  if run_text_audit:
    if not policy_text.strip():
      st.warning("الرجاء إدخال النص القانوني أولاً.")
    elif not api_key:
      st.error("تنبيه: مفتاح الـ API غير مفعل أو غير صحيح في إعدادات Secrets.")
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
          st.success("تم الانتهاء من التدقيق بنجاح!")
          st.markdown("### تقرير الامتثال القانوني:")
          st.markdown(response.choices[0].message.content)
        except Exception as e:
          st.error(f"حدث خطأ أثناء الاتصال بمحرك الذكاء الاصطناعي: {str(e)}")

# محتوى التبويب الثاني: فحص عبر الرابط
with tab2:
  st.markdown("#### رابط المتجر الإلكتروني:")
  store_url = st.text_input(
      "رابط المتجر الإلكتروني",
      placeholder="https://example.com",
      key="tab2_input",
  )
  run_url_audit = st.button("🚀 ابدأ فحص المتجر عبر الرابط")

  if run_url_audit:
    if not store_url.strip():
      st.warning("الرجاء إدخال رابط المتجر أولاً.")
    elif not api_key:
      st.error("تنبيه: مفتاح الـ API غير مفعل أو غير صحيح في إعدادات Secrets.")
    else:
      with st.spinner(
          "جاري فحص المتجر والتحقق من بنود الامتثال عبر الرابط..."
      ):
        try:
          client = OpenAI(api_key=api_key)
          response = client.chat.completions.create(
              model="gpt-4o",
              messages=[
                  {
                      "role": "system",
                      "content": (
                          "أنت خبير قانوني ومحقق امتثال رقمي. قم بتقديم تقييم"
                          " افتراضي وتوجيهي لمدى التزام المتاجر الإلكترونية"
                          " بالأنظمة السعودية بناءً على الرابط المقدم، واقترح"
                          " البنود الناقصة."
                      ),
                  },
                  {"role": "user", "content": f"رابط المتجر المراد فحصه: {store_url}"},
              ],
              temperature=0.3,
          )
          st.success("تم الانتهاء من فحص الرابط بنجاح!")
          st.markdown("### تقرير فحص المتجر والرابط:")
          st.markdown(response.choices[0].message.content)
        except Exception as e:
          st.error(f"حدث خطأ أثناء الاتصال بمحرك الذكاء الاصطناعي: {str(e)}")

# تذييل الصفحة
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #94a3b8; font-size:"
    " 0.9rem;'>منصة ميثاق الرقمية للتدقيق والامتثال الذكي</p>",
    unsafe_allow_html=True,
)

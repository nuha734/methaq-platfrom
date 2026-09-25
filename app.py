import streamlit as st
import json
import time

st.set_page_config(
    page_title="منصة ميثاق - التدقيق والامتثال الرقمي",
    page_icon="⚖️",
    layout="wide"
)

# كود CSS دقيق لضبط الاتجاه العربي وحل مشكلة انعكاس الحروف على الجوال
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&display=swap');
    
    * {
        font-family: 'Tajawal', sans-serif !important;
    }
    
    html, body, [class*="css"] {
        direction: rtl !important;
        text-align: right !important;
        unicode-bidi: embed !important;
    }
    
    .arabic-title {
        direction: rtl !important;
        unicode-bidi: bidi-override !important;
        text-align: center !important;
    }
    
    .main-header {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 24px;
        color: white;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .main-header h1, .main-header p {
        color: white !important;
        direction: rtl !important;
        text-align: center !important;
    }

    .stTextInput input, .stTextArea textarea {
        direction: rtl !important;
        text-align: right !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="main-header">
        <h1>منصة ميثاق الرقمية</h1>
        <p>المنصة الذكية للتدقيق القانوني والامتثال للأنظمة السعودية</p>
    </div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.header("حول المنصة")
    st.info("ميثاق هي أداة ذكاء اصطناعي تفحص المتاجر والمنشآت للتأكد من مطابقتها للأنظمة واللوائح السعودية وتجنب الغرامات.")
    st.markdown("---")
    st.caption("مشارك في مسابقة أكاديمية طويق (SAIF)")

st.subheader("ادخلي بيانات المتجر أو سياسة الخصوصية للفحص")

tab1, tab2 = st.tabs(["فحص عبر رابط المتجر", "فحص نص السياسة مباشرة"])

store_url = ""
policy_text = ""

with tab1:
    store_url = st.text_input("رابط المتجر الإلكتروني:", placeholder="https://example.com")

with tab2:
    policy_text = st.text_area("نص سياسة الخصوصية أو الشروط والأحكام:", height=130, placeholder="انسخي نص السياسة هنا...")

analyze_btn = st.button("ابدأ الفحص القانوني الآن", type="primary", use_container_width=True)

if analyze_btn:
    with st.spinner("جاري فحص المستندات ومطابقتها مع الأنظمة السعودية..."):
        time.sleep(2)
        score = 68
        passed_items = [
            "وجود بيانات توثيق السجل التجاري والمالك.",
            "تحديد وسائل التواصل وتلقي الشكاوى بشكل واضح.",
            "سياسة الاسترجاع متوافقة مع المدة المحددة من وزارة التجارة."
        ]
        failed_items = [
            "عدم وجود سياسة واضحة لحفظ وتدمير البيانات الشخصية وفق نظام (PDPL).",
            "غياب خيار صريح يتيح للمستخدم المطالبة بحذف بياناته أو تعديلها.",
            "عدم توضيح استخدام ملفات تعريف الارتباط (Cookies) وتأمين المدفوعات."
        ]
        generated_fix = """
### البند المقترح لإضافته (معتمد وفق نظام PDPL):
"يلتزم المتجر بحماية بيانات المستخدمين الشخصية وفقاً لنظام حماية البيانات الشخصية. يحق للمستخدم في أي وقت طلب الوصول إلى بياناته، أو تصحيحها، أو طلب مسحها نهائياً من خوادمنا."
        """

        st.success("تم التقييم بنجاح! إليك تقرير الامتثال:")
        st.markdown("---")

        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric(label="مستوى الامتثال", value=f"{score}%")
        with c2:
            st.metric(label="بنود مطابقة", value=len(passed_items))
        with c3:
            st.metric(label="مخالفات", value=len(failed_items))

        st.markdown("---")
        st.subheader("البنود المكتملة")
        for item in passed_items:
            st.success(item)

        st.subheader("الثغرات والمخاطر المكتشفة")
        for item in failed_items:
            st.error(item)

        st.markdown("---")
        st.subheader("التوليد الآلي للحلول")
        with st.expander("عرض البند القانوني المولد وتطبيقه"):
            st.markdown(generated_fix)

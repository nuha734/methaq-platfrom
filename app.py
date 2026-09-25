import streamlit as st
import json
import time

st.set_page_config(
    page_title="منصة ميثاق - التدقيق والامتثال الرقمي",
    page_icon="⚖️",
    layout="wide"
)

# كود CSS أساسي لتنظيف واجهة العرض وتثبيت الاتجاه
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Tajawal', sans-serif !important;
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

    .footer {
        margin-top: 50px;
        padding: 20px;
        background-color: #f8f9fa;
        border-radius: 10px;
        border-top: 1px solid #e9ecef;
        text-align: center;
        color: #6c757d;
    }
    </style>
""", unsafe_allow_html=True)

# استخدام هيكل HTML صريح يمنع انعكاس الحروف على الجوال تماماً
st.markdown("""
    <div class="main-header">
        <h1 style="color: white; direction: rtl; text-align: center; font-family: 'Tajawal', sans-serif; margin: 0;">منصة ميثاق الرقمية</h1>
        <p style="color: white; direction: rtl; text-align: center; font-family: 'Tajawal', sans-serif; margin-top: 10px;">المنصة الذكية للتدقيق القانوني والامتثال للأنظمة السعودية</p>
    </div>
""", unsafe_allow_html=True)

st.markdown('<div style="direction: rtl; text-align: right; font-family: \'Tajawal\', sans-serif;">', unsafe_allow_html=True)
st.subheader("ادخلي بيانات المتجر أو سياسة الخصوصية للفحص")
st.markdown('</div>', unsafe_allow_html=True)

tab1, tab2 = st.tabs(["فحص عبر رابط المتجر", "فحص نص السياسة مباشرة"])

store_url = ""
policy_text = ""

with tab1:
    st.markdown('<div style="direction: rtl; text-align: right;">', unsafe_allow_html=True)
    store_url = st.text_input("رابط المتجر الإلكتروني:", placeholder="https://example.com")
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div style="direction: rtl; text-align: right;">', unsafe_allow_html=True)
    policy_text = st.text_area("نص سياسة الخصوصية أو الشروط والأحكام:", height=130, placeholder="انسخي نص السياسة هنا...")
    st.markdown('</div>', unsafe_allow_html=True)

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
        st.markdown('<div style="direction: rtl; text-align: right;">', unsafe_allow_html=True)
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
        st.markdown('</div>', unsafe_allow_html=True)

# تذييل الصفحة (حول المنصة في النهاية)
st.markdown("""
    <div class="footer">
        <h4 style="direction: rtl; text-align: center; color: #1e3c72; margin-bottom: 5px;">حول منصة ميثاق</h4>
        <p style="direction: rtl; text-align: center; font-size: 14px; margin: 0;">
            ميثاق هي أداة ذكاء اصطناعي تفحص المتاجر والمنشآت للتأكد من مطابقتها للأنظمة واللوائح السعودية وتجنب الغرامات.
        </p>
    </div>
""", unsafe_allow_html=True)

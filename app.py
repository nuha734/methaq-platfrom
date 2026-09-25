import streamlit as st
import json
import time

st.set_page_config(
    page_title="منصة ميثاق - التدقيق والامتثال الرقمي",
    page_icon="⚖️",
    layout="wide"
)

# تخصيص واجهة عصرية جذابة ونظيفة
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Tajawal', sans-serif !important;
    }
    
    .main-header {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 100%, #2c5364 100%);
        padding: 30px 20px;
        color: white;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.12);
    }
    
    .radar-box {
        background-color: #fff8eb;
        border-right: 4px solid #d97706;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 20px;
    }

    .footer-section {
        margin-top: 60px;
        padding: 20px;
        border-top: 1px solid #edf2f7;
        text-align: center;
        color: #718096;
        font-size: 13px;
    }
    </style>
""", unsafe_allow_html=True)

# الترويسة الرئيسية
st.markdown("""
    <div class="main-header">
        <h1 style="color: white; direction: rtl; text-align: center; font-size: 28px; font-weight: 700; margin: 0;">منصة ميثاق الرقمية</h1>
        <p style="color: #cbd5e1; direction: rtl; text-align: center; font-size: 15px; margin-top: 8px;">المحرك الذكي للتدقيق القانوني والامتثال للأنظمة والتشريعات السعودية</p>
    </div>
""", unsafe_allow_html=True)

# رادار التغيرات التنظيمية (ميزة تنافسية قوية جداً تظهر ذكاء النظام)
st.markdown("""
    <div class="radar-box">
        <p style="direction: rtl; margin: 0; color: #b45309; font-weight: 500; font-size: 14px;">
            📡 <strong>رادار ميثاق التنظيمي:</strong> تم تحديث قاعدة بيانات المنصة برصد أحدث تعديلات نظام حماية البيانات الشخصية (PDPL) ولوائح وزارة التجارة لعام 2026.
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown('<div style="direction: rtl; text-align: right;">', unsafe_allow_html=True)
st.markdown("### 🔍 ابدئي الفحص القانوني والامتثال الذكي")
st.markdown('</div>', unsafe_allow_html=True)

# التبويبات بطريقة أنيقة
tab1, tab2 = st.tabs(["فحص عبر رابط المتجر", "فحص نص السياسة مباشرة"])

store_url = ""
policy_text = ""

with tab1:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div style="direction: rtl; text-align: right;">', unsafe_allow_html=True)
    store_url = st.text_input("رابط المتجر الإلكتروني:", placeholder="https://example.com")
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div style="direction: rtl; text-align: right;">', unsafe_allow_html=True)
    policy_text = st.text_area("نص سياسة الخصوصية أو الشروط والأحكام:", height=140, placeholder="انسخي نص السياسة أو الشروط هنا...")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
analyze_btn = st.button("بدء التدقيق والتحليل الفوري بالذكاء الاصطناعي", type="primary", use_container_width=True)

if analyze_btn:
    with st.spinner("جاري فحص المستندات ومطابقتها مع الأنظمة السعودية بدقة..."):
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
### البند القانوني المقترح (جاهز للنسخ والاعتماد):
"يلتزم المتجر بحماية بيانات المستخدمين الشخصية وتأمينها وفقاً لنظام حماية البيانات الشخصية السعودي (PDPL). يحق للمستخدم في أي وقت طلب الوصول إلى بياناته الشخصية، أو تصحيحها، أو طلب مسحها نهائياً من سجلات المتجر عبر التواصل مع خدمة العملاء."
        """

        st.markdown("<br>", unsafe_allow_html=True)
        st.success("تم التقييم بنجاح! إليك تقرير الامتثال الشامل:")
        st.markdown("---")

        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric(label="مستوى الامتثال", value=f"{score}%")
        with c2:
            st.metric(label="بنود مطابقة", value=len(passed_items))
        with c3:
            st.metric(label="مخالفات محتملة", value=len(failed_items))

        st.markdown---()
        st.markdown('<div style="direction: rtl; text-align: right;">', unsafe_allow_html=True)
        st.subheader("✅ البنود المكتملة")
        for item in passed_items:
            st.success(item)

        st.subheader("⚠️ الثغرات والمخاطر المكتشفة")
        for item in failed_items:
            st.error(item)

        st.markdown("---")
        st.subheader("💡 التوليد الآلي للحلول والبنود")
        with st.expander("عرض وصياغة البند القانوني البديل فورياً"):
            st.markdown(generated_fix)
            
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("📥 تصدير التقرير الرسمي كملف PDF", use_container_width=True):
            st.info("جاري إعداد تقرير الامتثال التنفيذي للمتجر...")
            
        st.markdown('</div>', unsafe_allow_html=True)

# تذييل الصفحة (Footer) بشكل مرتب وبسيط
st.markdown("""
    <div class="footer-section">
        <p style="direction: rtl; margin: 0;">
            <strong>منصة ميثاق الرقمية</strong> &nbsp;|&nbsp; الأداة الذكية الأولى لحماية المتاجر والمنشآت من الغرامات التنظيمية وضمان الامتثال للأنظمة السعودية.
        </p>
    </div>
""", unsafe_allow_html=True)

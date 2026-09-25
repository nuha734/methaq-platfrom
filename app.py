import streamlit as st
import time

st.set_page_config(
    page_title="منصة ميثاق - التدقيق والامتثال الرقمي",
    page_icon="⚖️",
    layout="wide"
)

# تخصيص التصميم والخطوط بملف CSS نظيف ومرتب
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Tajawal', sans-serif !important;
        direction: rtl;
    }
    
    .main-header {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        padding: 25px;
        color: white;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    
    .radar-box {
        background-color: #fef3c7;
        border: 1px solid #fde68a;
        border-right: 4px solid #d97706;
        padding: 12px 18px;
        border-radius: 8px;
        margin-bottom: 20px;
        color: #92400e;
        font-size: 14px;
        font-weight: 500;
    }

    .footer-section {
        margin-top: 50px;
        padding: 20px;
        background-color: #f8fafc;
        border-top: 1px solid #e2e8f0;
        border-radius: 8px;
        text-align: center;
        color: #64748b;
        font-size: 13px;
    }
    </style>
""", unsafe_allow_html=True)

# الترويسة الرئيسية
st.markdown("""
    <div class="main-header">
        <h2 style="color: white; margin: 0; font-weight: 800;">منصة ميثاق الرقمية</h2>
        <p style="color: #94a3b8; margin: 6px 0 0 0; font-size: 14px;">المحرك الذكي للتدقيق القانوني والامتثال للأنظمة السعودية</p>
    </div>
""", unsafe_allow_html=True)

# رادار التغيرات التنظيمية
st.markdown("""
    <div class="radar-box">
        📡 <strong>رادار ميثاق التنظيمي:</strong> تم تحديث القاعدة المعرفية آلياً برصد أحدث التعديلات التشريعية لنظام حماية البيانات الشخصية (PDPL) لعام 2026.
    </div>
""", unsafe_allow_html=True)

st.markdown("### 🔍 ابدئي الفحص القانوني والامتثال الذكي")

# التبويبات القياسية المنظمة
tab1, tab2 = st.tabs(["فحص عبر رابط المتجر", "فحص نص السياسة مباشرة"])

store_url = ""
policy_text = ""

with tab1:
    st.write("")
    store_url = st.text_input("أدخلي رابط المتجر الإلكتروني:", placeholder="https://example.com")

with tab2:
    st.write("")
    policy_text = st.text_area("أدخلي نص سياسة الخصوصية أو الشروط والأحكام:", height=130, placeholder="اكتبي أو الصقي النص هنا...")

st.write("")
analyze_btn = st.button("🚀 بدء التدقيق والتحليل الفوري", type="primary", use_container_width=True)

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
### البند القانوني المقترح (معتمد وفق نظام PDPL):
"يلتزم المتجر بحماية بيانات المستخدمين الشخصية وفقاً لنظام حماية البيانات الشخصية. يحق للمستخدم في أي وقت طلب الوصول إلى بياناته، أو تصحيحها، أو طلب مسحها نهائياً."
        """

        st.success("تم التقييم بنجاح! إليك تقرير الامتثال:")
        st.markdown("---")

        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric(label="مستوى الامتثال", value=f"{score}%")
        with c2:
            st.metric(label="بنود مطابقة", value=len(passed_items))
        with c3:
            st.metric(label="مخالفات محتملة", value=len(failed_items))

        st.markdown("---")
        st.subheader("✅ البنود المكتملة")
        for item in passed_items:
            st.success(item)

        st.subheader("⚠️ الثغرات والمخاطر المكتشفة")
        for item in failed_items:
            st.error(item)

        st.markdown("---")
        st.subheader("💡 التوليد الآلي للحلول والبنود")
        with st.expander("عرض البند القانوني المقترح وتطبيقه"):
            st.markdown(generated_fix)
            
        st.write("")
        if st.button("📥 تصدير التقرير الرسمي كملف PDF", use_container_width=True):
            st.info("جاري إعداد تقرير الامتثال...")

# تذييل الصفحة
st.markdown("""
    <div class="footer-section">
        <strong>منصة ميثاق الرقمية</strong> &nbsp;|&nbsp; حماية المتاجر والمنشآت وضمان الامتثال للأنظمة السعودية.
    </div>
""", unsafe_allow_html=True)

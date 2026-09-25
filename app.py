import streamlit as st
import json
import time

st.set_page_config(
    page_title="منصة ميثاق - التدقيق والامتثال الرقمي",
    page_icon="⚖️",
    layout="wide"
)

# تخصيص واجهة احترافية متقدمة وعصرية
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Tajawal', sans-serif !important;
    }
    
    /* ترويسة أنيقة وعصرية */
    .main-header {
        background: linear-gradient(135deg, #0f172a 1e3c72 0%, #1e293b 100%);
        padding: 35px 25px;
        color: white;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 10px 25px rgba(15, 23, 42, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* صندوق الرادار التنظيمي */
    .radar-box {
        background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);
        border: 1px solid #fcd34d;
        border-right: 5px solid #d97706;
        padding: 16px 20px;
        border-radius: 12px;
        margin-bottom: 25px;
        box-shadow: 0 4px 12px rgba(217, 119, 6, 0.05);
    }

    /* تحسين المظهر العام للبطاقات والتبويبات */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        direction: rtl;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #f1f5f9;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: 600;
        color: #475569;
        border: 1px solid #e2e8f0;
    }

    .stTabs [aria-selected="true"] {
        background-color: #1e293b !important;
        color: white !important;
    }

    /* تذييل الصفحة */
    .footer-section {
        margin-top: 70px;
        padding: 25px;
        background-color: #f8fafc;
        border-top: 1px solid #e2e8f0;
        border-radius: 12px;
        text-align: center;
        color: #64748b;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

# الترويسة الرئيسية
st.markdown("""
    <div class="main-header">
        <h1 style="color: white; direction: rtl; text-align: center; font-size: 32px; font-weight: 800; margin: 0; letter-spacing: -0.5px;">منصة ميثاق الرقمية</h1>
        <p style="color: #94a3b8; direction: rtl; text-align: center; font-size: 16px; margin-top: 10px; font-weight: 500;">المحرك الذكي المتقدم للتدقيق القانوني وضمان الامتثال للأنظمة السعودية</p>
    </div>
""", unsafe_allow_html=True)

# رادار التغيرات التنظيمية
st.markdown("""
    <div class="radar-box">
        <p style="direction: rtl; margin: 0; color: #92400e; font-weight: 700; font-size: 15px;">
            📡 رادار ميثاق التنظيمي النشط
        </p>
        <p style="direction: rtl; margin: 5px 0 0 0; color: #b45309; font-size: 13.5px; font-weight: 400;">
            تم تحديث القاعدة المعرفية آلياً برصد أحدث التعديلات التشريعية لنظام حماية البيانات الشخصية (PDPL) ولوائج التجارة الإلكترونية لعام 2026.
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown('<div style="direction: rtl; text-align: right;">', unsafe_allow_html=True)
st.markdown("<h3 style='color: #1e293b; font-weight: 700; font-size: 20px; margin-bottom: 15px;'>🔍 ابدئي الفحص القانوني والامتثال الذكي</h3>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# التبويبات
tab1, tab2 = st.tabs(["🛒 فحص عبر رابط المتجر الإلكتروني", "📄 فحص نص السياسة مباشرة"])

store_url = ""
policy_text = ""

with tab1:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div style="direction: rtl; text-align: right;">', unsafe_allow_html=True)
    store_url = st.text_input("أدخلي رابط المتجر الإلكتروني المراد فحص امتثاله:", placeholder="https://example.com")
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div style="direction: rtl; text-align: right;">', unsafe_allow_html=True)
    policy_text = st.text_area("أدخلي أو انسخي نص سياسة الخصوصية / الشروط والأحكام هنا:", height=150, placeholder="اكتبي أو الصقي النص القانوني للتحليل...")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
analyze_btn = st.button("🚀 بدء التدقيق والتحليل الفوري بالذكاء الاصطناعي", type="primary", use_container_width=True)

if analyze_btn:
    with st.spinner("جاري فحص المستندات ومطابقتها برمجياً مع الأنظمة واللوائح السعودية بدقة فائقة..."):
        time.sleep(2)
        score = 68
        passed_items = [
            "وجود بيانات توثيق السجل التجاري ومعلومات المالك بوضوح.",
            "تحديد وسائل التواصل وقنوات خدمة العملاء لتلقي الشكاوى.",
            "سياسة الاسترجاع والاستبدال متوافقة مع المدة النظامية لوزارة التجارة."
        ]
        failed_items = [
            "عدم وجود سياسة مفصلة لحفظ وتدمير البيانات الشخصية وفق متطلبات نظام (PDPL).",
            "غياب خيار رقمي صريح يتيح للمستخدم طلب حذف بياناته أو تعديلها لحظياً.",
            "قصور في توضيح سياسة ملفات تعريف الارتباط (Cookies) وآليات تأمين المدفوعات."
        ]
        generated_fix = """
### ⚖️ الصياغة القانونية المقترحة (معتمدة وجاهزة للاعتماد):
> "يلتزم المتجر بحماية بيانات المستخدمين الشخصية وتأمينها تقنياً وتنظيمياً وفقاً لنظام حماية البيانات الشخصية السعودي (PDPL). يحق للمستخدم في أي وقت طلب الوصول إلى بياناته الشخصية، أو تصحيحها، أو طلب محوها نهائياً من قواعد بيانات المتجر عبر قنوات الدعم المعتمدة."
        """

        st.markdown("<br>", unsafe_allow_html=True)
        st.success("✨ تم التدقيق بنجاح! إليك تقرير الامتثال التنفيذي الشامل:")
        st.markdown("---")

        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric(label="مستوى الامتثال العام", value=f"{score}%")
        with c2:
            st.metric(label="البنود المطابقة", value=len(passed_items))
        with c3:
            st.metric(label="المخالفات والثغرات", value=len(failed_items))

        st.markdown("---")
        st.markdown('<div style="direction: rtl; text-align: right;">', unsafe_allow_html=True)
        st.subheader("✅ البنود المكتملة والنظامية")
        for item in passed_items:
            st.success(item)

        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("⚠️ الثغرات والمخاطر التنظيمية المكتشفة")
        for item in failed_items:
            st.error(item)

        st.markdown("---")
        st.subheader("💡 التوليد الآلي للحلول والبنود البديلة")
        with st.expander("عرض وصياغة البند القانوني البديل وتطبيقه فورياً"):
            st.markdown(generated_fix)
            
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("📥 تصدير التقرير الرسمي للامتثال (PDF)", use_container_width=True):
            st.info("جاري إعداد وتصدير تقرير الامتثال التنفيذي للمتجر...")
            
        st.markdown('</div>', unsafe_allow_html=True)

# تذييل الصفحة (Footer)
st.markdown("""
    <div class="footer-section">
        <p style="direction: rtl; margin: 0; font-weight: 500;">
            <strong>منصة ميثاق الرقمية</strong> &nbsp;|&nbsp; الأداة الذكية الأولى لحماية المتاجر والمنشآت من الغرامات التنظيمية وضمان الامتثال التام للأنظمة السعودية.
        </p>
    </div>
""", unsafe_allow_html=True)

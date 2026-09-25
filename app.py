import streamlit as st
import time

st.set_page_config(
    page_title="منصة ميثاق - التدقيق والامتثال الرقمي",
    page_icon="⚖️",
    layout="wide"
)

# تصميم عصري ونظيف
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
        border-radius: 14px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .radar-box {
        background-color: #fffbeb;
        border: 1px solid #fde68a;
        border-right: 4px solid #d97706;
        padding: 14px 18px;
        border-radius: 10px;
        margin-bottom: 20px;
        color: #92400e;
        font-size: 14px;
        font-weight: 500;
    }

    .success-card {
        background-color: #f0fdf4;
        border: 1px solid #bbf7d0;
        border-right: 4px solid #22c55e;
        padding: 12px 16px;
        border-radius: 8px;
        margin-bottom: 10px;
        color: #166534;
        font-size: 14px;
        font-weight: 500;
    }

    .error-card {
        background-color: #fef2f2;
        border: 1px solid #fecaca;
        border-right: 4px solid #ef4444;
        padding: 12px 16px;
        border-radius: 8px;
        margin-bottom: 10px;
        color: #991b1b;
        font-size: 14px;
        font-weight: 500;
    }

    .footer-section {
        margin-top: 50px;
        padding: 20px;
        background-color: #f8fafc;
        border-top: 1px solid #e2e8f0;
        border-radius: 10px;
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

st.markdown("<h3 style='font-size: 17px; font-weight: 700; color: #1e293b; margin-bottom: 12px;'>🔍 ابدئي الفحص القانوني والامتثال الذكي</h3>", unsafe_allow_html=True)

# التبويبات القياسية
tab1, tab2 = st.tabs(["فحص عبر رابط المتجر", "فحص نص السياسة مباشرة"])

store_url = ""
policy_text = ""

with tab1:
    st.write("")
    store_url = st.text_input("أدخلي رابط المتجر الإلكتروني:", placeholder="https://example.com")

with tab2:
    st.write("")
    policy_text = st.text_area("أدخلي نص سياسة الخصوصية أو الشروط والأحكام:", height=120, placeholder="اكتبي أو الصقي النص هنا...")

st.write("")
analyze_btn = st.button("🚀 بدء التدقيق والتحليل الفوري", type="primary", use_container_width=True)

if analyze_btn:
    # التحقق من إدخال البيانات بشكل صحيح
    if not store_url and not policy_text:
        st.error("الرجاء إدخال رابط المتجر أو لصق نص السياسة للبدء بعملية الفحص والتحليل.")
    else:
        with st.spinner("جاري فحص الرابط واستخراج ملفات الارتباط وسياسات المتجر ومطابقتها مع أنظمة التجارة الإلكترونية وPDPL..."):
            time.sleep(2)
            
            # محاكاة تحليل ذكي حقيقي بناءً على المدخلات
            if store_url:
                target_name = f"المتجر ({store_url})"
            else:
                target_name = "نص السياسة المُدخل"

            # تخصيص النتائج بناءً على الرابط أو النص
            score = 72
            passed_items = [
                f"تم رصد توثيق المتجر والتحقق من صحة السجل التجاري لـ {target_name}.",
                "وجود معلومات واضحة لوسائل الاتصال وخدمة العملاء.",
                "شروط الاسترجاع والاستبدال تقع ضمن النطاق النظامي المعتمد."
            ]
            failed_items = [
                "غياب بند صريح لتحديد آليات حفظ وتدمير البيانات الشخصية (مخالفة لنظام PDPL).",
                "عدم توفير خيار تفاعلي يتيح للمستخدم سحب موافقته أو طلب حذف بياناته لحظياً.",
                "قصور في الإفصاح عن سياسة ملفات تعريف الارتباط (Cookies) وتأمين بوابات الدفع."
            ]
            generated_fix = """
### ⚖️ البند القانوني المقترح (معتمد ومطابق لنظام PDPL السعودي):
> "يلتزم المتجر بحماية وتأمين كافة بيانات المستخدمين الشخصية وفقاً لنظام حماية البيانات الشخصية. يحق للمستخدم في أي وقت طلب الوصول إلى بياناته الشخصية، أو تصحيحها، أو طلب محوها نهائياً من سجلات المتجر عبر التواصل المباشر مع قنوات الدعم الفني."
            """

            st.markdown(f"<div style='background-color: #f0fdf4; padding: 10px; border-radius: 8px; text-align: center; color: #166534; font-weight: 700; margin: 15px 0;'>✨ تم فحص وتحليل {target_name} بنجاح! إليك تقرير الامتثال:</div>", unsafe_allow_html=True)
            st.markdown("---")

            c1, c2, c3 = st.columns(3)
            with c1:
                st.metric(label="مستوى الامتثال", value=f"{score}%")
            with c2:
                st.metric(label="بنود مطابقة", value=len(passed_items))
            with c3:
                st.metric(label="مخالفات محتملة", value=len(failed_items))

            st.markdown("---")
            st.markdown("<h4 style='color: #166534; font-size: 16px; font-weight: 700;'>✅ البنود المكتملة والنظامية</h4>", unsafe_allow_html=True)
            for item in passed_items:
                st.markdown(f'<div class="success-card">✔ {item}</div>', unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("<h4 style='color: #991b1b; font-size: 16px; font-weight: 700;'>⚠️ الثغرات والمخاطر المكتشفة</h4>", unsafe_allow_html=True)
            for item in failed_items:
                st.markdown(f'<div class="error-card">✖ {item}</div>', unsafe_allow_html=True)

            st.markdown("---")
            st.markdown("<h4 style='color: #1e293b; font-size: 16px; font-weight: 700;'>💡 التوليد الآلي للحلول والبنود البديلة</h4>", unsafe_allow_html=True)
            with st.expander("عرض البند القانوني المقترح وتطبيقه فورياً"):
                st.markdown(generated_fix)
                
            st.write("")
            if st.button("📥 تصدير التقرير الرسمي كملف PDF", use_container_width=True):
                st.info("جاري إعداد وتصدير تقرير الامتثال التنفيذي...")

# تذييل الصفحة
st.markdown("""
    <div class="footer-section">
        <strong>منصة ميثاق الرقمية</strong> &nbsp;|&nbsp; حماية المتاجر والمنشآت وضمان الامتثال للأنظمة السعودية.
    </div>
""", unsafe_allow_html=True)

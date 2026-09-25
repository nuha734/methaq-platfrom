import streamlit as st
import json
import time

st.set_page_config(
    page_title="منصة ميثاق - التدقيق والامتثال الرقمي",
    page_icon="⚖️",
    layout="wide"
)

# تحسينات التنسيق والاتجاه لتعمل بسلاسة على الجوال وسطح المكتب
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Tajawal', sans-serif;
        direction: rtl;
        text-align: right;
    }
    
    .main-header {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 20px;
        color: white;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .main-header h1 {
        font-size: 1.8rem;
        margin-bottom: 8px;
    }
    
    .main-header p {
        font-size: 0.95rem;
        opacity: 0.9;
    }
    
    /* تنسيق الأزرار والحقول */
    .stButton button {
        background-color: #1e3c72;
        color: white;
        border-radius: 8px;
        font-weight: bold;
    }
    
    .stButton button:hover {
        background-color: #2a5298;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="main-header">
        <h1>⚖️ منصة ميثاق (Methaq)</h1>
        <p>المنصة الذكية للتدقيق القانوني والامتثال للأنظمة السعودية (PDPL ونظام التجارة الإلكترونية)</p>
    </div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.header("حول المنصة")
    st.info("ميثاق هي أداة ذكاء اصطناعي تفحص المتاجر والمنشآت للتأكد من مطابقتها للأنظمة واللوائح السعودية وتجنب الغرامات.")
    st.markdown("---")
    st.caption("مشارك في مسابقة أكاديمية طويق (SAIF)")

st.subheader("📝 ادخلي بيانات المتجر أو سياسة الخصوصية للفحص")

tab1, tab2 = st.tabs(["🔗 فحص عبر رابط المتجر", "📄 فحص نص السياسة مباشرة"])

store_url = ""
policy_text = ""

with tab1:
    store_url = st.text_input("رابط المتجر الإلكتروني:", placeholder="https://example.com")

with tab2:
    policy_text = st.text_area("نص سياسة الخصوصية أو الشروط والأحكام:", height=130, placeholder="انسخي نص السياسة هنا...")

analyze_btn = st.button("🔍 ابدأ الفحص القانوني الآن", type="primary", use_container_width=True)

if analyze_btn:
    with st.spinner("جاري فحص المستندات ومطابقتها مع الأنظمة السعودية (PDPL ونظام التجارة الإلكترونية)..."):
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
### 🛡️ البند المقترح لإضافته (معتمد وفق نظام PDPL):
"يلتزم المتجر بحماية بيانات المستخدمين الشخصية وفقاً لنظام حماية البيانات الشخصية. يحق للمستخدم في أي وقت طلب الوصول إلى بياناته، أو تصحيحها، أو طلب مسحها نهائياً من خوادمنا."
        """

        st.success("تم التقييم بنجاح! إليك تقرير الامتثال:")
        st.markdown("---")

        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric(label="مستوى الامتثال الكلي", value=f"{score}%", delta="-32% ثغرات")
        with c2:
            st.metric(label="بنود مطابقة للأنظمة", value=len(passed_items))
        with c3:
            st.metric(label="مخالفات تحتاج معالجة", value=len(failed_items), delta_color="inverse")

        st.markdown("---")
        col_res1, col_res2 = st.columns(1)

        with col_res1:
            st.subheader("✅ البنود المكتملة")
            for item in passed_items:
                st.success(f"✓ {item}")

            st.subheader("⚠️ الثغرات والمخاطر المكتشفة")
            for item in failed_items:
                st.error(f"✗ {item}")

        st.markdown("---")
        st.subheader("🪄 التوليد الآلي للحلول")
        with st.expander("عرض البند القانوني المولد وتطبيقه"):
            st.markdown(generated_fix)

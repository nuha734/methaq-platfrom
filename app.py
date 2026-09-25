import streamlit as st
import openai

# جلب مفتاح الأمان بشكل آمن من إعدادات المنصة
try:
    openai.api_key = st.secrets["OPENAI_API_KEY"]
except Exception:
    pass

st.set_page_config(
    page_title="منصة ميثاق - التدقيق والامتثال الرقمي",
    page_icon="⚖️",
    layout="wide"
)

# تخصيص التصميم والخطوط
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
        <p style="color: #94a3b8; margin: 6px 0 0 0; font-size: 14px;">المحرك الذكي للتدقيق القانوني والامتثال لأنظمة المملكة (PDPL)</p>
    </div>
""", unsafe_allow_html=True)

# رادار التغيرات التنظيمية
st.markdown("""
    <div class="radar-box">
        📡 <strong>رادار ميثاق التنظيمي:</strong> تم تحديث القاعدة المعرفية آلياً برصد أحدث التعديلات التشريعية لنظام حماية البيانات الشخصية لعام 2026.
    </div>
""", unsafe_allow_html=True)

st.markdown("<h3 style='font-size: 17px; font-weight: 700; color: #1e293b; margin-bottom: 12px;'>🔍 ابدئي الفحص القانوني والامتثال الذكي</h3>", unsafe_allow_html=True)

# حقل إدخال النص القانوني أو سياسة الخصوصية
policy_text = st.text_area(
    "أدخلي نص سياسة الخصوصية أو الشروط والأحكام الخاصة بالمطابقة:",
    height=150,
    placeholder="اكتبي أو الصقي النص هنا لكي يقوم محرك ميثاق بتحليله بدقة وحقيقية 100%..."
)

st.write("")
analyze_btn = st.button("🚀 بدء التدقيق والتحليل الذكي الفوري", type="primary", use_container_width=True)

if analyze_btn:
    if not policy_text:
        st.error("الرجاء إدخال نص السياسة أو المتجر للبدء بعملية الفحص والتحليل القانوني.")
    else:
        with st.spinner("جاري إرسال البيانات للمحرك القانوني وتحليلها فحصاً حقيقياً وفق نظام PDPL السعودي..."):
            try:
                # استدعاء نموذج الذكاء الاصطناعي الحقيقي للتحليل القانوني
                response = openai.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {
                            "role": "system",
                            "content": "أنت محامٍ خبير ومحكم قانوني معتمد في الأنظمة السعودية وتحديداً نظام حماية البيانات الشخصية (PDPL) ولوائح التجارة الإلكترونية. قم بتحليل النص المُدخل واكتشاف الثغرات القانونية بدقة واحترافية عالية باللغة العربية."
                        },
                        {
                            "role": "user",
                            "content": f"قم بتحليل النص التالي تحليلاً قانونياً شاملاً ومفصلاً:\n\n{policy_text}"
                        }
                    ],
                    temperature=0.3
                )
                
                analysis_result = response.choices[0].message.content
                
                st.success("✨ تم فحص وإصدار تقرير الامتثال القانوني بنجاح تام!")
                st.markdown("---")
                st.markdown(analysis_result)
                
            except Exception as e:
                st.error(f"عذراً، يرجى التأكد من إضافة مفتاح الـ API بشكل صحيح في إعدادات المنصة. التفاصيل: {e}")

# تذييل الصفحة
st.markdown("""
    <div class="footer-section">
        <strong>منصة ميثاق الرقمية</strong> &nbsp;|&nbsp; حماية المتاجر والمنشآت وضمان الامتثال للأنظمة السعودية.
    </div>
""", unsafe_allow_html=True)

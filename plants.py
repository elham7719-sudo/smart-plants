
import streamlit as st
import google.generativeai as genai
from PIL import Image

# إعداد مفتاح الـ API - قومي بلصق مفتاحك بين علامات التنصيص بالأسفل
genai.configure(api_key="AIzaSyDI0nxZzskWnZZ6E4Osk5iDh7pqFxRrr0w")

st.set_page_config(page_title="مستكشف النباتات الطبية", page_icon="🌿")
st.markdown("<h1 style='text-align: center; color: #2E7D32;'>🌿 مستكشف النباتات الطبية الذكي</h1>", unsafe_allow_html=True)

option = st.radio("اختر طريقة إدخال الصورة:", ("استخدام الكاميرا", "رفع ملف من الجهاز"))

image_file = None
if option == "استخدام الكاميرا":
    image_file = st.camera_input("التقط صورة للنبتة")
else:
    image_file = st.file_uploader("اختر صورة نبتة...", type=["jpg", "jpeg", "png"])

if image_file is not None:
    img = Image.open(image_file)
    st.image(img, caption='الصورة المختارة', use_column_width=True)
    
    if st.button("تحليل النبتة ومعرفة الفوائد ✨"):
        with st.spinner('جاري التحليل...'):
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                prompt = "تعرف على هذه النبتة واذكر اسمها العلمي، فوائدها الطبية، ووصفة لاستخدامها."
                response = model.generate_content([prompt, img])
                st.success("النتيجة:")
                st.write(response.text)
            except Exception as e:
                st.error(f"حدث خطأ: {e}")

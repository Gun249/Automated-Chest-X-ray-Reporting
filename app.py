# app.py
from model.train import predict

import streamlit as st
from PIL import Image

st.header("🖼️ Automated Chest X-ray Reporting")

uploaded_file = st.file_uploader(
    "Please upload your picture for prediction!", 
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    st.image(image, caption='รูปภาพที่อัปโหลด', use_container_width =True)
    
    st.write("---") 

    # สร้างปุ่มให้ผู้ใช้กดเพื่อเริ่มการทำนายผล
    if st.button('🚀 ทำการทายผล (Predict)'):
        # แสดง Spinner ขณะที่กำลัง "ประมวลผล"
        with st.spinner('กำลังวิเคราะห์รูปภาพ โปรดรอสักครู่...'):
            # เรียกใช้ฟังก์ชันจำลองการทำนาย
            label, confidence = predict(image)
        
        # แสดงผลลัพธ์หลังจากประมวลผลเสร็จ
        st.subheader("ผลการทำนาย:")
        
        # ใช้ st.success สำหรับการแสดงผลที่เป็นบวก
        st.success(f"**ผลลัพธ์:** {label}") 
        
        # ใช้ st.info สำหรับการแสดงข้อมูลเพิ่มเติม
        st.info(f"**ความมั่นใจ (Confidence):** {confidence:.2f}%")
        
        # แสดง Progress Bar ตามค่าความมั่นใจ
        st.progress(int(confidence))

else:
    st.info("กรุณาอัปโหลดรูปภาพเพื่อเริ่มต้นใช้งาน")
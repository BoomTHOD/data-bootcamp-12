# 🍕 Data Analysis Project: Sales & Customer Segmentation

โปรเจกต์นี้เป็นการนำข้อมูลการขายและพฤติกรรมลูกค้ามาวิเคราะห์เพื่อหา Insight ทางธุรกิจ โดยแบ่งการทำงานออกเป็น 2 ส่วนหลัก คือการวิเคราะห์ยอดขายร้านอาหารและการทำ Customer Segmentation

## 📊 Project Overview
* **Part 1: Pizza Sales Analysis** - วิเคราะห์แนวโน้มการขายและเมนูยอดนิยมเพื่อช่วยในการจัดการ Inventory
* **Part 2: RFM Analysis** - การจัดกลุ่มลูกค้า (Segmentation) ตามพฤติกรรมการซื้อ เพื่อวางแผนกลยุทธ์ Marketing

## 🛠️ Tech Stack & Tools
* **Database Query:** SQL (ใช้สำหรับดึงข้อมูลและทำ Aggregation)
* **Visualization:** [ระบุเครื่องมือที่คุณใช้ เช่น Matplotlib, Seaborn หรือ Tableau]

## 🔍 Key Analysis & Insights
### 1. Pizza Sales Insights
* พบว่าช่วงเวลา [ระบุช่วงเวลา] เป็นช่วงที่มียอดขายสูงสุด
* เมนูที่สร้าง Revenue มากที่สุดคือ [ชื่อเมนู]
* พบว่าในช่วงเวลา 12.00-13.00 น. เป็นช่วงที่ขายดีที่สุดควรวางแผนการจัดการพนักงาน(staffing) ให้เพียงพอต่อการบริการในแต่ละจุด
* เมนูที่ควรจัดโปรโมขั่นเพื่อเรียกยอดขายหรือนำไปจัดชุดเซตเพื่อเพิ่ม Ticket AVG

### 2. RFM Segmentation Results
เราแบ่งกลุ่มลูกค้าโดยใช้เกณฑ์ Recency, Frequency และ Monetary:
* **Champions:** ลูกค้ากลุ่มที่ซื้อบ่อยและยอดสูง -> *กลยุทธ์: มอบสิทธิพิเศษสะสมแต้ม*
* **At Risk:** ลูกค้าที่เคยซื้อเยอะแต่หายไปนาน -> *กลยุทธ์: ส่งโปรโมชั่น Win-back*

### 3. Zomato Market Analysis & Pricing Strategy
วิเคราะห์ตลาดร้านอาหารเพื่อหาความสัมพันธ์ระหว่าง "ราคา", "คะแนนรีวิว" และ "ประเภทอาหาร" ในแต่ละพื้นที่
Key Findings:
Rating vs. Cost: ร้านที่มีบริการสั่งออนไลน์ (Online Order) มักจะได้คะแนน Rating เฉลี่ยสูงกว่าร้านที่ไม่มีอย่างเห็นได้ชัด (เฉลี่ย 4.14 เทียบกับ 3.62)
Popular Cuisines: อาหารกลุ่ม North Indian และกลุ่ม Cafe/Italian เป็นตลาดใหญ่ที่มีการแข่งขันสูงและมีจำนวน Votes หนาแน่น
Location Insights: ย่าน Electronic City เป็นพื้นที่ที่มีจำนวนร้านอาหารหนาแน่นที่สุด (840 ร้าน) แต่มีคะแนนเฉลี่ยกลางๆ ที่ 3.49 ซึ่งเป็นโอกาสในการเจาะตลาดร้านอาหารคุณภาพสูง

## 📁 File Structure
* `Project/SQL.PY`: บรรจุ SQL Queries ทั้งหมดที่ใช้ในการทำ RFM และ Sales Analysis
* `Visualization/`: โฟลเดอร์เก็บกราฟและผลลัพธ์จากการวิเคราะห์

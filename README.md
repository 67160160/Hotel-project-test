# 🏨 HotelStay - ระบบจองที่พักออนไลน์ (Frontend Scaffold)

โปรเจกต์นี้เป็นส่วนหนึ่งของกิจกรรมการเรียนรู้ในการแปลง User Journey สู่โค้ดจริง โดยเน้นการพัฒนาชิ้นส่วนหน้าบ้าน (Frontend) ด้วย HTML, CSS และ JavaScript ธรรมดา (Vanilla JS) ไม่พึ่งพา Framework ออกแบบโครงสร้างรองรับแบบ Single-Page Application (SPA) เพื่อให้ง่ายต่อการเรียนรู้ และพร้อมส่งต่อไปยังขั้นตอนการรันผ่าน Docker Compose ร่วมกับ FastAPI ในสัปดาห์ถัดไป

---

## 👥 บริบทของระบบ (System Context) & Persona

* **Persona**: "คุณต้น" อายุ 30 ปี วางแผนทริปครอบครัวช่วงวันหยุดยาว ต้องการที่พักราคาคุ้มค่าใกล้แหล่งท่องเที่ยว[cite: 3]
* **เป้าหมาย (Goal)**: เปรียบเทียบและจองที่พักที่ตรงงบประมาณ วันที่ และจำนวนผู้เข้าพัก พร้อมมั่นใจว่าจองสำเร็จจริง[cite: 3]
* **Pain Points ที่ระบบนี้ช่วยแก้ไข**:
    * ราคาที่แสดงหน้ารายการไม่รวมภาษี/ค่าธรรมเนียม ทำให้ราคาจริงสูงกว่าที่คาด (ระบบนี้ใช้ราคาสุทธิ Net Price โชว์โปร่งใสตั้งแต่ขั้นตอนเลือกห้อง)[cite: 3]
    * ไม่แน่ใจว่าการจองสำเร็จจริงหรือไม่ (ระบบมีหน้าตั๋วยืนจอง Voucher พร้อมรหัสการจองชัดเจนหลังทำรายการสำเร็จ)[cite: 3]

---

## 🗺️ User Journey Steps ที่ระบบรองรับในปัจจุบัน
1. **หน้าค้นหาและรายการที่พัก (Stage 1)**: ค้นหาตามจุดหมาย วันเช็คอิน-เช็คเอาท์ และจำนวนผู้เข้าพัก พร้อมฟังก์ชันกรองชื่อที่พัก[cite: 3]
2. **หน้าเลือกห้องพัก (Stage 2)**: แสดงประเภทห้องที่ว่างและสิ่งอำนวยความสะดวกสำหรับครอบครัวแยกตามโรงแรม[cite: 3]
3. **หน้ากรอกข้อมูล & สรุปราคา (Stage 3)**: มีกล่องสรุปราคา Net Price ที่ชัดเจนก่อนกดยืนยัน และแบบฟอร์มเก็บข้อมูลผู้เข้าพักหลัก[cite: 3]
4. **หน้าสรุปผลสำเร็จ (Stage 4)**: แสดงรหัสการจอง (Booking Confirmation Code) เพื่อให้ผู้ใช้มั่นใจว่าจองสำเร็จจริง[cite: 3]

---


---

## 🚀 วิธีการติดตั้งและรันโปรเจกต์ (How to Run)

### 🔹 สำหรับการทดสอบใช้งานบนเครื่อง Local (สัปดาห์ที่ 1)
1. ดาวน์โหลดหรือคัดลอกไฟล์โค้ดระบบนี้ไว้ในเครื่องคอมพิวเตอร์ของคุณ
2. ดับเบิ้ลคลิก (Double-click) ที่ไฟล์หน้าเว็บหลักเพื่อเปิดใช้งานผ่านเว็บเบราว์เซอร์ (เช่น Google Chrome, Microsoft Edge, Safari) ได้ทันทีโดยไม่ต้องติดตั้งซอฟต์แวร์เพิ่มเติม

### 🔹 สำหรับการรันระบบเต็มรูปแบบ (สัปดาห์ที่ 2 เป็นต้นไป)
เมื่อนำระบบเข้าสู่โครงสร้าง Scaffold เต็มรูปแบบแล้ว สามารถสั่งรัน Backend + DB + Frontend ได้ด้วยคำสั่งเดียว[cite: 2]:
```bash
docker compose up
├── app/                        # โค้ดหลักของแอปพลิเคชัน
│   ├── api/                    # API Endpoints และ Routers
│   │   └── v1/
│   │       ├── endpoints/      # Controllers (auth, users, items)
│   │       └── router.py       # Central Route Aggregator
│   ├── core/                   # ระบบส่วนกลาง (Database, Security, JWT)
│   ├── models/                 # SQLAlchemy Database Entities
│   ├── schemas/                # Pydantic Schemas (Data Validation)
│   ├── services/               # Business Logic & Database Queries
│   ├── config.py               # Application Settings & Env Config
│   └── main.py                 # Application Entry Point
├── tests/                      # Automated Unit Tests
├── .dockerignore
├── .env                        # Environment Variables
├── .env.example
├── Dockerfile                  # Container Build Config
├── docker-compose.yml          # Container Orchestration Config
├── README.md
└── requirements.txt            # Python Dependencies

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

⚡ วิธีการรันระบบ (How to Run)

เลือกวิธีรันที่เหมาะสมกับรูปแบบการทำงานของคุณ:

🟢 วิธีที่ 1: รันทุกอย่างด้วย Docker Compose (แนะนำ)

เหมาะสำหรับการรันระบบทั้งหมดโดยไม่ต้องลง Python หรือ Node.js บนเครื่อง





เปิดโปรแกรม Docker Desktop บนเครื่องคอมพิวเตอร์



สร้างไฟล์ .env จากไฟล์ตัวอย่าง:

Bash

cp .env.example .env




สั่ง Build และรันระบบ:

Bash

docker compose up --build




การเข้าใช้งาน:





Backend API Docs (Swagger): http://localhost:8000/docs



Backend API Docs (ReDoc): http://localhost:8000/redoc

หากต้องการหยุดรัน ให้กด Ctrl + C บน Terminal หรือพิมพ์:

Bash

docker compose down


🟡 วิธีที่ 2: รัน Backend แบบ Local (สำหรับพัฒนาโค้ด Python)

เหมาะสำหรับการแก้โค้ดฝั่ง Backend และต้องการทดสอบรันอย่างรวดเร็ว





สร้างและเปิดใช้งาน Virtual Environment:





Windows:

Bash

python -m venv venv
.\venv\Scripts\activate




macOS / Linux:

Bash

python3 -m venv venv
source venv/bin/activate




ติดตั้ง Dependencies ทั้งหมด:

Bash

pip install -r requirements.txt




เตรียมไฟล์ .env:

Bash

cp .env.example .env




สั่งรัน FastAPI Server:

Bash

uvicorn app.main:app --reload --port 8000


🔵 วิธีที่ 3: รัน Frontend (กรณีมีส่วนหน้าเว็บ)

หากมีโค้ดฝั่งหน้าเว็บอยู่ในโฟลเดอร์ frontend:





เปิด Terminal หน้าต่างใหม่ แล้วเข้าไปที่โฟลเดอร์ frontend:

Bash

cd frontend




ติดตั้ง Package ของ Node.js:

Bash

npm install




สั่งรันระบบ Development Server:

Bash

npm run dev




เข้าดูหน้าเว็บตาม URL ที่ปรากฏบน Terminal (ปกติคือ http://localhost:5173 หรือ http://localhost:3000)

📑 ขั้นตอนการทดสอบสิทธิ์และทดสอบ API





เปิดเบราว์เซอร์ไปที่ Swagger UI (http://localhost:8000/docs)



ลงทะเบียนผู้ใช้: ไปที่ Endpoint POST /api/v1/users/ เพื่อสร้างบัญชี



เข้าสู่ระบบ: ไปที่ Endpoint POST /api/v1/auth/login กรอก Email/Password เพื่อขอรับ Access Token



ยืนยันตัวตน: คัดลอก Token ที่ได้ -> กดปุ่ม Authorize (มุมขวาบนของ Swagger) -> วาง Token ลงในช่อง แล้วกด Authorize



ทดสอบใช้งาน: ทดสอบสั่งสร้างหรือลบสินค้าผ่าน POST /api/v1/items/ หรือ DELETE /api/v1/items/{id}

🧪 การรัน Automated Tests

สั่งรัน Unit Test เพื่อตรวจสอบความถูกต้องของระบบ:

Bash

# บนเครื่อง Local
pytest

# บน Docker Container
docker compose exec web pytest


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

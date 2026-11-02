# Digital Threat Intelligence Dashboard
**Professional Enterprise Threat Intelligence Platform — React Edition**

แพลตฟอร์มวิเคราะห์และประเมินภัยคุกคามในระบบนิเวศดิจิทัล (Digital Threat Intelligence) ระดับ Enterprise พัฒนาด้วยสถาปัตยกรรม **React 18 + TypeScript + Vite + Tailwind CSS** ควบคู่กับ **Python FastAPI Backend** ครอบคลุมการวิเคราะห์ข้อมูลความมั่นคงปลอดภัยไซเบอร์ทั้งในระดับสากลและประเทศไทยจากชุดข้อมูลจริง 6 ชุด

---

## 🚀 สรุปสถานะการรันระบบ (Live Services)

ระบบกำลังรันและพร้อมใช้งานทันทีบนเครื่องของคุณ:

| ส่วนงาน | สภาพแวดล้อม | URL ที่เปิดใช้งาน | หน้าที่ |
|---|---|---|---|
| **Integrated Platform (แนะนำ)** | FastAPI + Production React Dist | **`http://localhost:8000`** | เข้าใช้งาน Full Web Application รวม UI และ API ในพอร์ตเดียว |
| **Frontend Dev Server** | Vite HMR Dev Server | **`http://localhost:5173`** | หน้าจอ React Dev สำหรับการพัฒนาต่อยอดแบบ Real-time |
| **REST API Documentation** | Swagger / OpenAPI | **`http://localhost:8000/docs`** | เอกสารและเครื่องมือทดสอบ API ทุก Endpoint |

---

## 🛠️ เทคโนโลยีที่ใช้ในระบบ (Technology Stack)

### Frontend (User Interface & Visualizations)
- **React 18 & TypeScript:** โครงสร้างหลักแบบ Component-driven มี Type Safety 100%
- **Vite:** โมเดิร์นบิลด์ทูลสำหรับการพัฒนาที่รวดเร็วและบันเดิล Production เล็กกะทัดรัด
- **Tailwind CSS:** การจัดสไตล์ Dark Intelligence Platform (Background `#0B1120`, Card `#151F32`, Accent `#3B82F6`, `#06B6D4`)
- **Lucide React:** ไอคอนระดับองค์กรที่อ่านง่าย สะอาดตา และไม่มีการใช้ Emoji เป็นไอคอนหลัก
- **Recharts:** กราฟสถิติแบบ Interactive รองรับ Tooltip, Hover, Responsive Layout และ Dark Theme
- **React Router Dom (v6):** การนำทางแบบ Single Page Application (SPA) ข้าม 4 หน้าหลักอย่างราบรื่น

### Backend (Analytical & Data Processing Engine)
- **FastAPI & Uvicorn:** ASGI Web Framework ประสิทธิภาพสูง รองรับ Async REST API
- **Pandas & NumPy:** ทำความสะอาดข้อมูล จัดการ Missing Data, Datetime และ Vectorized Calculation
- **Scikit-learn:** อัลกอริทึม Latent Dirichlet Allocation (LDA) สำหรับ Topic Modeling และ TF-IDF
- **SciPy:** สถิติทดสอบสมมติฐาน Chi-Square Test of Independence และการคำนวณ Cramer's V
- **Statsmodels:** การวิเคราะห์อนุกรมเวลา Moving Average, Robust Z-Score (MAD), IQR Outlier Detection
- **PyArrow:** Parquet Caching Layer ช่วยให้โหลดข้อมูลหลายหมื่นเรคคอร์ดได้ในเสี้ยววินาที

---

## 📂 โครงสร้างระบบ (Project Structure)

```text
final basic_program/
├── backend/                    # FastAPI Backend Application
│   ├── main.py                 # จุดเข้าใช้งานหลัก, CORS, Mount React Static Dist
│   ├── api/                    # API Routers แยกตามโดเมน
│   │   ├── overview.py         # GET /api/overview
│   │   ├── ai_risk.py          # GET /api/ai-risk
│   │   ├── disinformation.py   # GET /api/disinformation
│   │   ├── scam.py             # GET /api/scam
│   │   ├── data_quality.py     # GET /api/data-quality
│   │   └── filters.py          # GET /api/filters
│   └── services/               # โมดูลวิเคราะห์และโหลดข้อมูล
│       ├── data_loader.py      # Singleton DataLoader สำหรับอ่าน Parquet Caches
│       └── analytics.py        # คำนวณสถิติ, Anomaly, Pareto, Chi-Square, LDA
├── frontend/                   # React + TypeScript + Vite Application
│   ├── src/
│   │   ├── api/client.ts       # Axios API Client เชื่อมต่อ Backend
│   │   ├── components/         # Reusable UI & Layout Components
│   │   │   ├── common/         # KpiCard, InsightBox, LoadingSkeleton, DataQualityModal
│   │   │   └── layout/         # Sidebar, Topbar, MainLayout
│   │   ├── pages/              # 4 หน้าหลักของระบบ
│   │   │   ├── OverviewPage.tsx
│   │   │   ├── AiRiskPage.tsx
│   │   │   ├── DisinformationPage.tsx
│   │   │   └── OnlineScamPage.tsx
│   │   ├── types/index.ts      # TypeScript Interfaces
│   │   ├── App.tsx             # Route Configuration
│   │   └── index.css           # Tailwind Directives & Enterprise Styling
│   ├── tailwind.config.js      # ปรับแต่งธีมสี Dark Intelligence
│   └── dist/                   # Production Bundle พร้อมเสิร์ฟผ่าน FastAPI
├── Dataset/                    # ข้อมูลดิบต้นฉบับทั้ง 6 ชุด (Read-only)
│   ├── 00_Data_Guide_TH.pdf
│   ├── 01_AI_Incident_Database/
│   ├── 02_Freedom_on_the_Net/
│   ├── 03_EUvsDisinfo/
│   └── 04_Thai_Disinformation_and_Scams/
├── data/                       # Data Pipeline
│   ├── preprocessor.py         # สคริปต์ Clean และสร้าง Parquet Cache
│   └── cache/                  # Parquet Caches
├── requirements.txt            # Python Dependencies
└── README.md                   # คู่มือระบบ
```

---

## 📊 รายละเอียดฟังก์ชันใน 4 หน้าหลัก (Page Details)

### 1. PAGE 1: OVERVIEW — ภาพรวมภัยคุกคามดิจิทัล
- **6 KPI Cards:** แสดงตัวเลข แยกหน่วย ช่วงเวลา และแหล่งที่มาอย่างเคร่งครัด
  - AI Incidents: `1,775` เหตุการณ์ (AIID)
  - Disinformation: `18,249` บทความ (EUvsDisinfo)
  - AFNC Total Posts: `17,726` โพสต์ (ศูนย์ต่อต้านข่าวปลอม ไทย)
  - Confirmed Fake News: `9,520` เรื่อง (53.7% ของโพสต์ AFNC)
  - Online Scam Cases: `381,390` คดี (หรือ `302,079` คดีเมื่อตัดสัปดาห์ผิดปกติ)
  - Financial Loss: `18,177.4` ล้านบาท (ACSC)
- **Interactive Visualizations:**
  1. AI Incident Annual Trend (แท่งรายปีพร้อมการเติบโตแบบก้าวกระโดดหลัง 2023)
  2. EUvsDisinfo Trend (เส้นรายปีแสดงพีคช่วงปี 2020–2022)
  3. AFNC Verdict Distribution (Donut Chart สัดส่วนคำตัดสิน)
  4. Online Scam Cases & Loss Weekly Trend (คดีและมูลค่าความเสียหายรายสัปดาห์)
- **Data Coverage Matrix:** แสดงตารางขอบเขตข้อมูล ช่วงเวลา และรอบการอัปเดตของทั้ง 6 ฐานข้อมูล

---

### 2. PAGE 2: AI & DIGITAL RISK — ความเสี่ยง AI และเสรีภาพเน็ต
- **ตอบคำถามหลัก:**
  - เหตุการณ์ AI เพิ่มขึ้นอย่างไร: เติบโตมากกว่า 70% ต่อปีหลังการแพร่หลายของ Generative AI
  - หมวดความเสี่ยงที่พบมากที่สุด: *Malicious Actors & Misuse (566 เหตุการณ์, 31.9%)* และ *AI system safety/failure (17.6%)*
  - กลุ่มผู้ใช้งานที่ก่อเหตุการณ์สูงสุด: กลุ่ม *Scammers (มิจฉาชีพ)* ติดอันดับ 1 ตามด้วยบริษัทยักษ์ใหญ่เทคโนโลยี
  - คะแนน Freedom on the Net ของไทย: ได้คะแนน 39/100 (อยู่ในกลุ่ม *Not Free* ต่ำกว่าเกณฑ์ 40 คะแนนต่อเนื่อง 10 ปี)
- **Interactive Controls & Analysis:**
  - ตัวกรองช่วงปี (Slider/Dropdown), ตัวกรอง Risk Domain
  - ตารางเปรียบเทียบคะแนนเสรีภาพอินเทอร์เน็ต 72 ประเทศทั่วโลก พร้อมช่องค้นหาแบบเรียลไทม์
  - กราฟแท่งจำแนก 3 องค์ประกอบของคะแนน: *Obstacles to Access*, *Limits on Content*, *Violations of User Rights*
  - **ข้อพึงระวังระเบียบวิธีวิจัย:** ระบุคำเตือนชัดเจนว่า **ห้ามสรุปความสัมพันธ์เชิงเหตุและผล (No Causation)** ข้ามมิติข้อมูล

---

### 3. PAGE 3: DISINFORMATION — วิเคราะห์ข้อมูลบิดเบือนและข่าวปลอม
- **ตอบคำถามหลัก:**
  - หัวข้อข้อมูลบิดเบือนที่พบมากที่สุด: EUvsDisinfo เน้นสงครามในยูเครนและประเด็นนาซี ส่วนไทยเน้นเรื่องสุขภาพ มะเร็ง และนโยบายรัฐบาล
  - หมวดข่าวปลอมในไทยที่พบสูงสุด: หมวดนโยบายรัฐบาล (35.4%) และผลิตภัณฑ์สุขภาพ (21.4%)
  - ภาษาใน EUvsDisinfo: อังกฤษ (35.9%) รัสเซีย (31.9%) อาหรับ (18.9%)
- **เครื่องมือวิเคราะห์เชิงสถิติและ Machine Learning:**
  - **Chi-Square Test of Independence:** ทดสอบความสัมพันธ์ระหว่างหมวดหมู่ข่าวกับคำตัดสิน ($\chi^2 = 2,504.6, p < 0.001$, เซลล์ความถี่ต่ำกว่าเกณฑ์ 0.0% ผ่านเกณฑ์ $\le 20\%$) ค่า Cramer's V = 0.285 สะท้อนความสัมพันธ์ระดับปานกลาง
  - **Latent Dirichlet Allocation (LDA):** แสดงการ์ดผลลัพธ์การจำแนก 4 หัวข้อแฝงพร้อมคำสำคัญ
  - **Top Keywords & Tags:** คำสำคัญยอดนิยมของข่าวต่างประเทศและแท็กประเด็นของไทย
  - **Interactive Drill-Down Table:** ตารางค้นหาและคลิกดูตัวอย่างข้อความจริงจากฐานข้อมูล

---

### 4. PAGE 4: ONLINE SCAM — อาชญากรรมหลอกลวงออนไลน์
- **ตอบคำถามหลัก:**
  - สถิติคดีเฉลี่ย: 5,000–7,500 คดี/สัปดาห์ เสียหายสัปดาห์ละ 250–450 ล้านบาท
  - ประเภทมิจฉาชีพที่สร้างความเสียหายสูงสุด: *หลอกให้ลงทุน (Investment Scams)* สร้างความเสียหายสูงสุดเฉลี่ยต่อคดี ขณะที่ *หลอกซื้อขายสินค้า* พบบ่อยสุดในด้านจำนวนคดี
  - **Pareto Analysis (กฎ 80/20):** ความเสียหายสะสมกว่า 80% กระจุกตัวในมิจฉาชีพเพียง 2–3 รูปแบบหลัก
- **การตรวจจับความผิดปกติและสหสัมพันธ์:**
  - ตรวจจับสัปดาห์ผิดปกติด้วย **Robust Z-Score (Median/MAD)** และ **IQR Outlier Bounds**
  - แสดงและไฮไลต์สัปดาห์ **16–22 ส.ค. 2026** (79,311 คดี / 2,775 ล้านบาท สูงกว่าปกติ 13 เท่า) พร้อมปุ่ม Toggle กรองออกเพื่อไม่ให้ค่าสถิติผิดเพี้ยน
  - เมทริกซ์สหสัมพันธ์ (Pearson / Spearman) ระหว่างคดีออนไลน์กับข่าวปลอมใน `weekly_panel`
  - สหสัมพันธ์แบบเหลื่อมเวลา (Lagged Cross-Correlation -4 ถึง +4 สัปดาห์) พบค่าความสัมพันธ์สูงสุดที่ Lag 0 ถึง +1
  - **Short-Term Trend Projection:** การประมาณการ 4 สัปดาห์ข้างหน้าด้วย Moving Average Drift ควบคู่กับแถบความเชื่อมั่น 95% CI พร้อมระบุคำเตือนข้อจำกัดของข้อมูลอย่างรัดกุม

---

## 💻 คู่มือการติดตั้งและเปิดใช้งาน (Setup & Run Guide)

### 1. การติดตั้ง Dependencies
```powershell
# ติดตั้ง Python Packages (แนะนำผ่าน uv หรือ pip)
& "$HOME\.local\bin\uv.exe" pip install -r requirements.txt

# ติดตั้ง Node.js Packages สำหรับ Frontend
$env:PATH = "$HOME\.local\node;" + $env:PATH
cd frontend
npm install
npm run build
cd ..
```

### 2. การเปิดใช้งานเซิร์ฟเวอร์
```powershell
# เปิดใช้งาน FastAPI Server (เสิร์ฟทั้ง REST API และ React Web App ที่พอร์ต 8000)
.venv\Scripts\uvicorn.exe backend.main:app --port 8000 --host 0.0.0.0
```

เปิดเว็บเบราว์เซอร์ไปที่: **`http://localhost:8000`**

---

## 🛡️ มาตรฐานความถูกต้องของข้อมูล (Data Integrity Protocols)
1. **รักษาข้อมูลดิบต้นฉบับ 100%:** ไม่มีการดัดแปลงหรือเขียนทับไฟล์ใน `Dataset/`
2. **แยก Missing Data ออกจาก Zero:** ในสถิติรายสัปดาห์ สัปดาห์ที่ไม่มีข้อมูล ACSC จะคงเป็น `NaN` ไม่เติมด้วย 0
3. **โปร่งใสเรื่องสัปดาห์ที่ถูก Flag:** ไฮไลต์สัปดาห์สงกรานต์และสัปดาห์ 16–22 ส.ค. 2026 พร้อมสวิตช์ Toggle
4. **ไม่สรุปความสัมพันธ์เป็นเหตุและผล (Correlation $\neq$ Causation):** ทุกกราฟมีคำอธิบายข้อจำกัดเชิงสถิติอย่างถูกต้องตามหลักวิชาการ

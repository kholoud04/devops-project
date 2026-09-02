'''
from fastapi import FastAPI

app = FastAPI(title="DevOps Demo App")

@app.get("/")
def read_root():
    return {"status": "success", "message": "DevOps Pipeline is Working!", "version": "v1.0.0"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
'''

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# مسار الصفحة الرئيسية للمسبحة
@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>المسبحة الإلكترونية</title>
        <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap" rel="stylesheet">
        <style>
            * { box-sizing: border-box; }
            body {
                font-family: 'Tajawal', sans-serif;
                background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
                color: #f8fafc;
                display: flex;
                align-items: center;
                justify-content: center;
                min-height: 100vh;
                margin: 0;
                padding: 20px;
            }
            .card {
                background: rgba(255, 255, 255, 0.05);
                backdrop-filter: blur(12px);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 20px;
                padding: 30px;
                max-width: 440px;
                width: 100%;
                text-align: center;
                box-shadow: 0 20px 35px rgba(0, 0, 0, 0.4);
            }
            h1 { margin-top: 0; color: #38bdf8; font-size: 26px; }
            select {
                width: 100%;
                padding: 12px 15px;
                border-radius: 12px;
                border: 1px solid rgba(255, 255, 255, 0.2);
                background: #1e293b;
                color: #f8fafc;
                font-size: 16px;
                font-family: 'Tajawal', sans-serif;
                outline: none;
                margin-bottom: 25px;
                cursor: pointer;
            }
            .counter-box {
                font-size: 72px;
                font-weight: bold;
                color: #38bdf8;
                margin: 15px 0;
                user-select: none;
                transition: transform 0.1s ease;
            }
            .btn-click {
                width: 140px;
                height: 140px;
                border-radius: 50%;
                background: linear-gradient(135deg, #0284c7, #0369a1);
                border: none;
                color: white;
                font-size: 22px;
                font-weight: bold;
                font-family: 'Tajawal', sans-serif;
                cursor: pointer;
                box-shadow: 0 10px 20px rgba(2, 132, 199, 0.4);
                transition: transform 0.1s, box-shadow 0.1s;
                margin: 15px auto;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            .btn-click:active {
                transform: scale(0.92);
                box-shadow: 0 4px 10px rgba(2, 132, 199, 0.2);
            }
            .btn-reset {
                background: rgba(239, 68, 68, 0.15);
                color: #f87171;
                border: 1px solid rgba(239, 68, 68, 0.3);
                padding: 8px 20px;
                border-radius: 8px;
                cursor: pointer;
                font-family: 'Tajawal', sans-serif;
                font-size: 14px;
                margin-top: 15px;
                transition: background 0.2s;
            }
            .btn-reset:hover {
                background: rgba(239, 68, 68, 0.3);
            }
            .footer-tag {
                margin-top: 25px;
                font-size: 12px;
                color: #64748b;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>المسبحة الإلكترونية 📿</h1>
            
            <select id="dhikrSelect" onchange="resetCounter()">
                <option value="سبحان الله">سبحان الله</option>
                <option value="الحمد لله">الحمد لله</option>
                <option value="لا إله إلا الله">لا إله إلا الله</option>
                <option value="الله أكبر">الله أكبر</option>
                <option value="لا حول ولا قوة إلا بالله">لا حول ولا قوة إلا بالله</option>
                <option value="أستغفر الله">أستغفر الله</option>
                <option value="سبحان الله وبحمده">سبحان الله وبحمده</option>
                <option value="سبحان الله العظيم">سبحان الله العظيم</option>
                <option value="اللهم صلِّ وسلّم على نبينا محمد">اللهم صلِّ وسلّم على نبينا محمد</option>
                <option value="حسبي الله ونعم الوكيل">حسبي الله ونعم الوكيل</option>
            </select>

            <div class="counter-box" id="counter">0</div>
            <button class="btn-click" onclick="countUp()"> </button>
            <br>
            <button class="btn-reset" onclick="resetCounter()">إعادة ضبط العداد</button>

            <div class="footer-tag"> </div>
        </div>

        <script>
            let count = 0;
            const counterElement = document.getElementById('counter');

            function countUp() {
                count++;
                counterElement.innerText = count;
                counterElement.style.transform = 'scale(1.1)';
                setTimeout(() => {
                    counterElement.style.transform = 'scale(1)';
                }, 100);
            }

            function resetCounter() {
                count = 0;
                counterElement.innerText = count;
            }
        </script>
    </body>
    </html>
    """

# مسار إضافي لفحص صحة التطبيق وضمان نجاح الـ Testing
@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "electronic-misbaha"}
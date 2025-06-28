# استخدم صورة رسمية من Python
FROM python:3.11-slim

# إعداد المتغيرات
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# تثبيت المتطلبات الأساسية
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# تعيين مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ ملفات المشروع
COPY . .

# تثبيت الباكيجات
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# فتح منفذ Streamlit
EXPOSE 8501

# أمر التشغيل
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

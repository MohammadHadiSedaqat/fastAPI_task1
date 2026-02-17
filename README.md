# # 🚀 FastAPI Explorer & Modern UI

This project is a full-stack starter application featuring a FastAPI backend and a Modern, Responsive Web UI. It allows users to interact with various API endpoints dynamically through a polished interface.

---

## 🇮🇷 راهنمای فارسی (Persian Guide)

<div dir="rtl">

### 📝 معرفی پروژه
این پروژه یک ابزار تعاملی و مدرن برای کار با APIهای طراحی شده با FastAPI است. رابط کاربری (UI) این پروژه با استفاده از HTML5، CSS3 و جاوااسکریپت خام (Vanilla JS) ساخته شده تا بدون نیاز به کتابخانه‌های سنگین، تجربه‌ای سریع و زیبا ارائه دهد.

### 🛠 ویژگی‌های کلیدی
* بک‌بند هوشمند: استفاده از FastAPI برای مدیریت درخواست‌ها و پاسخ‌های JSON.
* رابط کاربری مدرن: طراحی شده با افکت‌های شیشه‌ای (Glassmorphism) و پس‌زمینه متحرک Gradient.
* پیش‌نمایش زنده URL: نمایش لحظه‌ای آدرس درخواست (Endpoint) همزمان با تایپ کاربر.
* پشتیبانی کامل از CORS: تنظیم شده برای جلوگیری از خطاهای دسترسی هنگام ارتباط فرانت‌ند با سرور.
* پاسخ‌های انیمیشنی: دارای افکت Flash هنگام دریافت داده‌های جدید از سرور.

### 📂 ساختار فایل‌ها
* train.py: کدهای پایتون شامل تنظیمات Middleware و نقاط پایانی (Endpoints).
* index.html: ساختار رابط کاربری و منطق برنامه برای ارسال درخواست‌های Fetch.
* style.css: تمامی استایل‌ها، انیمیشن‌ها و طراحی ریسپانسیو.

### 🚀 نحوه اجرا و راه‌اندازی
۱. نصب کتابخانه‌ها:
ابتدا مطمئن شوید Python روی سیستم شما نصب است، سپس دستور زیر را بزنید:
pip install fastapi uvicorn

۲. اجرای سرور بک‌بند:
فایل اصلی پایتون را با استفاده از Uvicorn اجرا کنید:
uvicorn train:app --reload

۳. مشاهده رابط کاربری:
فایل index.html را در مرورگر باز کنید. حالا می‌توانید با تغییر منوی کشویی و وارد کردن مقادیر، عملکرد API را تست کنید.

</div>

---

## 🇬🇧 English Guide

### 📝 Project Overview
A sleek, interactive tool to explore FastAPI endpoints. It features a reactive frontend that builds request URLs in real-time and displays JSON responses in a clean, code-highlighted format.

### 🛠 Key Features
* High Performance: Powered by FastAPI for lightning-fast API responses.
* Modern UI/UX: Features a dynamic animated gradient background and responsive layout.
* Live URL Preview: Updates the request URL instantly as you type or change endpoints.
* CORS Enabled: Pre-configured middleware to allow cross-origin requests from the web UI.
* Visual Feedback: Includes animation triggers (flash effect) upon successful data retrieval.

### 📂 File Structure
* train.py: The Python backend containing API logic and CORS configuration.
* index.html: The frontend structure and asynchronous fetch logic.
* style.css: Custom styling, including the glassmorphism effect and animations.

### 🚀 Setup and Installation
1.  Install Dependencies:
    Make sure you have Python installed, then run:
    pip install fastapi uvicorn

2.  Run the Backend:
    Start the FastAPI server using Uvicorn:
    uvicorn train:app --reload

3.  Launch the UI:
    Simply open index.html in any modern web browser. Ensure the backend is running at http://127.0.0.1:8000.

---

### 🛣 API Endpoints Included
| Endpoint | Type | Description |
| :--- | :--- | :--- |
| / | Root | Returns a welcome "Hello World" message. |
| /user?name=... | Query | Demonstrates query parameter handling. |
| /hello/{name} | Path | Classic path-based greeting. |
| /username/{username} | Path | Specific user identification path. |
| /{name} | Direct | Catch-all style direct path parameter. |

---
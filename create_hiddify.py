import requests

MARZBAN_URL = "http://YOUR-SERVER-IP:8000"          # آدرس سرورت
API_KEY = "YOUR-ADMIN-API-TOKEN"                    # توکن API

data = {
    "username": "hiddify-user-1",                   # نام کاربری دلخواه
    "data_limit": 10 * 1024**3,                     # محدودیت حجم 10 گیگابایت
    "expiry_time": "30d",                           # اعتبار 30 روز
    "proxies": [
        {
            "type": "vless",
            "inbound_id": 1
        }
    ]
}

response = requests.post(
    f"{MARZBAN_URL}/api/users",
    headers={"Authorization": f"Bearer {API_KEY}"},
    json=data
)

if response.status_code == 201:
    user = response.json()
    sub_link = f"{MARZBAN_URL}/api/v1/user/{user['uuid']}/subscription"
    print("✅ اشتراک هیدفای ساخته شد!")
    print("لینک اشتراک:", sub_link)
else:
    print("❌ خطا در ساخت اشتراک:")
    print(response.status_code, response.text)

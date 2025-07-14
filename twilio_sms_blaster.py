import os
from twilio.rest import Client
import time
from datetime import datetime

# بيانات Twilio - عدّلها بنفسك هنا
ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
AUTH_TOKEN = "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"
TWILIO_NUMBER = "+14155551234"

def banner():
    os.system('clear')
    print("""[91m
██████╗ ██████╗  █████╗  ██████╗  █████╗ ███╗   ███╗███████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔══██╗████╗ ████║██╔════╝
██████╔╝██████╔╝███████║██║  ███╗███████║██╔████╔██║█████╗  
██╔═══╝ ██╔═══╝ ██╔══██║██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
██║     ██║     ██║  ██║╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
╚═╝     ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝

                By: i love dana, ruby, reema ❤️
    [0m""")

def send_sms(to_number, message_body, count):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    print("\n[⚔] بدأ الإرسال...\n")
    success = 0
    fail = 0
    log = []

    for i in range(count):
        try:
            msg = client.messages.create(
                body=message_body,
                from_=TWILIO_NUMBER,
                to=to_number
            )
            print(f"\033[92m[✔] الرسالة {i+1}/{count} تم إرسالها! SID: {msg.sid}\033[0m")
            log.append(f"✔ Message {i+1} SID: {msg.sid}")
            success += 1
        except Exception as e:
            print(f"\033[91m[✘] فشل في إرسال الرسالة {i+1}: {e}\033[0m")
            log.append(f"✘ Message {i+1} Failed: {e}")
            fail += 1
        time.sleep(1)  # تأخير لتفادي الحظر

    # حفظ التقرير
    with open("sms_report.txt", "w") as rep:
        rep.write("--- SMS Report ---\n")
        rep.write(f"To: {to_number}\n")
        rep.write(f"Date: {datetime.now()}\n")
        rep.write(f"Message: {message_body}\n")
        rep.write(f"Total Sent: {success}\n")
        rep.write(f"Total Failed: {fail}\n")
        rep.write("\nDetails:\n")
        rep.write("\n".join(log))

    print("\n📄 تم حفظ تقرير الإرسال في sms_report.txt\n")

def main():
    banner()
    to_number = input("📨 أدخل رقم الجوال المستهدف (مثال: +9665xxxxxxxx): ").strip()
    message_body = input("💬 أدخل نص الرسالة: ").strip()
    count = int(input("📦 عدد الرسائل (1-50): "))

    if count < 1 or count > 50:
        print("❌ العدد غير صحيح. يجب أن يكون بين 1 و 50.")
        return

    send_sms(to_number, message_body, count)

if __name__ == '__main__':
    main()

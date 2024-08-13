import random
from faker import Faker

fake = Faker()

def generate_spam_messages(count):
    # List of possible message templates in Thai related to OTP, scams, gambling, loans, etc.
    templates = [
        "สวัสดี รหัส OTP ของคุณสำหรับการตรวจสอบบัญชีคือ {otp}. กรุณาใส่รหัสเพื่อดำเนินการต่อ.",
        "เรียน คุณได้รับเลือกให้ได้รับรางวัลพิเศษ! ใช้รหัส {otp} เพื่อรับรางวัลของคุณตอนนี้!",
        "สวัสดี การทำธุรกรรมล่าสุดของคุณต้องการการตรวจสอบ. ใช้ OTP {otp} เพื่อยืนยันตัวตนของคุณ.",
        "แจ้งเตือน บัญชีของคุณถูกตั้งค่าสถานะสำหรับกิจกรรมที่ไม่ปกติ. ตรวจสอบด้วย OTP {otp}.",
        "ยินดีด้วย คุณได้รับบัตรของขวัญมูลค่า 100,000 บาท. ใส่ OTP {otp} เพื่อรับรางวัลของคุณ.",
        "สวัสดี คำขอรีเซ็ตรหัสผ่านของคุณได้รับแล้ว. ใช้ OTP {otp} เพื่อรีเซ็ตรหัสผ่านของคุณ.",
        "เรียน มีการพยายามเข้าสู่ระบบใหม่. ยืนยันด้วย OTP {otp} เพื่อรักษาความปลอดภัยบัญชีของคุณ.",
        "สวัสดี กรุณาใช้ OTP {otp} เพื่อเสร็จสิ้นการตั้งค่าประวัติส่วนตัวของคุณ. ใช้ได้ในเวลาจำกัดเท่านั้น!",
        "เร่งด่วน: บัญชีของคุณต้องการการตรวจสอบ. ใช้ OTP {otp} เพื่อหลีกเลี่ยงการระงับบัญชี.",
        "ข้อเสนอพิเศษสำหรับคุณ! ใช้ OTP {otp} เพื่อรับส่วนลด 20% สำหรับการซื้อครั้งถัดไป.",
        "🔥 โปรโมชั่นพิเศษ! คุณสามารถรับโบนัส 5000 บาทในการเล่นคาสิโนออนไลน์เพียงใช้รหัส {otp} 🔥",
        "💰 สมัครกู้เงินออนไลน์วันนี้ รับดอกเบี้ยต่ำพิเศษ! ใช้รหัส {otp} เพื่อยืนยันการสมัครของคุณ.",
        "🎉 ยินดีด้วย! คุณได้รับการอนุมัติสินเชื่อด่วน 10,000 บาท. ใช้ OTP {otp} เพื่อดำเนินการต่อ.",
        "🌟 โปรโมชั่นล่าสุด! เล่นเกมสล็อตและรับฟรี 100 สปิน ใช้ OTP {otp} เพื่อเริ่มเล่นเลย!",
        "🚀 สมัครตอนนี้เพื่อรับโบนัส 200% สำหรับการเดิมพันในเว็บพนัน! ใช้รหัส {otp} เพื่อรับโบนัส.",
        "🔒 การแจ้งเตือนความปลอดภัย: ใช้ OTP {otp} เพื่อล็อกอินเข้าบัญชีของคุณ.",
        "✨ โปรโมชั่นพิเศษ! รับเครดิตเพิ่ม 2,000 บาททันทีหลังจากสมัครสมาชิกใหม่และใช้รหัส {otp}.",
        "🎁 ลุ้นรับ iPhone 15 เมื่อสมัครสินเชื่อด่วนตอนนี้! ใช้รหัส {otp} เพื่อเข้าร่วม.",
        "🚨 บัญชีของคุณถูกล็อคชั่วคราว. กรุณาใช้ OTP {otp} เพื่อปลดล็อคและยืนยันตัวตนของคุณ.",
        "💸 รับดอกเบี้ย 0% ในการกู้ยืมครั้งแรก! ใช้ OTP {otp} เพื่อสมัครทันที.",
        "⚠️ การตรวจสอบความปลอดภัย: บัญชีของคุณถูกล็อกเพื่อป้องกัน. ใช้ OTP {otp} เพื่อยืนยันตัวตนของคุณ.",
        "💥 โปรโมชั่นฉลองครบรอบ! รับฟรีโบนัส 300% เมื่อเติมเงินครั้งแรก ใช้รหัส {otp} เพื่อรับสิทธิ์.",
        "📱 สมัครแพ็กเกจอินเทอร์เน็ตเร็วสูงวันนี้และรับฟรีข้อมูล 50GB! ใช้ OTP {otp} เพื่อสมัคร.",
        "🔔 คำเตือน: บัญชีของคุณอาจถูกบุกรุก. กรุณายืนยันการเข้าสู่ระบบด้วย OTP {otp}.",
        "📢 ประกาศ: รับฟรีเครดิตเดิมพัน 5,000 บาท เมื่อสมัครสมาชิกใหม่และใช้รหัส {otp}.",
        "💬 คุณมีข้อความใหม่! กรุณายืนยันตัวตนด้วย OTP {otp} เพื่ออ่านข้อความสำคัญของคุณ.",
        "🏆 โปรโมชั่นสุดพิเศษ! รับโบนัส 5,000 บาท เมื่อทำการฝากเงินครั้งแรก ใช้รหัส {otp} เพื่อรับสิทธิ์.",
        "🚨 ข้อควรระวัง: มีความพยายามในการเข้าสู่ระบบจากอุปกรณ์ใหม่. ใช้ OTP {otp} เพื่อยืนยัน.",
        "💥 โปรโมชั่นเติมเงินวันนี้ รับฟรี 200 บาททันที! ใช้รหัส {otp} เพื่อรับข้อเสนอ.",
        "🔑 รหัสยืนยันสำหรับเข้าสู่ระบบคือ {otp}. กรุณาใส่รหัสเพื่อดำเนินการต่อ.",
        "📧 คุณมีอีเมลใหม่รออยู่! ใช้ OTP {otp} เพื่อเข้าสู่ระบบและอ่านอีเมล.",
        "🎰 ลุ้นรางวัลใหญ่ในคาสิโนออนไลน์ของเรา! ใช้ OTP {otp} เพื่อเริ่มเล่น.",
        "🏠 สนใจลงทุนอสังหาฯ? ใช้ OTP {otp} เพื่อรับข้อเสนอพิเศษ!",
        "🔧 การยืนยันการซ่อมแซม: ใช้ OTP {otp} เพื่อยืนยันการบริการ.",
        "🛍️ ใช้ OTP {otp} เพื่อรับส่วนลด 50% สำหรับการสั่งซื้อครั้งถัดไป!",
        "🏦 ธนาคารของคุณต้องการ OTP {otp} เพื่อยืนยันการเข้าสู่ระบบ.",
        "💼 สินเชื่อธุรกิจด่วน รับเงินกู้ทันทีด้วย OTP {otp}.",
        "📱 รับซิมการ์ดฟรีเมื่อใช้ OTP {otp} สำหรับการสมัครวันนี้!",
        "📢 สนใจลงทุนในหุ้น? ใช้ OTP {otp} เพื่อรับคำแนะนำพิเศษ!",
        "🏢 การตรวจสอบการเข้าสู่ระบบสำหรับองค์กรของคุณ ใช้ OTP {otp}.",
        "🚗 โปรโมชั่นพิเศษสำหรับการประกันภัยรถยนต์! ใช้ OTP {otp} เพื่อรับส่วนลด.",
        "🎟️ รับบัตรกำนัลฟรีมูลค่า 500 บาท! ใช้ OTP {otp} เพื่อยืนยัน.",
        "🎲 ลุ้นรางวัลใหญ่ในคาสิโนออนไลน์ของเรา! ใช้ OTP {otp} เพื่อเริ่มเล่นทันที.",
        "🏠 ข้อเสนอพิเศษ! ลงทุนในอสังหาริมทรัพย์ด้วย OTP {otp}.",
        "💼 บริการสินเชื่อพิเศษสำหรับธุรกิจใหม่ ใช้ OTP {otp} เพื่อสมัคร.",
        "📲 รับอินเทอร์เน็ตฟรี! ใช้ OTP {otp} เพื่อยืนยันการสมัครของคุณ.",
        "🎁 ชิงรางวัลใหญ่! ใช้ OTP {otp} เพื่อเข้าร่วมการจับรางวัลพิเศษ.",
        "🚨 การแจ้งเตือนสำคัญ: บัญชีของคุณถูกล็อกชั่วคราว ใช้ OTP {otp} เพื่อปลดล็อก."
    ]

    # Generate messages based on random selection from templates
    messages = []
    for _ in range(count):
        template = random.choice(templates)  # Select a random template
        otp = random.randint(100000, 999999)  # Generate a random 6-digit OTP
        message = template.format(otp=otp)
        messages.append(message)
    
    return messages
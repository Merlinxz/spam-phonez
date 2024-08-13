import random
from faker import Faker

fake = Faker()

def generate_spam_messages(count):
    # Updated list of possible message templates in Thai, including more diverse applications and usage contexts
    templates = [
        "สวัสดี รหัส OTP ของคุณสำหรับการตรวจสอบบัญชีคือ {otp}. กรุณาใส่รหัสเพื่อดำเนินการต่อ. ลิงก์: {link}",
        "เรียน คุณได้รับเลือกให้ได้รับรางวัลพิเศษ! ใช้รหัส {otp} เพื่อรับรางวัลของคุณตอนนี้! ดาวน์โหลดเอกสาร: {file}",
        "สวัสดี การทำธุรกรรมล่าสุดของคุณต้องการการตรวจสอบ. ใช้ OTP {otp} เพื่อยืนยันตัวตนของคุณ. ลิงก์: {link}",
        "แจ้งเตือน บัญชีของคุณถูกตั้งค่าสถานะสำหรับกิจกรรมที่ไม่ปกติ. ตรวจสอบด้วย OTP {otp}. ลิงก์: {link}",
        "ยินดีด้วย คุณได้รับบัตรของขวัญมูลค่า 100,000 บาท. ใส่ OTP {otp} เพื่อรับรางวัลของคุณ. ดาวน์โหลดเอกสาร: {file}",
        "สวัสดี คำขอรีเซ็ตรหัสผ่านของคุณได้รับแล้ว. ใช้ OTP {otp} เพื่อรีเซ็ตรหัสผ่านของคุณ. ลิงก์: {link}",
        "เรียน มีการพยายามเข้าสู่ระบบใหม่. ยืนยันด้วย OTP {otp} เพื่อรักษาความปลอดภัยบัญชีของคุณ. ลิงก์: {link}",
        "สวัสดี กรุณาใช้ OTP {otp} เพื่อเสร็จสิ้นการตั้งค่าประวัติส่วนตัวของคุณ. ใช้ได้ในเวลาจำกัดเท่านั้น! ดาวน์โหลดเอกสาร: {file}",
        "เร่งด่วน: บัญชีของคุณต้องการการตรวจสอบ. ใช้ OTP {otp} เพื่อหลีกเลี่ยงการระงับบัญชี. ลิงก์: {link}",
        "ข้อเสนอพิเศษสำหรับคุณ! ใช้ OTP {otp} เพื่อรับส่วนลด 20% สำหรับการซื้อครั้งถัดไป. ลิงก์: {link}",
        "🔥 โปรโมชั่นพิเศษ! คุณสามารถรับโบนัส 5000 บาทในการเล่นคาสิโนออนไลน์เพียงใช้รหัส {otp} 🔥 ลิงก์: {link}",
        "💰 สมัครกู้เงินออนไลน์วันนี้ รับดอกเบี้ยต่ำพิเศษ! ใช้รหัส {otp} เพื่อยืนยันการสมัครของคุณ. ลิงก์: {link}",
        "🎉 ยินดีด้วย! คุณได้รับการอนุมัติสินเชื่อด่วน 10,000 บาท. ใช้ OTP {otp} เพื่อดำเนินการต่อ. ดาวน์โหลดเอกสาร: {file}",
        "🌟 โปรโมชั่นล่าสุด! เล่นเกมสล็อตและรับฟรี 100 สปิน ใช้ OTP {otp} เพื่อเริ่มเล่นเลย! ลิงก์: {link}",
        "🚀 สมัครตอนนี้เพื่อรับโบนัส 200% สำหรับการเดิมพันในเว็บพนัน! ใช้รหัส {otp} เพื่อรับโบนัส. ลิงก์: {link}",
        "🔒 การแจ้งเตือนความปลอดภัย: ใช้ OTP {otp} เพื่อล็อกอินเข้าบัญชีของคุณ. ลิงก์: {link}",
        "✨ โปรโมชั่นพิเศษ! รับเครดิตเพิ่ม 2,000 บาททันทีหลังจากสมัครสมาชิกใหม่และใช้รหัส {otp}. ลิงก์: {link}",
        "🎁 ลุ้นรับ iPhone 15 เมื่อสมัครสินเชื่อด่วนตอนนี้! ใช้รหัส {otp} เพื่อเข้าร่วม. ลิงก์: {link}",
        "🚨 บัญชีของคุณถูกล็อคชั่วคราว. กรุณาใช้ OTP {otp} เพื่อปลดล็อคและยืนยันตัวตนของคุณ. ลิงก์: {link}",
        "💸 รับดอกเบี้ย 0% ในการกู้ยืมครั้งแรก! ใช้ OTP {otp} เพื่อสมัครทันที. ดาวน์โหลดเอกสาร: {file}",
        "⚠️ การตรวจสอบความปลอดภัย: บัญชีของคุณถูกล็อกเพื่อป้องกัน. ใช้ OTP {otp} เพื่อยืนยันตัวตนของคุณ. ลิงก์: {link}",
        "💥 โปรโมชั่นฉลองครบรอบ! รับฟรีโบนัส 300% เมื่อเติมเงินครั้งแรก ใช้รหัส {otp} เพื่อรับสิทธิ์. ลิงก์: {link}",
        "📱 สมัครแพ็กเกจอินเทอร์เน็ตเร็วสูงวันนี้และรับฟรีข้อมูล 50GB! ใช้ OTP {otp} เพื่อสมัคร. ลิงก์: {link}",
        "🔔 คำเตือน: บัญชีของคุณอาจถูกบุกรุก. กรุณายืนยันการเข้าสู่ระบบด้วย OTP {otp}. ลิงก์: {link}",
        "📢 ประกาศ: รับฟรีเครดิตเดิมพัน 5,000 บาท เมื่อสมัครสมาชิกใหม่และใช้รหัส {otp}. ลิงก์: {link}",
        "💬 คุณมีข้อความใหม่! กรุณายืนยันตัวตนด้วย OTP {otp} เพื่ออ่านข้อความสำคัญของคุณ. ลิงก์: {link}",
        "🏆 โปรโมชั่นสุดพิเศษ! รับโบนัส 5,000 บาท เมื่อทำการฝากเงินครั้งแรก ใช้รหัส {otp} เพื่อรับสิทธิ์. ลิงก์: {link}",
        "🚨 ข้อควรระวัง: มีความพยายามในการเข้าสู่ระบบจากอุปกรณ์ใหม่. ใช้ OTP {otp} เพื่อยืนยัน. ลิงก์: {link}",
        "💥 โปรโมชั่นเติมเงินวันนี้ รับฟรี 200 บาททันที! ใช้รหัส {otp} เพื่อรับข้อเสนอ. ลิงก์: {link}",
        "🔑 รหัสยืนยันสำหรับเข้าสู่ระบบคือ {otp}. กรุณาใส่รหัสเพื่อดำเนินการต่อ. ลิงก์: {link}",
        "📧 คุณมีอีเมลใหม่รออยู่! ใช้ OTP {otp} เพื่อเข้าสู่ระบบและอ่านอีเมล. ลิงก์: {link}",
        "🎰 ลุ้นรางวัลใหญ่ในคาสิโนออนไลน์ของเรา! ใช้ OTP {otp} เพื่อเริ่มเล่น. ลิงก์: {link}",
        "🏠 สนใจลงทุนอสังหาฯ? ใช้ OTP {otp} เพื่อรับข้อเสนอพิเศษ! ลิงก์: {link}",
        "🔧 การยืนยันการซ่อมแซม: ใช้ OTP {otp} เพื่อยืนยันการบริการ. ลิงก์: {link}",
        "🛍️ ใช้ OTP {otp} เพื่อรับส่วนลด 50% สำหรับการสั่งซื้อครั้งถัดไป! ลิงก์: {link}",
        "🏦 ธนาคารของคุณต้องการ OTP {otp} เพื่อยืนยันการเข้าสู่ระบบ. ลิงก์: {link}",
        "💼 สินเชื่อธุรกิจด่วน รับเงินกู้ทันทีด้วย OTP {otp}. ลิงก์: {link}",
        "📱 รับซิมการ์ดฟรีเมื่อใช้ OTP {otp} สำหรับการสมัครวันนี้! ลิงก์: {link}",
        "📢 สนใจลงทุนในหุ้น? ใช้ OTP {otp} เพื่อรับคำแนะนำพิเศษ! ลิงก์: {link}",
        "🏢 การตรวจสอบการเข้าสู่ระบบสำหรับองค์กรของคุณ ใช้ OTP {otp}. ลิงก์: {link}",
        "🚗 โปรโมชั่นพิเศษสำหรับการประกันภัยรถยนต์! ใช้ OTP {otp} เพื่อรับส่วนลด. ลิงก์: {link}",
        "🎟️ รับบัตรกำนัลฟรีมูลค่า 500 บาท! ใช้ OTP {otp} เพื่อยืนยัน. ลิงก์: {link}",
        "🎲 ลุ้นรางวัลใหญ่ในคาสิโนออนไลน์ของเรา! ใช้ OTP {otp} เพื่อเริ่มเล่นทันที. ลิงก์: {link}",
        "🏠 ข้อเสนอพิเศษ! ลงทุนในอสังหาริมทรัพย์ด้วย OTP {otp}. ลิงก์: {link}",
        "💼 บริการสินเชื่อพิเศษสำหรับธุรกิจใหม่ ใช้ OTP {otp} เพื่อสมัคร. ลิงก์: {link}",
        "📲 รับอินเทอร์เน็ตฟรี! ใช้ OTP {otp} เพื่อยืนยันการสมัครของคุณ. ลิงก์: {link}",
        "🎁 ชิงรางวัลใหญ่! ใช้ OTP {otp} เพื่อเข้าร่วมการจับรางวัลพิเศษ. ลิงก์: {link}",
        "🚨 การแจ้งเตือนสำคัญ: บัญชีของคุณถูกล็อกชั่วคราว ใช้ OTP {otp} เพื่อปลดล็อก. ลิงก์: {link}",
        "🔥 โปรโมชั่นพิเศษ! คุณสามารถรับโบนัส 5000 บาทในการเล่นคาสิโนออนไลน์เพียงใช้รหัส {otp} 🔥 ลิงก์: {link}",
        "🌟 โปรโมชั่นล่าสุด! เล่นเกมสล็อตและรับฟรี 100 สปิน ใช้ OTP {otp} เพื่อเริ่มเล่นเลย! ลิงก์: {link}",
        "🚀 สมัครตอนนี้เพื่อรับโบนัส 200% สำหรับการเดิมพันในเว็บพนัน! ใช้รหัส {otp} เพื่อรับโบนัส. ลิงก์: {link}",
        "🔒 การแจ้งเตือนความปลอดภัย: ใช้ OTP {otp} เพื่อล็อกอินเข้าบัญชีของคุณ. ลิงก์: {link}",
        "✨ โปรโมชั่นพิเศษ! รับเครดิตเพิ่ม 2,000 บาททันทีหลังจากสมัครสมาชิกใหม่และใช้รหัส {otp}. ลิงก์: {link}",
        "🎁 ลุ้นรับ iPhone 15 เมื่อสมัครสินเชื่อด่วนตอนนี้! ใช้รหัส {otp} เพื่อเข้าร่วม. ลิงก์: {link}",
        "🚨 บัญชีของคุณถูกล็อคชั่วคราว. กรุณาใช้ OTP {otp} เพื่อปลดล็อคและยืนยันตัวตนของคุณ. ลิงก์: {link}",
        "💸 รับดอกเบี้ย 0% ในการกู้ยืมครั้งแรก! ใช้ OTP {otp} เพื่อสมัครทันที. ดาวน์โหลดเอกสาร: {file}",
        "⚠️ การตรวจสอบความปลอดภัย: บัญชีของคุณถูกล็อกเพื่อป้องกัน. ใช้ OTP {otp} เพื่อยืนยันตัวตนของคุณ. ลิงก์: {link}",
        "💥 โปรโมชั่นฉลองครบรอบ! รับฟรีโบนัส 300% เมื่อเติมเงินครั้งแรก ใช้รหัส {otp} เพื่อรับสิทธิ์. ลิงก์: {link}",
        "📱 สมัครแพ็กเกจอินเทอร์เน็ตเร็วสูงวันนี้และรับฟรีข้อมูล 50GB! ใช้ OTP {otp} เพื่อสมัคร. ลิงก์: {link}",
        "🔔 คำเตือน: บัญชีของคุณอาจถูกบุกรุก. กรุณายืนยันการเข้าสู่ระบบด้วย OTP {otp}. ลิงก์: {link}",
        "📢 ประกาศ: รับฟรีเครดิตเดิมพัน 5,000 บาท เมื่อสมัครสมาชิกใหม่และใช้รหัส {otp}. ลิงก์: {link}",
        "💬 คุณมีข้อความใหม่! กรุณายืนยันตัวตนด้วย OTP {otp} เพื่ออ่านข้อความสำคัญของคุณ. ลิงก์: {link}",
        "🏆 โปรโมชั่นสุดพิเศษ! รับโบนัส 5,000 บาท เมื่อทำการฝากเงินครั้งแรก ใช้รหัส {otp} เพื่อรับสิทธิ์. ลิงก์: {link}",
        "🚨 ข้อควรระวัง: มีความพยายามในการเข้าสู่ระบบจากอุปกรณ์ใหม่. ใช้ OTP {otp} เพื่อยืนยัน. ลิงก์: {link}",
        "💥 โปรโมชั่นเติมเงินวันนี้ รับฟรี 200 บาททันที! ใช้รหัส {otp} เพื่อรับข้อเสนอ. ลิงก์: {link}",
        "🔑 รหัสยืนยันสำหรับเข้าสู่ระบบคือ {otp}. กรุณาใส่รหัสเพื่อดำเนินการต่อ. ลิงก์: {link}",
        "📧 คุณมีอีเมลใหม่รออยู่! ใช้ OTP {otp} เพื่อเข้าสู่ระบบและอ่านอีเมล. ลิงก์: {link}",
        "🎰 ลุ้นรางวัลใหญ่ในคาสิโนออนไลน์ของเรา! ใช้ OTP {otp} เพื่อเริ่มเล่น. ลิงก์: {link}",
        "🏠 สนใจลงทุนอสังหาฯ? ใช้ OTP {otp} เพื่อรับข้อเสนอพิเศษ! ลิงก์: {link}",
        "🔧 การยืนยันการซ่อมแซม: ใช้ OTP {otp} เพื่อยืนยันการบริการ. ลิงก์: {link}",
        "🛍️ ใช้ OTP {otp} เพื่อรับส่วนลด 50% สำหรับการสั่งซื้อครั้งถัดไป! ลิงก์: {link}",
        "🏦 ธนาคารของคุณต้องการ OTP {otp} เพื่อยืนยันการเข้าสู่ระบบ. ลิงก์: {link}",
        "💼 สินเชื่อธุรกิจด่วน รับเงินกู้ทันทีด้วย OTP {otp}. ลิงก์: {link}",
        "📲 รับซิมการ์ดฟรีเมื่อใช้ OTP {otp} สำหรับการสมัครวันนี้! ลิงก์: {link}",
        "📢 สนใจลงทุนในหุ้น? ใช้ OTP {otp} เพื่อรับคำแนะนำพิเศษ! ลิงก์: {link}",
        "🏢 การตรวจสอบการเข้าสู่ระบบสำหรับองค์กรของคุณ ใช้ OTP {otp}. ลิงก์: {link}",
        "🚗 โปรโมชั่นพิเศษสำหรับการประกันภัยรถยนต์! ใช้ OTP {otp} เพื่อรับส่วนลด. ลิงก์: {link}",
        "🎟️ รับบัตรกำนัลฟรีมูลค่า 500 บาท! ใช้ OTP {otp} เพื่อยืนยัน. ลิงก์: {link}",
        "🎲 ลุ้นรางวัลใหญ่ในคาสิโนออนไลน์ของเรา! ใช้ OTP {otp} เพื่อเริ่มเล่นทันที. ลิงก์: {link}",
        "🏠 ข้อเสนอพิเศษ! ลงทุนในอสังหาริมทรัพย์ด้วย OTP {otp}. ลิงก์: {link}",
        "💼 บริการสินเชื่อพิเศษสำหรับธุรกิจใหม่ ใช้ OTP {otp} เพื่อสมัคร. ลิงก์: {link}",
        "📲 รับอินเทอร์เน็ตฟรี! ใช้ OTP {otp} เพื่อยืนยันการสมัครของคุณ. ลิงก์: {link}",
        "🎁 ชิงรางวัลใหญ่! ใช้ OTP {otp} เพื่อเข้าร่วมการจับรางวัลพิเศษ. ลิงก์: {link}",
        "🚨 การแจ้งเตือนสำคัญ: บัญชีของคุณถูกล็อกชั่วคราว ใช้ OTP {otp} เพื่อปลดล็อก. ลิงก์: {link}"
    ]
    
    # Suspicious links and shortened URLs
    suspicious_links = [
        fake.url(), 
        "http://bit.ly/" + str(random.randint(100000, 999999)),
        "http://tinyurl.com/" + str(random.randint(100000, 999999)),
        "http://short.url/" + str(random.randint(100000, 999999)),
        "http://discounts.com/" + str(random.randint(100000, 999999)),
        "http://offers.net/" + str(random.randint(100000, 999999)),
        "http://deals.org/" + str(random.randint(100000, 999999)),
        fake.url() + "/promo/" + str(random.randint(100000, 999999)),
        "http://socialmedia.com/" + str(random.randint(100000, 999999)),
        "http://downloadapp.net/" + str(random.randint(100000, 999999)),
        "http://newapp.io/" + str(random.randint(100000, 999999)),
        "http://getsocialapp.com/" + str(random.randint(100000, 999999)),
        "http://joinnow.app/" + str(random.randint(100000, 999999)),
        "http://trendingapp.org/" + str(random.randint(100000, 999999)),
        "http://social.network/" + str(random.randint(100000, 999999)),
        "http://playnow.app/" + str(random.randint(100000, 999999)),
        "http://installapp.io/" + str(random.randint(100000, 999999)),
        "http://appdownload.co/" + str(random.randint(100000, 999999)),
        "http://newfeatures.app/" + str(random.randint(100000, 999999)),
        "https://www.facebook.com/" + str(random.randint(100000, 999999)),
        "https://twitter.com/" + str(random.randint(100000, 999999)),
        "https://www.instagram.com/" + str(random.randint(100000, 999999)),
        "https://www.linkedin.com/in/" + str(random.randint(100000, 999999)),
        "https://www.youtube.com/" + str(random.randint(100000, 999999)),
        "https://www.tiktok.com/@user" + str(random.randint(100000, 999999)),
        "https://www.snapchat.com/add/user" + str(random.randint(100000, 999999)),
        "https://www.whatsapp.com/qr/" + str(random.randint(100000, 999999)),
        "https://www.reddit.com/user/" + str(random.randint(100000, 999999)),
        "https://www.pinterest.com/" + str(random.randint(100000, 999999)),
        "https://www.tumblr.com/blog/" + str(random.randint(100000, 999999)),
        "https://www.discord.gg/" + str(random.randint(100000, 999999)),
        "https://play.google.com/store/apps/details?id=com." + str(random.randint(100000, 999999)),
        "https://apps.apple.com/us/app/id" + str(random.randint(100000, 999999)),
        "https://www.microsoft.com/store/apps/" + str(random.randint(100000, 999999)),
        "https://www.amazon.com/appstore" + str(random.randint(100000, 999999)),
        "https://www.shopify.com/apps/" + str(random.randint(100000, 999999)),
        "https://www.zoom.us/download" + str(random.randint(100000, 999999)),
        "https://www.skype.com/en/download-skype/skype-for-computer/",
        "https://slack.com/downloads/" + str(random.randint(100000, 999999)),
        "https://www.spotify.com/download/" + str(random.randint(100000, 999999)),
        "https://www.netflix.com/signup" + str(random.randint(100000, 999999)),
        "https://www.hulu.com/start" + str(random.randint(100000, 999999)),
    ]

    # File attachments
    file_attachments = [
        "document.pdf",
        "file.docx",
        "invoice.zip",
        "payment.exe",
        "offer.pptx",
        "details.rar",
        "resume.docx",
        "invoice.xlsx",
        "instructions.pdf",
        "setup.exe",
        "report.csv",
        "update.zip",
        "app-release.apk",         # Android APK
        "android-debug.apk",       # Android debug APK
        "app-bundle.aab",          # Android App Bundle
        "android-config.json",    # Android configuration
        "app.ipa",                 # iOS App Archive
        "ios-config.plist",        # iOS configuration
        "ios-debug.ipa",           # iOS debug IPA
        "app-store.ipa",           # iOS App Store IPA
        "app.dmg",                 # macOS Disk Image
        "macOS-install.pkg",       # macOS Installer Package
        "mac-app.zip",             # macOS application archive
        "setup.msi",               # Windows Installer Package
        "windows-update.exe",      # Windows update executable
        "driver-install.exe",      # Windows driver installation executable
        "app.deb",                 # Linux Debian package
        "app.rpm",                 # Linux RPM package
        "linux-update.tar.gz",     # Linux update archive
        "cross-platform.jar",      # Java Archive
        "cross-platform.zip",      # Cross-platform archive
        "universal-app.tar.gz",    # Universal application archive
    ]

    # Generate the list of spam messages
    spam_messages = []
    for _ in range(count):
        template = random.choice(templates)
        otp = str(random.randint(100000, 999999))
        link = random.choice(suspicious_links)
        file = random.choice(file_attachments)
        message = template.format(otp=otp, link=link, file=file)
        spam_messages.append(message)
    
    return spam_messages
import os
import time

# smtplib 用于邮件的发信动作
import smtplib
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


os.system("adb shell input keyevent 224")  # 点亮屏幕
#os.system("adb shell input keyevent 26")  # 电源打开屏幕
time.sleep(0.5)
os.system("adb shell input swipe 552 1416 552 523")  # 上划
time.sleep(0.5)
#os.system("adb shell input text 6666")  # 解锁
time.sleep(0.5)
os.system("adb shell am start -n com.alibaba.android.rimet/com.alibaba.android.rimet.biz.LaunchHomeActivity")  # 打开钉钉
time.sleep(0.5)
s = os.popen("adb shell dumpsys activity | find \".SignUpWithPwdActivity\"").read()
time.sleep(30)

#time.sleep(20)
#****************打卡完毕后自动发送文件****
# 设备截屏保存到sdcard
os.system("adb shell screencap -p /sdcard/DCIM/Screenshots/ding.png")
time.sleep(0.5)
# 传送到计算机
os.system("adb pull /sdcard/DCIM/Screenshots/ding.png")
# 删除设备截屏
#os.system("adb shell rm -r /sdcard/DCIM/Screenshots/sdsds.png")

# 发信方的信息：发信邮箱，QQ 邮箱授权码
from_addr = '*******@qq.com'
password = '****'     # QQ 邮箱smtp授权码

# # 收信方邮箱
to_addr = '******@qq.com'

# 发信服务器
smtp_server = 'smtp.qq.com'

# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
#msg = MIMEText('send by python', 'plain', 'utf-8')
msg = MIMEMultipart('related')
content = MIMEText('<html><body><img src="cid:imageid" alt="imageid"></body></html>', 'html', 'utf-8')  # 正文
# 邮件头信息
msg.attach(content)
msg['From'] = Header(from_addr)
msg['To'] = Header(to_addr)
msg['Subject'] = Header('dinding_daka')  # 主题

file = open("E:/study2/python/ding.png", "rb")
img_data = file.read()
file.close()

img = MIMEImage(img_data)
img.add_header('Content-ID', 'imageid')
msg.attach(img)


# 开启发信服务，这里使用的是加密传输
server = smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server, 465)
# 登录发信邮箱
server.login(from_addr, password)
# 发送邮件
server.sendmail(from_addr, to_addr, msg.as_string())
# 关闭服务器
server.quit()
#
#server=smtplib.SMTP_SSL(smtp_server)

os.system("adb shell input keyevent 3")



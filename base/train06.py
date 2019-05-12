from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import urllib

sender = '783808649@qq.com'
receivers = ['783808649@qq.com']
smtp_server = 'smtp.qq.com'
smto_pwd='oozrrpfhkdglbeij'

def mail():
    # 请自行修改下面的邮件发送者和接收者

    message = MIMEText('正文', 'plain', 'utf-8')
    message['From'] = Header('张三', 'utf-8')
    message['To'] = Header('接收人', 'utf-8')
    message['Subject'] = Header('示例代码实验邮件', 'utf-8')
    smtper = SMTP(smtp_server)
    # 请自行修改下面的登录口令
    smtper.login(sender, smto_pwd)
    smtper.sendmail(sender, receivers, message.as_string())
    print('普通邮件发送完成!')

def mail_with_file():
    # 创建一个带附件的邮件消息对象
    message = MIMEMultipart()

    # 创建文本内容
    text_content = MIMEText('附件中有本月数据请查收', 'plain', 'utf-8')
    message['Subject'] = Header('本月数据', 'utf-8')
    # 将文本内容添加到邮件消息对象中
    message.attach(text_content)

    # 读取文件并将文件作为附件添加到邮件消息对象中
    with open('train01.py', 'rb') as f:
        txt = MIMEText(f.read(), 'base64', 'utf-8')
        txt['Content-Type'] = 'text/plain'
        txt['Content-Disposition'] = 'attachment; filename=hello.txt'
        message.attach(txt)
    # 读取文件并将文件作为附件添加到邮件消息对象中
    with open('haha.xlsx', 'rb') as f:
        xls = MIMEText(f.read(), 'base64', 'utf-8')
        xls['Content-Type'] = 'application/vnd.ms-excel'
        xls['Content-Disposition'] = 'attachment; filename=haha.xlsx'
        message.attach(xls)

    # 创建SMTP对象
    smtper = SMTP(smtp_server)
    smtper.login(sender, smto_pwd)
    smtper.sendmail(sender, receivers, message.as_string())
    smtper.quit()
    print('附件邮件发送完成!')


if __name__ == '__main__':
    mail_with_file()

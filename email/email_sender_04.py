from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP_SSL


class SmtpInfo:
    def __init__(self, server, port, user_mail, user, password):
        self.server = server
        self.port = port
        self.user_mail = user_mail
        self.user = user
        self.password = password

    def send_mail(self, target_mail, subject, contents, attachment=False):
        msg = MIMEMultipart("alternative")

        if attachment:
            msg = MIMEMultipart('mixed')

        msg['From'] = self.user_mail
        msg['to'] = target_mail
        msg['Subject'] = subject

        text = MIMEText(contents)
        msg.attach(text)

        smtp = SMTP_SSL(self.server, self.port)
        smtp.login(self.user, self.password)
        smtp.sendmail(self.user_mail, target_mail, msg.as_string())
        smtp.close()


if __name__ == "__main__":
    gmail_info = SmtpInfo("smtp.gmail.com",
                          465,
                          "devfuner@gmail.com",
                          "devfuner",
                          open('password').read().strip())

    gmail_info.send_mail('devfuner@gmail.com',  # 메일을 받을 주소
                         '메일이 도착했습니다.',  # 메일 제목
                         '파이썬을 사용한 메일자동화입니다.')  # 메일 내용

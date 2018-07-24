import email_sender_04 as sender


if __name__ == "__main__":
    gmail_info = sender.SmtpInfo("smtp.gmail.com",
                                 465,
                                 "devfuner@gmail.com",
                                 "devfuner",
                                 open('password').read().strip())

    for i in range(10):
        gmail_info.send_mail('devfuner@gmail.com',  # 메일을 받을 주소
                             str(i) + '폭탄메일이 도착했습니다.',  # 메일 제목
                             '파이썬을 사용한 메일자동화입니다.')  # 메일 내용


import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login("sender mail", "sender password")

server.sendmail("reels@instagram.com",    #sender mail
                "posts@instagram.com", #receiver mail
                "Tu toh geya")    #message

print("Mail sent")





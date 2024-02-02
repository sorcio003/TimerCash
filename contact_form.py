import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def send_to_worker(finished, email, receiver, pay, time, password):
    message = MIMEMultipart("alternative")
    message["Subject"] = "Python Timer Cash Auto Message"
    message["From"] = email
    message["To"] = receiver[2]

    text = """"""
    
    html = """"""
    
    if not finished:
        html = """\
        <html>
        <body>
        <h1 style="
            font-size: larger; 
            font-family:Verdana, Geneva, Tahoma, sans-serif;
            " align="center">TimerCash Python</h1>

        <h1 style="
            font-size: xx-large; 
            font-family:Verdana, Geneva, Tahoma, sans-serif;
            " align="center">Il Tuo Lavoro <br> è inizato <br> Adesso</h1>
        <img src="cid:Mailtrapimage" alt="logo" style="width: 250px;display: block;
            margin-left: auto;
            margin-right: auto; ">
        <p>Ciao """ + receiver[0] + """<br><br>
        Siamo felici di informati che alle ore """ + time.strftime("%X") + """ <br> 
        hai iniziato il tuo lavoro di<br>
        '""" + receiver[5] + """'.<br><br>
        Ti informiamo che il tuo lavoro sta richiedendo """ + str(receiver[6]) + """ € a ora<br><br>
        Se le specifiche riportate non corrispondono all'accordo<br>
        da te sottoscritto con il tuo datore, ti preghiamo di contattare<br>
        il tuo datore di lavoro all'indirizzo """ + receiver[4] + """ e bloccare il timer<br><br>
        Grazie,<br>
        Team TimerCash
        </body>
        </html>
        """
    else:
        html = """\
        <html>
        <body>
        <h1 style="
            font-size: larger; 
            font-family:Verdana, Geneva, Tahoma, sans-serif;
            " align="center">TimerCash Python</h1>

        <h1 style="
            font-size: xx-large; 
            font-family:Verdana, Geneva, Tahoma, sans-serif;
            " align="center">Il Tuo Lavoro <br> è finito <br> Adesso</h1>
        <img src="cid:Mailtrapimage" alt="logo" style="width: 250px;display: block;
            margin-left: auto;
            margin-right: auto; ">
        <p>Ciao """ + receiver[0] + """<br><br>
        Siamo felici di informati che alle ore """ + time.strftime("%X") + """ <br> 
        hai finito il tuo lavoro di<br>
        '""" + receiver[5] + """'.<br><br>
        Ti informiamo che il tuo lavoro sta richiedendo """ + str(pay) + """ €<br><br>
        Se le specifiche riportate non corrispondono all'accordo<br>
        da te sottoscritto con il tuo datore, ti preghiamo di contattare<br>
        il tuo datore di lavoro all'indirizzo """ + receiver[4] + """ e bloccare il timer<br><br>
        Grazie,<br>
        Team TimerCash
        </body>
        </html>
        """
    
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)
    
    fp = open('logo.png', 'rb')
    image = MIMEImage(fp.read())
    fp.close()

    image.add_header('Content-ID', '<Mailtrapimage>')
    message.attach(image)

    sever = smtplib.SMTP("smtp.gmail.com:587")
    sever.starttls()
    sever.login(email, password)
    sever.sendmail(email, receiver[2], message.as_string())
    sever.quit()

def send_to_datore(finished, email, receiver, pay, time, password):
    message = MIMEMultipart("alternative")
    message["Subject"] = "Python Timer Cash Auto Message"
    message["From"] = email
    message["To"] = receiver[4]

    text = """"""
    
    html = """"""
    
    if not finished:
        html = """\
        <html>
        <body>
        <h1 style="
            font-size: larger; 
            font-family:Verdana, Geneva, Tahoma, sans-serif;
            " align="center">TimerCash Python</h1>

        <h1 style="
            font-size: xx-large; 
            font-family:Verdana, Geneva, Tahoma, sans-serif;
            " align="center">Il Tuo dipendente <br> ha inizato il suo <br> Lavoro</h1>
        <img src="cid:Mailtrapimage" alt="logo" style="width: 250px;display: block;
            margin-left: auto;
            margin-right: auto; ">
        <p>Ciao """ + receiver[3] + """<br><br>
        Siamo felici di informati che alle ore """ + time.strftime("%X") + """ <br> 
        il tuo dipendente """ + receiver[0] + """ """ + receiver[1] + """ ha inizato il suo lavoro di<br>
        '""" + receiver[5] + """' per te.<br><br>
        Ti informiamo che il tuo dipendete richiede """ + str(receiver[6]) + """ € a ora<br>
        per il suo lavoro.<br><br>
        Se le specifiche riportate non corrispondono all'accordo<br>
        da te sottoscritto con il tuo dipendente, ti preghiamo di contattare<br>
        il tuo dipendente all'indirizzo """ + receiver[2] + """ e bloccare il timer<br><br>
        Grazie,<br>
        Team TimerCash
        </body>
        </html>
        """
    else:
        html = """\
        <html>
        <body>
        <h1 style="
            font-size: larger; 
            font-family:Verdana, Geneva, Tahoma, sans-serif;
            " align="center">TimerCash Python</h1>

        <h1 style="
            font-size: xx-large; 
            font-family:Verdana, Geneva, Tahoma, sans-serif;
            " align="center">Il Tuo dipendente <br> ha finito il suo <br> Lavoro</h1>
        <img src="cid:Mailtrapimage" alt="logo" style="width: 250px;display: block;
            margin-left: auto;
            margin-right: auto; ">
        <p>Ciao """ + receiver[3] + """<br><br>
        Siamo felici di informati che alle ore """ + time.strftime("%X") + """ <br> 
        il tuo dipendente """ + receiver[0] + """ """ + receiver[1] + """ ha finito il suo lavoro di<br>
        '""" + receiver[5] + """' per te.<br><br>
        Ti informiamo che il tuo dipendete richiede """ + str(pay) + """€<br>
        per il suo lavoro.<br><br>
        Se le specifiche riportate non corrispondono all'accordo<br>
        da te sottoscritto con il tuo dipendente, ti preghiamo di contattare<br>
        il tuo dipendente all'indirizzo """ + receiver[2] + """ e bloccare il timer<br><br>
        Grazie,<br>
        Team TimerCash
        </body>
        </html>
        """
    
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)
    
    fp = open('logo.png', 'rb')
    image = MIMEImage(fp.read())
    fp.close()

    image.add_header('Content-ID', '<Mailtrapimage>')
    message.attach(image)

    sever = smtplib.SMTP("smtp.gmail.com:587")
    sever.starttls()
    sever.login(email, password)
    sever.sendmail(email, receiver[4], message.as_string())
    sever.quit()

def SendEmail(finished, receiver, pay):
    password = "vfou jlwf kvxx uaal"
    
    email = "pythontimercash@gmail.com"
    
    time = datetime.now()
    
    pay = round(pay, 2)
    
    send_to_datore(finished, email, receiver, pay, time, password)

    send_to_worker(finished, email, receiver, pay, time, password)

    #print("Email has been sent to " + receiver[2])

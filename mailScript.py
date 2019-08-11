from tkinter import *
import smtplib  #It enables you to send email

def send_mera_mail():
    server = smtplib.SMTP('smtp.gmail.com',587) #Establish connection between our connection and gmail's connection 

    server.ehlo()   #Extended HELO (EHLO) is an Extended Simple Mail Transfer Protocol (ESMTP) command sent by an email server to identify itself when connecting to another email server to start the process of sending an email. It is followed with the sending email server's domain name.

    server.starttls()   #Encrypting our connection
    server.ehlo()   

    server.login(' your email id from where you want to send ',' input_your_generated password ') #Your gmail email and the generated password
    
    bobalice_info = bobalice.get()
    body_info = body.get()
    subject_info = subject.get()

    msg = f"Subject: {subject_info}\n\n{body_info}" #Formatting the subject and body

    server.sendmail(
            ' your email id from where you want to send ',
            bobalice_info,
            msg
            )       #Sender email, receiver email and the message
    server.quit()   #Closing the connection

    bobalice_entry.delete(0,END)
    body_entry.delete(0,END)
    subject_entry.delete(0,END)

    Label(screen1, text = "Sucessfully Sent", fg = "green" ,font = ("calibri", 11)).pack()

def mera_mail():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("Send Email")
  screen1.geometry("300x250")
  
  global bobalice
  global body
  global subject

  global bobalice_entry

  global subject_entry

  global body_entry

  bobalice = StringVar()
  body = StringVar()
  subject = StringVar() 
  

  Label(screen1, text = "Please enter the following:").pack()
  Label(screen1, text = "").pack()
  Label(screen1, text = "To: * ").pack()
  bobalice_entry = Entry(screen1, textvariable = bobalice)
  bobalice_entry.pack()
  Label(screen1, text = "Subject * ").pack()
  subject_entry =  Entry(screen1, textvariable = subject)
  subject_entry.pack()
  Label(screen1, text = "Body * ").pack()
  body_entry =  Entry(screen1, textvariable = body)
  body_entry.pack()
  Label(screen1, text = "").pack()
  Button(screen1, text = "Send", width = 10, height = 1, command = send_mera_mail).pack()



def main_screen():
  global screen
  screen = Tk()
  screen.geometry("300x250")
  screen.title("Khud Ka Email")
  Label(text = "Hello, thevirtualbuddy", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text = "").pack()
  Button(text = "Send Email",height = "2", width = "30", command = mera_mail).pack()

  screen.mainloop()

main_screen()
  

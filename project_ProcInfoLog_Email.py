import psutil
from sys import *
import logging
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def My_Email(log_name,email_id):

    sender="maheshkawhale1712@gmail.com"
    receiver=email_id
    password="Hello@1234"
    body="""\
        hi sir,
        my name is Mahesh Kawhale, i am sending this email to you 
        as i want to do project testing ....
        so,this is my project, how do you feel 
        let know me...
        thanks...."""

    msg=MIMEMultipart()
    msg["To"]=receiver
    msg["From"]=sender
    msg["subject"]="testing for my project...."

    msg.attach(MIMEText(body,"plain"))
    filename=log_name
    attachment=open(filename,"rb")
    p=MIMEBase("application" ,"octet-stream")
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)

    s=smtplib.SMTP("smtp.gmail.com",587)
    try:
        s.starttls()
        s.login(sender,password)
        text=msg.as_string()
        s.sendmail(sender,receiver,text)
        s.quit()
    except Exception as obj :
        print("exception occured:", obj)


def Displayprocess():
    proc_list=[]
    for process in psutil.process_iter():
        try:
            pinfo=process.as_dict(attrs=["username","name","pid"])
            proc_list.append(pinfo)
          
        except(psutil.NoSuchProcess,psutil.AccessDenied):
            pass
    return proc_list 

def log_file(log_name,email_id):
    P_list=Displayprocess()
    logging.basicConfig(filename=log_name,filemode="w",format="%(asctime)s %(message)s",
                                     encoding='utf-8',level=logging.DEBUG)  
    logger=logging.getLogger()
    logger.info("........From : Mahesh Kawhale...........")                                                          
    for element in P_list:
        logging.info(element)
    return log_name,email_id   

    
def main():
    print("....automation script : Mahesh Kawhale.....")
    print("application name:",argv[0])
    print("number of arguments are :",len(argv)-1)

    if(len(argv)==2):
        if (argv[1] == "-u") or (argv[1] == "-U"):
            print("Usage : Script is used display all current process in log file and")
            print("send it to the email ")
            exit()
        elif (argv[1] == "-h") or (argv[1] == "-H"):
            print("Help : first_argument: log_name ")
            print("second argument : Email Id")
            exit()  
        else:
            print("invalid number of arguments:")
            print("-u: Usage")
            print("-h : Help")
            exit()     
    if(len(argv)==3):
        try:
            log_name,email_id=log_file(argv[1],argv[2])
            My_Email(log_name,email_id)
            print("task gets completed successfully.........")
        except(Exception):
            print("Invalid number of arguments") 

        
if __name__=="__main__":
    main()    


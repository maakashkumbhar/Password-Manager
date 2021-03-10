import pymongo
from datetime import date
import tkinter as tk

################
CLIENT = pymongo.MongoClient('localhost',27017)
manager_db = CLIENT.AuthenticationData ## here we connected with the database
information = manager_db.authentication_data ## here we connect to the collection
#authentication_data = information['authentication_data']
LETTERS = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',
8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',
16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z',26:'@',27:'#',28:'.',29:' '}
letters = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11
           ,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,
           'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25,'@':26,'#':27,'.':28,' ':29}

################
def record_add(email,password,user_id,website):
    record = {
            'email_id':email,
            'password':password,
            'user_id':user_id,
            'date':str(date.today()),
            'website':website
    }
    information.insert_one(record)
    print("New Record added")

def record_fetch(website):
     records  = information.find_one({"website":"{0}".format(website)})
     print("The Email is:{0}".format(records['email_id']))
     print("The Password is:{0}".format(records['password']))
     print("The User_id is:{0}".format(records['user_id']))
     print("The Date is:{0}".format(records['date']))
     print("The Website is:{0}".format(records['website']))
     #print(records)
def encrypt_text(message_text,key):
    encrypted_text = ''
    for alphabet in message_text:
        alphabet = alphabet.upper()
        alphabet = '{}'.format(alphabet)
        value = (letters[alphabet]*key)%26
        encrypted_text += LETTERS[value]
        print(encrypted_text)
        return encrypted_text

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Password Manager')
    email_var = tk.StringVar()
    password_var = tk.StringVar()
    user_id_var = tk.StringVar()
    website_var = tk.StringVar()
    ##################################
    input_frame = tk.Frame(root)
    email_input_label = tk.Label(input_frame,text="Email")
    email_input_label.grid(row=0,column=0)
    ##################################
    email_entry = tk.Entry(input_frame)
    email_entry.grid(row=0,column=1)
    email_input = email_var.get()
    ##################################
    password_label = tk.Label(input_frame,text="Password")
    password_label.grid(row=0,column=2)
    ###############################@##
    password_entry = tk.Entry(input_frame)
    password_entry.grid(row=0,column=3)
    password_input = password_var.get()
    ##################################
    user_id_label = tk.Label(input_frame,text = "User_id")
    user_id_label.grid(row=1,column=0) 
    ##################################
    user_id_entry = tk.Entry(input_frame)
    user_id_entry.grid(row=1,column=1)
    user_id_input = user_id_var.get()
    ##################################
    website_label = tk.Label(input_frame,text = "Website")
    website_label.grid(row=1,column=2)
    ##################################
    website_entry = tk.Entry(input_frame)
    website_entry.grid(row=1,column=3)
    website_input = website_var.get()
    ##################################
    submit_button = tk.Button(input_frame,text="Submit Data",command = record_add(email_input,password_input,user_id_input,website_input))
    submit_button.grid(row=3,column=2)
    ##################################
    input_frame.pack(padx = 1,pady=1)
    #################################
    root.geometry('500x400')
    root.mainloop()
    #print("Enter the Authentication Data:")
    #print("1:Enter New Data \n 2:View Data")
    #choice = int(input())
    #if(choice==1):
    #    print("Enter Your Email:")
    #    email_id = str(input())
    #    print("Enter Password:")
    #    password = str(input())
    #   password = encrypt_text(password,7)
    #    print("Enter Userid")
    #   user_id = str(input())
    #   print("Enter Website Name:")
    #   website = str(input())
    #
    #    record_add(email_id,password,user_id,website)
    #else:
    #    print("Enter the website you want to search password for:")
    #    website_name = str(input())
    #    record_fetch(website_name)
    


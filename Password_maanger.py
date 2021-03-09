import pymongo
from datetime import date

################
CLIENT = pymongo.MongoClient()
manager_db = CLIENT["AuthenticationData"]
information = manager_db.authentication_data
authentication_data = information['authentication_data']
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

def record_fetch():
    get_info = authentication_data.objects()
    for info in get_info:    
        print(info.email)
        print(info.website)

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
    print("Enter the Authentication Data:")
    print("1:Enter New Data \n 2:View Data")
    choice = int(input())
    if(choice==1):
        print("Enter Your Email:")
        email_id = str(input())
        print("Enter Password:")
        password = str(input())
        #password = encrypt_text(password,7)
        print("Enter Userid")
        user_id = str(input())
        print("Enter Website Name:")
        website = str(input())

        record_add(email_id,password,user_id,website)
    else:
        record_fetch()
    


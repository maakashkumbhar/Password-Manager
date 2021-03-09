############
#Aim: Implementing the Multiplicative cypher
#Author : Akash Kumbhar
#Purpose:Project Purpose
############
import random

LETTERS = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',
8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',
16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z',26:'@',27:'#',28:'.',29:' '}

letters = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11
           ,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,
           'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25,'@':26,'#':27,'.':28,' ':29}
message_text =  'i#ama@kash'
def encrypt_text(message_text,key):
    encrypted_text = ''
    for alphabet in message_text:
        alphabet = alphabet.upper()
        alphabet = '{}'.format(alphabet)
        value = (letters[alphabet]*key)%26
        encrypted_text += LETTERS[value]
        print(encrypted_text)
def decrypt_text(encrypted_text,key):
    pass        

encrypt_text(message_text,8)

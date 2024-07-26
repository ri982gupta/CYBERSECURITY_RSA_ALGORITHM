from tkinter import *
import string
# RSA-in-Python
# Simple implementation of the RSA algorithm in Python and Python GUI(Tkinter)
# ******************************Function Area**********************************
# (1). RSA
        #1. select two primes p q
        #2. calculate n = p*q
        #3. calcualte t(n)=(p-1)*(q-1)
        #4. select e gcd(t(n),e)=1
        #5. determine d ed=1 mode t(n)
        # public key:pu{e,n}
        # private key:pr{d,n}
        #6. encryption: ciphertext=plaintext ** e mod n
        #7. decryption: plaintext=ciphertext ** d mod n






# 2. Calculate n=p*q
def get_n(p,q):
    return p*q

# 3. calculate t(n)=(p-1)*(q-1)
def get_tn(p,q):
    return (p-1)*(q-1)

# 4-1. select e gcd(t(n),e)=1 gcd(x,y) is for get_e(tn)
def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)

# 4-2. get public key= e,n
def get_e(tn):
    e=2 #prime number starts from 2
    #gcd(tn,e)=1 tn & e are relative prime
    while gcd(tn,e)!=1:
        e=e+1
    # this way can find the minimal prime
    return e

# 5. determine d get private key= d, n
# ed congurent 1 (mod t(n)), so: ed = t(n)*n+1
def get_d(e, tn):
    # e is part of public key
    n=1
    while (tn*n+1) % e !=0:
        n=n+1
    d=(tn*n+1)/e
    return d

# 6.7 encrypt and decrypt
# encryption: ciphertext=plaintext ** e mod n
# decryption: plaintext=ciphertext ** d mod n
def rsa(M, key_ed, n):
    return_data = 1
    M = M % n

    while key_ed != 0:
        if key_ed % 2 == 1:
            return_data = (return_data * M)
        M = M % n
        key_ed = key_ed / 2
    
    return return_data



# (2). interface function
# ++++++++++++++++++++++++++++Encryption Function++++++++++++++
def submitclick_encrypt():
    #get plaintext the user input
    plaintext = entryvalue.get()
    #get the value of tn n e d 
    tn=get_tn(2357, 1733)
    n=get_n(2357, 1733)
    e=get_e(tn)
    d=get_d(e, tn)

    print ("Plaintext:",plaintext)
    # print public key and private 
    print ("Public Key:(",e,",",n,")")
    print ("Private key:(",d,",",n,")")

    # encryption
    # string convert into the number
    plaintext1=int(plaintext)
    ciphertext=rsa(plaintext1,e,n)

    print ('Ciphertext:', ciphertext)
    # output to the listbox
    listbox.insert(0,ciphertext)


    # ++++++++++++++++++++Decryption Function +++++++++++++++++++
def submitclick_decrypt():
    #get the ciphertext the user input
    ciphertext = entryvalue2.get()

    # get the value of tn n e d
    tn=get_tn(2357,1733)
    n=get_n(2357,1733)
    e=get_e(tn)
    d=get_d(e, tn)

    print ("Ciphertext:",ciphertext)
    #print public key and private key
    print ("Public Key:(",e,",",n,")")
    print ("Private Key:(",d,",",n,")")

    # Decryption
    ciphertext=int(ciphertext)
    plaintext=rsa(ciphertext,d,n)

    print ('Plaintext:',  plaintext)
    #output to the listbox
    listbox2.insert(0,plaintext)

# ********************************Function Area End***************************







# *****************************GUI Area***************************************
root = Tk()
# GUI title

# Definition size of window
root.geometry("1200x6000")

# set window color
root.configure(bg='SteelBlue1')

root.title('RSA CRYPTOSYSTEM')

Tops = Frame(root, width=1600, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, relief=SUNKEN)
f1.pack(side=TOP)

lblInfo = Label(Tops,font=('helvetica', 42, 'bold'),
               text="SECRET MESSAGING \n RSA ALGORITHM",
               fg="DodgerBlue2", bd=10, anchor='w')

lblInfo.grid(row=0,column=0)

# *****************************Plaintext input********************************
l = Label(f1,font=('arial', 16,'bold'),
          text='INPUT THE PLAINTEXT',bd=16,anchor="w")
l.grid(row=1,column=0)

# input plaintext
entryvalue = Entry(f1, font=('arial',16,'bold'),
                   bd=10, insertwidth=2,bg="SteelBlue3")
entryvalue.grid(row=2,column=0)

# click the Encrypt button
button = Button(f1,font=('arial',16,'bold'),
                text="ENCRYPT",command=submitclick_encrypt,bg="gray25",bd=16,anchor="w")
button.grid(row=3,column=0)

# show the ciphertext info.
show = Label(f1, font=('arial', 16,'bold'),
             text='SHOW CIPHERTEXT',bd=16,anchor="w")
show.grid(row=4,column=0)

listbox = Listbox(f1,height = 2, width = 40,font=('arial',20,'bold'),
                  bd=10,bg="SteelBlue3")
listbox.grid(row=5,column=0)
# *****************************Plaintext input ending************************



# ****************************ciphertext input*******************************
label = Label(f1,font=('arial', 16, 'bold'),
              text='INPUT THE CIPHERTEXT', bd=16,anchor="w")
label.grid(row=6, column=0)

# input ciphertext
entryvalue2 = Entry(f1, font=('arial',16,'bold'),
                    bd=10, insertwidth=2,bg="SteelBlue3")
entryvalue2.grid(row=7, column=0)

# click the Decrypt button
button2 = Button(f1,font=('arial',16,'bold'),
                 text="DECRYPT",command=submitclick_decrypt,bg="gray25",bd=16,anchor="w")
button2.grid(row=8, column=0)

# show the plaintext info.
show2 = Label(f1, font=('arial',16,'bold'),
              text='SHOW PLAINTEXT',bd=16,anchor="w")
show2.grid(row=9, column=0)

listbox2 = Listbox(f1, height = 2, width = 40,font=('arial',20,'bold'),
                   bd=10, bg="SteelBlue3")
listbox2.grid(row=10, column=0)
# *************************ciphertext input ending*************************

root.mainloop()

# **************************GUI Area End******************************








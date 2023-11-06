#for i in range(97, 123):
 #   print(chr(i) ,end="")
#print("\n")
#for i in range(0, 99):
 #   print(i , " = ", hex(i))

#for i in range(0, 100):
 #   if i < 10:
  #      print(chr(48) + str(i) , end=", ")
   # elif i <= 99:
    #    print(str(i) , end=", ")
#def uppercase(str):
 #   for i in str:
  #      i = ord(i)
   #     i = i - 32
    #    print(chr(i),  end="")
     #   end="/n"

#uppercase("clear")
#def fizz():
 #   for i in range(1, 101):
  #      if i % 3 == 0 and i % 5 == 0:
   #         i = "FizzBuzz"
    #    elif i % 3 == 0:
     #       i = "Fizz"
      #  elif i % 5 == 0:
       #     i = "Buzz"
        #print(i, end=" ")
#fizz()
#def pow(a, b):
 #   c = a ** b
  #  print(c)
    
    
#pow(-4, 5)

#for i in range(97, 122):
 #   k = ord(chr(i)) - 32
  #  print(f"%s" % (chr(k)), chr(i), end="")
#print()

#for i in range(122, 96, -2):
 #   print(chr(i) + chr(i - 33), end="")
#for i in range(10):
 #   for j in range(i + 1, 10):
  #      if i == 0:
   #         print("0{:1d}, ".format(j), end="")
    #    else:
     ##  if i != 8 or j != 9:
       #     print("", end="")
#import smtplib

#app_pass = 'ozfn xrea czya cbjo'
#server = smtplib.SMTP('smtp.gmail.com', 587)  # Gmail SMTP server and port
#server.starttls()  # Enable TLS encryption
#server.login('alexdelei125@gmail.com', app_pass)  # Your Gmail credentials
#server = smtplib.SMTP('localhost')
#server.sendmail('alexdelei125@gmail.com', 'alexdelei125@gmail.com',
 #               """
  #                  To:alexdelei125@gmail.com
   #                 From:alexdelei125@gmail.com
#
 #                   Hello, How are you doing
#""")
#server.quit()
#def add(a, b):

 #   print("{:d}".format(a), "+" , "{:d}".format(b), "=" , "{:d}".format(a + b))
#add(1, 2)
name = input("Eneter your name: ")
for i in name:
    if i == 'a':
        i = ''
    print(i, end="")
print()
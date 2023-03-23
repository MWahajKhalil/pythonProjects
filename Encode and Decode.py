while True: 
 def encrypt():
  list1 = []
  code = input("Enter the code you want to encrypt :")
  list1.append(code)
  list2 = []
  for i in range(len(list1)):
     for j in range(len(list1[i])):
         list3 = (list1[i][j])
         list2.append(list3)


  for f in list2:
     if f != ' ':       
        ab = (ord(f)+6)
        print(ab,end = '')
        print(".",end = '')
     if f == ' ':
        ab = (",")
        print(ab,end = '')
        



 def decode():

      de1 =(input("Enter the list you want to decode"))
      ac = ''
      for j in de1:
        if j != ',' and j != '.':
            ab = j
            ac = ac + j
        if j == ".":
            acd = int(ac)
            print(chr(acd-6),end = '')
            ac = ''
        if j == ',':
            print(" ",end = '')
          



 main1 = input("\nDo you want to encrypt(e) or decode(d) :")
 if (main1 == "e"):
     encrypt()
 if main1 == "d":
     decode()   




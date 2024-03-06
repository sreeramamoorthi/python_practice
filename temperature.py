while 1 :
  print (" 1 ==> C to F")
  print (" 2==> F to C")
  print ("3==> Exit")
  choice = int (input('Enter your choice :'))
  if choice == 1:
    c = float (input("Enter Celsius :"))
    cf = float (((9/5.0)*c)+32)
    print ("F value : ",cf )
  if choice == 2:
    f = float (input("Enter Fahrenheit :"))
    cc = float (((5/9.0))*(f-32))
    print ("F value :",cc)
  if choice == 3:
    break;

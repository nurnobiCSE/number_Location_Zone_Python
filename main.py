import phonenumbers
from phonenumbers import timezone,geocoder,carrier

number = input("Enter number with for BD : ")
number = "+88"+number
phone_number_parse = phonenumbers.parse(number)
times = timezone.time_zones_for_number(phone_number_parse)
carear = carrier.name_for_number(phone_number_parse,"en")
reg_Of_number = geocoder.description_for_number(phone_number_parse,"en")

strr = phone_number_parse
strr = str(strr)
exact_number = ['0']
strr = strr.split()
exact_number.append(strr[-1])
exact_number = ''.join(exact_number)
print("The exact number is : ",exact_number)

times = str(times)
times = times.split("'")
print("Time-Zone Area of This Number : ",times[1])
print("Operator Of This Number : "+carear)
print("Country Of This Number : "+reg_Of_number)

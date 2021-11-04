
def convert_to_celsius(temperatures):

   celsius = (float(temperatures)-32)/1.8
   return float(round(celsius, 2))

#print(convert_to_celsius(68))

temperatures = (1, 2, 3)
temperatures_converted_to_list = list(temperatures)
#print(temperatures_converted_to_list)

celsius_list = []
for temperature_to_convert in temperatures_converted_to_list:
    temperature_converted = convert_to_celsius(temperature_to_convert)
    celsius_list.append(temperature_converted)
#print(celsius_list)
celsius_tuple = tuple(celsius_list)
print(celsius_tuple)
print(temperatures)
print(tuple(zip(temperatures, celsius_tuple)))




#def temperature_tuple(temperatures, input_unit_of_measurement):

     #celsius_list = []
     #for i in range(list_length):
     #     converted_value = convert_to_celsius(temperatures)
     #     celsius_list.append(converted_value)
     #return celsius_list

#print(temperature_tuple(p1, p2))

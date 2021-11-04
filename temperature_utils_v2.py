from typing import Iterable, Tuple

def convert_to_kelvin(celsius_temp):
    kelvin = float(celsius_temp)+ 273.15
    return float(round(kelvin, 2))

def temperature_tuple(temperatures: Iterable, input_unit_of_measurement: str) -> Tuple[Tuple[float, float]]:

    temperatures_converted_to_list = list(temperatures)

    if input_unit_of_measurement == "f":
        celsius_list = []
        for temperature_to_convert in temperatures_converted_to_list:
            temperature_converted = convert_to_celsius(temperature_to_convert)
            celsius_list.append(temperature_converted)
        celsius_tuple = tuple(celsius_list)
        return tuple(zip(temperatures, celsius_tuple))

    elif input_unit_of_measurement == "k":
        kelvin_list = []
        for temperature_to_convert in temperatures_converted_to_list:
            temperature_converted = convert_to_kelvin(temperature_to_convert)
            kelvin_list.append(temperature_converted)
        kelvin_tuple = tuple(kelvin_list)
        return tuple(zip(temperatures, kelvin_tuple))

    else:
        fahrenheit_list = []
        for temperature_to_convert in temperatures_converted_to_list:
            temperature_converted = convert_to_fahrenheit(temperature_to_convert)
            fahrenheit_list.append(temperature_converted)
        fahrenheit_tuple = tuple(fahrenheit_list)
        return tuple(zip(temperatures, fahrenheit_tuple))

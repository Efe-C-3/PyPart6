from typing import Iterable, Tuple


def convert_to_celsius(fahrenheit_temp: float) -> float:
    """
    Given a float representing a temperature in fahrenheit, return the corresponding value in celsius.

    :param fahrenheit_temp: A float representing a temperature in fahrenheit
    :return: A float representing the corresponding value of the fahrenheit_temp parameter in celsius
    """
    celsius = (float(fahrenheit_temp)-32)/1.8
    return float(round(celsius, 2))


def convert_to_fahrenheit(celsius_temp: float) -> int:
    """
    Given a float representing a temperature in celsius, return the corresponding value in fahrenheit.

    :param celsius_temp: A float representing a temperature in celsius
    :return:  A float representing the corresponding value of the celsius_temp parameter in fahrenheit
    """
    fahrenheit = (float(celsius_temp)*1.8) + 32
    return int(round(fahrenheit, 2))


def temperature_tuple(temperatures: Iterable, input_unit_of_measurement: str) -> Tuple[Tuple[float, float]]:
    """
    Given a tuple or a list of temperatures, this function returns a tuple of tuples.
    Each tuple contains two values. The first is the value of the temperatures parameter. The second is the the value of
    the first converted to the unit of measurement specified in the input_unit_of_measurement parameter.

    :param temperatures: An iterable containing temperatures
    :param input_unit_of_measurement: The unit a measure to use to convert the values in the temperatures parameter
    :return: A tuple of tuples
    """
    temperatures_converted_to_list = list(temperatures)

    if input_unit_of_measurement == "f":
        celsius_list = []
        for temperature_to_convert in temperatures_converted_to_list:
            temperature_converted = convert_to_celsius(temperature_to_convert)
            celsius_list.append(temperature_converted)
        celsius_tuple = tuple(celsius_list)
        return tuple(zip(temperatures, celsius_tuple))

    else:
        fahrenheit_list = []
        for temperature_to_convert in temperatures_converted_to_list:
            temperature_converted = convert_to_fahrenheit(temperature_to_convert)
            fahrenheit_list.append(temperature_converted)
        fahrenheit_tuple = tuple(fahrenheit_list)
        return tuple(zip(temperatures, fahrenheit_tuple))


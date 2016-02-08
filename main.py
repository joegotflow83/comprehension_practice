"""This is a python script designed to practice writing list comprehensions
and improving skills

Author: Joseph Moran
Created: 02/08/16

!/usr/local/env python3.5
"""
from statistics import mean


my_string = "List Comprehensions are the Greatest!".lower()

def remove_vowels(string):
	"""Remove all vowels in the string"""
	return [letter for letter in string if letter not in 'aeiou']

def water_temps(temps):
	"""Display water temps"""
	return [(temp[5], float(temp[4])) for temp in temps]

def convert_to_F(temps):
	"""Convert from Celsius to Farenheight"""
	return [conversion_formula(temp[4]) for temp in temps]

def conversion_formula(num):
	"""Formula for conversion"""
	return (num * (9 / 5) + 32)

def wave_height_records(data):
	"""Create a dictionary displaying date and wave height"""
	records = {}
	formatted_data = {record[5]: record[1] for record in data}
	return formatted_data

def average_wave_height(data):
	"""Return the average wave height for each day"""
	pass

def homework_1(data):
	"""Return homework 1 grades of students"""
	average = mean({grade['Homework 1'] for grade in data.values()})
	return average

data = {'Gale': {'Homework 1': 88, 'Homework 2': 76}, 
		'Jordan': {'Homework 1': 92, 'Homework 2': 87}, 
		'Peyton': {'Homework 1': 84, 'Homework 2': 77}, 
		'River': {'Homework 1': 85, 'Homework 2': 91}
		}

# id,Wave Height,Wave Period,Avg Waves Per Second,Water Temp,Date
data_set = [
	[0, 1.55, 8.33, 5.04, 26.5, '2015-08-01'],
	[1, 1.97, 8.33, 5.96, 26.2, '2015-08-02'],
	[2, 1.89, 9.09, 5.97, 26.2, '2015-08-03'],
	[3, 1.62, 12.5, 6.7, 26.2, '2015-08-04'],
	[4, 1.72, 9.09, 7.31, 26.5, '2015-08-05'],
	[5, 4.09, 13.33, 9.58, 26.9, '2015-08-06'],
	[6, 3.52, 11.11, 8.2, 27.0, '2015-08-07'],
	[7, 2.18, 8.33, 6.0, 26.9, '2015-08-08'],
	[8, 2.14, 9.09, 6.25, 27.1, '2015-08-09'],
	[9, 2.2, 9.09, 6.15, 27.0, '2015-08-10'],
	[10, 1.8, 10.53, 6.3, 26.9, '2015-08-11'],
	[11, 1.99, 8.33, 6.25, 26.8, '2015-08-12'],
	[12, 1.81, 8.33, 6.02, 26.9, '2015-08-13'],
	[13, 1.8, 8.33, 5.46, 27.1, '2015-08-14'],
	[14, 1.75, 7.69, 5.06, 27.1, '2015-08-15'],
	[15, 1.6, 7.69, 5.0, 27.2, '2015-8-16'],
	[16, 1.43, 7.69, 6.25, 27.5, '2015-08-17'],
	[17, 1.51, 9.09, 6.8, 27.7, '2015-08-18'],
	[18, 1.54, 7.69, 6.84, 27.6, '2015-08-19'],
	[19, 1.52, 7.69, 6.63, 28.1, '2015-08-20'],
	[20, 1.47, 7.69, 5.74, 27.5, '2015-0821'],
	[21, 1.71, 8.33, 5.46, 27.7, '2015-08-22'],
	[22, 2.02, 7.69, 5.58, 27.4, '2015-08-23'],
	[23, 0.98, 9.09, 5.44, 27.4, '2015-08-25'],
	[24, 0.8, 9.09, 6.28, 28.0, '2015-08-26'],
	[25, 0.64, 7.69, 5.26, 28.7, '2015-08-27'],
	[26, 0.89, 15.38, 6.89, 28.9, '2015-08-28'],
	[27, 1.42, 18.18, 7.95, 28.5, '2015-08-29'],
	[28, 1.7, 15.38, 7.34, 28.1, '2015-8-30'],
	[29, 1.83, 7.14, 6.28, 27.8, '2015-08-31']
]

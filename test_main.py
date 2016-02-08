import unittest

import main


class MainTest(unittest.TestCase):


	def setUp(self):
		"""Set up testing environment"""
		self.waves = [
		# id,Wave Height,Wave Period,Avg Waves Per Second,Water Temp,Date
			[0, 1.55, 8.33, 5.04, 26.5, '2015-08-01'],
			[1, 1.97, 8.33, 5.96, 26.2, '2015-08-02'],
		]
		self.students = {'Gale': {'Homework 1': 88, 'Homework 2': 76}, 
		'Jordan': {'Homework 1': 92, 'Homework 2': 87}, 
		}

	def tearDown(self):
		"""Tear down testing environment"""
		self.waves = None
		self.students = None

	def test_vowels_removed(self):
		"""Test that the vowels are actually removed from the string"""
		self.assertEqual(main.remove_vowels('this is test'), 
				 ['t', 'h', 's', ' ', 's', ' ', 't', 's', 't'])

	def test_water_temps_displayed(self):
		"""Test that the dates and water temps are converted to floats and returned"""
		self.assertEqual(main.water_temps(self.waves), [('2015-08-01', 26.5), ('2015-08-02', 26.2)])

	def test_conversion_formula(self):
		"""Test formula actually converts from Celsius to Farenheight"""
		self.assertEqual(main.conversion_formula(27), 80.6)

	def test_celsius_to_farenheight(self):
		"""Test that a list of temperatures are converted to Farenheight"""
		self.assertEqual(main.convert_to_F(self.waves), [79.7, 79.16])

	def test_wave_height_records(self):
		"""Test that the date and the wave height is returned"""
		self.assertEqual(main.wave_height_records(self.waves), {'2015-08-01': 1.55, '2015-08-02': 1.97})

	def test_average_wave_height(self):
		"""Test that the average wave height for the month is returned"""
		self.assertEqual(main.average_wave_height(self.waves), 1.76)

	def test_homework_1_mean(self):
		"""Test that the scores of the students for homework 1 are averaged"""
		self.assertEqual(main.homework_1(self.students), 90)

if __name__ == '__main__':
	unittest.main()
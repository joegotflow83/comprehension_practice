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

	def test_error_for_remove_vowels(self):
		"""Test that a typer error occurs when a string is not passed"""
		with self.assertRaises(TypeError):
			main.remove_vowels(5)
			main.remove_vowels(['hello', 'world'])
			main.remove_vowels({'hi': 'whats up', 'num' : 90})

	def test_error_for_water_temps(self):
		"""Test that a type error occurs when an anyting but a list is passed in"""
		with self.assertRaises(TypeError):
			main.water_temps(5)
			main.wave_temps('this is a test')
			main.wave_temps({'name': 'test', 'age': 10})

	def test_error_for_convert_to_F(self):
		"""Test that a type error occurs when anything but a list is passed in"""
		with self.assertRaises(TypeError):
			main.convert_to_F(5)
			main.convert_to_F('yayyyyyyy')
			main.convert_to_F({'this': 'is', 'a': 'dictionary'})

	def test_error_for_conversion_formula(self):
		"""Test that a type error occurs if an int is not passed"""
		with self.assertRaises(TypeError):
			main.conversion_formula('25')
			main.conversion_formula(['numbers', '12', '5', '2'])
			main.conversion_formula({'you': 'get', 'the': 'jist'})

	def test_error_for_homework(self):
		"""Test that a type error occurs if dictionary is not passed"""
		with self.assertRaises(AttributeError):
			main.homework_1(5)
			main.homework_1('last test')
			main.homework_1(['hi', 'done', 'now'])

if __name__ == '__main__':
	unittest.main()
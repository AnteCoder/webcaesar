import string

def alphabet_position(letter):
	lowercase = string.ascii_lowercase
	uppercase = string.ascii_uppercase
	if lowercase.find(letter) >= 0:
		value = lowercase.find(letter)
	if uppercase.find(letter) >= 0:
		value = uppercase.find(letter)

	return value

def rotate_character(char, rot):
	if char in string.ascii_lowercase:
		new = (string.ascii_lowercase[(alphabet_position(char) + rot) % 26])
	elif char in string.ascii_uppercase:
		new = (string.ascii_uppercase[(alphabet_position(char) + rot) % 26])
	else:
		new = char

	return new

def encrypt(text, rot):
	new = ""
	for l in text:
		new += rotate_character(l, rot)

	return new

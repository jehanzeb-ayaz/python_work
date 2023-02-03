glossary = {
"list": "An ordered collection of elements, can be of any data type.",
"dictionary": "An unordered collection of key-value pairs, where keys are unique and can be used to access the corresponding value.",
"string": "A sequence of characters.",
"loop": "A control flow statement that allows code to be executed repeatedly based on a certain condition.",
"function": "A named block of code that performs a specific task and can be called multiple times in a program."
}

for word, meaning in glossary.items():
	print(f"{word}: \n\t{meaning}\n")
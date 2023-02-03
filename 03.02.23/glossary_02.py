glossary = {
    "string": "A sequence of characters.",
    "boolean": "A data type that represents true or false.",
    "integer": "A whole number.",
    "float": "A number with a decimal point.",
    "list": "A collection of items in a particular order."
}

glossary["tuple"] = "An ordered, immutable collection of items."
glossary["dictionary"] = "A collection of key-value pairs."
glossary["function"] = "A block of code that performs a specific task."
glossary["class"] = "A blueprint for creating objects."
glossary["module"] = "A file containing Python definitions and statements."

for key, value in glossary.items():
    print(f"{key.title()}: {value}")

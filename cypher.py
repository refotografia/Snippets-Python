# from 100 Days of Code with Angela Yu, my version of the Caesar Cypher Machine #
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(plain_text, shift_amount, c_direction):
  output = ""
  if c_direction == "decode":
    shift_amount *= -1
  for char in plain_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      output += alphabet[new_position]
    else:
      output += char
  
  print(f'''The {c_direction}d text is {output}''')

should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  caesar(text, shift, direction)
  result = input("Type 'yes' if you want to go again, or type 'no' to end.\n")
  if result == "no":
    should_continue = False
    print("Goodbye!")

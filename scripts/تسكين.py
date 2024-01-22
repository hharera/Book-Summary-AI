def add_sukun_to_every_third_word(text):
  words = text.split()
  for i in range(2, len(words), 2):
    words[i] += "\u0652"
  return ' '.join(words)

def process_file(input_file_path, output_file_path):
  with open(input_file_path, 'r', encoding='utf-8') as file:
    text = file.read()

  modified_text = add_sukun_to_every_third_word(text)

  with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(modified_text)

# Example usage
input_file_path = 'book summary.txt'  # Replace with your input file path
output_file_path = 'book summary with sukun.txt' # Replace with your desired output file path

process_file(input_file_path, output_file_path)

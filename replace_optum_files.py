import sys
import os
import gzip

def replace_delimiter(input_location, output_location):
	for root, dirs, files in os.walk(input_location):
		for file in files:
			input_file = os.path.join(root, file)
			f_input = gzip.open(input_file, 'rt')
			file_content = f_input.read()
			file_content = file_content.replace('||', '|')
			f_input.close()

			output_file = root.replace(input_location, output_location)
			#checking for output location
			if not os.path.exists(output_file):
				os.makedirs(output_file)
			output_file = os.path.join(output_file, file)
			f_output = gzip.open(output_file, 'wt')
			f_output.write(file_content)
			f_output.close()

if __name__ == '__main__':
	input_location = r'/input'
	output_location = r'/output'
	replace_delimiter(input_location, output_location)


	
	
	

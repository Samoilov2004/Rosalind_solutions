input_file = './BA1A_input.txt'
output_file = './BA1A_output.txt'

with open(input_file, 'r') as f:
	Text = f.readline().strip()
	Pattern = f.readline().strip()

def PatternCount(Text, Pattern):
    count = 0
    pattern_length = len(Pattern)
    text_length = len(Text)

    for i in range(text_length - pattern_length + 1):
        if Text[i:i + pattern_length] == Pattern:
            count += 1

    return count

result = PatternCount(Text, Pattern)

print(result)
with open(output_file, 'w') as f:
	f.write(str(result))
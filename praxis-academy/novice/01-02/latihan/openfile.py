with open('count.py') as f:
    read_data = f.read()

# We can check that the file has been automatically closed.
f.closed

for line in f:
    print(line, end='count.py')


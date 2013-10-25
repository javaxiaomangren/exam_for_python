import time

start_time = time.time()

def block(file, size=65536):
	while True:
		nb = file.read(size)
		if not nb:
			break
		yield nb

with open('searchs', 'r') as f:
	print sum([line.count('\n') for line in block(f)])

print time.time() - start_time
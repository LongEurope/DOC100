file1 = open(r'DOC100\Intermediate-(15-\Day26\practicething\file1.txt', mode='r')
file2 = open(r'DOC100\Intermediate-(15-\Day26\practicething\file2.txt', mode='r')

file1_list = [item.strip('\n') for item in file1]
file2_list = [item.strip('\n') for item in file2]

result = [n for n in file1_list if n in file2_list]

print(result)

file1.close()
file2.close()
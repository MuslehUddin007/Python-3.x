# while else
count = 0
while(count < 3):
    count += 1
    print('Hello, Musleh')
else:
    print('In Else Block')

# single statement while block
count = 0
#while(count == 0): print('Hello Geeks')

# for else
list = ['geeks','for','geeks']
for index in range(len(list)):
    print(list[index])
else:
    print('Inside else block')

# left piramid
for i in range(1,5):
    for j in range(i):
        print(i, end=' ')
    print()

# enumerate()
for key, value in enumerate(['The','Big','Bang','Theory']):
    print(key, value)

# zip
questions = ['name','colour','shape']
answers = ['apple','red','a circle']

for question,answer in zip(questions,answers):
    print('What is your {0} ? I am {1}'.format(question,answer))

# iteritems,items
# sorted
#reversed

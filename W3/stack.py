
def Stack(prompt=' Push to Stack (type null if done): '):
    stack = []
    while True:
        top = input(prompt)
        if top in ('n', 'nu', 'nul', 'null'):
            break
        else:
            stack.append(top)
Stack()

print('\n Within Stack: ', Stack, end='\n\n')
print(' <<< Pop the Stack --> LIFO : Last-In-First-Out ')

for _ in range(len(Stack)): # Could we use "for top in stack:" instead?
    print(' pop Stack : ', Stack.pop())
    print('\n ******* Stack = ', Stack)

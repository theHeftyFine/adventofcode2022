from math import floor

class Monkey:

    inspected = 0
    
    def __init__(self, items, operation, left, right, test, success, failure):
        self.items = items
        self.operation = operation
        self.test = test
        self.success = success
        self.failure = failure
        self.left = left
        self.right = right
        
    def __str__(self):
        output = f'Items: {self.items} \n'
        output += f'Operation: {self.left} {self.operation} {self.right} \n'
        output += f'Divisor: {self.test} \n'
        output += f'Success: throw to monkey {self.success} \n'
        output += f'Failure: throw to monkey {self.failure} '
        return output
        
    def inspect(self, item):
        l = self.left
        r = self.right
        if l == 'old':
            if r == 'old':
                return self.calc(item, item)
            else:
                return self.calc(item, int(r))
        elif r == 'old':
            return self.calc(int(l), item)
        else:
            return self.calc(int(l), int(r))
        
    def calc(self, left, right):
        if self.operation == '*':
            return left * right
        else:
            return left + right
            
    def add_item(self, item):
        self.items.append(item)

def read_monkey(input):
    item_terms = input.readline().strip().split()
    items = [int(item.strip(',')) for item in item_terms[2:len(item_terms)]]
        
    operation_terms = input.readline().strip().split()
    left, op, right = operation_terms[3:len(operation_terms)]
    
    test_terms = input.readline().strip().split()
    divisor = int(test_terms[-1])
    
    success_terms = input.readline().strip().split()
    success = int(success_terms[-1])
    
    failure_terms = input.readline().strip().split()
    failure = int(failure_terms[-1])
    
    return Monkey(items, op, left, right, divisor, success, failure)
    
def get_inspected(m):
    return m.inspected
    
def get_divisor(m):
    return m.test
      
def watch_monkeys(rounds, shouldworry = False):
    input = open("input.txt")

    monkeys = []

    line = input.readline()
        
    while line != '':
        terms = line.strip().split()
        if len(terms) > 0 and terms[0] == 'Monkey':
            monkeys.append(read_monkey(input))
        line = input.readline()
        
    round = 0
    
    # the only property of items we're interested in is it's divisibility
    # a number divisible by the product of some numbers is divisible by all it's component numbers
    # i.e 360 is divisible by 10, 6 and 3, but also divisible by (10*3*6) = 180
    # calculate a main_divisor by multiplying all monkey's test divisors, to use as a modulo to keep item size in check
    
    main_divisor = 1
     
    for div in list(map(lambda m: m.test, monkeys)):
        main_divisor *= div
    
    while round < rounds:
        for monkey in monkeys:
            for item in monkey.items:
                new_val = monkey.inspect(item)
                
                if not shouldworry:
                    new_val = floor(new_val / 3)
                else:
                    new_val %= main_divisor
                    
                if new_val % monkey.test == 0:
                    monkeys[monkey.success].add_item(new_val)
                else:
                    monkeys[monkey.failure].add_item(new_val)
                monkey.inspected += 1
            monkey.items = []
        
        round += 1
    return monkeys
    
monkeys_1 = watch_monkeys(20)   

inspections = list(map(get_inspected, monkeys_1))
inspections.sort(reverse=True)

solution_1 = inspections[0] * inspections[1]

monkeys_2 = watch_monkeys(10_000, True)

inspections = list(map(get_inspected, monkeys_2))
inspections.sort(reverse=True)

solution_2 = inspections[0] * inspections[1]

print('solution 01:', solution_1)
print('solution 02:', solution_2)

    
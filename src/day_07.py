"""
Part 1:
Find all the possibly correct equations using + or *. Evaluate left to right.

Part 2:


"""

example = 'inputs/ex_07.txt'
actual = 'inputs/day_07.txt'


def part1(data):
    def generate_operations(nums, target):
        def helper(index, expr, results):
            # Base case: If we used all numbers, store the expression
            if index == len(nums):
                results.append(expr)
                return
            
            # Recursive case: Add each operator between numbers
            for op in ['+', '*']:
                partial = eval(expr)  # evaluate from left to right

                if partial > target:  # truncate: total will only grow
                    return
                    
                helper(index + 1, f"{partial}{op}{nums[index]}", results)

        # Start the recursive process
        results = []
        if nums:
            helper(1, str(nums[0]), results)  # Start with the first number
        return results
    
    with open(data, 'r') as f:
        equations = [line.strip() for line in f.readlines()]

    result = []
    for equation in equations:
        target, numbers = equation.split(':')
        target = int(target)
        numbers = [int(n) for n in numbers.split()]
        for comb in generate_operations(numbers, target):
            if eval(comb) == target:
                result.append(target)
                break

    return sum(result)


assert part1(example) == 3749
print("Part 1:", part1(actual))


def part2(data):
    def generate_operations(nums, target):
        def helper(index, expr, results):
            # Base case: If we used all numbers, store the expression
            if index == len(nums):
                results.append(expr)
                return
            
            # Recursive case: Add each operator between numbers
            for op in ['+', '*', '||']:
                try:
                    partial = eval(expr)  # evaluate from left to right
                except SyntaxError:
                    partial = int(''.join(expr.split("||")))

                if partial > target:
                    return

                helper(index + 1, f"{partial}{op}{nums[index]}", results)

        # Start the recursive process
        results = []
        if nums:
            helper(1, str(nums[0]), results)  # Start with the first number
        return results


    with open(data, 'r') as f:
        equations = [line.strip() for line in f.readlines()]

    result = []
    for equation in equations:
        target, numbers = equation.split(':')
        target = int(target)
        numbers = [int(n) for n in numbers.split()]
        for comb in generate_operations(numbers, target):
            try:
                final = eval(comb)
            except SyntaxError:
                final = int(''.join(comb.split('||')))

            if final == target:
                result.append(target)
                break

    return sum(result)

assert part2(example) == 11387
print("Part 2:", part2(actual))

def get_max_num(*numbers):   

         numbers = [*numbers]

         initial_maximum = numbers[0]

         for number in numbers:   

            if number >  initial_maximum:

                initial_maximum = number

         return initial_maximum

    

    

result = get_max_num(5,6,12,98,0,7,65,8,998,764)

print(result)

""" I took my time to understand 'SELECTION SORT ALGORITHM' and wrote this algorithm to finding the maximum number from a set of numbers... ☺️"""

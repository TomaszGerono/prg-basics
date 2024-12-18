def f(subjects):
    # Given subjects and grades return the name of the subject for which the average grade is the lowest
    def average(total, sum):
        return sum / total
    
    def list_sum(list: list):
        sum = 0
        for grade in grades:
            sum += grade

        return sum
    

    dict_of_averages: dict = {}

    my_total = 0
    my_sum = 0

    
    for subject, grades in subjects.items():

        my_total = len(grades)

        my_sum = list_sum(grades)

        dict_of_averages[subject] = average(my_total, my_sum)


    # find subject with lowest avg
    lowest_avg = max(dict_of_averages.values())
    lowest_subject = ""

    for subject, avg in dict_of_averages.items():
        if avg < lowest_avg:
            lowest_avg = avg
            lowest_subject = subject

    
    return lowest_subject

if __name__ == "__main__":
    subjects = {"bio" : [3,3,4,4,3], "his": [3,3,4,3,3]}

    print(f(subjects)) # returns "his"

    subjects = {"math" : [3,4,4], "geo" : [5,4,4,4], "comp" : [5,4]}
    
    print(f(subjects)) # returns "math"
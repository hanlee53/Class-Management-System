# Han Lee
# 420-LCU Computer Programming, section 02
# S. Hilal, instructor
# Assignment 4

from matplotlib import pyplot as plt
import numpy as np

student_list = open("A4-data.txt",'r')
students = {}

for line in student_list:
    student_record = line.split(",")
    student_dict = {}
    student_dict['name'] = student_record[0]
    student_dict['prg'] = student_record[2]
    student_dict['T1'] = student_record[3]
    student_dict['T2'] = student_record[4]
    student_dict['A1'] = student_record[5]
    student_dict['A2'] = student_record[6]
    student_dict['A3'] = student_record[7]
    student_dict['P'] = student_record[8]

    students[student_record[1]] = student_dict

while True : 

    choice = input('''
1- How many different students are there?
2- How many different programs are there?
3- What program has the most number of students?
4- Display class statistics: number of students, class average, mean and median based on total grade.
5- Display all the students in a particular program.
6- List all the programs that have 3 or more students enrolled.
7- Print the full record for a given student. 
8- Display a pie chart plot to show the distribution of students among the different programs. 
9- Display a bar chart to display the letter grade distributions.
10- Exit

Select an option by entering its number or 10 to exit: ''')

    print("\n--------------------------------------------------------------------------")

    students_diff = {}
    count = 0

    for x in students :

        l = students[x]['name']

        if l in students_diff :
            students_diff[l] += 1
        else:
            students_diff[l] = 1
                
    for x in students_diff :
        count +=1

    # Displays how many students there are
    if choice == "1":

        student_list = open("A4-data.txt",'r')
        student_list1 = student_list.read().splitlines()
        student_list2 = []
        for line in student_list1:
            lines = line.split(",")
            student_list2.append(lines)

        total_grade = 0

        for x in student_list2:
            total_grade = int(x[3]) + int(x[4]) + int(x[5]) + int(x[6]) + int(x[7]) + int(x[8])

            x.append(total_grade)
            
            if total_grade <= 65 :
                x.append("F")
            elif total_grade <= 74 :
                x.append("C")                  
            elif total_grade <= 86 :
                x.append("B")
            else :
                x.append("A")
             
        print("\nThere are", count, "different students: \n")

        l1 = 1

        for x in student_list2:
            print(l1,"-",x[0],"\t",x[1],"\t",x[2],"\t",x[3],"\t",x[4],"\t",x[5],"\t",x[6],"\t",x[7],"\t",x[8],"\t",x[9],"\t",x[10])
            l1 += 1

        print("\n--------------------------------------------------------------------------")
        
    program_diff = {}
    count = 0

    for x in students :

        l = students[x]['prg']

        if l in program_diff :
            program_diff[l] += 1
        else:
            program_diff[l] = 1
                
    for x in program_diff :
        count +=1

    # Displays how many diffrent programs exist 
    if choice == "2":
                    
        print("\nThere are", count, "different programs: \n")

        l1 = 1

        for x in program_diff:
            print(l1,"-",x,program_diff[x],"students enrolled.")
            l1 +=1
            
        print("\n--------------------------------------------------------------------------")

    # Displays program with most students
    if choice == "3":
        
        max_l = max(program_diff, key=program_diff.get)

        print("\n",max_l, "has the most students.")

        print("\n--------------------------------------------------------------------------")

    # Number of students, class average, median, mode
    if choice == "4":
        
        student_list = open("A4-data.txt", 'r')
        student_list1 = student_list.read().splitlines()
        student_list2 = []
        for line in student_list1:
            lines = line.split(",")
            student_list2.append(lines)

        total_grade = 0

        for x in student_list2:
            total_grade = int(x[3]) + int(x[4]) + int(x[5]) + int(x[6]) + int(x[7]) + int(x[8])

            x.append(total_grade)

            if total_grade <= 65:
                x.append("F")
            elif total_grade <= 74:
                x.append("C")
            elif total_grade <= 86:
                x.append("B")
            else:
                x.append("A")
        
        # Prints number of students   
        print('Number of student: ', len(students))

        # Prints class average
        grades_sum = []
        
        for x in student_list2:
            grades_sum.append(x[9])

        print("Average", sum(grades_sum)/len(grades_sum))

        # Prints class median
        if len(grades_sum) % 2 == 0:    # if even
            position = int((len(grades_sum) + 1)/2)
            print("Median", grades_sum[position-1])
        else:                           # if odd
            position = int(len(grades_sum) / 2)
            print(("Median", grades_sum[position-1] + grades_sum[position])/2)

        # Prints class mode
        maximum = 0
        for x in grades_sum:
            if grades_sum.count(x) >= maximum:
                maximum = x

        print('Mode', maximum)


    # Display all students in specific program
    if choice == "5":
        
        wanted_program = input("\nEnter the program code: " ).upper()

        student_list = open("A4-data.txt", 'r')
        student_list1 = student_list.read().splitlines()
        student_list2 = []
        for line in student_list1:
            lines = line.split(",")
            student_list2.append(lines)

        total_grade = 0

        for x in student_list2:
            total_grade = int(x[3]) + int(x[4]) + int(x[5]) + int(x[6]) + int(x[7]) + int(x[8])

            x.append(total_grade)

            if total_grade <= 65:
                x.append("F")
            elif total_grade <= 74:
                x.append("C")
            elif total_grade <= 86:
                x.append("B")
            else:
                x.append("A")

        wanted_students = []
        for x in student_list2 :
            for y in x:
                if y == wanted_program:
                    wanted_students.append(x)
                    #print("\nStudent ID :",x,", Student name :",students[x]['name'],", Total grade :",students[x]['A3'])
        if wanted_program != []:
            for x in wanted_students:
                print(x[0],x[1],x[9],x[10])
        else:
            print("\nInvalid input.")

    programs = {}
    progrmas_list = []

    for x in students :

        p = students[x]['prg']

        if p in programs:
            programs[p] += 1
        else :
            programs[p] = 1

    # List all programs with 3 or more students
    if choice == "6": 

        s_programs = sorted(programs.items(), key=lambda x: x[1], reverse=True)

        count3 = 1

        for a in s_programs:

            print("\n",count3,"- Program Code:",a[0],", Number of Students:",a[1])
            count3 += 1

            if count3 == 11:
                print("\n--------------------------------------------------------------------------")
                break
    # Print student's full record
    if choice == "7":

        student_list = open("A4-data.txt",'r')
        student_list1 = student_list.read().splitlines()
        student_list2 = []
        for line in student_list1:
            lines = line.split(",")
            student_list2.append(lines)

        total_grade = 0

        for x in student_list2:
            total_grade = int(x[3]) + int(x[4]) + int(x[5]) + int(x[6]) + int(x[7]) + int(x[8])

            x.append(total_grade)
            
            if total_grade <= 65 :
                x.append("F")
            elif total_grade <= 74 :
                x.append("C")                  
            elif total_grade <= 86 :
                x.append("B")
            else :
                x.append("A")

        wanted_id = input("\nEnter the ID of a student: ")

        if wanted_id in students and len(wanted_id) == 4 : # Check if the wanted_id is amongst the student_id, then check if it is a valid ID
        
            for x in student_list2:
                if x[1] == wanted_id:
                    print("\nName:", x[0], "   ",   "ID: ", x[1], "\nTest Grades:", ",".join(x[3:5]), "  ", "Assignment Grades:", ",".join(x[5:8]), "   ", "Project Grade:", x[8],"\nTotal Grade:", x[9], "   ", "Letter Grade:", x[10])
                    print("\n--------------------------------------------------------------------------")
                    
        else: 
            print("ID invalid. Request Rejected")
            print("\n--------------------------------------------------------------------------")

    # Display pie chart
    if choice == "8":
        student_list = open("A4-data.txt",'r')
        student_list1 = student_list.read().splitlines()
        student_list2 = []
        for line in student_list1:
            lines = line.split(",")
            student_list2.append(lines)

        dist = []
        for x in student_list2:
            dist.append(x[2])

        prgs = ['HH', 'HP', 'B1', 'B2', 'H2']
        data = [dist.count("HH"), dist.count("HP"), dist.count("B1"), dist.count("B2"), dist.count("H2")]

        fig = plt.figure(figsize = (10, 7))
        plt.pie(data, labels = prgs)
        plt.show()

    # Display bar chart
    if choice == "9":
        student_list = open("A4-data.txt",'r')
        student_list1 = student_list.read().splitlines()
        student_list2 = []
        for line in student_list1:
            lines = line.split(",")
            student_list2.append(lines)

        total_grade = 0

        for x in student_list2:
            total_grade = int(x[3]) + int(x[4]) + int(x[5]) + int(x[6]) + int(x[7]) + int(x[8])

            x.append(total_grade)
            
            if total_grade <= 65 :
                x.append("F")
            elif total_grade <= 74 :
                x.append("C")                  
            elif total_grade <= 86 :
                x.append("B")
            else :
                x.append("A")

        dist = []
        for x in student_list2:
            dist.append(x[10])

        grade = ['A', 'B', 'C', 'F']
        data = [dist.count("A"), dist.count("B"), dist.count("C"), dist.count("F")]

        fig = plt.figure(figsize = (10, 7))
        plt.bar(grade, data, color ='blue', width = 0.4)
        plt.show()

    # Exit program
    if choice == "10":
        break

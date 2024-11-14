import random
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
students.sort()
classes = ['Математика', 'Русский язык', 'Информатика']
students_marks = {}
for student in students:
    students_marks[student] = {}
    for class_ in classes:
        marks = [random.randint(1, 5) for i in range(3)]
        students_marks[student][class_] = marks
for student in students:
        print(f'''{student}
        {students_marks[student]}''')

        print('''
            Список команд:
            1. Добавить оценки ученика по предмету
            2. Вывести средний балл по всем предметам по каждому ученику
            3. Вывести все оценки по всем ученикам
            4. Удалить оценку
            5. Редактирование ученика
            6. Добавить новый предмет
            7. Вывод информации по всем оценкам для определенного ученика
            8. Вывести средний балл по всем предметам по определенного ученика
             ''')

while True:
            command = int(input('Введите команду: '))
            if command == 1:
                print('1. Добавить оценку ученика по предмету')
                student = input('Введите имя ученика: ')
                class_ = input('Введите предмет: ')
                mark = int(input('Введите оценку: '))
                if student in students_marks.keys() and class_ in students_marks[student].keys():
                    students_marks[student][class_].append(mark)
                    print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
                else:
                 print('ОШИБКА: неверное имя ученика или название предмета')

            elif command == 2:
                print('2. Вывести средний балл по всем предметам по каждому ученику')
                for student in students:
                    print(student)
                    for class_ in classes:
                        marks_sum = sum(students_marks[student][class_])
                        marks_count = len(students_marks[student][class_])
                        print(f'{class_} - {marks_sum // marks_count}')
                    print()

            elif command == 3:
                print('3. Вывести все оценки по всем ученикам')
                for student in students:
                    print(student)
                    for class_ in classes:
                        print(f'\t{class_} - {students_marks[student][class_]}')
                    print()

            elif command == 4:
                print('4. Удалить оценку:')
                name = input('Введите имя ученика: ')
                class_ = input('Введите предмет: ')
                print(f'''{name}
                    Оценки по: {class_} {students_marks[student][class_]}''')
                mark = int(input('Введите оценку которую нужно удалить:'))
                if name in students_marks.keys() and class_ in students_marks[student].keys():
                    if mark in students_marks[student][class_]:
                     students_marks[student][class_].remove(mark)
                    print('Оценка удалена')
                    print(f'''{name}
                    {students_marks[student]}''')
                else:
                   print('Оценки в списке нет')

            elif command == 5:
                print('5. Редактирование ученика:')
                student = input('Введите имя ученика: ')
                newStudent = input('Введите новое имя ученика: ')
                if student in students_marks.keys():
                    students_marks[newStudent] = students_marks[student]
                    del students_marks[student]

                    print(f'Имя{student} изменен на {newStudent}')
                    print(f'''{newStudent}
                               {students_marks[newStudent]}''')
                else:
                    print('Неправильное имя ученика')

            elif command == 6:
                print('6. Добавить новый предмет:')
                newclass = input('Введите название нового предмета: ')
                classes.append(newclass)
                for student_classes in students_marks.values():
                    student_classes[newclass] = []
                print(f'Предмет {newclass} успешно добавлен.')


                for student in students:
                    print(f'''{student}
                        {students_marks[student]}''')

            elif command == 7:
                print('7. Вывод информации по всем оценкам для определенного ученика:')
                student = input('Введите имя ученика: ')
                for class_ in classes:
                    print(f'\t{class_} - {students_marks[student][class_]}')
                print()

            elif command == 8:
                print('8. Вывести средний балл по всем предметам для определенного ученика:')
                student = input('Введите имя ученика: ')
                for class_ in classes:
                      marks_sum = sum(marks)
                      marks_count = len(marks)
                      print(f'{class_} - {marks_sum // marks_count}')
                      print()


Александра
        {'Математика': [4, 4, 1], 'Русский язык': [3, 1, 2], 'Информатика': [2, 4, 2]}

            Список команд:
            1. Добавить оценки ученика по предмету
            2. Вывести средний балл по всем предметам по каждому ученику
            3. Вывести все оценки по всем ученикам
            4. Удалить оценку
            5. Редактирование ученика
            6. Добавить новый предмет
            7. Вывод информации по всем оценкам для определенного ученика
            8. Вывести средний балл по всем предметам по определенного ученика
             
Ангелина
        {'Математика': [4, 5, 3], 'Русский язык': [2, 5, 3], 'Информатика': [1, 1, 4]}

            Список команд:
            1. Добавить оценки ученика по предмету
            2. Вывести средний балл по всем предметам по каждому ученику
            3. Вывести все оценки по всем ученикам
            4. Удалить оценку
            5. Редактирование ученика
            6. Добавить новый предмет
            7. Вывод информации по всем оценкам для определенного ученика
            8. Вывести средний балл по всем предметам по определенного ученика
             
Аполлон
        {'Математика': [4, 4, 4], 'Русский язык': [3, 3, 3], 'Информатика': [3, 2, 2]}

            Список команд:
            1. Добавить оценки ученика по предмету
            2. Вывести средний балл по всем предметам по каждому ученику
            3. Вывести все оценки по всем ученикам
            4. Удалить оценку
            5. Редактирование ученика
            6. Добавить новый предмет
            7. Вывод информации по всем оценкам для определенного ученика
            8. Вывести средний балл по всем предметам по определенного ученика
             
Дарья
        {'Математика': [1, 2, 4], 'Русский язык': [4, 2, 2], 'Информатика': [1, 4, 2]}

            Список команд:
            1. Добавить оценки ученика по предмету
            2. Вывести средний балл по всем предметам по каждому ученику
            3. Вывести все оценки по всем ученикам
            4. Удалить оценку
            5. Редактирование ученика
            6. Добавить новый предмет
            7. Вывод информации по всем оценкам для определенного ученика
            8. Вывести средний балл по всем предметам по определенного ученика
             
Ярослав
        {'Математика': [5, 5, 4], 'Русский язык': [5, 5, 3], 'Информатика': [2, 4, 1]}

            Список команд:
            1. Добавить оценки ученика по предмету
            2. Вывести средний балл по всем предметам по каждому ученику
            3. Вывести все оценки по всем ученикам
            4. Удалить оценку
            5. Редактирование ученика
            6. Добавить новый предмет
            7. Вывод информации по всем оценкам для определенного ученика
            8. Вывести средний балл по всем предметам по определенного ученика
             
Введите команду: 8
8. Вывести средний балл по всем предметам для определенного ученика:
Введите имя ученика: Ангелина
Математика - 2

Русский язык - 2

Информатика - 2


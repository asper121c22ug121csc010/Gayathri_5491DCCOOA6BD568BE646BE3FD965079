
class Student:

  def_init_(self,name,roll_number,cgpa):
      self.name= name 
  self.roll_nmber=roll_number
  self.cgpa=cgpa

def sort_students(student_list):
   #sort the list of students in descending order of CGPA
  sorted _students =sorted(students_list,
                           key=lambda student:
                           student.cgpa,
                                       reverse=true)  
  return sorted_students

    #Example usage:
  students=[
    student("Hari","A123",7.8),
    student("siva","A124",7.9),
    student("gayu","A125",8.5),
  ]
  sorted_students=
  sort_student(students)
  # print the sorted list of students
for student in sorted_students:
    print("Name:{},Roll number:{},CGPA:{}".
    format(student.name,
                 student.
roll_number,
           student.cgpa))


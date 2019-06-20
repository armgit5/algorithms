class Professor
 attr_reader :name, :class_name, :exam_date
 def initialize(name, class_name, student, secretary, dean)
   @name = name
   @class = class_name

   @student = student
   @secretary = secretary
   @dean = dean
 end
 def set_midterm(midterm_date)
   @exam_date = midterm_date
   @student.update(self)
   @secretary.update(self)
   @dean.update(self)
 end
end

class Student
 def update(prof)
   puts "I need to start studying for Prof #{prof.name} exam on the #{prof.exam_date}"
 end
end

class Secretary
 def update(prof)
   puts "I will find a room for the midterm on the #{prof.exam_date}"
 end
end

class Dean
 def update(prof)
   puts "I will go over the midterm before #{prof.exam_date}"
 end
end

student = Student.new
secretary = Secretary.new
dean = Dean.new
prof = Professor.new("Jeff Professor", "Software Engineering", student, secretary, dean)
prof.set_midterm("Oct 25th")

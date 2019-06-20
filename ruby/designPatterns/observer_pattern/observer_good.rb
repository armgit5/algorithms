
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

class Professor
 attr_reader :name, :class_name, :exam_date
 attr_accessor :observers

 def initialize(name, class_name)
   @name = name
   @class = class_name
   @observers = []
 end
 def set_midterm(midterm_date)
   @exam_date = midterm_date
   notify_observers
 end
 def add_observer(observer)
   @observers << observer
 end
 def notify_observers
   observers.each do |observer|
     observer.update(self)
   end
 end
end

student = Student.new
secretary = Secretary.new
dean = Dean.new
prof = Professor.new("Jeff Professor", "Software Engineering")

prof.add_observer(student)
prof.add_observer(secretary)
prof.add_observer(dean)

prof.set_midterm("Oct 25th")

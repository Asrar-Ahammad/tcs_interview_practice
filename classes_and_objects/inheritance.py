class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def print_name(self):
        return f"{self.fname} {self.lname}"

class student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname, lname) # (or) Person.__init__(self, fname, lname)
        self.graduation_year = year

s1 = student("Asrar", "Ahammad",2024)
print(s1.print_name())


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
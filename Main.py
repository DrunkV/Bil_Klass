from Bil import Bil #Från Bil fil import Bil klass
from Person import Person #Från Person fil import Person Klass

p1 = Person("Bruno", "Silva")
b1 = Bil("MEU542", "Peugeot", 2016, 1100, 90, p1)
print(f"{b1.Person.förnamn} {b1.Person.efternamn} har en {b1.fabrikat}, reg. nummer {b1.reg_num}")
p2 = Person("André", "Silva")
b2 = Bil("IRM001", "Renault", 2027, 1100, 90, p2)
print(f"{b2.Person.förnamn} {b2.Person.efternamn} har en {b2.fabrikat}, reg. nummer {b2.reg_num}")
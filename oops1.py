# intiate class
class employee:
    # special function/ magic methos/ dunder method ( constructor)
    def __init__(self):
        # print(id(self))
        # print("started executing the attributes or data")
        self.id = 123
        self.salary = 50000
        self.designation = "Software Engineer"

        # print("completed executing the attributes or data")

    
    def travel(self, destination):
        print("started executing the method")
        print(f" employee is travelling to {destination}")


#creating an obj/instance of the class
 
sam = employee()
# sam.name = "sam kumar"

# print(sam.name)

# nani = employee()

#printing the attributes
#print(sam.id)
# print(id(sam))
# print(id(nani))

# calling the method
# sam.travel("New York")


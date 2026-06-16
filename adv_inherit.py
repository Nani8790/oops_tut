# # #single or basic inheritance

# # #base class
# # class Parent:
# #     def __init__(self, name):
# #         self.name = name


# #     def greet(self):
# #         print(f"Hello my name is {self.name}.")


# # #Derived class
# # class child(Parent):
# #     def play(self):
# #         print(f"{self.name} is playing")




# # child_name = child("Alice")
# # child_name.greet()
# # child_name.play()


# #   Multi level inheritance

# #base class

# class grandparent:
#     def __init__(self, name):
#         self.name = name

#     def tell_story(self):
#         print(f"{self.name} tells a story")


# class parent(grandparent):
#     def work(self):
#         print(f"{self.name} is working.")

# class children(parent):
#     def play(self):
#         print(f"{self.name} is playing.")
        


# child = children("nani")

# child.tell_story()
# child.work()
# child.play()

#3. Hierarchical Inheritance


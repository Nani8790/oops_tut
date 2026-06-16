from oops_proj import chatbook

user1 = chatbook()
print(user1.id)

#static method (can use directly from class rather than obj )
chatbook.set_id(10)
user2 = chatbook()
print(user2.id)

# print(user1._chatbook__name)


#getter and setter
# print(user1.get_name())
# user1.set_name("Agent1")
# print(user1.get_name())


# a1 = [1,2,3,4]
# print(len(a1))

# #method
# user1 = chatbook()
# user1.send_message()

friends = ["Harry", "Sam", "Voldemort", "Rob", "Sirius"]
other_friends = ["Holly", "Berry", "Samuel"]
print(friends)

print(friends[1:3])  # excludes the element on the last index
friends.extend(other_friends)
print(friends)
friends.append("another guy")
print(friends)
friends.insert(3, 50000)
print(friends)


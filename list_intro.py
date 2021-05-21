computer_parts = ["CPU",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]
print(computer_parts)

#computer_parts[2] = "Trackball"
#   **from the documentation of python website
computer_parts[3:] = "Trackball"
print(computer_parts)

#   This will replace the strings as we wanted earlier.
computer_parts[3:] = ["Trackball"]
print(computer_parts)


# for part in computer_parts:
#     print(part)
#
# print("-"*45)
# print(computer_parts[2])
# print("-"*45)
# print(computer_parts[0:4:2])
# print("-"*45)
# print(computer_parts[0:4])
# print("-"*45)
# print(computer_parts[-1])


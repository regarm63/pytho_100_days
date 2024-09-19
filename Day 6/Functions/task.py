# def my_function():
#     print("Hello")
#     print("Bye")
#
# my_function()
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# this is for hurdle 4
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
#
# for step in range(6):
#     jump()

# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#
#     while front_is_clear():
#         move()
#     turn_left()
#
#
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()
#
#  this code works but can get stuck in a loop
#  debug can be done but wait till day 15!
#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
guest_list = ['worm', 'cheeto']

uninvited = 'worm'

guest_list.remove(uninvited)

guest_list.insert(1, 'max')

message = f"Come to dinner, {guest_list[0].title()}\nCome to dinner, {guest_list[1].title()}"

print(message)
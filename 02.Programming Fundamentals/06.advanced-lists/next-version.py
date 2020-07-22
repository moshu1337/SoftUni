current_version = input().split('.')
new_version_number = int("".join(current_version)) + 1
new_version_string = list(str(new_version_number))


print('.'.join(new_version_string))

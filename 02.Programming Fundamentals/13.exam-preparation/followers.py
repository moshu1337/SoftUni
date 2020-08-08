likes = {}
comments = {}

while True:
    cmd_input = input()

    if cmd_input == "Log out":
        break

    tokens = cmd_input.split(": ")
    command = tokens[0]
    username = tokens[1]

    if command == "New follower":
        if username in likes:
            continue

        likes[username] = 0
        comments[username] = 0
    elif command == "Like":
        count = int(tokens[2])

        if username not in likes:
            likes[username] = 0
            comments[username] = 0

        likes[username] += count
    elif command == "Comment":
        if username not in comments:
            likes[username] = 0
            comments[username] = 0

        comments[username] += 1
    elif command == "Blocked":
        if username in likes:
            del likes[username]
            del comments[username]
        else:
            print(f"{username} doesn't exist.")

print(f"{len(likes)} followers")
sorted_likes = dict(sorted(likes.items(), key=lambda u: (-u[1], u[0])))

for username, count_likes in sorted_likes.items():
    count_comments = comments[username]
    print(f"{username}: {count_likes + count_comments}")

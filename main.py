import random as rd
should_continue=True
print('''

     8                            8
     8      /```|     .@@@@@,     8
     8     |  66|_    @@@@@@@@,   8 (\/)
     8     C     _)   aa`@@@@@@   8  \/
     8(\/)  \ ._|    (_   ?@@@@   8
    |8:\/:~:~) /:~:~: =' @@@@~:~:~8
    |8::::::/\\/`\;_:::\ (__::::::8
    |8:::::| \ '|___/` \\// `\):::8
    |8::::|| | '|::/ /  ^^  \ \:::8
    |8::::|| | ' \:| \__/\__/ |:::8
    |8o:::|\ \  ' |:\_\    /_/::::8o
    |"8o:::=\ \===::/`\`%%`/'\::::"8o
    |\"8o~|  \_\  \|   `""`   |:~:~\8o
    \ \"8o\   )))  \           \::::"8o
     \ \"8o\`.  \   \           \::::"8o
      \|~~~~~| -|| -|mmmmmmmmmmmm~~~~~|
       `~~~~~|  ||  |~~|  |~|  |~~~~~~
     jgs     |  ||  |  |__| |__|
             |  ||  |  \  | \  |
             |__||__|  (~~^\(~~^\
             (   \   \  `-._)`-._)
              `-._)-._)

''')
print("Welcome to the Love Calculator ❤️")
while should_continue:
    male_name=input("Enter your name:\n")
    female_name=input("Enter your partner's name:\n")
    percent=rd.randint(0,100)
    print(f"Love between {male_name} & {female_name} is {percent}%.")
    user_inp=input("Do you want to check any other result? Y or N?\n").lower()
    if user_inp=='n':
        print("Thanks for using the love calculator.")
        should_continue=False
#u: is_it_the_onion_
#p: abcbanana123
import praw
from random import shuffle

reddit = praw.Reddit(
client_id="Xe1a2lw3BsjuOw",
client_secret="abwEEA0qj29Fhfea8RCge2IEbK4",
user_agent="desktop:myonionapp:1.0.0 (by /u/jmang00)"
)

print('Welcome to )

try:
    n = int(input('How many articles do you want to try? '))
except ValueError:
    n = 10
print()

print('Searching for articles...')

titles = []
for sub in ['theonion','nottheonion']:
    if n % 2 == 1 and sub == 'nottheonion':
        limit = (n-1)/2
    else:
        limit = round(n/2)
    for submission in reddit.subreddit(sub).hot(limit=limit):
        titles.append([submission.title,submission.url,sub])


score = 0

shuffle(titles)
for title in titles:
    print(title[0])
    while True:
        choice = input("Do you think that's a real article title? (y/n): ")
        if choice == "y":
            if title[2] == 'nottheonion':
                print("Correct! That's a real article.")
                score += 1
            else:
                print("Wrong! That's an Onion article!")
            print(title[1])
            print()
            break
        elif choice == "n":
            if title[2] == 'theonion':
                print("Correct! That's an Onion article!")
                score += 1
            else:
                print("Wrong! That's a real article.")
            print(title[1])
            print()
            break

print(f'Score: {score}/{n} ({round(score/n*100)}%)')

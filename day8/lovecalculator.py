'''Love calculator exercise'''

# I wasn't sure how to go about this one, primarily because I remembered a similar counting
# thing done in the hangman game but I wasn't able to replicate it in the same way.
def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()

    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e

    score = int(str(first_digit) + str(second_digit))
    print(score)

calculate_love_score("Nezzy", "Celeste")
# My main issue with all these codes and exercises is that I understand how
# each concept works, but don't fully understand how to implement it or even consider it.
# Mind kinda goes to mush when thinking of the solution to the logic, but I think that takes
# more practice and experience. After all this is just day 8.

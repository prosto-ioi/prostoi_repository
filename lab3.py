import random
import itertools

def grams_to_ounces(grams):
    return 28.3495231 * grams

def fahrenheit_to_celsius(f):
    return (5 / 9) * (f - 32)

def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return None

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(lst):
    return [x for x in lst if is_prime(x)]

def string_permutations(s):
    return list(itertools.permutations(s))

def reverse_sentence(s):
    return " ".join(s.split()[::-1])

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

def spy_game(nums):
    code = [0, 0, 7]
    idx = 0
    for num in nums:
        if num == code[idx]:
            idx += 1
            if idx == len(code):
                return True
    return False

def sphere_volume(r):
    return (4/3) * 3.14159 * (r**3)

def unique_list(lst):
    unique = []
    for i in lst:
        if i not in unique:
            unique.append(i)
    return unique

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

def histogram(lst):
    for x in lst:
        print("*" * x)

def guess_the_number():
    name = input("Hello! What is your name?\n")
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1, 20)
    guesses = 0
    while True:
        guess = int(input("Take a guess.\n"))
        guesses += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break

movies = [
{"name": "Usual Suspects","imdb": 7.0,"category": "Thriller"},
{"name": "Hitman","imdb": 6.3,"category": "Action"},
{"name": "Dark Knight","imdb": 9.0,"category": "Adventure"},
{"name": "The Help","imdb": 8.0,"category": "Drama"},
{"name": "The Choice","imdb": 6.2,"category": "Romance"},
{"name": "Colonia","imdb": 7.4,"category": "Romance"},
{"name": "Love","imdb": 6.0,"category": "Romance"},
{"name": "Bride Wars","imdb": 5.4,"category": "Romance"},
{"name": "AlphaJet","imdb": 3.2,"category": "War"},
{"name": "Ringing Crime","imdb": 4.0,"category": "Crime"},
{"name": "Joking muck","imdb": 7.2,"category": "Comedy"},
{"name": "What is the name","imdb": 9.2,"category": "Suspense"},
{"name": "Detective","imdb": 7.0,"category": "Suspense"},
{"name": "Exam","imdb": 4.2,"category": "Thriller"},
{"name": "We Two","imdb": 7.2,"category": "Romance"}
]

# 14. IMDB > 5.5
def is_good_movie(movie):
    return movie["imdb"] > 5.5

# 15. Sublist IMDB > 5.5
def good_movies(movies):
    return [m for m in movies if m["imdb"] > 5.5]

# 16. Movies by category
def movies_by_category(movies, category):
    return [m for m in movies if m["category"] == category]

# 17. Average IMDB score
def avg_imdb(movies):
    return sum(m["imdb"] for m in movies) / len(movies)

# 18. Average IMDB score by category
def avg_imdb_category(movies, category):
    category_movies = [m for m in movies if m["category"] == category]
    return sum(m["imdb"] for m in category_movies) / len(category_movies)

if __name__ == "__main__":
    print("Grams to ounces (100g):", grams_to_ounces(100))
    print("Fahrenheit to Celsius (100F):", fahrenheit_to_celsius(100))
    print("Solve puzzle:", solve(35, 94))
    print("Filter primes:", filter_prime([1,2,3,4,5,6,7,11]))
    print("Permutations of 'abc':", string_permutations("abc"))
    print("Reverse sentence:", reverse_sentence("We are ready"))
    print("Has 33:", has_33([1,3,3]))
    print("Spy game:", spy_game([1,2,4,0,0,7,5]))
    print("Sphere volume (r=3):", sphere_volume(3))
    print("Unique list:", unique_list([1,2,2,3,3,4]))
    print("Palindrome 'madam':", is_palindrome("madam"))
    print("Histogram:")
    histogram([4, 9, 7])
    print("Good movies:", good_movies(movies))
    print("Movies in Romance:", movies_by_category(movies, "Romance"))
    print("Average IMDB:", avg_imdb(movies))
    print("Average Romance IMDB:", avg_imdb_category(movies, "Romance"))

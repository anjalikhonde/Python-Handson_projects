import random

def fake_random_news():
    fake_subjects = [
        "Shah Rukh Khan",
        "Virat Kohli",
        "Nirmala Sitharaman",
        "A Mumbai Cat",
        "A Group of Monkeys",
        "Prime Minister Modi",
        "An Auto Rickshaw Driver from Delhi",
        "A Software Engineer",
        "A College Student",
        "A Tea Seller",
        "A Cricket Umpire",
        "A Police Officer",
        "A Robot",
        "A Ghost",
        "A Bollywood Director",
        "A School Principal",
        "A Doctor",
        "A YouTuber",
        "A Gamer",
        "A Farmer",
        "A News Reporter",
        "An Astronaut",
        "A Panda",
        "A Dog",
        "A Cow",
        "A Tiger",
        "An Alien",
        "A Time Traveler",
        "A Billionaire",
        "A Street Magician"
    ]

    fake_actions = [
        "launches",
        "cancels",
        "dances with",
        "eats",
        "declares war on",
        "orders",
        "celebrates",
        "steals",
        "finds",
        "discovers",
        "builds",
        "buys",
        "sells",
        "throws",
        "wins",
        "loses",
        "starts",
        "ends",
        "paints",
        "hugs",
        "chases",
        "teaches",
        "sings with",
        "plays cricket with",
        "argues with",
        "laughs at",
        "takes a selfie with",
        "rides",
        "flies over",
        "cooks",
        "opens",
        "closes",
        "investigates",
        "adopts",
        "invites",
        "arrests",
        "promotes",
        "rejects",
        "creates",
        "destroys"
    ]

    fake_places_or_things = [
        "at Red Fort",
        "in a Mumbai Local Train",
        "a plate of samosas",
        "inside Parliament",
        "at Ganga Ghat",
        "during an IPL Match",
        "at India Gate",
        "inside a shopping mall",
        "on the Moon",
        "at a railway station",
        "inside a classroom",
        "on Marine Drive",
        "inside a metro train",
        "at a wedding",
        "during a press conference",
        "at a cricket stadium",
        "inside a hospital",
        "at a tea stall",
        "in a village",
        "at the airport",
        "inside a cinema hall",
        "at a birthday party",
        "inside a temple",
        "at a bus stop",
        "on a beach",
        "inside a five-star hotel",
        "at a college canteen",
        "during a live TV show",
        "on top of a mountain",
        "inside a supermarket",
        "at a science fair",
        "during a music concert",
        "inside a library",
        "at a water park",
        "on a cricket pitch",
        "inside a spaceship",
        "at a zoo",
        "during a marathon",
        "at a police station",
        "inside a secret laboratory"
    ]
    return fake_subjects,fake_actions,fake_places_or_things


def fake_sports_news():
    sports_subjects = [
    "Virat Kohli", "Rohit Sharma", "MS Dhoni", "Jasprit Bumrah",
    "Hardik Pandya", "A Cricket Fan", "The Indian Team",
    "A Football Coach", "A Tennis Player", "A Wrestler"
]

    sports_actions = [
    "wins", "loses", "celebrates", "breaks", "cancels",
    "announces", "hits", "scores", "trains with", "challenges"
]

    sports_places = [
    "at Wankhede Stadium", "during IPL", "at Eden Gardens",
    "inside the dressing room", "during World Cup",
    "at a football ground", "inside a sports academy",
    "during practice", "at the Olympics", "on the cricket pitch"
]  
    return sports_subjects, sports_actions, sports_places


def fake_politics_news():
    politics_subjects = [
    "Prime Minister Modi", "Rahul Gandhi", "A Chief Minister",
    "An MLA", "A Member of Parliament", "The Election Commission",
    "A Political Party", "A Minister", "The Finance Minister", "The Governor"
]

    politics_actions = [
    "announces", "rejects", "approves", "launches",
    "discusses", "debates", "visits", "promises",
    "questions", "celebrates"
]

    politics_places = [
    "inside Parliament", "at Red Fort", "during an election rally",
    "at India Gate", "inside the Secretariat",
    "during a press conference", "at Raj Bhavan",
    "inside the Assembly", "at Rashtrapati Bhavan", "in Delhi"
]
    return politics_subjects, politics_actions, politics_places

def fake_temple_news():
    temple_subjects = [
    "A Priest", "Lord Ganesha", "A Devotee",
    "Temple Committee", "A Sadhu", "Pilgrims",
    "Temple Elephant", "A Spiritual Guru", "A Monk", "A Volunteer"
]

    temple_actions = [
    "offers", "blesses", "decorates", "organizes",
    "celebrates", "lights", "cleans", "prays in",
    "visits", "announces"
]

    temple_places = [
    "at Tirupati Temple", "inside Kedarnath Temple",
    "at Siddhivinayak Temple", "during Aarti",
    "at Mahakaleshwar Temple", "inside a temple hall",
    "during Navratri", "at Somnath Temple",
    "at Kashi Vishwanath", "during Mahashivratri"
]
    return temple_subjects, temple_actions, temple_places

def fake_bollywood_news():
    bollywood_subjects = [
    "Shah Rukh Khan", "Salman Khan", "Aamir Khan",
    "Deepika Padukone", "Alia Bhatt", "Ranbir Kapoor",
    "A Film Director", "A Choreographer", "A Producer", "A Singer"
]

    bollywood_actions = [
    "announces", "dances with", "signs", "rejects",
    "celebrates", "wins", "films", "launches",
    "performs at", "visits"
]

    bollywood_places = [
    "at Film City", "during an award show",
    "inside a movie set", "at a premiere",
    "during a music launch", "inside a studio",
    "at a fan event", "during shooting",
    "in Mumbai", "at a press conference"
]
    return bollywood_subjects, bollywood_actions, bollywood_places

def fake_technology_news():
    technology_subjects = [
    "Google", "Microsoft", "Apple", "OpenAI",
    "A Hacker", "A Software Engineer", "An AI Robot",
    "A Programmer", "A Startup", "A Tech Company"
]

    technology_actions = [
    "launches", "creates", "updates", "deletes",
    "discovers", "develops", "hacks", "tests",
    "improves", "reveals"
]

    technology_places = [
    "inside a data center", "during a tech conference",
    "at Google HQ", "on GitHub",
    "inside a server room", "at CES",
    "inside a laboratory", "during a software update",
    "on the internet", "inside Silicon Valley"
]
    return technology_subjects, technology_actions, technology_places

def fake_college_news():
    college_subjects = [
    "A Professor", "A Student", "The Principal",
    "A Class Monitor", "A Fresher", "A Senior",
    "The Placement Officer", "A Lab Assistant",
    "A College Club", "The Dean"
]

    college_actions = [
    "announces", "wins", "fails", "organizes",
    "cancels", "starts", "celebrates",
    "forgets", "submits", "teaches"
]

    college_places = [
    "inside the classroom", "at the canteen",
    "during exams", "inside the library",
    "at the college gate", "inside the lab",
    "during placement", "at the auditorium",
    "inside the hostel", "during the annual fest"
]
    return college_subjects, college_actions, college_places

def fake_horror_news():
    horror_subjects = [
    "A Ghost", "A Vampire", "A Witch",
    "A Haunted Doll", "A Zombie",
    "A Monster", "A Spirit", "A Skeleton",
    "A Black Cat", "An Invisible Man"
]

    horror_actions = [
    "appears", "laughs at", "haunts",
    "chases", "scares", "follows",
    "screams at", "captures", "vanishes from",
    "hides in"
]

    horror_places = [
    "inside an old mansion", "at midnight",
    "inside a forest", "near a cemetery",
    "inside a haunted school", "inside a tunnel",
    "during a thunderstorm", "inside an abandoned hospital",
    "on a lonely road", "inside a cave"
]
    return horror_subjects, horror_actions, horror_places

def fake_space_news():
    space_subjects = [
    "An Astronaut", "NASA", "ISRO",
    "A Space Robot", "An Alien",
    "A Scientist", "A Satellite",
    "A Rocket", "A Space Tourist", "A Mars Rover"
]

    space_actions = [
    "discovers", "launches", "lands on",
    "captures", "explores", "finds",
    "builds", "visits", "tests", "photographs"
]

    space_places = [
    "on Mars", "on the Moon",
    "inside the ISS", "in deep space",
    "near Jupiter", "inside a rocket",
    "during a space mission", "on an asteroid",
    "near Saturn", "inside a space station"
]
    return space_subjects, space_actions, space_places

def fake_food_news():
    food_subjects = [
    "A Chef", "A Food Blogger", "A Restaurant",
    "A Pizza", "A Burger", "A Plate of Biryani",
    "A Tea Seller", "A Sweet Shop", "A Waiter", "A Customer"
]

    food_actions = [
    "prepares", "eats", "throws", "orders",
    "cooks", "shares", "burns", "decorates",
    "serves", "wins"
]

    food_places = [
    "inside a restaurant", "at a wedding",
    "during lunch", "at a food festival",
    "inside a kitchen", "at a tea stall",
    "during dinner", "inside a bakery",
    "at a buffet", "inside a café"
]
    return food_subjects, food_actions, food_places

def fake_random_funny_news():
    funny_subjects = [
    "A Monkey", "A Dog", "A Cat",
    "A Penguin", "A Robot", "A Time Traveler",
    "An Alien", "A Billionaire", "A Magician", "A Superhero"
]

    funny_actions = [
    "steals", "dances with", "hugs",
    "orders", "rides", "eats",
    "throws", "laughs at", "paints", "chases"
]

    funny_places = [
    "inside a shopping mall", "at the beach",
    "inside a metro", "on the Moon",
    "during an IPL match", "inside a supermarket",
    "at a birthday party", "inside a zoo",
    "on a mountain", "inside a spaceship"
]
    return funny_subjects, funny_actions, funny_places

def createfake_news(subjects, actions, places_or_things):

    while True:
        fake_news = f"{random.choice(subjects)} {random.choice(actions)} {random.choice(places_or_things)}"

        print("\n📰 Generated Fake News")
        print("-" * 50)
        print(fake_news)
        print("-" * 50)

        save = input("\nDo you want to save this news? (y/n): ").lower()

        if save in ["y", "yes"]:
            with open("fake_news.txt", "a") as f:
                f.write(fake_news + "\n")
            print("✅ News saved successfully!")

        user_input = input("\nGenerate another news from this category? (y/n): ").lower()

        if user_input not in ["y", "yes"]:
            break

def select_field():

    while True:

        line = "=" * 50

        print("\n========== Fake News Generator ==========\n")
        print(line)
        print("1. Random News")
        print("2. Sports News")
        print("3. Politics News")
        print("4. Temple News")
        print("5. Bollywood News")
        print("6. Technology News")
        print("7. College News")
        print("8. Horror News")
        print("9. Space News")
        print("10. Food News")
        print("11. Random Funny News")
        print("12. Exit")
        print(line)

        user_choice = input("\nEnter your choice (1-12): ")

        if user_choice == "1":
            subjects, actions, places = fake_random_news()

        elif user_choice == "2":
            subjects, actions, places = fake_sports_news()

        elif user_choice == "3":
            subjects, actions, places = fake_politics_news()

        elif user_choice == "4":
            subjects, actions, places = fake_temple_news()

        elif user_choice == "5":
            subjects, actions, places = fake_bollywood_news()

        elif user_choice == "6":
            subjects, actions, places = fake_technology_news()

        elif user_choice == "7":
            subjects, actions, places = fake_college_news()

        elif user_choice == "8":
            subjects, actions, places = fake_horror_news()

        elif user_choice == "9":
            subjects, actions, places = fake_space_news()

        elif user_choice == "10":
            subjects, actions, places = fake_food_news()

        elif user_choice == "11":
            subjects, actions, places = fake_random_funny_news()

        elif user_choice == "12":
            print("\n👋 Thank you for using Fake News Generator!")
            break

        else:
            print("\n❌ Invalid choice! Please enter a number between 1 and 12.")
            continue

        createfake_news(subjects, actions, places)


select_field()



import random

# ============================================
#               WORD CLASS
# ============================================

class Word:

    def __init__(self, name, category, meaning):
        self.name = name
        self.category = category
        self.meaning = meaning

    def display(self):
        print("\n======================================")
        print("WORD :", self.name)
        print("CATEGORY :", self.category)
        print("MEANING :")
        print(self.meaning)
        print("======================================")


# ============================================
#             DICTIONARY CLASS
# ============================================

class FantasyDictionary:

    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def alphabetical(self):
        self.words.sort(key=lambda x: x.name.lower())

        current = ""

        for word in self.words:
            letter = word.name[0].upper()

            if letter != current:
                current = letter
                print("\n")
                print("=" * 40)
                print(letter)
                print("=" * 40)

            word.display()

    def search(self, name):
        for word in self.words:
            if word.name.lower() == name.lower():
                word.display()
                return word

        print("\nWord not found.")
        return None

    def random_word(self):
        return random.choice(self.words)


# ============================================
#               PLAYER CLASS
# ============================================

class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.favourites = []
        self.learned = []

    def add_score(self):
        self.score += 1

    def add_favourite(self, word):
        if word not in self.favourites:
            self.favourites.append(word)

    def learned_word(self, word):
        if word not in self.learned:
            self.learned.append(word)

    def show_profile(self):
        print("\n============== PROFILE ==============")
        print("Player :", self.name)
        print("Score :", self.score)
        print("Words Learned :", len(self.learned))
        print("Favourite Words :", len(self.favourites))
        print("=====================================")


# ============================================
#                GAME CLASS
# ============================================

class Game:

    def __init__(self):
        self.dictionary = FantasyDictionary()
        self.player = None
        self.load_words()

    def welcome(self):
        print("""
============================================================

        FANTASY DICTIONARY

Words • Magic • Kingdoms • Lore • Gods

============================================================
""")
        name = input("Enter your name : ")
        self.player = Player(name)

    def menu(self):
        while True:
            print("""

================ MENU ==================

1. Browse Dictionary
2. Search Word
3. Flash Cards
4. Guess the Word
5. Multiple Choice Quiz
6. Random Word
7. Word of the Day
8. My Profile
9. Exit

========================================

""")

            choice = input("Choice : ")

            if choice == "1":
                self.dictionary.alphabetical()

            elif choice == "2":
                word = input("Enter word : ")
                self.dictionary.search(word)

            elif choice == "3":
                self.flashcards()

            elif choice == "4":
                self.guess_word()

            elif choice == "5":
                self.mcq()

            elif choice == "6":
                self.random_word()

            elif choice == "7":
                self.word_of_the_day()

            elif choice == "8":
                self.player.show_profile()

            elif choice == "9":
                print("\nGoodbye!")
                break

            else:
                print("Invalid choice.")

    def flashcards(self):
        print("\n========== FLASHCARDS ==========\n")

        cards = self.dictionary.words[:]
        random.shuffle(cards)

        for word in cards:
            print("\n--------------------------------")
            print("WORD :")
            print(word.name)

            input("\nPress ENTER to reveal the meaning...")

            print("\nCATEGORY :", word.category)
            print("MEANING :")
            print(word.meaning)

            choice = input("\nDid you memorize it? (y/n): ")

            if choice.lower() == "y":
                self.player.learned_word(word.name)
                print("Great! Added to learned words.")
            else:
                print("Keep practicing!")

            again = input("\nNext flashcard? (y/n): ")

            if again.lower() != "y":
                break

    def guess_word(self):
        print("\n========== GUESS THE WORD ==========\n")

        questions = self.dictionary.words[:]
        random.shuffle(questions)

        score = 0

        for word in questions[:10]:
            print("\nMeaning:")
            print(word.meaning)

            answer = input("\nYour Answer : ")

            if answer.lower() == word.name.lower():
                print("\nCorrect!")
                score += 1
                self.player.add_score()
                self.player.learned_word(word.name)
            else:
                print("\nWrong!")
                print("Correct Answer :", word.name)

        print("\n======================")
        print("Final Score :", score, "/10")
        print("======================")

    def mcq(self):
        print("\n========== MULTIPLE CHOICE QUIZ ==========\n")

        score = 0
        words = self.dictionary.words[:]
        random.shuffle(words)

        for question in words[:10]:
            correct = question.name
            options = [correct]

            while len(options) < 4:
                option = random.choice(words).name
                if option not in options:
                    options.append(option)

            random.shuffle(options)

            print("\nMeaning:")
            print(question.meaning)
            print()

            for i in range(4):
                print(str(i + 1) + ".", options[i])

            choice = input("\nEnter option (1-4): ")

            try:
                selected = options[int(choice) - 1]
            except (ValueError, IndexError):
                selected = None

            if selected == correct:
                print("\nCorrect!")
                score += 1
                self.player.add_score()
            else:
                print("\nWrong!")
                print("Correct Answer :", correct)

        print("\n======================")
        print("Score :", score, "/10")
        print("======================")

    def random_word(self):
        print("\n========== RANDOM WORD ==========\n")

        word = self.dictionary.random_word()
        word.display()

        choice = input("\nSave as Favourite? (y/n): ")

        if choice.lower() == "y":
            self.player.add_favourite(word.name)
            print("\nAdded to favourites!")

    def word_of_the_day(self):
        print("\n========== WORD OF THE DAY ==========\n")

        word = random.choice(self.dictionary.words)
        word.display()

    # ============================================
    #           LOAD DICTIONARY WORDS
    # ============================================

    def load_words(self):
        entries = [
            ("Abeyance", "Lunar Phase",
             "The waning or new moon of Lumithia, when alchemical resonance reaches its weakest point."),
            ("Alchemy", "Magical Discipline",
             "The manipulation of matter and energy through resonance, practiced by gifted individuals."),
            ("Alchemical Resonance", "Magic",
             "The inner current of power flowing through all living things."),
            ("Alchemisation", "Process",
             "The process of transforming one material into another."),
            ("Alloy", "Material",
             "A fusion of two or more metals designed to alter resonance."),
            ("Animancy", "School of Magic",
             "Manipulation of thought, memory, and consciousness."),
            ("Arin", "Character",
             "The heir to the Kingdom of Nizahl, Jasad's greatest enemy."),
            ("Array", "Alchemical Symbol",
             "A symbolic diagram used to channel resonance."),
            ("Ascendence", "Lunar Phase",
             "The waxing or full moon when resonance reaches its peak."),
            ("Awaleen", "Race",
             "Magical beings that inhabit the world."),
            ("Ferrons", "Guild Family",
             "An influential family renowned for steelwork and engineering."),
            ("Hanim", "Title",
             "A respectful title for a noblewoman."),
            ("Holdfasts", "Royal Bloodline",
             "Paladia's divine ruling bloodline."),
            ("Jasad", "Kingdom",
             "A fallen kingdom destroyed because its people possessed magic."),
            ("Lich", "Undead",
             "An Undying who preserves consciousness within a corpse."),
            ("Luminescence", "Life Energy",
             "Condensed life force used by vivimancers and necromancers."),
            ("Lumithia", "Moon / Goddess",
             "The larger moon associated with war and alchemy."),
            ("Lumithium", "Metal",
             "An indestructible resonance-rich metal."),
            ("Luna", "Moon / Goddess",
             "The smaller moon representing balance and renewal."),
            ("Mo'lian'shi", "Rare Metal",
             "A rare eastern metal that suppresses resonance."),
            ("Necromancy", "Forbidden Magic",
             "The manipulation of death and decay."),
            ("Necrothralls", "Undead",
             "Reanimated corpses controlled through necromancy."),
            ("Nizahl", "Kingdom",
             "The powerful kingdom that conquered Jasad."),
            ("Nullium", "Alloy",
             "A metal that blocks resonance and regeneration."),
            ("Order of the Eternal Flame", "Organization",
             "A religious and military order devoted to destroying necromancy."),
            ("Paladin", "Sacred Warrior",
             "A sworn protector of the Principate."),
            ("Principate", "Title",
             "The divinely appointed ruler of Paladia."),
            ("Qayida", "Title",
             "A military leader who commands armies with magic."),
            ("Quintessence", "Pantheon",
             "The five divine forces governing creation."),
            ("Reanimation", "Necromantic Ritual",
             "Reviving and binding a corpse using forbidden alchemy."),
            ("Repertoire", "Trait",
             "The unique range of materials an alchemist can manipulate."),
            ("Resonance", "Primordial Energy",
             "The living force connecting all matter and fueling alchemy."),
            ("Resistance", "Faction",
             "A rebel group fighting the Undying."),
            ("Sacred Faith", "Religion",
             "Paladia's dominant religion centered on Sol."),
            ("Sol", "Deity",
             "The sun god representing life, light, and divine resonance."),
            ("Sylvia", "Character",
             "The secret queen and last heir to Jasad."),
            ("Essiya", "Character",
             "Another name for Sylvia."),
            ("The Entombment", "Historical Event",
             "Three powerful figures sacrificed their powers to imprison a magic-mad ruler."),
            ("The Great Disaster", "Historical Event",
             "A cataclysm that awakened resonance and created the second moon."),
            ("Transference", "Forbidden Technique",
             "The movement of a soul from one vessel into another."),
            ("Transmutation", "Technique",
             "The permanent transformation of matter or living beings."),
            ("Undying", "Faction",
             "Immortal beings created through necromantic alchemy."),
            ("Vitality", "Life Energy",
             "The essence of life used for healing and regeneration."),
            ("Vivimancy", "School of Magic",
             "The magic of life and healing."),
            ("Waleema", "Tradition",
             "A traditional feast or celebration, often held for weddings."),
        ]

        for name, category, meaning in entries:
            self.dictionary.add_word(Word(name, category, meaning))


# ============================================
#                   RUN GAME
# ============================================

if __name__ == "__main__":
    game = Game()
    game.welcome()
    game.menu()
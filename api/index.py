

from flask import Flask, render_template, request, jsonify
import random
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "..", "frontend", "templates"),
    static_folder=os.path.join(BASE_DIR, "..", "frontend", "static")
)
# ============================================
#               WORD CLASS
# ============================================

class Word:
    def __init__(self, name, category, meaning):
        self.name = name
        self.category = category
        self.meaning = meaning

    def to_dict(self):
        return {
            "name": self.name,
            "category": self.category,
            "meaning": self.meaning
        }

# ============================================
#          FANTASY DICTIONARY CLASS
# ============================================

class FantasyDictionary:
    def __init__(self):
        self.words = []
        self.load_words()

    def add_word(self, name, category, meaning):
        self.words.append(Word(name, category, meaning))

    def search(self, keyword):
        for word in self.words:
            if word.name.lower() == keyword.lower():
                return word
        return None

    def alphabetical(self):
        return sorted(self.words, key=lambda x: x.name.lower())

    def random_word(self):
        return random.choice(self.words)

    def word_of_day(self):
        random.seed(7)
        return random.choice(self.words)

    def load_words(self):

        entries = [

            ("Abeyance","Lunar Phase",
             "The waning or new moon of Lumithia, when alchemical resonance reaches its weakest point."),

            ("Alchemy","Magical Discipline",
             "The manipulation of matter and energy through resonance."),

            ("Alchemical Resonance","Magic",
             "The inner current of power flowing through all living things."),

            ("Alchemisation","Process",
             "The process of transforming one material into another."),

            ("Alloy","Material",
             "A fusion of two or more metals designed to alter resonance."),

            ("Animancy","School of Magic",
             "Manipulation of thought, memory and consciousness."),

            ("Arin","Character",
             "The heir to the Kingdom of Nizahl."),

            ("Array","Alchemical Symbol",
             "A symbolic diagram used to channel resonance."),

            ("Ascendence","Lunar Phase",
             "The waxing or full moon when resonance reaches its peak."),

            ("Awaleen","Race",
             "Magical beings that inhabit the world."),

            ("Ferrons","Guild Family",
             "An influential family renowned for steelwork."),

            ("Hanim","Title",
             "A respectful title for a noblewoman."),

            ("Holdfasts","Royal Bloodline",
             "Paladia's divine ruling bloodline."),

            ("Jasad","Kingdom",
             "A fallen kingdom destroyed because its people possessed magic."),

            ("Lich","Undead",
             "An Undying who preserves consciousness within a corpse."),

            ("Luminescence","Life Energy",
             "Condensed life force used by vivimancers."),

            ("Lumithia","Moon / Goddess",
             "The larger moon associated with war and alchemy."),

            ("Lumithium","Metal",
             "An indestructible resonance-rich metal."),

            ("Luna","Moon / Goddess",
             "The smaller moon representing balance and renewal."),

            ("Mo'lian'shi","Rare Metal",
             "A rare eastern metal that suppresses resonance."),

            ("Necromancy","Forbidden Magic",
             "The manipulation of death and decay."),

            ("Necrothralls","Undead",
             "Reanimated corpses controlled through necromancy."),

            ("Nizahl","Kingdom",
             "The powerful kingdom that conquered Jasad."),

            ("Nullium","Alloy",
             "A metal that blocks resonance and regeneration."),

            ("Order of the Eternal Flame","Organization",
             "A religious and military order devoted to destroying necromancy."),

            ("Paladin","Sacred Warrior",
             "A sworn protector of the Principate."),

            ("Principate","Title",
             "The divinely appointed ruler of Paladia."),

            ("Qayida","Title",
             "A military leader who commands armies with magic."),

            ("Quintessence","Pantheon",
             "The five divine forces governing creation."),

            ("Reanimation","Necromantic Ritual",
             "Reviving and binding a corpse using forbidden alchemy."),

            ("Repertoire","Trait",
             "The unique range of materials an alchemist can manipulate."),

            ("Resonance","Primordial Energy",
             "The living force connecting all matter."),

            ("Resistance","Faction",
             "A rebel group fighting the Undying."),

            ("Sacred Faith","Religion",
             "Paladia's dominant religion centered on Sol."),

            ("Sol","Deity",
             "The sun god representing life and light."),

            ("Sylvia","Character",
             "The secret queen and last heir to Jasad."),

            ("Essiya","Character",
             "Another name for Sylvia."),

            ("The Entombment","Historical Event",
             "Three powerful figures sacrificed their powers to imprison a magic-mad ruler."),

            ("The Great Disaster","Historical Event",
             "A cataclysm that awakened resonance."),

            ("Transference","Forbidden Technique",
             "The movement of a soul from one vessel into another."),

            ("Transmutation","Technique",
             "Permanent transformation of matter or living beings."),

            ("Undying","Faction",
             "Immortal beings created through necromantic alchemy."),

            ("Vitality","Life Energy",
             "The essence of life used for healing."),

            ("Vivimancy","School of Magic",
             "The magic of life and healing."),

            ("Waleema","Tradition",
             "A traditional feast or celebration.")
        ]

        for item in entries:
            self.add_word(*item)

dictionary = FantasyDictionary()

# ============================================
#                ROUTES
# ============================================
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/wordofday")
def word_of_day():
    word = dictionary.word_of_day()
    return jsonify(word.to_dict())

@app.route("/random")
def random_word():
    word = dictionary.random_word()
    return jsonify(word.to_dict())

@app.route("/browse")
def browse():
    words = dictionary.alphabetical()
    return jsonify([w.to_dict() for w in words])

@app.route("/search")
def search():
    keyword = request.args.get("word", "")
    result = dictionary.search(keyword)
    if result:
        return jsonify(result.to_dict())
    return jsonify({"error": "Word not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)

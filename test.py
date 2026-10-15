##rules = [
    ##{"name": "No pets clause", "citation": "RTA s. 14"},
    ##{"name": "Damage deposit", "citation": "RTA s. 105-106"},
##]

##for rule in rules:
    ##print(f"{rule['name']} - {rule['citation']}")


def clean_text(text):
    text_list = text.lower().split()
    cleaned_words = []
    for word in text_list:
        cleaned_words.append(word.strip(".,;:!?"))
    cleaned_text = " ".join(cleaned_words)
    cleaned_text= " " + cleaned_text + " "
    return cleaned_text

print(clean_text("No PETS allowed.   Pay a Damage  Deposit!"))


def contains_phrase(cleaned_text, phrase):
    phrase = " " + phrase + " "
    if phrase in cleaned_text:
        return True
    return False

rules = [
    {
     "name": "No Pets Clause",
     "phrases": ["pet", "pets"],
     "message": "Your lease mentions pets. In Ontario, 'no pets' clauses are generally void.",
     "citation": "RTA s. 14"
    },

    {
     "name": "Damage or Security Deposit",
     "phrases": ["damage deposit", "security deposit", "damage deposits", "security deposits"],
     "message": "Your lease asks for a damage or security deposit. In Ontario, landlords can generally only collect a last month’s rent deposit and a refundable key deposit. A damage or security deposit is likely not allowed (Residential Tenancies Act, s. 105–106).",
     "citation": "RTA s. 105-106"
     }
]

text = clean_text("Pets are not allowed. Tenant must be competent.")
print(contains_phrase(text, "pets"))            # True  (first word!)
print(contains_phrase(text, "pet"))             # False (only in "competent")
print(contains_phrase(text, "competent"))       # True  (last word!)
print(contains_phrase(text, "damage deposit"))  # False
print(contains_phrase(clean_text("Pay a damage deposit."), "damage deposit"))  # should be True
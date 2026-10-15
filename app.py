import streamlit as st


def clean_text(text):
    text_list = text.lower().split()
    cleaned_words = []
    for word in text_list:
        cleaned_words.append(word.strip(".,;:!?"))
    cleaned_text = " ".join(cleaned_words)
    cleaned_text= " " + cleaned_text + " "
    return cleaned_text



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
     "message": "Your lease asks for a damage or security deposit. In Ontario, landlords can generally only collect a last month’s rent deposit and a refundable key deposit. A damage or security deposit is likely not allowed.",
     "citation": "RTA s. 105-106"
     }
]



st.title("LeaseCheck")  

lease = st.text_area("Paste your lease agreement here: ")    



if st.button("Check my lease"):

    found = False
    text = clean_text(lease)

    for rule in rules:
        for phrase in rule['phrases']:
            
            if contains_phrase(text,phrase):
                st.warning(f"{rule['message']} - {rule['citation']}")
                found = True
                break

    if not found:
        st.success("No issues found")




    

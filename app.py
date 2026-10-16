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
     },

    {
     "name": "Post Dated Cheques / Automatic Payments",
     "phrases": ["post-dated cheques", "post-dated cheque", "postdated cheques", "postdated cheque", "post dated cheques", "post dated cheque", "post-dated checks", "post-dated check", "postdated checks", "postdated check", "post dated checks", "post dated check", "pre-authorized debit", "pre-authorized debits", "preauthorized debit", "preauthorized debits", "pre authorized debit", "pre authorized debits", "automatic withdrawal", "automatic withdrawals", "automatic payment", "automatic payments"],
     "message": "Your lease mentions post-dated cheques or automatic payments. In Ontario, a landlord generally can’t require a specific payment method, though you can choose to agree to one.",
     "citation": "RTA s. 108"
     },

     {
     "name": "Landlord Entry Without Notice",
     "phrases": ["enter at any time", "enter without notice", "enter the unit without notice", "enter the unit at any time", "enter the premises without notice", "enter the premises at any time", "enter the rental unit without notice", "enter the rental unit at any time", "access the unit at any time", "access the premises at any time", "entry without notice", "entry at any time"],
     "message": "Your lease may allow the landlord to enter without proper notice. In Ontario, landlords generally must give 24 hours’ written notice and the notice must state the date, time and the reason for entering.",
     "citation": "RTA ss. 26–27"      
     },

     {
     "name": "You must move out when the lease ends", #ai canidate
     "phrases": ["must vacate at the end of the term", "must vacate at the end of the lease", "vacate the premises at the end of the term", "vacate the premises at the end of the lease", "vacate the unit at the end of the term", "vacate the unit at the end of the lease", "must move out at the end of the term", "must move out at the end of the lease", "lease will not be renewed", "lease shall not be renewed", "no month-to-month", "will not continue month-to-month"],
     "message": "Your lease may mention that you must move out by the end of the fixed-term lease. In Ontario, your lease does not end when the term ends. It automatically continues on a month to month basis, without the need to move out or sign a new lease.",
     "citation": "RTA s. 38"      
     },

     {
     "name": "Late Fees", 
     "phrases": ["late fee", "late fees", "late charge", "late charges", "late penalty", "late penalties", "late payment penalty", "late payment penalties", "late payment fee", "late payment fees", "penalty for late payment", "penalty for late rent"],
     "message": "Your lease may require you to pay late fees. In Ontario, landlords generally can’t charge late fees or penalties. The one exception is a bounced cheque: the landlord can charge their bank’s fee plus up to $20.",
     "citation": "RTA s. 134"      
     },

     {
     "name": "Tenant responsible for all repairs", 
     "phrases": ["responsible for all repairs", "responsible for all maintenance", "responsible for all repairs and maintenance", "responsible for repairs and maintenance", "responsible for maintenance and repairs", "pay for all repairs", "rented as is", "in as is condition", "as is condition", "accepts the unit as is", "accepts the premises as is", "rented as-is", "in as-is condition", "as-is condition", "accepts the unit as-is", "accepts the premises as-is"],
     "message": "Your lease may mention that you must be responsible for all repairs. In Ontario, landlords are responsible for keeping the unit in good repair, and a lease can’t shift that duty to the tenant. Tenants can only be held responsible for damage they or their guests cause.",
     "citation": "RTA s. 20"      
     },


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




    

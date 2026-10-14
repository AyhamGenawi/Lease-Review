import streamlit as st



st.title("LeaseCheck")  

lease = st.text_area("Paste your lease agreement here: ")     

if st.button("Check my lease"):
    word_list = lease.lower().split() #lowercase so capitalization doesnt matter, and split removes any extra spaces

    found = False   #Rule 1: Now we start to check if lease mentions pet clause
    for word in word_list: #must check WHOLE word so cases like "competent" or "carpet" dont say theres a pet clause
        clean_word = word.strip(".,;:!?")   #makes sure "pet." does not fail
        if clean_word in  ("pet", "pets"):
            st.warning("Your lease mentions pets. In Ontario, 'no pets' clauses are generally void.")
            found = True # mark that we found the variable, so we dont display "Not found" message
            break

    if not found:
        st.success("No pet clauses found. ")


    #Rule 2: Checking if lease mentions damage or security deposit ---
    #Resetting found variable, so result from pet case does not follow over
    found = False
    for i in range (len(word_list)):
        clean_word = word_list[i].strip(".,;:!?")
        if i != len(word_list) - 1:         #in order to skip checking the next word, if we are at the end of the list to avoid a index error.
            clean_next_word = word_list[i+1].strip(".,;:!?")
            if (clean_word == "damage" or clean_word == "security") and clean_next_word == "deposit":  #looking for two word combinations either "damage deposit" or "security deposit".
                st.warning("Your lease asks for a damage or security deposit. In Ontario, landlords can generally only collect a last month’s rent deposit and a refundable key deposit. A damage or security deposit is likely not allowed (Residential Tenancies Act, s. 105–106).")
                found = True
                break

    if not found:
        st.success("No damage or security deposits found. ")



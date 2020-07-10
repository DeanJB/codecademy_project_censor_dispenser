# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
#print(proprietary_terms)

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]



#Function for obtaining variants of words in list to censor
def get_all_variants(list):
    for each in range(0, len(list)):
        list.append(list[each].title())
        list.append(list[each].upper())
        list.append(list[each] + "s")
    return list

#testing above function
#print(get_all_variants(proprietary_terms))

#-------Function for single phrase/word censoring----------

def censor(document, censor):
  censored_item = ""
  for x in range(0,len(censor)):
    if censor[x] == " ":
      censored_item = censored_item + " "
    else:
    	censored_item = censored_item + "X"
  return document.replace(censor, censored_item)

# Uncomment to test function
#print(censor_phrase("learning algorithms", email_one))

#-------Function for censoring multiple phrases/words given in a list------   

def censor_multi(document, censors):
    to_censor = get_all_variants(censors)
    for word in to_censor:
        censored_item = ""
        for x in range(0,len(word)):
            if word[x] == " ":
                censored_item = censored_item + " "
            else:
    	        censored_item = censored_item + "X"
        document = document.replace(word, censored_item)
    return document

#Test multi censor function
#print(censor_multi(email_two, proprietary_terms))

def censor_after_usage(document, list):
    to_censor = get_all_variants(list)
    for word in to_censor:
        censored_item = ""
        for x in range(0,len(word)):
            if word[x] == " ":
                censored_item = censored_item + " "
            else:
    	        censored_item = censored_item + "X"
        
        document = document.replace(word, censored_item)
    return document
    
    
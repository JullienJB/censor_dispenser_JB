# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
punctuation = [",", ".", "?", "!", "%", "/", "(", ")","\n"] #line break included as punctuation
code_1 = "XXXXXX" #string that will be the replacement for the hidden words 

import re #regular expression module 

def censor_funct_1(email, phrase, code):
  x_email = email.replace(phrase,code)
  return x_email

phrase_1 = "learning algorithms"

task_1 = (censor_funct_1(email_one, phrase_1, code_1))
#print(task_1)


def censor_funct_2(email, terms_list, code):
  for term in terms_list:
      term_search = r"\b{}\b".format(term) #"\b{}\b" helps identify the exact str as an individual word, rather than inside another word
      email = re.sub(term_search, code, email, flags=re.IGNORECASE) #introducing flags to be able to handle distinct letter cases
  return email  
      

task_2 = censor_funct_2(email_two, proprietary_terms, code_1)
#print(task_2)

def censor_funct_3(email, terms_list, neg_list, code):
    for term in terms_list:
        term_search = r"\b{}\b".format(term)
        email = re.sub(term_search, code, email, flags=re.IGNORECASE)
    for neg in neg_list:
        neg_search = r"\b{}\b".format(neg)
        neg_count = re.findall(neg_search, email, flags=re.IGNORECASE) #creates a list of all the findings of the indicated substring on string
        if len(neg_count) >= 2: #checks is the negative terms appears at least twice, which was the condition given
            email = re.sub(neg_search, code, email, flags=re.IGNORECASE)
    return email

task_3 = censor_funct_3(email_three, proprietary_terms, negative_words, code_1)
#print(task_3)


def censor_funct_4(email, terms_list, neg_list, code):
    forbidden_words = terms_list + neg_list #creates a list that contains all terms to censor
    for word in forbidden_words:
        word_search = r"\b{}\b".format(word)
        email = re.sub(word_search, code, email, flags=re.IGNORECASE)
    
    email = email.replace("\n\n", " \n\n") #operation included to separate correctly words in space separations (line breaks create confusion on program) and to be able to keep line spacing for joining at the end
    email_word_list = email.split(" ") #creates a new list based on the censored email string (limited only to the censor terms) 
    censor_indexes = []
    
    for i in range(len(email_word_list)): #this loop generates a list with the index position of censor words
        if code in email_word_list[i]:
            censor_indexes.append(i) #defines the position in list of censored words
            
    adjacent_censor_indexes = list(set([(i-1) for i in censor_indexes if i-1 not in censor_indexes] + [(i+1) for i in censor_indexes if (i+1) not in censor_indexes]))
    #The above line creates the list of the extra elements to censor. The set() method is used to eliminate duplicates, then applied list() to return the object type as a list.
    
    for index in adjacent_censor_indexes: #for loop to iterate each of the adjacent indexes of the censor words
        for symbol in punctuation: #for loop to make sure we take into account all punctuation defined objets
            censored_part = email_word_list[index].strip(symbol) #creates a temporary variable, which is used to describe the part of the string to change without including punctuation (to avoid replacement of punctuation for the code). Does not modify the original list.
        email_word_list[index] = email_word_list[index].replace(censored_part, code)
    
    email = " ".join(email_word_list) #All set, Lets join everything as it should be!      
    return email


task_4 = censor_funct_4(email_four, proprietary_terms, negative_words, code_1)
#print(task_4)

    
          
          




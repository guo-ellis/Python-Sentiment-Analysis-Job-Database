# Ellis Guo
import pickle

def read_text(text_path):

    '''

    Opens and reads the text file, catches FileNotFoundError

    Parameters: 
        text_path (string): contains file name
    
    Returns:
        text_list (list): list of strings

    
    >>>Contents of my file, (text.txt):
        user1,Hello
        user2,How are you today?
        user3,Good I hope!
        user4,Ok take care!
    >>>read_text(text.txt)
        ['Hello \n', 'How are you today? \n', 'Good I hope! 
        \n','Ok take care! \n']
    

    '''
    
    try:
        posts = open(text_path, 'r')
        text_list = []
        for line in posts:
            text_list.append(line.split(",")[1])
        return(text_list)
        posts.close()
    except FileNotFoundError:
        print("File does not exist")

def read_pickle(path_to_pkl):

    """

    Returns the dictionary in the pickle file

    Parameters:
        path_to_pkl (string): string containing path to pickle file
    
    Returns: 
        word_dict (dictionary)

    >>>Contents of my pkl file("sentiment_dictionary.pkl")
        {"POSITIVE": ["great", "love", "recommend", "laugh", "happy",
        "brilliant"], "NEGATIVE": ["terrible", "awful", "hideous", "sad",
        "cry", "bad"], "NEUTRAL": ["meh", "indifferent", "ignore"]}
    >>>read_pickle("sentiment_dictionary.pkl")
        {"POSITIVE": ["great", "love", "recommend", "laugh", "happy",
        "brilliant"], "NEGATIVE": ["terrible", "awful", "hideous", "sad",
        "cry", "bad"], "NEUTRAL": ["meh", "indifferent", "ignore"]}
    
    """

    pick = open(path_to_pkl, "rb")
    word_dict = pickle.load(pick)
    pick.close
    return word_dict

def sentiment_frequencies(text, dictionary_word):

    """

    Returns the count of the occurrence of each sentiment category
    in the input text, and will output the sentiment occurrence counts 
    as frequency

    Parameters:
    text (string)

    Returns:
    dictionary_word (dictionary)

    >>>sentiment_frequencies("Hello", {"POSITIVE": "Hello", 
    "NEGATIVE": "Hi"})
    {'POSITIVE': 1.0, 'NEGATIVE': 0.0}
    
    >>>sentiment_frequencies("Hello Hi Hello", {"POSITIVE": 
    "Hello", "NEGATIVE": "Hi"})
    {'POSITIVE': 0.67, 'NEGATIVE': 0.33}
    
    >>>sentiment_frequencies("Hi Heyah", {"POSITIVE": "Hello", 
    "NEGATIVE": ["Hi", "Heyah"]})
    {'POSITIVE': 0.0, 'NEGATIVE': 1.0}

    """
    
    new_list = text.split()
    freq = {}
    dict_frequency = {}

    freq = dict(dictionary_word.fromkeys(dictionary_word, 0))

    for word in new_list:
        for key, values in dictionary_word.items():
            if word in values:
                freq[key] += 1

    for key, value in freq.items():
        dict_frequency[key] = value
        dict_frequency[key] = round(dict_frequency.get(key)/len(new_list), 2)

    return dict_frequency


def compute_polarity(dict_frequency):

    """
    Returns the dictionary key with the highest frequency

    Parameters:
        dict_frequency (dictionary)
    
    Returns:
        polarity (string): the key

    >>>compute_polarity({"POSITIVE":1, "NEGATIVE": 2, "NEUTRAL":3})
    NEUTRAL
    >>>compute_polarity({"POSITIVE":4, "NEGATIVE": 2, "NEUTRAL":3})
    POSITIVE
    >>>compute_polarity({"POSITIVE":-1, "NEGATIVE": 2, "NEUTRAL":1})
    NEGATIVE

    """

    max_value = None
    for key in dict_frequency:
        if (max_value is None) or (max_value < dict_frequency[key]):
            max_value = dict_frequency[key]
            polarity = key
    return polarity

def analyse_text(text_path, dict_path):

    """
    Returns the sentiment frequencies and polarity of each line in 
    text_path, and add the computed polarity value to list polarity.

    Parameters:
        text_path (string): path to text file
        dict_path (string): path to sentiment dictionary saved in pkl

    Returns:
        list_polarity (list)

    Contents of my file, (file.txt):

        user1,hello
        user2,goodbye
        user3,welcome

    Contents of my pkl file (pickle.pkl):

        {POSITIVE: ['hello'], NEGATIVE: ['goodbye'], NEUTRAL: ['welcome']}
    
    >>>analyse_text(file.txt, pickle.pkl):
    ['POSITIVE', 'NEGATIVE', 'NEUTRAL']


    Contents of my file, (file.txt):

        user1,hello
        user2,goodbye
        user3,bonjour

    Contents of my pkl file (pickle.pkl):

        {POSITIVE: ['hello', 'bonjour'], NEGATIVE: ['goodbye'], NEUTRAL: ['welcome']}
    
    >>>analyse_text(file.txt, pickle.pkl):
    ['POSITIVE', 'NEGATIVE', 'POSITIVE']


    Contents of my file, (file.txt):

        user1,hello bonjour bonjour
        user2,goodbye welcome hello
        user3,welcome

    Contents of my pkl file (pickle.pkl):

        {POSITIVE: ['hello', 'welcome], NEGATIVE: ['goodbye'], NEUTRAL: ['bonjour']}
    
    >>>analyse_text(file.txt, pickle.pkl):
    ['NEUTRAL', 'POSITIVE', 'POSITIVE']

    """

    text_file = read_text(text_path)
    dict_file = read_pickle(dict_path)
    stop_words = ["!",".","?",";","\n"]

    list_polarity = []
    new_list = []

    for line in text_file:
        line = line.strip()
        line = line.lower()
        temp_line = line
        for i in line:
            for x in stop_words:
                if i == x:
                    temp_line = temp_line.replace(i, "")
        list_polarity.append(compute_polarity(sentiment_frequencies(temp_line, dict_file)))
    return list_polarity


class Company:

    """
    This class represents a Company object

    Instance attributes:
        name (string)
        location (string)
    """

    def __init__(self, name, location):
        self.name = name
        self.location = location

    def update_location(self, update_location):
        self.location = update_location

class JobOffer:

    """
    This class represents a JobOffer object

    Instance attributes:
        title (string)
        description (string)
        company (class)
        contract (string)
        salary (int)
    """

    def __init__(self, title, company, contract, salary, description):
        self.title = title
        self.company = company
        self.contract = contract
        self.salary = salary
        self.description = description
    
    def update_description(self, update_description):
        self.description = update_description
    
    def __str__(self):
        return ("Title: " + self.title + "\nCompany: " + str(self.company.name) + "\nLocation: " + str(self.company.location) + "\nContract: " + str(self.contract) + "\nDescription: " + str(self.description) + "\nSalary: " + str(self.salary))

def build_job_database():
    
    print("Welcome to New Job Entry! Let's create our first entry."
          "\nPLEASE ENTER REQUESTED DATA FOR OFFER 1")
    title1 = input("Title: ")
    company_name1 = input("Company: ")
    loc1 = input("Location: ")
    contract1 = input("Contract: ")
    desc1 = input("Description: ")
    salary1 = input("Salary: ")

    company_1 = Company(company_name1, loc1)
    job_offer_1 = JobOffer(title1, company_1, contract1, int(salary1), desc1)

    print("PLEASE ENTER REQUESTED DATA FOR OFFER 2")
    title2 = input("Title: ")
    company_name2 = input("Company: ")
    loc2 = input("Location: ")
    contract2 = input("Contract: ")
    desc2 = input("Description: ")
    salary2 = input("Salary: ")

    company_2 = Company(company_name2, loc2)
    job_offer_2 = JobOffer(title2, company_2, contract2, int(salary2), desc2)

    print("Employer modified OFFER 1 description!"
          "\nPLEASE ENTER THE UPDATED OFFER 1 DESCRIPTION")

    desc1 = input("Description: ")
    job_offer_1 = JobOffer(title1, company_1, contract1, int(salary1), desc1)

    print("Find updated OFFER 1 below:")
    print(job_offer_1)



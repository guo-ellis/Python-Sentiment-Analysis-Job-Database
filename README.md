# Python-Sentiment-Analysis-Job-Database

The purpose of the provided code is to implement a sentiment analysis system (Part A) and a job database (Part B) using object-oriented programming principles.

Part A: Sentiment Analysis

This section aims to analyze the sentiment of given text data using a rule-based approach.
It consists of several functions:

read_text(text_path): Reads a text file containing user comments, extracts the comments, and returns them as a list of strings.
read_pickle(path_to_pkl): Reads a pickle file containing a sentiment dictionary and returns the dictionary.
sentiment_frequencies(text, dictionary_word): Computes the frequency of each sentiment category (positive, negative, neutral) appearing in the text.
compute_polarity(dict_frequency): Determines the most prominent sentiment observed based on the frequency dictionary.
analyze_text(text_path, dict_path): Integrates the previous functions to analyze the sentiment of each line in a text file and returns a list of computed polarities.

Part B: Job Database

This section involves creating a job database for a talent recruitment company using classes and objects.

It defines two classes:
Company: Represents a company offering job opportunities. It has attributes for the company name and location, along with methods for initializing and updating the location.
JobOffer: Represents a job offer, including attributes for the title, description, company, contract type, and salary. It also includes methods for initializing, updating the description, and generating a string representation of the job offer.

Additionally, there is a function build_job_database() that creates instances of JobOffer, updates one of the descriptions, and prints out the details of the offers.

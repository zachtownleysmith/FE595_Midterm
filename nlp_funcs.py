import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import ngrams

nltk.download('stopwords')
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


# Define Function for Parts of Speech Tagging
def pos_tagging(input_string, input_tags):
    words = word_tokenize(input_string)
    tagged = nltk.pos_tag(words)

    if input_tags.lower() == "all":
        output = tagged
    elif input_tags.lower() == "verb":
        output = [(word, tag) for word, tag in tagged if tag in ("VB", "VBG", "VBD", "VBN", "VBP", "VBZ")]
    elif input_tags.lower() == "noun":
        output = [(word, tag) for word, tag in tagged if tag in ("NN", "NNS", "NNP", "NNPS")]
    else:
        output = ["", ""]
    return output


# Define a function for counting word frequency
def word_freq(input_string):
    words = word_tokenize(input_string)
    freq_table = dict()
    stop_words = set(stopwords.words("english"))

    for entry in words:
        word = entry.lower()
        if word in stop_words:
            continue
        if word in freq_table:
            freq_table[word] += 1
        else:
            freq_table[word] = 1
    return freq_table


# Define a function for returning the polarity of input text
def text_sentiment(input_string):
    # Create instance of pre-trained model
    sia = SentimentIntensityAnalyzer()

    output = sia.polarity_scores(input_string)
    return output


# Define a function for returning the n-grams of input text
def get_ngrams(input_string, gram_count):
    words = word_tokenize(input_string)
    grams = list(ngrams(words, gram_count))
    return grams


if __name__ == "__main__":
    test = "Zach really really would like this to work"

    print("Nouns")
    test_output = pos_tagging(input_string=test, input_tags="Noun")
    print(test_output)
    print("")

    print("Verbs")
    test_output = pos_tagging(input_string=test, input_tags="Verb")
    print(test_output)
    print("")

    print("All POS Tags")
    test_output = pos_tagging(input_string=test, input_tags="all")
    print(test_output)
    print("")

    print("Word Frequencies")
    test_output = word_freq(input_string=test)
    print(test_output)
    print("")

    print("Sentiment")
    test_output = text_sentiment(input_string=test)
    print(test_output)
    print("")

    print("N-Grams")
    test_output = get_ngrams(input_string=test, gram_count=2)
    print(test_output)

    print(int("")+2)


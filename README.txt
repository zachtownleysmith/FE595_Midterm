This API performs natural language processing on POST requests.
Supported services:

Parts of Speech Tagging

Word Frequency Counting

Sentiment Analysis

Return N-Grams



Required JSON POST format:
{
text: "string to perform nlp on"


service: "POS, WRDFREQ, SENTIMENT, NGRAMS, or ALL"


pos_tags: "noun, verb, or all"


gram_num: "an integer for n_grams"


}

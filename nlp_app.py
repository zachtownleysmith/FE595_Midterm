from nlp_funcs import pos_tagging, word_freq, text_sentiment
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/nlp', methods=['POST', 'GET'])
def serve_nlp():
    if request.method == 'POST':

        # For POST Requests, first check that the payload is JSON
        if request.is_json:
            user_input = request.get_json()
            text = user_input['text']
            service = user_input['service']
            pos_tags = user_input['pos_tags']

            if service == 'POS':
                nlp_out = pos_tagging(input_string=text, input_tags=pos_tags)
                dict_out = {"Parts_Of_Speech": nlp_out}

            elif service == 'WRDFREQ':
                nlp_out = word_freq(input_string=text)
                dict_out = {"Word_Frequency": nlp_out}

            elif service == 'SENTIMENT':
                nlp_out = text_sentiment(input_string=text)
                dict_out = {"Sentiment": nlp_out}

            elif service == 'ALL':
                nlp_1 = pos_tagging(input_string=text, input_tags=pos_tags)
                nlp_2 = word_freq(input_string=text)
                nlp_3 = text_sentiment(input_string=text)
                dict_out = {
                    "Parts_Of_Speech": nlp_1,
                    "Word_Frequency": nlp_2,
                    "Sentiment": nlp_3
                }

            else:
                dict_out = {"MSG": "Requested Service not Supported"}

            json_out = jsonify(dict_out)
            return json_out, 200

        else:
            return "Post request must be JSON", 400

    elif request.method == 'GET':
        instructions = "This API performs natural language processing on POST requests. /n" \
                       "Supported services: /n" \
                       "   Parts of Speech Tagging /n" \
                       "   Word Frequency Counting /n" \
                       "   Sentiment Analysis /n" \
                       "/n" \
                       "Required JSON POST format: /n" \
                       "text: (string to perform nlp on) /n" \
                       "service: (POS, WRDFREQ, SENTIMENT, or ALL) /n" \
                       "pos_tags: (noun, verbs, or all)"
        return instructions, 200
    else:
        return "Request must be GET or POST", 400


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
    #app.run(host='127.0.0.1', port=5000)
    #Delete
'''

test_input = {
    "service": "SENTIMENT",
    "text": "This will work really really well",
    "pos_tags": "all"
}

text = test_input['text']
service = test_input['service']
pos_tags = test_input['pos_tags']

if service == 'POS':
    nlp_out = pos_tagging(input_string=text, input_tags=pos_tags)
    testing = {"Parts_Of_Speech": nlp_out}
elif service == 'WRDFREQ':
    nlp_out = word_freq(input_string=text)
    testing = {"Word_Frequency": nlp_out}
elif service == 'SENTIMENT':
    nlp_out = text_sentiment(input_string=text)
    testing = {"Sentiment": nlp_out}

print(nlp_out)
print(testing)
'''

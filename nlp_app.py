from nlp_funcs import pos_tagging, word_freq, text_sentiment, get_ngrams
from flask import Flask, request, jsonify, render_template

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
            gram_num = user_input['gram_num']

            if service == 'POS':
                nlp_out = pos_tagging(input_string=text, input_tags=pos_tags)
                dict_out = {"Parts_Of_Speech": nlp_out}

            elif service == 'WRDFREQ':
                nlp_out = word_freq(input_string=text)
                dict_out = {"Word_Frequency": nlp_out}

            elif service == 'SENTIMENT':
                nlp_out = text_sentiment(input_string=text)
                dict_out = {"Sentiment": nlp_out}

            elif service == 'NGRAMS':
                try:
                    gram_num = int(gram_num)
                    nlp_out = get_ngrams(input_string=text, gram_count=gram_num)
                    dict_out = {"N_Grams": nlp_out}
                except ValueError:
                    dict_out = {"MSG": "gram_num must be an integer"}

            elif service == 'ALL':
                nlp_1 = pos_tagging(input_string=text, input_tags=pos_tags)
                nlp_2 = word_freq(input_string=text)
                nlp_3 = text_sentiment(input_string=text)

                # Check to ensure gram_num is INT for NGRAM function
                try:
                    gram_num = int(gram_num)
                    nlp_4 = get_ngrams(input_string=text, gram_count=gram_num)
                except ValueError:
                    nlp_4 = {"MSG": "gram_num must be an integer"}

                dict_out = {
                    "Parts_Of_Speech": nlp_1,
                    "Word_Frequency": nlp_2,
                    "Sentiment": nlp_3,
                    "N_Grams": nlp_4
                }

            else:
                dict_out = {"MSG": "Requested Service not Supported"}

            json_out = jsonify(dict_out)
            return json_out, 200

        else:
            return "Post request must be JSON", 400

    elif request.method == 'GET':

        return render_template("instructions.html"), 200
    else:
        return "Request must be GET or POST", 400


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)

'''
test_input = {
    "service": "SENTIMENT",
    "text": "This will work really really well",
    "pos_tags": "all"
    "gram_num" "2"
}
'''

from nlp_funcs import pos_tagging, word_freq, text_sentiment
from flask import Flask, request

app = Flask(__name__)


@app.route('/nlp', methods=['POST', 'GET'])
def serve_nlp():
    if request.method == 'POST':
        user_input = request.get_json()
        print(user_input)

        text = user_input['text']
        service = user_input['service']
        pos_tags = user_input['pos_tags']

        if request.is_json():
            if service == 'POS':
                nlp_out = pos_tagging(input_string=text, input_tags=pos_tags)
            elif service == 'WRDFREQ':
                nlp_out = word_freq(input_string=text)
            elif service == 'SENTIMENT':
                nlp_out = text_sentiment(input_string=text)
            else:
                nlp_out = 'Requested Service not Found'
            print(nlp_out)
            return "Successful Post", 200
        else:
            return "Post request must be JSON", 400

    elif request.method == 'GET':
        return "Learn how to do a Post Request", 404
    else:
        return "Request must be GET or POST", 400


if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=8000)
    app.run(host='127.0.0.1', port=5000)

'''
test_input = {
    "service": "WRDFREQ",
    "text": "This will work really really well",
    "pos_tags": "noun"
}

text = test_input['text']
service = test_input['service']
pos_tags = test_input['pos_tags']

if service == 'POS':
    nlp_out = pos_tagging(input_string=text, input_tags=pos_tags)
elif service == 'WRDFREQ':
    nlp_out = word_freq(input_string=text)
elif service == 'SENTIMENT':
    nlp_out = text_sentiment(input_string=text)
'''

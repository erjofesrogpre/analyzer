from flask import Flask, render_template, request, jsonify, send_file
from analyzer import *
import csv

app = Flask(__name__,template_folder='templates',static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    content = request.json['content']
    word_count = word_counter(content)
    paragraph_count = paragraph_counter(content)
    sentence_count = sentence_counter(content)
    vowel_count, consonant_count = vowel_and_consonant_counter(content)
    lowercase_count, uppercase_count = lowercase_and_upercase_counter(content)
    word_frequency = word_frequence(content)
    return jsonify({
        'wordCount': word_count,
        'paragraphCount': paragraph_count,
        'sentenceCount': sentence_count,
        'vowelCount': vowel_count,
        'consonantCount': consonant_count,
        'lowercaseCount': lowercase_count,
        'uppercaseCount': uppercase_count,
        'wordFrequency': word_frequency
    })

@app.route('/download_csv', methods=['POST'])
def download_csv():
    content = request.json['content']
    data = [['Amount of words:'],
            ['Amount of paragraphs'],
            ['Amount of sentences'],
            ['Amount of vowels'],
            ['Amount of consonants'],
            ['Amount of lowercases'],
            ['Amount of uppercases']]
    word_count = word_counter(content)
    paragraph_count = paragraph_counter(content)
    sentence_count = sentence_counter(content)
    vowel_count, consonant_count = vowel_and_consonant_counter(content)
    lowercase_count, uppercase_count = lowercase_and_upercase_counter(content)
    word_frequency = word_frequence(content)
    data[0].append(word_count)
    data[1].append(paragraph_count)
    data[2].append(sentence_count)
    data[3].append(vowel_count)
    data[4].append(consonant_count)
    data[5].append(lowercase_count)
    data[6].append(uppercase_count)
    with open("Analysis",'w',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    return send_file(csvfile,as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
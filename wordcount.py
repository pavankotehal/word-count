__author__ = "Pavan Kotehal"

# PLEASE RUN USING PYTHON 3
import operator
import os, glob
from config import wordcount_limit, words_excluded
import datetime

"""
Script expects the filename.txt as input( the file should be in the same location as the script)
It parses through the text file and generates wordcount.
The result will be saved in new directory called Result
The Config.py script is configuration file where you can add minimum number of occurence to be considered
you can also exclude words by adding them in WORDS_EXCLUDED variable
"""

def clean_word_list(word_list):
	clean_word_list = []

	for word in word_list:
		symbols = "~!@#$%^&*()_{}[]:\";'\|,./<>?`-='"

		for i in range(0, len(symbols)):
			word = word.replace(symbols[i], '')

		if len(word) > 0:
			clean_word_list.append(word)

	create_frequency_dictionary(clean_word_list)


def create_frequency_dictionary(word_list):
    word_count = {}
    result_list = []

    for word in word_list:
        if (word in word_count) and (word not in words_excluded):
            word_count[word] += 1
        else:
            word_count[word] = 1

    for key,value in sorted(word_count.items(), key=operator.itemgetter(1), reverse=True):
        result_item = [key, value]
        if value >= wordcount_limit:
            result_list.append(result_item)
            print(key, value)
    
    write_output(result_list)


def write_output(list):
    timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    current_dir = os.getcwd()
    filename = "result"+timestamp+".txt"

    if not os.path.exists(os.path.join(current_dir, "result")):
        os.makedirs(os.path.join(current_dir, "result"))

    result_path = ((os.path.join(current_dir, "result")+"/"+filename))
    print("the path for the result is {0}".format(result_path))
    
    result = open(result_path, "w+")
    for li in list:
        result.write("{0} -- {1} times \n".format(li[0], li[1]))
    result.close()


def main(file_name):
	word_list = []
	fx = open(file_name, 'r')

	file_line_content = fx.readlines()

	for post_text in file_line_content:
		content = post_text
		
		words = content.lower().split()

		for each_word in words:
			word_list.append(each_word)

	clean_word_list(word_list)

if __name__ == "__main__":
    try:
        filename = input('Enter a filename: ') #or 'sample.txt'
        main(filename)
    except FileNotFoundError:
        print("Given file doesn't exists !!!, please add the file in the same folder where the wordcount script is located")
    
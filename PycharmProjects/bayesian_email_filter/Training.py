import nltk
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize

from os import listdir  # for reading all the files
from os.path import isfile, join

nltk.data.path = ['nltk_data']  # add path to NLTK file
stopwords = set(stopwords.words('english'))  # load stopwords
spam_path = 'data/spam/'
easy_ham_path = 'data/easy_ham/'


def get_words(message):
    all_words = set(
        wordpunct_tokenize(message.replace('=\\n', '').lower()))  # make set of word and remove = and new line

    msg_words = [word for word in all_words if word not in stopwords and len(word) > 2]  # remove stopword from list

    return msg_words


def get_mail_from_file(file_name):
    message = ''
#read line form mail convert in string
    with open(file_name,encoding="latin-1") as mail_file: #for using ascii compatible encoding to preserve error
        for line in mail_file:
            if line == '\n':
                for line in mail_file:
                    message += line

    return message


def make_training_set(path):
    training_set = {}
    mails_in_dir = [mail_file for mail_file in listdir(path) if isfile(join(path, mail_file))]

    for mail_name in mails_in_dir:
        message = get_mail_from_file(path + mail_name)
        terms = get_words(message)
        for term in terms:
            if term in training_set:
                training_set[term] = training_set[term] + 1
            else:
                training_set[term] = 1



    return training_set


print('')
print('Loading training sets...')
s_t_set = make_training_set(spam_path)
h_t_set = make_training_set(easy_ham_path)
n=len(s_t_set)+len(h_t_set)-len(set(h_t_set.keys()).intersection(set(s_t_set.keys())))
print('Training Complete!!!!')


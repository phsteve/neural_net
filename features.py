import string

dq_english = open('english-sentences.txt', 'r')
dq_spanish = open('spanish-sentences.txt', 'r')
english_training = dq_english.readlines(200)
spanish_training = dq_spanish.readlines(200)

#print english_training
#len_spanish = 0
#len_english = 0
#

#freq_dist_english = {}
#freq_dist_spanish = {}

def make_freq_dist(string):
    #could be a dictionary comprehension?
    length = 0
    freq_dist = {}
    for char in string:
        length += 1
        if char in freq_dist:
            freq_dist[char]+=1
        else:
            freq_dist[char]=1
    return freq_dist, length

#freq_dist_english, len_english = make_freq_dist(dq_english)
#freq_dist_spanish, len_spanish = make_freq_dist(dq_spanish)

#print len_english, freq_dist_english
#print len_spanish, freq_dist_spanish

# for letter in string.ascii_letters:
#     try:
#         print letter, 100*(float(freq_dist_spanish[letter])/len_spanish-float(freq_dist_english[letter])/len_english)
#     except KeyError:
#         print "DOESN'T EXIST"

training_data = {}
def add_training_data(data, training_data, label):
    for line in data:
        training_data[line] = label
    return training_data

add_training_data(english_training, training_data, 'English')
add_training_data(spanish_training, training_data, 'Spanish')



#print training_data

# training_data = make_training_data([english_training, spanish_training])

#English = 0
#Spanish = 1



# def percentage_spanish(freq_dist, letter):
#     #trivial?
#     return freq_dist[letter]/len_spanish

# def percentage_english(freq_dist, letter):
#     return freq_dist[letter]/len_english
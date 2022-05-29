import pickle

pickle_in = open('key_list', 'rb')
cucumber = pickle.load(pickle_in)

print(cucumber)

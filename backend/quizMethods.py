import random
import json







def makeQuiz():

    random_numbers = random.sample(range(len(dictionary)), 4)
    

    correct_user_name = dictionary[userslist[random_numbers[0]]]['display name']

    correct_user_picurl = dictionary[userslist[random_numbers[0]]]['picurl']
    size_of_tweetlist = len(dictionary[ userslist[random_numbers[0]] ]['tweets'])
    correct_user_tweet = dictionary[ userslist[random_numbers[0]] ]['tweets'][random.randrange(0,size_of_tweetlist)]
    correct_user_dict = {'display_name':correct_user_name , 'image' : correct_user_picurl}

    wrong_user_1 = dictionary[userslist[random_numbers[1]]]['display name']
    wrong_pic_1 = dictionary[userslist[random_numbers[1]]]['picurl']
    wrong_user_dict1 = {'display_name' : wrong_user_1 , 'image' : wrong_pic_1}

    wrong_user_2 = dictionary[userslist[random_numbers[2]]]['display name']
    wrong_pic_2 = dictionary[userslist[random_numbers[2]]]['picurl']
    wrong_user_dict2 = {'display_name' : wrong_user_2 , 'image' : wrong_pic_2}


    wrong_user_3 = dictionary[userslist[random_numbers[3]]]['display name']
    wrong_pic_3 = dictionary[userslist[random_numbers[3]]]['picurl']
    wrong_user_dict3 = {'display_name' : wrong_user_3 , 'image' : wrong_pic_3}

    #order_numbers = random.sample(range(4),4)

    final_user_array = [correct_user_dict, wrong_user_dict1, wrong_user_dict2, wrong_user_dict3]
    random.shuffle(final_user_array)

    d = {"tweet" : correct_user_tweet, "correctUser" : correct_user_name, "candidates" : final_user_array}
    return d
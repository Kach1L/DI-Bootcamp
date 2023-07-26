# Ex 1
# import json
# import random
# import os

# path = os.path.dirname(os.path.realpath(__file__))
# print(path)
# def get_words_from_file(text):
#     with open(text,'r') as f:
#         all_lines = f.readlines()
#         return str(all_lines)

# # file = get_words_from_file(path+r"\sowpods.txt")
# # print(file)




# def get_random_sentence(text, length):
#     with open(text,'r') as f:
#         fixall_lines = f.readlines
#         ranwords = random.choice('sowpods.txt')
#         for i in text:
#             text[int(i)].replace('\n','')
#         print(str(fixall_lines))
#         print(ranwords)
        
#         sentence = ranwords.join(' ')
#         print(sentence.lower)
         
# sent = get_random_sentence(path+r"\sowpods.txt",7)
# print(sent)



# def main():
#     print('This program is supposed to get random words from a list and join them into a sentence.')
#     try:
#         rand = int(input('How long do you want your sentence to be? Between 2 to 20 please'))
#     except:
#         ValueError('Not between 2 to 20')
#         return
#     else:
#         print("Ok let's go")
#         file = get_words_from_file(path+r"\sowpods.txt")
#         print(file)
#         sent = get_random_sentence(path+r"\sowpods.txt",7)
#         print(sent)
        
        

# Ex 2    
# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payable":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""
# accsalary = (sampleJson["company"]["employee"]["payable"]["salary"])
# sampleJson["company"]["employee"]["birth_date"] = "01/02/2004"

# with open("sample_file.json", "w") as file:
#     json.dump(sampleJson, file)
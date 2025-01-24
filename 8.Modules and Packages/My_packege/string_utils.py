def find_vovels(str):
    dict={}
    list=['a','e','i','o','u','A','E','I','O','U']

    for char in str:
        if char in list:
            if char in dict:
                dict[char]+=1
            else:
                dict[char]=1
            
    print("* Vowels:-")
    print(dict)

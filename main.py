

#1----------------------------------

# from threading import Thread

# def butun_son(n):
#     s = 0
#     for i in range(n):
#         s += i
#     print(s)

# th = Thread(target=butun_son, args=(108,))
# th.start()
# th.join()


#2----------------------------------

# def katta_harf(values):
    
#     result = []
    
#     for i in names:
#         result.append(i.capitalize())
#     print(result)

# ismlar = ['alfred', 'tabitha', 'william', 'arla']

# th = Thread(target=katta_harf, args=(ismlar,))
# th.start()
# th.join()

#3----------------------------------



# def baho(values):
    
#     result = []
    
#     for i in baho:
#         if i > 75:
#             result.append(i)
#     print(result)

# baho = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

# th = Thread(target=baho, args=(baho,))
# th.start()
# th.join()

#4----------------------------------


# def palindrom_soz(values):
    
#     result = []
    
#     for i in words:
#         if i == i[::-1]:
#             result.append(i)
#     print(result)

# sozlar = ['Anna', 'Alla', 'Kazak', 'Dom']

# th = Thread(target=palindrom_soz, args=(sozlar,))
# th.start()
# th.join()

#5----------------------------------


# def harfni_tekshirish(values):
#     i = 0
#     matn = ""
#     while i < len(text):
#         if text[i] == 'e':
#             matn += '3'
#         else:
#             matn += text[i]
#         i += 1
#     print(matn)

# text = input("Matn kiriting: ")

# th = Thread(target=harfni_tekshirish, args=(text,))
# th.start()
# th.join()

#6----------------------------------


# def bosh_joy(values):
#     i = 0
#     matn = ""
#     while i < len(matn):
#         if text[i] != ' ':
#             matn += text[i]
#         i += 1
#     print(matn)

# text = input("Matn kiriting: ")

# th = Thread(target=bosh_joy, args=(text,))
# th.start()
# th.join()

#7----------------------------------


# def royxatni_2ga(values):
    
#     result = []
    
#     for i in values:
#         result.append(i * 2)
#     print(result)

# raqam = [1,2,3,4,5,6,7,8,9,10]

# th = Thread(target=royxatni_2ga, args=(raqam,))
# th.start()
# th.join()

def levenstein(str_1, str_2):
    n, m = len(str_1), len(str_2)
    if n > m:
        str_1, str_2 = str_2, str_1
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if str_1[j - 1] != str_2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    distance = current_row[n]

    max_length = max(len(str_1), len(str_2))
    accuracy_percentage = (1 - distance / max_length) * 100

    return distance, accuracy_percentage

str1 = 'Привет мир'
str2 = 'Привет мир'
# 1 задание Петрова
print(f'Обычное сравнение\nПервое слово: {str1} \nВторое слово: {str2}')
print(levenstein(str1, str2))

str1 = 'Привет мир'
str2 = 'Привет мир!'
print(f'\nЧастичное сравнение\nПервое слово: {str1} \nВторое слово: {str2}')
print(levenstein(str1, str2))

str1 = 'Привет наш мир'
str2 = 'наш Привет мир'
print(f'\nСравнение по токену\nПервое слово: {str1} \nВторое слово: {str2}')
print(levenstein(str1, str2))

str1 = 'Привет мир'
str2 = '!ПриВЕт, наш мир!'
print(f'\nПродвинутое обычное сравнение\nПервое слово: {str1} \nВторое слово: {str2}')
print(levenstein(str1, str2))

str1 = 'Саратов'
city = ["Москва", "Санкт-Петербург", "Саратов", "Краснодар", "Воронеж", "Омск", "Екатеринбург", "Орск", "Красногорск", "Красноярск", "Самара"]

ans = sorted([[levenstein(str1, i), i] for i in city], key=lambda x: x[0])

print(f'\nСписок\nПервое слово: {str1} \n{ans}')






from fuzzywuzzy import fuzz
from fuzzywuzzy import process

print('Самое обычное сравнение:')
a = fuzz.ratio('Привет мир', 'Привет мир')
print(a)
#Выводит в консоль: 100
print('Если мы изменим пару символов, то на выходе получим другое число.')
a = fuzz.ratio('Привет мир', 'Привт кир')
print(a)
#Выводит в консоль: 84

print('Частичное сравнение:')
print('Данный вид сравнения во всей второй строке ищет совпадение с начальной')
a = fuzz.partial_ratio('Привет мир', 'Привет мир!')
print(a)
#Выводит в консоль: 100

a = fuzz.partial_ratio('Привет мир', 'Люблю колбасу, Привет мир')
print(a)
#Выводит в консоль: 100
print('Но следует помнить про регистр, так как')
a = fuzz.partial_ratio('Привет мир', 'Люблю колбасу, привет мир')
print(a)
#Выводит в консоль: 90

print('Сравнение по токену')
print('Token Sort Ratio - Слова сравниваются друг с другом, независимо от регистра или порядка')
a = fuzz.token_sort_ratio('Привет наш мир', 'мир наш Привет')
print(a)
#Выводит в консоль: 100

a = fuzz.token_sort_ratio('Привет наш мир', 'мир наш любимый Привет')
print(a)
#Выводит в консоль: 78

a = fuzz.token_sort_ratio('1 2 Привет наш мир', '1 мир наш 2 ПриВЕт')
print(a)
#Выводит в консоль: 100

print('Token Set Ratio - Это сравнение, в отличие от прошлого, приравнивает строки, если их отличие заключается в повторении слов')
a = fuzz.token_set_ratio('Привет наш мир', 'мир мир наш наш наш ПриВЕт')
print(a)
#Выводит в консоль: 100

print('Продвинутое обычное сравнение')
a = fuzz.WRatio('Привет наш мир', '!ПриВЕт наш мир!')
print(a)
#Выводит в консоль: 100

a = fuzz.WRatio('Привет наш мир', '!ПриВЕт, наш мир!')
print(a)
#Выводит в консоль: 97

print('Работа со списком')
print('Для сравнения строки со строками из списка используется модуль process')
city = ["Москва", "Санкт-Петербург", "Саратов", "Краснодар", "Воронеж", "Омск", "Екатеринбург", "Орск", "Красногорск", "Красноярск", "Самара"]
a = process.extract("Саратов", city, limit=2)
# Параметр limit по умолчанию имеет значение 5
print(a)
#Выводит в консоль: [('Саратов', 100), ('Самара', 62)]
print('Если необходим только первый в списке, то лучше использовать extractOne')
city = ["Москва", "Санкт-Петербург", "Саратов", "Краснодар", "Воронеж", "Омск", "Екатеринбург", "Орск", "Красногорск", "Красноярск", "Самара"]
a = process.extractOne("Краногрск", city)
print(a)
#Выводит в консоль: ('Красногорск', 90)




import datetime

str1 = 'SJSySzsubQRgsRpRpzmNaebZubfLNTzVxNsMcxaMzyWPHNKZLPOyWlbHczsStYMXIOKtYDZXBaWjSUejIaDHHotNBJVzEbwkPCCPoqFjmbewVmsOlJNUuSySrZAobwOCwXHMmmDcWRaTwICiAIvptiKbLJgAeMmkwzpUWnZlZtPgExyazBfbIfCTZTmRAMVYGBlakLHqTdNtaCgMEsCICILDpflRcZxNHJhZFkrBegNXjyWvlaRbjmKpkUQIDuHXJhLnNzxHaydGfeAHVWQTBKUelekxenTvQKBZLMDPbNoooJhvCdiYTneaIyfDUOBOTCtOKTbSSXiMzZYkalgVdjZGbefUIYqZiPzHiwdFLUcBIndfYtZPgJFAeRDVFgxWOiIRrGFMnqvrQObnuluSkFBOrPPVyMGgtBMcTHqlswfGiPeFvHSTJaCFUfwJKifnWlFfCyZkgEuLUpPDkrIIgjnvBlzRyuBAUbndLnISiGiDDJMnySJWFYkUcMHMTPAkFedSUNEXaPUwiiUXPKfAJSUjGCndVFYvWDbLjWMAAJRRYQnHvhwoBbOOXvwRuYdMPwdTEkpFZbrQRqSxHxyiZJYpjFxLZsnCNJZogrHgLAeOShDHvCdfsWDpPhFdTrTbAvmxwLxAvpJWjwQCFNXsnoAuTMoobRlrsfsPeNbghCNsDNGHBrfnBwguNYWbNFTJZfFlZsAcofxvHMNqAaOKpggyWTWrCXPKWWnnQnXlZwwOaoWUIqzOpePkSQGsPsctqjCrizWutYVlEbTDEayRxFqTiMfAObIRBZmPjxFfeMgwXRVNXQrVRjvBknPFkxiWSDmxvAjsdcphFFidqphuVpogihcKlaTcUGmlKqIefZuZZRSObasVlfoyeFgJNzWQOcYpXTRoHJWtsBnyDPKloAeIsNrIbcVYzcKepHpPtGQvtxEFbQMOZAhpawBslswMmhkuXgDpRlxwigmOUxVljPFexQUzvMyScUNUZuLV'
str2 = 'embRreaxrMWgrewXdIiNHHPGCUjWBwMqFvgFOAIfDdgjxQQbIfpjGgLXFmHWSOlqESkvcKQrBinTzqMIEJMSuQohbkoTqzzipFziusCRiHybJwDGByqLZxXsbNNvPfsmuQEeLhahNFVIgPQAEFMqGhQJbwaWJvywGmaMHGBwEPNxIWYsUkRsgtLErqpMhrlcKtIcZFNqgCisxuGqpbArFIeCjXhiQlrnMJgDFfJYcJpeAshliUEXSTfgeEEPxLSjpSDMfolgcGMMWQGaifExnyJUOYDxwpHDRMXMUixbefmbrFRuKuKenmKxcRDUHnutHfQkyUgVxUnLnjFVXCSTUlpcZPUGdngrEGEeMmEUZfSDWuAxfRSVVSKvjEcDljbeZqRdUQjbBCZMprOTrXCXPwdejixONMMWyIKxOeOWzTcrcVjjWKZJJAxkMmtCXQowsAWVlmJOpNpBOvZFdIplswxAlaNeabIwlXyZLjutXDFjwpSBxIrBzqjBYKjkKeIXNICitNBMgLXwWnEIqXsNItjFfeLucMnwpWfQFdVQPeikRUZBPPfVCCSfjNOzEIBJMcBgBayPHAscQYzNTHiJglLVwDdJyRCVuxUBMWFQZfScoPUAJxmKjvNLezOiSInRSGfxPDxMqoZJdyzlqEwPqORArRQyNGgapBnChfTKqrGLzVUKAyowWJcLximAzzAiuUUOHvRxpTCkMXfIVYtwzsedSnenGXoDJPHVZUExbmKxrlFHsNymwcqbMJJouQyQlhAbClvKiPosfYEJIQNUPECVJniNXnDIAQuGkmvYVLVflmHqEbjFQlCXmtjXLoBZdDluoyfUvffDgxLuhoZStbtwGwuvhbYPvuuycPVdzOdkLGIJKaVKXZNLvCWMxtiGHSMbWdkUrMChNCYpDWIeDVdEMHWwLiRvMSAOvYsmuMJvBONGuvNkaRAQqiRJTNWEkkSTkgamZcevwlnRBRdPRNXiBtZtqsgqyYUWhDQV'


start = datetime.datetime.now()
print(levenstein(str1, str2))
finish = datetime.datetime.now()
print('Время работы: ' + str(finish - start))



start = datetime.datetime.now()
a = fuzz.ratio(str1, str2)
finish = datetime.datetime.now()
print('Время работы: ' + str(finish - start))

print(a)
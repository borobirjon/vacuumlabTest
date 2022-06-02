# if first letter is consonat:
#   replace all the remaining consonats with the first letter
#   example   mapa --> mama

# if the first letter is vowel:
#   add the next first consonat at the bigining for the string and replace the remaining consonants with first consonant.
#   example: alibaba --> lailala

# if there is group of consecutive consonant:
#   replace all consecutive consonant with the first consonant occured in the string
#   example: lampa --> lala

#  if there is a group of consecutive vowels:
#   replace all the consecutive vowels with the last vowels from that consecutive vowel group.
#   example: naomi --> noni

#  ignore all the consonant after the last vowel in the string.


import string
import re
letter = list(string.ascii_lowercase)
vowels = ['a', 'e', 'i', 'o', 'u']
consonant = []
for i in letter:
    if i not in vowels:
        consonant.append(i)
    else:
        pass


def speak_after_ignore(speak):
    ignore = re.search(r'([^aeiou]*)$', speak).group(1)
    if (len(ignore) == 0):
        return speak
    else:
        return speak[:(len(speak)-len(ignore))]


def childspeak(speak):
    speak1 = speak_after_ignore(speak)
    list_of_cons_groups = re.findall(r'[^aeiou]+', speak1)
    list_of_vowel_groups = re.findall(r'[aeiou]+', speak1)

    if speak1[0] in consonant:
        replace = '|'.join(str(i) for i in set(list_of_cons_groups))
        speak2 = re.sub(replace, speak1[0], speak1)
        for vow in set(list_of_vowel_groups):
            if len(vow) > 1:
                speak2 = re.sub(vow, vow[-1], speak2)
        return speak2

    if speak1[0] in vowels:
        count = 0
        for i in speak1:
            if i in consonant:
                count = count+1
                if count != 0:
                    first_consonant = i
                    break
        replace = '|'.join(str(i) for i in set(list_of_cons_groups))
        speak2 = re.sub(replace, first_consonant, speak1)
        for vow in set(list_of_vowel_groups):
            if len(vow) > 1:
                speak2 = re.sub(vow, vow[-1], speak2)
        return (first_consonant + speak2)


if __name__ == "__main__":
    with open("test.in", "r") as a_file:
        for line in a_file:

            with open("test1.in", "a") as w_file:
                w_file.write(childspeak(line)+'\n')

    with open("test1.in", 'r') as a_file:
        list1 = []
        list2 = []
        for line in a_file:
            list1.append(line)
        for i in list1:
            list2.append(list1.count(i)-1)

    with open("test.in", "r") as a_file:
        i = 0
        for line in a_file:
            print(line+str(list2[i]))
            i = i+1

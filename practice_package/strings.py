extract_file_name = lambda fp: fp.split("/")[-1].split("\\")[-1].split('.')[0]

encrypt_sentence = lambda string: ''.join([string[i] for i in range(len(string)) if i % 2 == 0]) + ''.join([string[i] for i in range(len(string)) if i % 2 != 0][::-1])

check_brackets = lambda string: (lambda balance, i: next((i + 1 for i in range(len(string)) if (balance := balance + (1 if string[i] == '(' else -1 if string[i] == ')' else 0)) < 0), -1) if balance <= 0 else -1)(0, 0)

reverse_domain = lambda domain: '.'.join(domain.split('.')[::-1])

count_vowel_groups = lambda word: sum(1 for i in range(len(word)) if word[i].lower() in 'aeiouy' and (i == 0 or word[i-1].lower() not in 'aeiouy'))

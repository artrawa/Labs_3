# TODO  Напишите функцию count_letters
alphabet = {}


def count_letters(text):
    text = text.lower()
    # print(text)
    list_letters = list(text)
    # print(list_letters)
    for i in list_letters:
        if i.isalpha():
            if i in alphabet:
                alphabet[i] = alphabet.get(i) + 1
            else:
                alphabet[i] = 1
    return alphabet


# TODO Напишите функцию calculate_frequency

def calculate_frequency(alphabet):
    list_value = alphabet.values()
    list_keys = alphabet.keys()
    number_letters = sum(list_value)
    #print(number_letters)
    for i in list_keys:
        alphabet[i] = alphabet.get(i) / number_letters
        print(f"{i}: {alphabet.get(i):.2f}")

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте

dict_ = count_letters(main_str)
calculate_frequency(dict_)
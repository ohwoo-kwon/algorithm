while True:
    text = input()
    is_ok = False
    mo_list = ["a", "e", "i", "o", "u"]
    mo_cnt = 0
    ja_cnt = 0
    prev_word = 0

    if text == "end":
        break

    for t in text:
        if not is_ok:
            if t in mo_list:
                is_ok = True

        if t in mo_list:
            mo_cnt += 1
            ja_cnt = 0
        else:
            ja_cnt += 1
            mo_cnt = 0

        if mo_cnt == 3 or ja_cnt == 3:
            print('<'+text+"> is not acceptable.")
            break

        if prev_word == t and (t != "e" and t != "o"):
            print('<' + text + "> is not acceptable.")
            break

        prev_word = t
    else:
        if is_ok:
            print('<' + text + "> is acceptable.")
        else:
            print('<' + text + "> is not acceptable.")
import random

def get_answer(anser_number):
  if anser_number == 1:
    return '確かそうだ'
  elif anser_number == 2:
    return '間違いなくそうだ'
  elif anser_number == 3:
    return 'はい'
  elif anser_number == 4:
    return 'なんとも。もういちどやってみて'
  elif anser_number == 5:
    return 'あとでもう一度きいてみて'
  elif anser_number == 6:
    return '集中してもう一度きいてみて'
  elif anser_number == 7:
    return '私の答えはノーです'
  elif anser_number == 8:
    return '見通しはそれほどよくない'
  elif anser_number == 9:
    return 'とても疑わしい'

# r = random.randint(1, 9)
# fortune = get_answer(r)
# print(fortune)

print(get_answer(random.randint(1, 9)))
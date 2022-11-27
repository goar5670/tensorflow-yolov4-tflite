from googletrans import Translator

if __name__ == '__main__':
  translator = Translator()
  filename = '../android/app/src/main/assets/coco.txt'
  target = 'ru'

  with open(filename, 'r+') as file:
    translated = []
    for line in file.readlines():
      if(len(line) < 2):
        continue
      translated_label = translator.translate(line[:-1], src='en', dest=target).text
      new_label = f'\n{line[:-1]} ({translated_label})'
      translated.append(new_label)
    print(translated)
    file.truncate(0)
    file.writelines(translated)

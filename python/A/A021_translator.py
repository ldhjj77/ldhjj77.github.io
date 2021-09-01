# pip install googletrans==4.0.0-rc1    # 구글번역기 알파버전 설치 / 기본버전은 사용불가

# {'af': 'afrikaans', 'am': 'amharic', 'ar': 'arabic', 'az': 'azerbaijani', 'be': 'belarusian', 
# 'bg': 'bulgarian', 'bn': 'bengali', 'bs': 'bosnian', 'ca': 'catalan', 'ceb': 'cebuano', 
# 'co': 'corsican', 'cs': 'czech', 'cy': 'welsh', 'da': 'danish', 'de': 'german', 
# 'el': 'greek', 'en': 'english', 'eo': 'esperanto', 'es': 'spanish', 'et': 'estonian', 
# 'eu': 'basque', 'fa': 'persian', 'fi': 'finnish', 'fil': 'Filipino', 'fr': 'french', 
# 'fy': 'frisian', 'ga': 'irish', 'gd': 'scots gaelic', 'gl': 'galician', 'gu': 'gujarati', 
# 'ha': 'hausa', 'haw': 'hawaiian', 'he': 'Hebrew', 'hi': 'hindi', 'hmn': 'hmong', 
# 'hr': 'croatian', 'ht': 'haitian creole', 'hu': 'hungarian', 'hy': 'armenian', 
# 'id': 'indonesian', 'ig': 'igbo', 'is': 'icelandic', 'it': 'italian', 'iw': 'hebrew', 
# 'ja': 'japanese', 'jw': 'javanese', 'ka': 'georgian', 'kk': 'kazakh', 'km': 'khmer', 
# 'kn': 'kannada', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'la': 'latin', 
# 'lb': 'luxembourgish', 'lo': 'lao', 'lt': 'lithuanian', 'lv': 'latvian', 'mg': 'malagasy', 
# 'mi': 'maori', 'mk': 'macedonian', 'ml': 'malayalam', 'mn': 'mongolian', 'mr': 'marathi', 
# 'ms': 'malay', 'mt': 'maltese', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'nl': 'dutch', 
# 'no': 'norwegian', 'ny': 'chichewa', 'pa': 'punjabi', 'pl': 'polish', 'ps': 'pashto', 
# 'pt': 'portuguese', 'ro': 'romanian', 'ru': 'russian', 'sd': 'sindhi', 'si': 'sinhala', 
# 'sk': 'slovak', 'sl': 'slovenian', 'sm': 'samoan', 'sn': 'shona', 'so': 'somali', 
# 'sq': 'albanian', 'sr': 'serbian', 'st': 'sesotho', 'su': 'sundanese', 'sv': 'swedish', 
# 'sw': 'swahili', 'ta': 'tamil', 'te': 'telugu', 'tg': 'tajik', 'th': 'thai', 
# 'tl': 'filipino', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'uz': 'uzbek', 
# 'vi': 'vietnamese', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 
# 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'zu': 'zulu'}
from googletrans import Translator
 
text1 = input('번역할 영어를 입력 : ')
text2 = input('번역할 한글을 입력 : ')

 
translator = Translator()
 
trans1 = translator.translate(text1, src='en', dest='ko')
trans2 = translator.translate(text2, src='ko', dest='en')
 
print("English to Korean: ", trans1.text)
print("Korean to English: ", trans2.text)




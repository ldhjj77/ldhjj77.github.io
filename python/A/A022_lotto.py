import requests

# url = 'http://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo='
# res = requests.get(url)
# print(res.json())

def inputroundnumber():
    roundNumber = input('당첨번호 확인할 회차를 입력해 주세요 : ')
    return roundNumber

def getjsonfromurl(url):
    return requests.get(url)

def existlottodata(json, roundNumber):
    if(json['returnValue'] == 'success'):
        print(json)
        return True
    else:
        print('존재하지 않는 회차번호 입니다.')
        return False

def writejsontofile(file, jsonData):
    fout = open(file, 'w')
    fout.write(str(jsonData))
    fout.close()


# 실제 함수들을 활용
roundNumber = - 1
while int(roundNumber) != 0:
    lottourl = 'http://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=+'
    roundNumber = inputroundnumber()
    url = lottourl + roundNumber
    
    res = getjsonfromurl(url)
    exist = existlottodata(res.json(), roundNumber)
    if(exist):
        writejsontofile('./A/A022_output.txt', res.json())
        



















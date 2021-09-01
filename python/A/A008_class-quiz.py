# 주어진 코드를 활용하여 부동산 프로그램을 작성하시오
# datatime & 

# 출력예제
# 총 3곳의 매물이 있습니다
# 동구 아파트 매매 5억 2020년
# 달성군 오피스텔 전체 3억 2021년
# 북구 빌라 월세 500/30 2019

# [코드]

class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.year = year
        
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.year)

houses = []
h1 = House("동구", "아파트", "매매", "5억", "2020년")
h2 = House("달성군", "오피스텔", "전세", "3억", "2021년")
h3 = House("북구", "빌라", "월세", "500/30", "2019년")

houses.append(h1)
houses.append(h2)
houses.append(h3)


print("총 {0}곳의 매물이 있습니다".format(len(houses)))
for house in houses:        # houses의 내용을 한개씩house에 집어넣음 
    house.show_detail()     # 순서대로 실행

















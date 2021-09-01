def 리스트분할(lst, n):     # 리스트를 몇개로 분할한 것인지
    return [lst[i:i+n] for i in range(0, len(lst), n)]
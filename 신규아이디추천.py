def solution(new_id):
    ##1단계
    new_id = new_id.lower()
    ##2단계
    result = ''
    for i in new_id:
        if i.isalnum() or i in '-_.':
            result += i
    ##3단계
    while '..' in result:
        result = result.replace('..', '.')
    ##4단계
    result = result.strip('.')
    ##5단계
    if result == '':
        result = 'a'
    ##6단계
    if len(result) >= 16:
        result = result[:15]
        if result[-1] == '.':
            result = result[:-1]
    ##7단계
    while len(result) <= 2:
        result += result[-1]

    answer = result
    return answer
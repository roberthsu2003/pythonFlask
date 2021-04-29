from random import choice

version = "1.1"
color = "red"
def get_description():
    '''
    回傳亂數的天氣狀況
    '''
    possibilities = ['下雨', '下雪', '陰天', '晴天', '冰雹', '霧霾']
    return choice(possibilities)
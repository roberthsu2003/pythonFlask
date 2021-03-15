#台北市串接Youbike網址
#https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json
'''
sno(站點代號)、sna(場站中文名稱)、tot(場站總停車格)、sbi(場站目前車輛數量)、sarea(場站區域)、mday(資料更新時間)、lat(緯度)、lng(經度)、ar(地點)、sareaen(場站區域英文)、snaen(場站名稱英文)、aren(地址英文)、bemp(空位數量)、act(全站禁用狀態)
'''

import requests
def getAreaSimpleInfo(siteName):
    simpleInfoOfArea = []
    siteCount = 0
    for site in youbikeData:
        if site['sarea'] == siteName:
            oneItem = {}
            oneItem['ar'] = site['ar']
            oneItem['bemp'] = site['bemp']
            oneItem['lat'] = site['lat']
            oneItem['lng'] = site['lng']
            oneItem['sna'] = site['sna']
            oneItem['tot'] = site['tot']
            oneItem['mday'] = site['mday']
            oneItem['sbi'] = site['sbi']
            siteCount += 1
            simpleInfoOfArea.append(oneItem)

    if siteCount == 0:
        return None
    return simpleInfoOfArea

response = requests.get('https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json')
response.encoding = 'utf-8'
downloadData = response.json()
downloadData1=downloadData['retVal']
#取出value值，轉為list
youbikeData = list(downloadData1.values())
#建立區域的list
areaSet = set()
for site in youbikeData:
    areaSet.add(site['sarea'])

areas= list(areaSet)


__all__ = ['areas','getAreaSimpleInfo']
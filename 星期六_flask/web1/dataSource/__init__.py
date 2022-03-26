import requests
import sqlite3
from sqlite3 import Error

def get_weather_of_taiwan():
    urlPathApi = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0001-001?Authorization=rdec-key-123-45678-011121314&format=JSON"
    try:
        response = requests.get(urlPathApi)
        response.raise_for_status()
    except requests.ConnectionError as e:
        print(e)
        return None
    except requests.HTTPError as e:
        print(e)
        return None
    except requests.Timeout as e:
        print(e)
        return None
    except requests.exceptions.RequestException as e:
        print(e)
        return None

    allData = response.json()
    locations = allData["records"]['location']
    weatherList = []
    for item in locations:
        itemDic = {}
        itemDic['縣市'] = item['parameter'][0]['parameterValue']
        itemDic['區域'] = item['parameter'][2]['parameterValue']
        itemDic['時間'] = item['time']['obsTime']
        itemDic['溫度'] = float(item['weatherElement'][3]['elementValue'])
        weatherList.append(itemDic)
    return weatherList

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file);
        print(sqlite3.version)
    except Error as e:
        print(e)
        return None

    return conn

def select_countries_tasks(conn):
    cursor = conn.cursor()
    sqlString = """
    SELECT  DISTINCT country
    FROM city
    ORDER BY country
    """
    cursor.execute(sqlString)
    countries = cursor.fetchall()
    return countries


def get_countries():
    conn = create_connection('citys.db')
    if conn is not None:
        print("資料庫連線成功")
        country_list = select_countries_tasks(conn)
        conn.close()
    return country_list



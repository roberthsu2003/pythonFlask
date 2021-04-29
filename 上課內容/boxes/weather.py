from .sources import daily, weekly

def allForcecast():
    print(daily.forecast())
    print(weekly.forecast())
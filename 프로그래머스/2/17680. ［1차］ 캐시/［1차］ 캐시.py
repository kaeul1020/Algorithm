def solution(cacheSize, cities):
    t = 0
    cache = []

    for city in cities:
        if city.lower() not in cache:
            t += 5
        else :
            cache.remove(city.lower())
            t += 1
        cache.append(city.lower())
        if len(cache) > cacheSize:
            cache.pop(0)       
    
    return t
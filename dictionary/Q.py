n = int(input())
city_to_country = {}
for _ in range(n):
    line = input().split()
    country = line[0]
    cities = line[1:]
    for city in cities:
        city_to_country[city] = country
m = int(input())
for _ in range(m):
    query_city = input()
    print(city_to_country[query_city])
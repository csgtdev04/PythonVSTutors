# Warm up Kahoot

# Lesson about Lists 

tv_shows = ["Mandalorian", "Just add Magic", "Drake & Josh", "Henry Danger", "Breaking Bad"]

word = "Sai" # indexes start 0
print(word[0])

# 1. Accessing elements in a list
print(tv_shows[2])
print(len(tv_shows))
print(tv_shows[0])
print(tv_shows[-1])
print(tv_shows[-5])

print(tv_shows[len(tv_shows) - 1])

# 2. Append method () - to carry out some action
tv_shows.append("Richy Rich")
tv_shows.append("Loki")
print(tv_shows)

# 3. Insert method (at index)
tv_shows.insert(2, "Loud House")
print(tv_shows)
tv_shows.insert(0, "Stranger Things")
print(tv_shows)

# 4. Replacing
del tv_shows[6]
tv_shows[0] = "Breaking Bad"
tv_shows.reverse()
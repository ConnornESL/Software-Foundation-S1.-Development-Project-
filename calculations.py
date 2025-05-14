# Define function to classify album
def classify_album(sales):
    sales = int(sales)
    if sales >= 3000000:
        return "Triple Platinum"
    elif sales >= 2000000:
        return "Double Platinum"
    elif sales >= 1000000:
        return "Platinum"
    if sales >= 500000:
        return "Gold"
    return "Not Classified"

# Define function to find best-selling album
def find_best_seller(data):
    best_row = data[0]
    best_sales = int(best_row[3])
    for row in data:
        sales = int(row[3])
        if sales > best_sales:
            best_row = row
            best_sales = sales
    return best_row

# Define function to find top 3 artists
def find_top_artists(data):
    artist_sales = []
    for row in data:
        artist = row[2]
        sales = int(row[3])
        found = False
        for item in artist_sales:
            if item[0] == artist:
                item[1] = item[1] + sales
                found = True
        if not found:
            artist_sales.append([artist, sales])
    sorted_artists = []
    while len(artist_sales) > 0:
        max_sales = 0
        max_artist = None
        max_index = 0
        for i in range(len(artist_sales)):
            if artist_sales[i][1] > max_sales:
                max_sales = artist_sales[i][1]
                max_artist = artist_sales[i][0]
                max_index = i
        sorted_artists.append([max_artist, max_sales])
        artist_sales.pop(max_index)
    if len(sorted_artists) > 3:
        return sorted_artists[0:3]
    return sorted_artists

# Define function to find worst-selling album
def find_worst_seller(data):
    worst_row = data[0]
    worst_sales = int(worst_row[3])
    for row in data:
        sales = int(row[3])
        if sales < worst_sales:
            worst_row = row
            worst_sales = sales
    return worst_row
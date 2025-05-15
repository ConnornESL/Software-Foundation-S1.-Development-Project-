# Import csv module for CSV reading
import csv
# Import calculation functions from calculations file
from calculations import classify_album, find_best_seller, find_top_artists, find_worst_seller

# Reads the CSV file into list of rows
def read_csv_file():
    data = []
    # Try opening file
    try:
        # Open CSV with UTF-8 encoding
        with open("bestselling_albums_by_year_in_UK.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)

            for row in reader:

                if len(row) == 4:
                    data.append(row)

                else:
                    print("Skipping row, wrong format:", row)

        return data
    
    # Handle file errors
    except Exception as e:

        print(f"Error reading file: {e}")
        return []

# Write results to output.csv
def write_output_csv(data, best_seller, top_artists, worst_seller):

    # Try writing to file

    try:

        with open("output.csv", "w") as file:
            
            
            file.write("Year,Album,Artist,Albums sold,Classification\n")

            for row in data:

                year, album, artist, sales = row

                sales = int(sales)

                classification = classify_album(sales)

                file.write(f"{year},{album},{artist},{sales},{classification}\n")

            file.write("\nBest Selling Album\nYear,Album,Artist,Albums sold\n")
            file.write(f"{best_seller[0]},{best_seller[1]},{best_seller[2]},{best_seller[3]}\n")
            file.write("\nTop 3 Artists by Total Sales\nArtist,Total Sales\n")
            
            for artist, sales in top_artists:

                file.write(f"{artist},{sales}\n")

            file.write("\nWorst Selling Album\nYear,Album,Artist,Albums sold\n")
            file.write(f"{worst_seller[0]},{worst_seller[1]},{worst_seller[2]},{worst_seller[3]}\n")

    # Handle file writing errors
    except Exception as e:

        print(f"Error writing output.csv: {e}")

# Main program
def main():
    data = read_csv_file()

    # If the function returns a null value
    if not data:
        print("No data to process")
        return
    
    best_seller = find_best_seller(data)
    top_artists = find_top_artists(data)
    worst_seller = find_worst_seller(data)

    write_output_csv(data, best_seller, top_artists, worst_seller)
    
    print("Results saved to output.csv")

# Run program
main()
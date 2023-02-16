import requests
import os
import time
# fields 
imageCount = 0; 
uniquePiecesCount = 0; 
API_KEY = "GETKEYFROMREBRICKABLE"
set_num = input("Enter set number:") #"7669-1"  # Replace with the set number you want to look up or input("Enter set number you want to search for: ")
   # create file for images to be placed into
if not os.path.exists(f"./Set_Images/{set_num}"):
    os.makedirs(f"./Set_Images/{set_num}")
# Make a GET request to the parts list API endpoint for the specified set number
url = f"https://rebrickable.com/api/v3/lego/sets/{set_num}/parts/?key={API_KEY}"
setData = requests.get(url)
# Check the status code of the setData to ensure the request was successful
if setData.status_code == 200:
    # Retrieve the data from the setData in JSON format
    data = setData.json()
    # Print the results
    print(f"Parts list for set {set_num}:")
    for part in data['results']:
        print(f"{part['quantity']}x {part['part']['name']} ({part['part']['part_num']})")
        uniquePiecesCount = uniquePiecesCount + 1
        url2 = f"https://rebrickable.com/api/v3/lego/parts/{part['part']['part_num']}/?key={API_KEY}"
        response = requests.get(url2)
        if response.status_code == 200:
            partData = response.json()
            partFigure = partData['part_img_url']
            partImage = requests.get(partFigure)
            with open(f"./Set_Images/{set_num}/{part['part']['part_num']}.png", "wb") as f:
                f.write(partImage.content)
            imageCount = imageCount + 1
else:
    print(f"Error: {setData.status_code}")
print("\n Unique Pieces: ", uniquePiecesCount, " Pieces with images: ", imageCount)

 

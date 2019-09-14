## Two Step Encryption
### Introduction
Applying Steganography followed by Visual Cryptography. Implementation based on the research paper titled **"Combine use of Steganography and Visual  Cryptography for Secured Data hiding in Computer Forensics"**

Steganography is the method of hiding secret data inside any form of digital media. The main idea behind steganography is to hide the existence of a data in any medium like audio, video, image etc.

Visual cryptography is a cryptographic technique which allows visual information (pictures, text, etc.) to be encrypted in such a way that the decrypted information appears as a visual image.

### Project
##### Structure
```
.
├── images
├── main.py
├── README.md
├── Reference_paper.pdf
├── requirements.txt
└── src
    ├── lsb_stegno.py
    └── n_share.py
```

##### File description
| File          | Description                                    |
|---------------|-----------------------------------------------------------|
| lsb_stegno.py | Methods to Encode and Decode data using LSB Steganography |
| n_share.py    | Methods to Split and Compress LSB Encoded images          |

### Algorithms
##### Steganography
###### Encoding data in image
```python
# Putting modified pixels in the new image 
newimg.putpixel((x, y), pixel) 
if (x == w - 1): 
    x = 0
    y += 1
else: 
    x += 1
```

###### Decoding data from image
```python
# string of binary data 
binstr = '' 
    
for i in pixels[:8]: 
    if (i % 2 == 0): 
        binstr += '0'
    else: 
        binstr += '1'
            
data += chr(int(binstr, 2)) 
if (pixels[-1] % 2 != 0): 
    return data 
```
##### Visual Cryptography
###### Generating shares
```python
# Split image based on random factor
n = int(np.random.randint(data[i, j, k] + 1))
img1[i, j, k] = n
img2[i, j, k] = data[i, j, k] - n
```

###### Compressing shares
```python
img[i, j, k] = img1[i, j, k] + img2[i, j, k]
```

##### Usage
###### Setup
Install dependencies
```
pip install -r requirements.txt
```
Run using python
```
python main.py
```

###### Message Encoding
```
1. Encode
2. Decode
Enter choice: 1
LSB encoding...
Enter image name(with extension): images/car.jpg
Enter data to be encoded : Testing two step encryption using steganography and visual cryptography.
Generating shares...
DONE
```

###### Message Decoding
```
1. Encode
2. Decode
Enter choice: 2
Compressing shares...
Decoded message: Testing two step encryption using steganography and visual cryptography.
```

### Result
<p align="center">
  <img src="./images/car.jpg" style="width:50%;height:50%;"><br>
  <i><b>Figure:</b> Initial sample image</i>
</p>

<p align="center">
  <img src="./images/share1.png" style="width:50%;height:50%;"><img src="./images/share2.png"style="width:50%;height:50%;"><br>
  <i><b>Figure:</b> Generated Shares (i) and (ii)</i>
</p>

<p align="center">
  <img src="./images/compress.png" style="width:50%;height:50%;"><br>
  <i><b>Figure:</b> Compressed image</i>
</p>
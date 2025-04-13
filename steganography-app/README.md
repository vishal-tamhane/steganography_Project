# Image Steganography Web Application

A web application that allows users to hide and reveal secret messages within images using steganography techniques.

## Features

- Encode secret messages into images
- Decode hidden messages from images
- Modern and user-friendly interface
- Real-time image preview
- Secure file handling

## Prerequisites

- Node.js (v14 or higher)
- Python (v3.7 or higher)
- npm (v6 or higher)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd steganography-app
```

2. Install backend dependencies:
```bash
cd backend
npm install
```

3. Install frontend dependencies:
```bash
cd ../frontend
npm install
```

4. Install Python dependencies:
```bash
pip install Pillow numpy
```

## Running the Application

1. Start the backend server:
```bash
cd backend
node server.js
```

2. Start the frontend development server:
```bash
cd frontend
npm start
```

3. Open your browser and navigate to `http://localhost:3000`

## Usage

1. **Encoding a Message:**
   - Click "Choose File" to select an image
   - Enter your secret message in the text area
   - Click "Encode Message"
   - The encoded image will be automatically downloaded

2. **Decoding a Message:**
   - Click "Choose File" to select an encoded image
   - Click "Decode Message"
   - The hidden message will be displayed below the buttons

## Security Notes

- The application uses LSB (Least Significant Bit) steganography
- Messages are not encrypted, so they can be extracted by anyone with the right tools
- For additional security, consider encrypting messages before encoding them

## Technologies Used

- Frontend: React.js
- Backend: Node.js with Express
- Image Processing: Python with Pillow and NumPy
- API Communication: Axios

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
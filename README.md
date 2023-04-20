# m3u8_proxy-cors

This is a simple Python proxy server that adds CORS headers to M3U8 playlist files. It allows you to bypass CORS restrictions when playing M3U8 playlists in browsers.

## Installation

To install and run the server, follow these steps:

1. Clone the repository:

```py
git clone https://github.com/masterz5398/m3u8_proxy-cors.git
```

2. Install dependencies:
    
```py
cd m3u8_proxy-cors
pip install -r requirements.txt
```
3. Start the server:
```py
python main.py
```

The server will start listening on port 5010 by default. You can change the port by setting the `port` variable in main.py

## Usage

To use the server, simply replace the URL of the M3U8 playlist file in your application with the URL of the proxy server. For example, if your original URL was `https://example.com/video.m3u8`, you would replace it with `http://localhost:5010/cors?url=https://example.com/video.m3u8`.

For m3u8s ending with #.mp4 you should add origin=aninin in query like ```http://localhost:5010/cors?url=https://example.com/video.m3u8&origin=aninin```


To set custom headers for a request you can do ```http://localhost:8000/cors?url=https://example.com/video.m3u8&headers={"User-Agent":"Mozilla/5.0 ...","referer":"https://example.com",...}```

don't put spaces between the headers(you can put it inside the quotes) you might get a 500 error, 

do not encode the url or headers as we do not have a decoder for it

## Deploying to Vercel
You can quickly deploy this project to Vercel with the following button:

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fmasterz5398%2Fm3u8_proxy-cors&project-name=m3u8-proxy-cors&repository-name=m3u8-proxy-cors)


contributions are welcome you can make a pull request I will review it and merge it if it benifits the program

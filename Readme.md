# QR Code Generator
```
A simple flask application aimed to convert your links into qr code.
```

## Curl
```
curl  -X POST \
  'http://127.0.0.1:5000/generate_qr_code' \
  --header 'Accept: */*' \
  --header 'User-Agent: Thunder Client (https://www.thunderclient.com)' \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "link":"https://textxet.netlify.app/"
}'
```
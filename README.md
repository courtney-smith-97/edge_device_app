# w251 HW 3
### Files and Folders
#### Each folder represents a container. MQTT is deployed twice, once in my VMWare Ubuntu VM and once in an AWS EC2.
- `mqtt`: contains the Dockerfile and .yaml files for running the MQTT broker/service; same deployments used locally and in the cloud
- `camera`: contains the Dockerfile, .yaml file, and cam.py file for connecting to the USB camera, detecting a face, capturing the image, and publishing the image to the local MQTT listener
- `listener`: contains the Dockerfile, .yaml file, and listener.py file for running the MQTT listener that receives the image (as a bytestring) from the face-detector deployment and publishes it to the remote MQTT broker running on an EC2 in AWS
- `aws_listener`: contains the Dockerfile, .yaml file, and im_upload.py file for receiving the bytestring from the remote MQTT broker, saving it as a `.png`, and pushing it to the S3 bucket 


### HW Questions
- I used QoS 0 because which specific images were transmitted and ultimately stored in the S3 wasn't important, so I didn't need a guarantee that each image would be transmitted at least once. QoS 0 is also fastest which would work well for this type of use case.
- I named my topic after the origin and type of the message (usb camera, images): `usbcam/images`


### S3 Link
Bucket is set as public but just in case, the second link is a presigned URL valid for 7 days

https://hw3-image-bucket.s3.amazonaws.com/01-02-2022_20-50-29.png

https://hw3-image-bucket.s3.us-east-1.amazonaws.com/01-02-2022_20-50-29.png?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLWVhc3QtMSJGMEQCIGZ5npXzpiwf%2F4lE1pL08pZ%2BtTMZ3YrXafHvpDI8UgtkAiBFJlU7i%2FlFO1Ur8jic5G4DoVGCkAcUzyzOusW6W9fYsSrkAghOEAAaDDM2NTIxNjYwOTQ3NyIMnLlE669M440e0ZnzKsECaC9YgaJFlnTo0uKxpS%2B4wSHch2%2BqZe2otT6iA%2Fns6u7kfbnlNemFq5EpnNofiAICk9vJejLIMrM99nXyXea6LklX0ZWChlY29gGlOZtXgdlaheKIZPlcK9vEUKnmVrpFNDHskuvyFLZddXVJzoCtouD%2F7YxzffQSPonSXqq1do8HTMQgoc0mMhZkMdVGH28Un5Q3%2BgekPZblEUVrp4HQb4qUmtREbm6klQkWEPa7SvCtKVbVOi3wRLIY6tRqvLzRH2ytXjOgQ7DTo7vJBcbHRapfQ5Hv42KGgvYoZLwUiJb9p1yB%2BqxMj3BDTCAhRdhEJos5InBspwKaAsVxtUSLJS3XGOPsJKthNYLZKqIIHHE8DBXjT5IGmwauqi10ylLMHTconwDZIXI%2FhpIKY0TAOnnUzu8SBvXNjzAKwKdWLiSKMKe45o8GOrQC7IY6IZueBXLjWCcAaq2EH3wKhYBknpqi07a0uRsFe3c1%2FDT3ZdfSyBsSE6l61pL4eO1urDXGP8Tk7q5Keydu3fbrMmMVWuFm49m6xI6u7xxWgv9O%2BO%2BXpyEp8Snki4czLeP6gHzSGiFGbNSwITE6cpM%2BK%2FKyGy5UyOKza%2FxgqSWtTWUeUdXzaJSHidSX6SGjmHugVbHHbtZFjXE7yfeXHfoF1jOW6MTVWQx9sZJA0xVNhbrx%2FHtmVFkzeJWMxtTbNEUUno%2FFy0U1N0zRIw4rrWHy0Kgg9DWmSUdYzaoUsrtjortZu8dsgVAN%2B%2Bt7MJcaNnsZtnPRAPscWYzGgWV69kq0%2F0QZFQhuNFAOX09Up9HWcxcBeHgFVXoq%2B3i14sqTszbe3y1PkHkRVIhXg3H56C03NSQ%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220202T055133Z&X-Amz-SignedHeaders=host&X-Amz-Expires=604800&X-Amz-Credential=ASIAVKCE3GTCTGFMPUWD%2F20220202%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=4438408c45b6e36947f10066a5a1efe33e4b3df982ca7d46b6a0f024b73e303e

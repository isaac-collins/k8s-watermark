cd frontend
sudo docker build -t isaaccollins/isaac-watermark:frontend3 .
sudo docker push isaaccollins/isaac-watermark:frontend3
cd ../backend
sudo docker build -t isaaccollins/isaac-watermark:backend3 .
sudo docker push isaaccollins/isaac-watermark:backend3
cd ..

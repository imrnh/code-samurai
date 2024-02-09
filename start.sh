docker build --tag=sol:latest .
docker run -it -p 8000:8000 --rm --name=sol sol:latest
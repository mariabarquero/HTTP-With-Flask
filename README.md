# HTTP-With-Flask

Http service get with flask

If you want create a virtual enviroment you can use the next command

```
virtualenv venv
```

Run the virtual enviroment

```
source venv/bin/activate
```

Then, build the flask app

```
docker build -t flask-app .
```

After run the image you can choose the port, in this example use the port 4000

```
docker run -it -p 4000:8080 -d flask-app
```

To check if the container is running, write the next command:

```
docker container ls 
```

Finally write this route in your browser with the port that you choose 

```
http://localhost:4000/
```

When finish stop the docker

```
docker stop [container ID]
```

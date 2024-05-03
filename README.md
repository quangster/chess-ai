#### Developed with:

- [React](https://reactjs.org/) - ^18.3.1
- [Node.js](https://nodejs.org/en/) - 20.12.2
- [Python](https://www.python.org/) - 3.12.3

## Run application with Docker
Make sure you have already installed Docker Engine
```bash
docker -v
```
=> Docker version 26.0.0, build 2ae903e
```bash
docker-composer --version
```
=> docker-compose version 1.29.2, build 5becea4c


### Build the images and run the containers:
```bash
docker-compose up -d --build
```

## Run application without Docker

Install server dependencies
```
cd server
pip install -r requirements.txt
```

Run server
```
python main.py
```

Open another terminal to run client\
Install client dependencies
```bash
cd client
npm install
```

Run client
```
npm start
```

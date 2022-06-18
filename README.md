# Online Messenger

Used technologies: python, django, websockets, javascript, redis

Requirements: git, docker, docker-compose

## Download
```bash
git clone https://github.com/woozlic/messenger.git
```

## Set environment variables

Create file named ".env" in this directory and put a random string in SECRET_KEY:
```bash
SECRET_KEY=there_must_be_random_string
```

## Run

```bash
docker-compose up -d --build
```

### IMPORTANT!

**Docker will automatically create 2 superusers with passwords for testing**

```test_1: admin```

```test_2: admin```

## Use

Visit [http://127.0.0.1:7777](http://127.0.0.1:7777) in your favorite browser
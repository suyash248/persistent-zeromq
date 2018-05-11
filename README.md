# Publisher Subscriber (ZeroMQ + Redis)
PUB-SUB using ZeroMQ, used Redis to persist tasks/messages.

Simulation -

![alt text](https://github.com/suyash248/pub-sub-persistable/blob/master/static/simulation.png "Pub-Sub simulation")

# Requirements
- Redis
- Python 3

# How to run?

```sh
$ cd <project-dir>
$ export PYTHONPATH="$PYTHONPATH:." # . corresponds to current directory(project-dir).
$ virtualenv -p python3 .env        # Create virtual environment.
$ pip install -r requirements.txt   # Install dependencies.
```

And then publisher can be started as - 
```python
$ python publisher.py
```
and subscriber(s) can be started as - 
```python
$ python subscriber.py
```

# Features
- Traditional Publisher-Subscriber model.
- Publisher can specify TTL(Time-to-live) while publishing a message to particular topic. So a message(with ttl = t secconds)
will expire after `t` seconds.
- A message is published on a topic(T) will be delivered to each subscriber of that topic(T) exactly once.
- If a subscriber goes down for a duration(D), then all the pending messages(with TTL > D) will be delivered to that subscriber once it comes back alive after duration(D).

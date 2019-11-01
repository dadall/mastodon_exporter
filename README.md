### Mastodon Exporter

#### Mastodon

[Mastodon](https://github.com/tootsuite/mastodon/) is a free, open-source social network server based on ActivityPub.

#### How does it work ?

You need python3 and pip

Two API endpoints are used :

* api/v1/instance
* api/v1/instance/activity

#### Docker usage

- Build 

```
docker build -t mastodon-exporter .
```

- Run 

```
docker run -d -e MASTODON_HOST="https://instance.url/" -p 9410:9410 mastodon-exporter
```

#### Standalone

Python3


```
pip3 install -r requirements.txt
```

Usage :

* Edit the instance_exporter to update the URL of you instance.
* Run it
* curl localhost:9410 to check if there are some metrics


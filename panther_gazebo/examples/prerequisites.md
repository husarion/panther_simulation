## docker && docker-compose

- `docker`: version 20.10.8

Installation:

```bash
sudo -E apt-get -y install apt-transport-https ca-certificates software-properties-common && \
curl -sL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - && \
arch=$(dpkg --print-architecture) && \
sudo -E add-apt-repository "deb [arch=${arch}] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" && \
sudo -E apt-get update && \
sudo -E apt-get -y install docker-ce
```

```bash
sudo systemctl daemon-reload
sudo systemctl restart docker
```

## docker-compose

- `docker-compose`: v1.27.0+ that supports `runtime: ... `. More info [here](https://docs.docker.com/compose/gpu-support/#use-of-service-runtime-property-from-compose-v23-format-legacy)

Based on [official guide](https://docs.docker.com/compose/install/):

1. Download `docker-compose` binary file

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

2. Make it executable

```bash
sudo chmod +x /usr/local/bin/docker-compose
```

3. Create a symbolic link

```bash
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```

## nvidia runtime

to install on ubuntu:

1. Add GPG key:

```bash
distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
   && curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add - \
   && curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
```

2. Update & install

```bash
sudo apt-get update
sudo apt-get install -y nvidia-docker2
sudo systemctl restart docker
```

3. Testing

```bash
sudo docker run --rm --gpus all nvidia/cuda:11.0-base nvidia-smi
```

4. Checking available runtimes:

```bash
$ docker info | grep 'Runtimes'
 Runtimes: io.containerd.runtime.v1.linux nvidia runc io.containerd.runc.v2
```
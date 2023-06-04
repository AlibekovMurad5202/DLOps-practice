FROM docker.io/continuumio/miniconda3

RUN apt-get update && \
    apt-get install python3 -y && \
    apt install python3-pip -y && \
    apt install python-is-python3 && \
    apt install git -y && \
    apt install curl -y && \
    apt-get install ffmpeg libsm6 libxext6 -y

RUN conda create -n yolo_env python=3.7 -y
SHELL ["conda", "run", "-n", "yolo_env", "/bin/bash", "-c"]
RUN conda install pytorch==1.7.0 torchvision==0.8.0 torchaudio==0.7.0 -c pytorch

RUN python -m venv DAMO-YOLO-env && \
    source DAMO-YOLO-env/bin/activate && \
    /DAMO-YOLO-env/bin/python -m pip install --upgrade pip && \
    git clone https://github.com/tinyvision/DAMO-YOLO.git && \
    /DAMO-YOLO-env/bin/pip install -r /DAMO-YOLO/requirements.txt && \
    /DAMO-YOLO-env/bin/pip install gdown urllib3 && \
    export PYTHONPATH=$PWD:$PYTHONPATH
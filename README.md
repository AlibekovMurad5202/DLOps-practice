# DAMO-YOLO Demo

Source of original project: [DAMO-YOLO](https://github.com/tinyvision/DAMO-YOLO.git)

PapersWithCode: [DAMO-YOLO: A Report on Real-Time Object Detection Design](https://paperswithcode.com/paper/damo-yolo-a-report-on-real-time-object)

> __NOTE__: If you don't have Docker, install it using [documentation](https://docs.docker.com/get-docker/)!
>
> __NOTE__: Available only for Windows and Linux!
>
> __NOTE__: If the inference of the model causes an error for you, it may be worth updating the paths in `download_model.py`!

## 1. Clone repo
```
git clone https://github.com/AlibekovMurad5202/DLOps-practice.git && cd DLOps-practice
```

## 2. Build docker image
```
docker build -t damoyolo .
```

## 3. Run docker image
Ubuntu:
```
docker run -it -v "$(pwd)":/DLOps damoyolo
```
Windows:
```
docker run -it -v <path_to_DLOps-practice>:/DLOps damoyolo
```
> Example (for Windows): `docker run -it -v "C:\Users\murad\Desktop\ITMM\tmp\DLOps-practice":/DLOps damoyolo`

## 4. Activate environment
```
conda activate yolo_env && source DAMO-YOLO-env/bin/activate
```

## 5. Download pretrained model and reference data from Google Drive
```
cd DLOps && python3 download_model.py -m "damoyolo_tinynasL25_S.pth"
```

## 6. Prepare and run inference and test
```
sed -i -e 's/\r$//' run.sh
chmod +x run.sh
./run.sh
```

## 7. Close docker
```
exit
docker ps -a
docker stop CONTAINER_ID
docker rm CONTAINER_ID
```

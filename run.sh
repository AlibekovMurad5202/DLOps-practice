#!/bin/bash

export PYTHONPATH=$PWD:$PYTHONPATH

cd ../DAMO-YOLO

python3 tools/demo.py \
    -f ./configs/damoyolo_tinynasL25_S.py \
    --engine ../DLOps/pretrained_models/damoyolo_tinynasL25_S.pth \
    --output_dir ../DLOps/result_images \
    --conf 0.6 \
    --infer_size 576 768 \
    --device cpu \
    --path ../DLOps/original_images/dog.jpg \
    image

python3 ../DLOps/test.py
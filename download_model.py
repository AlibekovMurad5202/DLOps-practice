import os
import urllib3
import argparse
import logging as log
import sys

from gdown import download as drive_download

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

MODELS_DIR_NAME = 'pretrained_models'
DATA_DIR_NAME = 'reference_images'

google_drive_ids = {
    "damoyolo_tinynasL20_T_418.pth" : {
        'model' : "1-9NzCRKJZs3ea_n35seEYSpq3M_RkhcT",
        'data' : ""
    },
    "damoyolo_tinynasL20_T.pth" : {
        'model' : "1-6fBf_oe9vITSTYgQkaYklL94REz2zCh",
        'data' : ""
    },
    "damoyolo_tinynasL25_S_456.pth" : {
        'model' : "1-0GV1lxUS6bLHTOs7aNojsItgjDT6rK8",
        'data' : ""
    },
    "damoyolo_tinynasL25_S.pth" : {
        'model' : "1cTFgzOWaRGPfoGj3Z1MKsK4rZvYkmNw_",
        'data' : "1RMCMg2A6Ei-tWjB6lsXhg0JPY6RvPMtQ"
    },
    "damoyolo_tinynasL35_M_487.pth" : {
        'model' : "1-RMevyb9nwpDBeTPttiV_iwfsiW_M9ST",
        'data' : ""
    },
    "damoyolo_tinynasL35_M.pth" : {
        'model' : "1-RoKaO7U9U1UrweJb7c4Hs_S_qKFDExc",
        'data' : ""
    }
}

def cli_argument_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('-m', '--model',
                        help='Name of pretrained model.',
                        choices=[
                            'damoyolo_tinynasL20_T_418.pth',
                            'damoyolo_tinynasL20_T.pth',
                            'damoyolo_tinynasL25_S_456.pth',
                            'damoyolo_tinynasL25_S.pth',
                            'damoyolo_tinynasL35_M_487.pth',
                            'damoyolo_tinynasL35_M.pth',
                        ],
                        type=str,
                        dest='model',
                        required=False)

    args = parser.parse_args()

    return args


def download_pretrained_model(log, file=''):
    if not os.path.isdir(MODELS_DIR_NAME):
        os.mkdir(MODELS_DIR_NAME)

    if not os.path.isdir(DATA_DIR_NAME):
        os.mkdir(DATA_DIR_NAME)

    model_id = google_drive_ids[file]['model']
    model = os.path.join(MODELS_DIR_NAME, file)
    if not os.path.exists(model):
        drive_download(id=model_id, output=model, quiet=False, use_cookies=False, verify=False)
    else:
        log.info('Model {} already exist!'.format(model))

    data_id = google_drive_ids[file]['data']
    data = os.path.join(DATA_DIR_NAME, 'dog.jpg')
    if not os.path.exists(data):
        drive_download(id=data_id, output=data, quiet=False, use_cookies=False, verify=False)
    else:
        log.info('Image {} already exist!'.format(data))


if __name__=="__main__":
    log.basicConfig(
        format='[ %(levelname)s ] %(message)s',
        level=log.INFO,
        stream=sys.stdout,
    )

    args = cli_argument_parser()

    download_pretrained_model(log, args.model)

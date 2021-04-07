# Import libraries
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

# TACO Dataset Path
# C 드라이브 용량문제로 데이터셋을 현재 프로젝트 디렉토리가 아닌,
# 외장 SSD 파일에 저장하여 불러오는 방식을 채택
# 차후적으로 파일 경로를 상대 경로로 리팩토링해야 함
dataset_path = "E:/TACO/data"
anns_file_path = dataset_path + "/annotations.json"

# Read annotations
with open(anns_file_path, "r") as f:
    dataset = json.loads(f.read())

categories = dataset["categories"]
annotations = dataset["annotations"]
images = dataset["images"]
cnt_cats = len(categories)
cnt_anns = len(annotations)
cnt_imgs = len(images)
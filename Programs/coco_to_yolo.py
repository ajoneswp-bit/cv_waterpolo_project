from sahi.utils.coco import Coco

# init Coco object
coco = Coco.from_coco_dict_or_path("coco.json", image_dir="coco_images/")

# export converted YOLO formatted dataset into given output_dir with a 80% train/20% val split
coco.export_as_yolo(
  output_dir="output/folder/dir",
  train_split_rate=0.80
)
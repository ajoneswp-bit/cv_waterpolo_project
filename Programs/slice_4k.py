from sahi.slicing import slice_coco

slice_coco(
    coco_annotation_file_path=coco_annotation_file_path,
    image_dir=image_dir,
    slice_height=960,
    slice_width=1280,
    overlap_height_ratio=0.25,
    overlap_width_ratio=0.25,
)
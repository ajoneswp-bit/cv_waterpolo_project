import os

i = 0
frame_number = 1680
while i < 100:
	if i%5 !=0:
		os.rename(fr"C:\Users\ajayn\CV_Project\YOLO\Dataset\labels\frame_00{frame_number}.txt", fr"C:\Users\ajayn\CV_Project\YOLO\Dataset\labels\train\frame_00{frame_number}.txt")
	else:
		os.rename(fr"C:\Users\ajayn\CV_Project\YOLO\Dataset\labels\frame_00{frame_number}.txt", fr"C:\Users\ajayn\CV_Project\YOLO\Dataset\labels\val\frame_00{frame_number}.txt")
	i=i+1
	frame_number=frame_number + 10
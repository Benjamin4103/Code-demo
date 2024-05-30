from ultralytics import YOLO
import cv2

model = YOLO(" your location ") 
class_names = model.names
print(class_names)

results = model.predict(source='1',
                        show=True,
                        conf=0.55,
                        half=False,
                        save_crop=False,
                        stream=True)  # predict on an image
print(results)

# Initialize a counter for generating unique IDs
counter = 1

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    for result in results:
        frame = result.orig_img  # Get the frame from the results
        boxes = result.boxes 
        for box in boxes:
            # Check if the detection meets your criteria
            if box.cls == 1 and box.conf > 0.7:
                # Cropping the image using bounding box coordinates
                x_min, y_min, x_max, y_max = box.xyxy[0]
                cropped_image = frame[int(y_min):int(y_max), int(x_min):int(x_max)]
                
                # Saving the cropped image with a unique filename
                image_filename = f'your location'
                cv2.imwrite(image_filename, cropped_image)
                print(f'Saved cropped image as {image_filename}')
                
                # Increment the counter for the next image
                counter += 1
                

cv2.destroyAllWindows()  # Close all OpenCV windows

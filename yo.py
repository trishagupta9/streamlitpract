from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")


def detect_objects(image_path):

    # Run YOLO prediction
    results = model(image_path)

    # Save detected image
    output_path = "outputs/result.jpg"

    results[0].save(filename=output_path)

    return output_path
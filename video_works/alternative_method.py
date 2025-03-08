import cv2
import time

def compress_video_opencv(input_video, output_video, target_size=(640, 480), frame_rate=20, quality=80):
    """
    Compresses a video using OpenCV.

    Args:
        input_video: Path to the input video file.
        output_video: Path to the output video file.
        target_size: Target size for resized frames (width, height).
        frame_rate: Target frame rate.
        quality: Compression quality (0-100).

    Returns:
        None
    """

    # Open the input video
    cap = cv2.VideoCapture(input_video)

    # Get video parameters
    original_frame_rate = cap.get(cv2.CAP_PROP_FPS)
    original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Create a video writer
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video, fourcc, frame_rate, target_size)

    # Process frames
    start_time = time.time()
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    processed_frames = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Resize the frame
        frame = cv2.resize(frame, target_size)

        # Write the compressed frame to the output video
        out.write(frame)

        processed_frames += 1
        elapsed_time = time.time() - start_time
        remaining_time = (elapsed_time / processed_frames) * (total_frames - processed_frames)
        print(f"Processing frame {processed_frames}/{total_frames} (Estimated remaining time: {remaining_time:.2f} seconds)")

    # Release resources
    cap.release()
    out.release()

    print("Video compressed successfully!")

# Example usage
input_video = "/Users/santhiya/Documents/multimedia_mac/S23Ultra/20240114_215731.mp4"
output_video = "compressed_video.mp4"
target_size = (420, 360)
frame_rate = 20
quality = 50

compress_video_opencv(input_video, output_video, target_size, frame_rate, quality)

# Example usage
# input_video = "/Users/santhiya/Documents/multimedia_mac/S23Ultra/20240101_123419.mp4"

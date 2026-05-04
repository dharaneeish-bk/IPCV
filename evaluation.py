def evaluate_tracking(success_count, total_frames):
    accuracy = (success_count / total_frames) * 100
    print("\n--- Evaluation ---")
    print(f"Total Frames: {total_frames}")
    print(f"Successful Tracking: {success_count}")
    print(f"Tracking Accuracy: {accuracy:.2f}%")
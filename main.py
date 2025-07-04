import argparse

from modules.pipeline import VideoPipeline
from modules.shear.shear_processor import ShearProcessor
from modules.torque.torque_processor import TorqueProcessor


def main():
    parser = argparse.ArgumentParser(description="Run video shear analysis pipeline.")
    parser.add_argument(
        "--video-path",
        "-v",
        type=str,
        default="0",  # Webcam by default
        help='Path to input video file or "0" for webcam.',
    )
    parser.add_argument(
        "--output-dir",
        "-o",
        type=str,
        default="./output_videos",
        help="Directory to save the output visualizations.",
    )
    args = parser.parse_args()

    # Handle webcam input
    video_source = 0 if args.video_path == "0" else args.video_path

    # Create pipeline
    pipeline = VideoPipeline(video_source, args.output_dir)

    # Add shear processor
    shear_processor = ShearProcessor(
        name="shear_analysis", method="weighted", h_field=13, w_field=18
    )
    pipeline.add_processor(shear_processor)

    # Add template matching processor
    template_processor = TorqueProcessor(
        name="torque_analysis",
        templates_folder="./modules/torque/templates",
        threshold=1.0,
    )
    pipeline.add_processor(template_processor)

    # Run pipeline
    pipeline.run(show_display=True)


if __name__ == "__main__":
    main()

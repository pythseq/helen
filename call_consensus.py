import argparse
import sys
from modules.python.TextColor import TextColor
from modules.python.models.predict import predict
from modules.python.FileManager import FileManager
"""
The Call Consensus method generates base predictions for images generated through MarginPolish. This script reads
hdf5 files generated by MarginPolish and produces another Hdf5 file that holds all predictions. The generated hdf5 file
is given to stitch.py which then stitches the segments using an alignment which gives us a polished sequence.

The algorithm is described here:

  1) INPUTS:
    - directory path to the image files generated by MarginPolish
    - model path directing to a trained model
    - batch size for minibatch prediction
    - num workers for minibatch processing threads
    - output directory path to where the output hdf5 will be saved
    - gpu mode indicating if GPU will be used
  2) METHOD:
    - Call predict function that loads the neural network and generates base predictions and saves it into a hdf5 file
        - Loads the model
        - Iterates over the input images in minibatch
        - For each image uses a sliding window method to slide of the image sequence
        - Aggregate the predictions to get sequence prediction for the entire image sequence
        - Save all the predictions to a file
  3) OUTPUT:
    - A hdf5 file containing all the base predictions   
"""


def polish_genome(image_filepath, model_path, batch_size, num_workers, output_dir, gpu_mode):
    """
    This method provides an interface too call the predict method that generates the prediction hdf5 file
    :param image_filepath: Path to directory where all MarginPolish images are saved
    :param model_path: Path to a trained model
    :param batch_size: Batch size for minibatch processing
    :param num_workers: Number of workers for minibatch processing
    :param output_dir: Path to the output directory
    :param gpu_mode: If true, predict method will use GPU.
    :return:
    """
    # inform the output directory
    sys.stderr.write(TextColor.GREEN + "INFO: " + TextColor.END + "OUTPUT DIRECTORY: " + output_dir + "\n")

    # create a filename for the output file
    output_filename = output_dir + "helen_predictions.hdf"

    # call the predict method to generate the prediction hdf5 file
    predict(image_filepath, output_filename, model_path, batch_size, num_workers, gpu_mode)

    # notify the user that process has completed successfully
    sys.stderr.write(TextColor.GREEN + "INFO: " + TextColor.END + "PREDICTION GENERATED SUCCESSFULLY.\n")
    sys.stderr.write(TextColor.GREEN + "INFO: " + TextColor.END + "COMPILING PREDICTIONS TO CALL VARIANTS.\n")


if __name__ == '__main__':
    '''
    Processes arguments and performs tasks.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--image_file",
        type=str,
        required=True,
        help="HDF5 file containing all image segments for prediction."
    )
    parser.add_argument(
        "--model_path",
        type=str,
        required=True,
        help="Path to the trained model."
    )
    parser.add_argument(
        "--batch_size",
        type=int,
        required=False,
        default=100,
        help="Batch size for testing, default is 100."
    )
    parser.add_argument(
        "--num_workers",
        type=int,
        required=False,
        default=4,
        help="Batch size for testing, default is 100."
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        required=False,
        default='vcf_output',
        help="Output directory."
    )
    parser.add_argument(
        "--gpu_mode",
        type=bool,
        default=False,
        help="If true then cuda is on."
    )
    FLAGS, unparsed = parser.parse_known_args()
    FLAGS.output_dir = FileManager.handle_output_directory(FLAGS.output_dir)

    # call the interface method that handles this task
    polish_genome(FLAGS.image_file,
                  FLAGS.model_path,
                  FLAGS.batch_size,
                  FLAGS.num_workers,
                  FLAGS.output_dir,
                  FLAGS.gpu_mode)


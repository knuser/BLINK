import os
import sys
import argparse
import pickle
import gc


parser = argparse.ArgumentParser()

parser.add_argument(
    "--input", type=str, help="The full path to the file to process", required=True
)
parser.add_argument(
    "--output", type=str, help="The full path to the output file", required=True
)

args = parser.parse_args()


input_file_path = args.input
output_file_path = args.output

if not os.path.isfile(input_file_path):
    print("Input file `{}` doesn't exist!".format(output_file_path))
    sys.exit()

if os.path.isfile(output_file_path):
    print("Output file `{}` already exists!".format(output_file_path))
    sys.exit()

input_partial_files = [input_file_path[:-1] + str(i + 1) for i in range(4)]
total_output = {}
for i, partial_file in enumerate(input_partial_files):
    print(f"Loading part {i}...")
    with open(partial_file, 'rb') as fb:
        total_output.update(pickle.load(fb))
        gc.collect()
    print("Done")

print("Saving final output")
with open(output_file_path, "wb") as f:
    pickle.dump(total_output, f, protocol=4)
# print('Portion of documents with improper xml: {:.2f}%'.format(docs_failed_xml*100/len(id_title2parsed_obj)))

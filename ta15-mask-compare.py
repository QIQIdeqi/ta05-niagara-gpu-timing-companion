"""Compare two RGB PNG foreground masks using a green-channel threshold."""

import argparse

from PIL import Image, ImageChops


def compare(reference, candidate, threshold):
    lookup = [255 if value > threshold else 0 for value in range(256)]
    with Image.open(reference) as ref, Image.open(candidate) as test:
        if ref.format != "PNG" or test.format != "PNG":
            raise ValueError("Both files must be PNG.")
        if ref.size != test.size:
            raise ValueError("Both images must have identical dimensions.")
        ref_mask = ref.convert("RGB").getchannel("G").point(lookup)
        test_mask = test.convert("RGB").getchannel("G").point(lookup)
        difference = ImageChops.difference(ref_mask, test_mask)
        return tuple(mask.histogram()[255] for mask in (ref_mask, test_mask, difference))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reference", help="Reference PNG for the same output frame")
    parser.add_argument("candidate", help="Candidate PNG for the same output frame")
    parser.add_argument("--threshold", type=int, default=30, help="Foreground requires G > threshold (default: 30)")
    args = parser.parse_args()
    if not 0 <= args.threshold <= 255:
        parser.error("threshold must be between 0 and 255")
    try:
        reference, candidate, differing = compare(args.reference, args.candidate, args.threshold)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    print(f"reference_foreground_pixels={reference}")
    print(f"candidate_foreground_pixels={candidate}")
    print(f"differing_mask_positions={differing}")


if __name__ == "__main__":
    main()

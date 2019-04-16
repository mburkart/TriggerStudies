
import logging
import argparse

from TauTriggerEfficiency import TauLegEfficiencies


def parse_args():
    parser = argparse.ArgumentParser(description="To be filled.")
    parser.add_argument("-w", "--working-points", type=str,
                        nargs="+", default=["all"],
                        choices=["all", "vloose", "loose", "medium",
                                 "tight", "vtight", "vvtight"],
                        help="The MVA tau Id working points the"
                             " efficiencies should be calculated for.")
    parser.add_argument("-i", "--input-file", type=str, required=True,
                        help="The input file containing the ntuples.")
    parser.add_argument("-o", "--output-file", type=str, default="output.root",
                        help="The output file. Defaults to %(default)s")
    parser.add_argument("-f", "--file-types", type=str, nargs="+",
                        choices=["DATA", "MC", "EMB"],
                        default=["DATA", "MC", "EMB"],
                        help="The sample types to be processed.")
    args = parser.parse_args()

    if "all" in args.working_points:
        args.working_points = ["vloose", "loose", "medium",
                               "tight", "vtight", "vvtight"]
    return args


def setup_logging(level=logging.WARNING):
    logging.basicConfig(level=level)


def main(args):
    wps = args.working_points
    triggers = ["MuTau", "ETau", "diTau"]
    filetypes = args.file_types

    eff = TauLegEfficiencies(
            args.output_file,
            args.input_file)
    for wp in wps:
        eff.add_wp(wp)
    for trg in triggers:
        eff.add_trigger_name(trg)
    for ft in filetypes:
        eff.add_filetype(ft)
    eff.create_efficiencies()
    return


if __name__ == "__main__":
    setup_logging(logging.INFO)
    args = parse_args()
    main(args)

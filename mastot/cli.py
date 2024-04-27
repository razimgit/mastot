from argparse import ArgumentParser, Namespace

from mastot.modification import modify
from mastot.transcription import transcribe


def main():
    parser = make_cmdline_parser()
    args = parser.parse_args()
    args.func(args)


def make_cmdline_parser() -> ArgumentParser:
    parser = ArgumentParser(description="Modify WAV audiofiles or recognize speech in such.\n\n")
    subparsers = parser.add_subparsers(dest="action", required=True, help="Available functions")

    modify_help_str = "Modify speed and volume"
    modify_subparser = subparsers.add_parser(
        "modify", description=modify_help_str, help=modify_help_str
    )
    modify_subparser.add_argument(
        "-s",
        "--speed",
        nargs="?",
        default=1,
        type=float,
        help='Speed multiplier like in YouTube. Default: 1. Doesn\'t support "time stretching" '
        "(changes duration but doesn't preserve pitch)",
    )
    modify_subparser.add_argument(
        "-v",
        "--volume",
        nargs="?",
        default=0,
        type=float,
        help="Volume change in decibels. Default: 0",
    )
    modify_subparser.add_argument(
        "-p",
        "--percent",
        action="store_true",
        help="If this argument is present, the resulting volume is %% of the original volume, "
        "similar to VLC's volume slider",
    )
    modify_subparser.set_defaults(func=call_modify_with_args)

    transcribe_help_str = "Transcribe English or Russian speech in an audiofile"
    transcribe_subparser = subparsers.add_parser(
        "transcribe", description=transcribe_help_str, help=transcribe_help_str
    )
    transcribe_subparser.add_argument(
        "-l",
        "--lang",
        default="en",
        choices=["en", "ru"],
        help="Language of speech in the audiofile. Default: en. Looks for a Vosk model "
        "in 'models/lang' directory",
    )
    transcribe_subparser.add_argument(
        "-m",
        "--model",
        help="Path to a directory of a Vosk model. 'lang' parameter is ignored if this is provided",
    )
    transcribe_subparser.set_defaults(func=call_transcribe_with_args)

    parser.add_argument("path", help="Path to a WAV audiofile")
    parser.add_argument(
        "output",
        help="Path to a resulting file. A modified audiofile or a transcription in JSON format",
    )

    return parser


def call_modify_with_args(args: Namespace):
    modify(args.path, args.output, args.speed, args.volume, args.percent)


def call_transcribe_with_args(args: Namespace):
    model = f"models/{args.lang}"
    if m := args.model:
        model = m

    transcribe(args.path, args.output, model)


if __name__ == "__main__":
    main()

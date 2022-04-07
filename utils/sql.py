def build_args(args: tuple) -> str:
    """build arg=$1, arg2=$2 from ("arg", "arg2",)"""
    args = [f"{arg}=${num}" for num, arg in enumerate(args, start=1)]
    return ", ".join(args)

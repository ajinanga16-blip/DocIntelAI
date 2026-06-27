import threading


def run_in_background(target, *args, **kwargs):
    """
    Run a function in a background thread.
    """

    thread = threading.Thread(
        target=target,
        args=args,
        kwargs=kwargs,
        daemon=True
    )

    thread.start()

    return thread
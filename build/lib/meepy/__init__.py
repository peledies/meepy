import inspect

class Meep:
    def morp(parent = None, expected = True, message = None):
        frame = inspect.currentframe().f_back
        info = inspect.getframeinfo(frame)

        text = "[Expected]" if expected else ""

        if message is not None:
            bracket = "*" * (len(message) + 4)
            print("\n{}\n* {} *\n{}\n".format(
                bracket,
                message,
                bracket
            ))

        print("***** MEEP MORP @ {} {}*****".format(
            info.lineno,
            text
        ))

        if parent is not None:
            print("{}.{}.{}:{}\n".format(
                parent.__class__.__module__,
                parent.__class__.__name__,
                info.function,
                info.lineno
            ))
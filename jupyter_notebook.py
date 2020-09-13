#!//usr/bin/env python3
from logging import getLogger

logger = getLogger(__name__)  # you can use other name

def jupyter_notebook(arglist):
    logger.info("epmt_notebook: %s", str(arglist))

    mode = None
    cmd_args = []
    all_args = arglist
    for index, arg in enumerate(all_args):
        if arg == "ipykernel_launcher":
            mode = "kernel"
            pass
        else:
            cmd_args.append(arg)

    if mode == "kernel":  # run iPython kernel with passed ops
        args = ["ipykernel_launcher"]
        args.extend(cmd_args)
        # This does not want argv[0]
        logger.info("ipython kernel argv: %s", str(args))
        # from IPython import start_ipython
        # start_ipython(argv=args)

        # Remove the CWD from sys.path while we load stuff.
        # This is added back by InteractiveShellApp.init_path()
        import sys
        if sys.path[0] == '':
            del sys.path[0]

        from ipykernel import kernelapp as app
        app.launch_new_instance()
    else:  # Run IPython Notebook with passed ops
        import sys
        from os.path import realpath
        from os import getcwd
        me = realpath(sys.argv[0])
        logger.debug("Using %s as binary", me)
        args = []
        args.extend(all_args)
        logger.info("notebook argv: %s", str(args))
        from notebook import notebookapp
        notebookapp.launch_new_instance(argv=args)
    return True

if __name__ == "__main__":
    import sys
    from logging import basicConfig, DEBUG

    basicConfig(level=DEBUG)
    jupyter_notebook(sys.argv[:-1])

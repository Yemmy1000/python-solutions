import gzip
import pickle


def export_pickle(filename, compress=False):
    fh = None
    try:
        if compress:
            fh = gzip.open(filename, "wb")
        else:
            fh = open(filename, "wb")
            pickle.dump(self, fh, pickle.HIGHEST_PROTOCOL)
        return True
    except (EnvironmentError, pickle.PicklingError) as err:
        print("{0}: export error: {1}".format(os.path.basename(sys.argv[0]), err))
        return False
    finally:
        if fh is not None:
            fh.close()

def main():
    fname = input("Enter file name: ")
    compr = int(input("Enter 1 - to compress and 0 - otherwise: "))
    export_pickle(fname, compr)

main()

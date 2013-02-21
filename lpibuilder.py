#!/usr/bin/env python

#########################################
#
#   lpibuilder.py:
#     Given a base path, search for 
#     an lpi file to build
#
#   author:
#     Matt Hulse <matt_hulse@mcafee.com>
#
#   date:
#     2013-02-21
#
#########################################

import argparse, glob, os


def contains_lpi(path):
    files = glob.glob(os.path.join(path,'*.lpi'))
    return len(files) > 0

def build_lpi(path):
    cmd = "lpibuild " + path
    print "running " + cmd
    os.system(cmd)

def find_lpi_path(currdir):
    if contains_lpi(currdir):
        return currdir
    else:
        if (currdir == '/'):
            return ''
        else:
            return find_lpi_path( os.path.split(os.path.abspath(currdir))[0] )

def main(currdir):
    lpi_path = find_lpi_path(currdir)

    if lpi_path:
        build_lpi(lpi_path) 


if __name__ == "__main__":
      ########################
    ##### Parse Arguments #####
     ########################
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="Base path to start from when looking for an lpi to build")
    args = parser.parse_args()

      #################
    ##### Run Main #####
     #################
    main(args.path)

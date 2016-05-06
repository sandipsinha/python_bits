import argparse
 
if __name__ == '__main__':
 
    parser = argparse.ArgumentParser( 'A test' )
    parser.add_argument( '--update',
                        action='store_true',
                        help='Something something something' )
 
    args = parser.parse_args()
 
    if args.update:
        print 'Found update argument.'
    else:
        print 'Did NOT find argument'

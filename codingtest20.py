# %load test_compress.py
from nose.tools import assert_equal

def compress(e):
    dictlist=[]
    for key, value in e.iteritems():
        temp =key+str(value)
        dictlist.append(temp)
        temp=' '
    return ''.join(sorted(dictlist))

def compress_string(string):
    # TODO: Implement me
    if string is None:
        return None
    if string > '' :
        b=[r.upper() for r in string if r != ' ']
        c=dict((letter,b.count(letter)) for letter in set(b))
        d=[vals for vals in c.values()]
        if max(d) <= 2:
            return string
        elif len(d) - (d.count(2) + d.count(1)) >= 0:
            return compress(c)
        else:
            return string
    else:
        return ''


class TestCompress(object):

    def test_compress(self, func):
        assert_equal(func(None), None)
        assert_equal(func(''), '')
        assert_equal(func('AABBCC'), 'AABBCC')
        assert_equal(func('AAABCCDDDD'), 'A3B1C2D4')
        print('Success: test_compress')


def main():
    test = TestCompress()
    test.test_compress(compress_string)


if __name__ == '__main__':
    main()

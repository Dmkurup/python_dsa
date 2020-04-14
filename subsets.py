
def subsets(inS):
    outS = []
    if len(inS) > 0:
        c = inS[0]
        for x in subsets(inS[1::]):
            outS.append(x + [c])
            outS.append(x)
        return outS
    else:
        outS.append([])
        return outS


def gen_subsets(inS):
    """use yield """
    if len(inS) > 0:
        head = inS[0]
        for tail in gen_subsets(inS[1:]):
            yield tail
            yield [head] + tail
    else:
        yield []

if __name__ == '__main__':
    inS = list('joey')
    # test function
    result = subsets(inS)
   # print(result)
    #print(len(result))
    # test generator
    #for s in gen_subsets(inS):
       # print(s)
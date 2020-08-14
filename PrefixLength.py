

def prefixLen(s):
	maxlen = len(s)
	lens = [maxlen]
	for i in xrange(maxlen - 1):
		j = i + 1
		k = 0
		l = 0
		while j < maxlen and s[j] == s[k]:
			j += 1
			k += 1
			l += 1
		lens.append(l)
	return lens

print prefixLen("defabdfedac")

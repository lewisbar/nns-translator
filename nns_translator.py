import re

def nns_translator():
	progression = input('Enter NNS progression:\n').replace('.', '')
	key = input('Enter key:\n').upper()
	rpre = r'-[1-7](?![x:])[\w\d]*(?!:)'
	rpost = r'[1-7]-(?![x:])[\w\d]*(?!:)'
	rno = r'[1-7](?![x:])[\w\d]*(?![:.])'
	r = '{}|{}|{}'.format(rpre, rpost, rno)
	nnums = re.findall(r, progression)
	
	chlist = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
	notelist = [1, 3, 5, 6, 8, 10, 12]
	
	for nnum in nnums:
		num_re = r'[1-7]'
		num = re.search(num_re, nnum).group()
		offset = chlist.index(key)
		indx = notelist[int(num)-1] + offset - 1
		if indx >= len(chlist):
			indx = indx - len(chlist)
			
		if re.search(r'\-', nnum):
			chord = re.sub(r'(-{})|{}-'.format(num, num), chlist[indx]+'m', nnum)
		else:
			chord = re.sub(num, chlist[indx], nnum, 1)
			
		progression = re.sub(r'(?<![\w-])'+nnum+r'(?![\w-])', chord, progression)
		
	print(progression + '\n')
	
	
if __name__ == '__main__':
	while True:
		nns_translator()

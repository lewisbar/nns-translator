import re
import pyperclip

def nns_translator():
	print('Enter NNS progression. Type "-" (hyphen) on a new line when you\'re done.\n')

	# Takes input lines until a line with only a hyphen occurs. That way, the user can paste multiline text.
	progression = '\n'.join(iter(input, '-')).replace('^', '')

	key = input('\nEnter key (in major):\n').upper()

    # Construct the regex to find nashville number units
	rpre = r'-[1-7](?![x:])\w*(?!:)'
	rpost = r'[1-7]-(?![x:])\w*(?!:)'
	rno = r'[1-7](?![x:])\w*(?!:)'
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
		
	print('---\nTranslation:\n{}\n'.format(progression))
	pyperclip.copy(progression)
	print('Translation copied to clipboard.')
	
	
if __name__ == '__main__':
	nns_translator()

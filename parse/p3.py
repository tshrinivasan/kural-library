#import sys
import simplejson
import json

#kural = sys.argv[1]
input = open('1.txt', "rt", encoding="utf-8").read()
#print infile
#chunk = input.read(4096)

#print( chunk)
#print infile.split('.')[0]

kural = input.split('.')[0].split()
number = kural[-8]
print(number)

kural_text = kural[-7] + " " + kural[-6] + " " + kural[-5] + " " + kural[-4] + "\n" + kural[-3] + " " + kural[-2] + " " + kural[-1]

print(kural_text) 

chapter_name = kural[2:-8]

print(' '.join(chapter_name))


parimel = input.split('பரிமேலழகர் உரை')[1].split('**')[0].strip()
print(parimel)


muva = input.split('மு.வரதராசனார் உரை')[1].split('**')[0].strip()
print(muva)


manakudavar = input.split('மணக்குடவர் உரை')[1].split('**')[0].strip()
print(manakudavar)





devaneyar = input.split('ஞா. தேவநேயப் பாவாணர்')[1].split('**')[0].strip()
print(devaneyar)


gupope = input.split('Rev. Dr. G.U.Pope Translations')[1].split('**')[0].strip()
print(gupope)


yogi =  input.split('Yogi Shuddhananda Translations')[1].split('**')[0].strip()
print(yogi)




kalaignar =  input.split('கலைஞர் உரை')[1].split('**')[0].strip()
print(kalaignar)





kural_dict={
'no':number,
'kural_text':kural_text,
'chapter_name':chapter_name,
'parimel':parimel,
'muva':muva,
'manakudavar':manakudavar,
'devaneyar':devaneyar,
'gupope':gupope,
'yogi':yogi,
'kalaignar':kalaignar
}

print(kural_dict)

#print(simplejson.dumps(kural_dict))
with open('data.json', 'wb') as fp:
	json.dump(kural_dict, fp,ensure_ascii=False,sort_keys = True, indent = 4,)



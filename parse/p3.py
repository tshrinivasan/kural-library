#import sys
import simplejson
import json

import os
from os.path import basename
for root, dirs, files in os.walk("../kurals"):
	for filename in files:
		if filename.endswith(".txt"):
			print( "../kurals/" +filename)
			base =  os.path.basename(filename)
			file_name_only= os.path.splitext(base)[0]
		                                       

			input = open("../kurals/"+filename, "rt", encoding="utf-8").read()


			kural = input.split('.')[0].split()
			number = kural[-8]
			print(number)

			kural_text = kural[-7] + " " + kural[-6] + " " + kural[-5] + " " + kural[-4] + "\n" + kural[-3] + " " + kural[-2] + " " + kural[-1]
		
			print(kural_text) 

			chapter_name = kural[2:-8]

			chapter_name = (' '.join(chapter_name))
			print(chapter_name)


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
			'01_no':number,
			'02_chapter_name':chapter_name,
			'03_kural_text':kural_text,
			'04_parimel':parimel,
			'05_muva':muva,
			'06_manakudavar':manakudavar,
			'07_devaneyar':devaneyar,
			'08_gupope':gupope,
			'09_yogi':yogi,
			'10_kalaignar':kalaignar
			}

			print(kural_dict)

	#print(simplejson.dumps(kural_dict))
			json_file = '%0*d' % (4, int(file_name_only) )
			with open(json_file +'.json', 'w') as fp:
				json.dump(kural_dict, fp,ensure_ascii=False,sort_keys=True,indent = 4,)


	#		kural_tet=open('kural.txt','w')
	#		kural_tet.write(number)
	#		kural_tet.write("\n\n")
		
	#		kural_tet.write(kural_text)
	#		kural_tet.write("\n\n")
		
	#		kural_tet.write(parimel)
	#		kural_tet.write("\n\n")

	#		kural_tet.write(manakudavar)
	#		kural_tet.write("\n\n")

	#		kural_tet.write(devaneyar)
	#		kural_tet.write("\n\n")


	#		kural_tet.write(gupope)
	#		kural_tet.write("\n\n")

	#		kural_tet.write(yogi)
	#		kural_tet.write("\n\n")

	#		kural_tet.write(kalaignar)
	#		kural_tet.write("\n\n")

	#		kural_tet.close()





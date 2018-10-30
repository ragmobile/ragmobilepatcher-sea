import json
import hashlib
import os
import sys

filesDir = "files"

originalFiles = []
patchedFiles = []

for filename in os.listdir(filesDir):
	if ".unity3d" in filename:
		obj = {}
		obj["file"] = filename
		obj["md5"] = hashlib.md5(open(filesDir+"/"+filename,'rb').read()).hexdigest() 
		if "patched" in filename:
			patchedFiles.append(obj)
		else:
			originalFiles.append(obj)    

patch = {}
original = {"original":originalFiles}
patched = {"patched":patchedFiles}
release = {"releases":[{"md5":"none"}]}


patch.update(original)
patch.update(patched)
patch.update(release)
patch["version"] = int(sys.argv[1])

print json.dumps(patch)    

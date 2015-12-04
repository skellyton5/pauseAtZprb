Skip to content
 

Search…
All gists
GitHub
New gist
@skellyton5
You don’t have any verified emails. We recommend verifying at least one email.
Email verification helps our support team verify ownership if you lose account access and allows you to receive all the notifications you ask for.
  Star 0
  Fork 0
  @MSURunnerMSURunner/adjustSpeedTemp
Created 3 years ago
Embed  
<script src="https://gist.github.com/MSURunner/4598137.js"></script>
  Download ZIP
 Code  Revisions 1
Raw  adjustSpeedTemp
#Name: Adjust Temp/Speed
#Info: Alter the speed and temp of the printer at a certain height
#Depend: GCode
#Type: postprocess
#Param: pauseLevel(float:5.0) Change height (mm)
#Param: newTemp(float:220) New Temp (*C)
#Param: oldSpeed(float:100) Old Speed (mm/s)
#Param: newSpeed(float:100) New Speed (mm/s)




import re

def getValue(line, key, default = None):
  if not key in line or (';' in line and line.find(key) > line.find(';')):
		return default
	subPart = line[line.find(key) + 1:]
	m = re.search('^[0-9]+\.?[0-9]*', subPart)
	if m == None:
		return default
	try:
		return float(m.group(0))
	except:
		return default

with open(filename, "r") as f:
	lines = f.readlines()

z = 0 
x = 0
y = 0
#Calculate the percentage change in speed
speedChange = 100 * (newSpeed)/(oldSpeed)

pauseState = 0
with open(filename, "w") as f:
	for line in lines:
		if getValue(line, 'G', None) == 1:
			newZ = getValue(line, 'Z', z)
			x = getValue(line, 'X', x)
			y = getValue(line, 'Y', y)
			if newZ != z:
				z = newZ
				if z < pauseLevel and pauseState == 0:
					pauseState = 1
				if z >= pauseLevel and pauseState == 1:
					pauseState = 2
					#Set new temp
					f.write("M104 S%f\n" % (newTemp))
					#Set new speed
					f.write("M220 S%f\n" % (speedChange))		
		f.write(line)
 @skellyton5
 Styling with Markdown is supported
Write Preview

Leave a comment
Attach files by dragging & dropping,  Choose Files selecting them, or pasting from the clipboard.
Comment
Status API Training Shop Blog About Pricing
© 2015 GitHub, Inc. Terms Privacy Security Contact Help

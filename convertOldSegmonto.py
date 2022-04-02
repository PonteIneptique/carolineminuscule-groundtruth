import re
import glob
import sys


Zone = {
	"Main": "MainZone",
	"DropCapital": "DropCapitalZone",
	"RunningTitle": "RunningTitleZone",
	"Margin": "MarginTextZone",
	"Numbering": "NumberingZone"
}
Line = {
	'Rubric': "RubricLine",
	'Default': "DefaultLine"
}
regex = re.compile(r'LABEL="(\w+)"(\s+)DESCRIPTION="([ \w]+)"')


def replace(match):
	label, space, desc = match.groups()
	if desc.startswith("block type"):
		desc = f"block type {Zone[label]}"
		label = Zone[label]
		#data.append(label)
	else:
		desc = f"line type {Line[label]}"
		label = Line[label]
	return f"""LABEL="{label}"{space}DESCRIPTION="{desc}\""""

for file in sys.argv[1:]:
	with open(file) as f:
		xml = f.read()

	xml = regex.sub(replace, xml)
	with open(file, "w") as f:
		f.write(xml)

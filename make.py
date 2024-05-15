import glob

contents_loc = "contents"
content_keyword = "CONTENT"
real_pages_loc = "docs" # github is only willing to 
# read either from the root of the git (inconvenient 
# for us) or from an internal folder specifically named "docs"

title_placeholder = "GETTITLE"
title_set_comment = "SETTITLE"

def get_title(contents):
	lines = contents.split("\n")
	l = next(l for l in lines if title_set_comment in l)
	t = l.split(f"{title_set_comment} ")[1]
	t = t.split(" -->")[0]
	return t


def fill_site():
	pages = glob.glob(f"{contents_loc}/*.html")

	with open("base.html","r") as f:
		base =f.read()
		
	for p in pages:
		with open(p,"r") as f:
			contents = f.read()
			new_contents = base.replace(content_keyword,contents)
			new_contents = new_contents.replace(title_placeholder,get_title(contents))
		with open(p.replace(contents_loc,real_pages_loc),"w") as f:
			f.write(new_contents)


if __name__ == "__main__":
	fill_site()
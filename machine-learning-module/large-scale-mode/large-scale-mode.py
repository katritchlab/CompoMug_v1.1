import os
path_to_descriptor_script = "CompoMug_descriptor.icm"
path_to_icm = "path_to_icm/icm64"
target = "./4eiy.pdb"
chain = "a"
ls_ri = list(range(60,62))
ls_aa = ["ala", "val", "gly", "met", "leu", "ile", "asn", "asp", "gln", "glu", "lys", "arg", "his", "cys", "pro", "ser", "thr", "trp", "tyr", "phe"]
ls = []
for ri in ls_ri:
	for aa in ls_aa:
		d = "compomug_descriptor_%s_%s_%s.txt" % (chain, aa, str(ri))
		cmd = " ".join([path_to_icm, path_to_descriptor_script, target, chain, aa, str(ri), d])
		os.system(cmd)
		if os.path.exists('./'+d): ls.append(d)
fl = open("compomug_list.txt", "w")
for i,d in enumerate(ls) : fl.write("%d,%s\n" % (i+1,d))
fl.close()
fd = open("compomug_descriptor.txt", "w")
for d in ls: fd.write(open(d, "r").readline().rstrip()+'\n')
fd.close()


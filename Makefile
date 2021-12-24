vXXX:
	make -C vXXX

v206:
	make -C v206

v308:
	make -C v308

v355:
	make -C v355	

v101:
	make -C v101

v203:
	make -C v203

v302:
	make -C v302

clean:
	make -C vXXX clean
	make -C v206 clean
	make -C v308 clean
	make -C v355 clean
	make -C v101 clean
	make -C v203 clean
	make -C v302 clean

.PHONY: clean vXXX clean v206 clean v308 clean v355 clean v101 clean v203 clean v302

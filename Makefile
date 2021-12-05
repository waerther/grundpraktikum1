vXXX:
	make -C vXXX

v206:
	make -C v206

v308:
	make -C v308

clean:
	make -C vXXX clean
	make -C v206 clean
	make -C v308 clean

.PHONY: clean vXXX clean v206 clean v308 

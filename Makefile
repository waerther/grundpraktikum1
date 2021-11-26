vXXX:
	make -C vXXX

v206:
	make -C v206
	make -C v206 clean

clean:
	make -C vXXX clean
	make -C v206 clean

.PHONY: clean vXXX clean v206

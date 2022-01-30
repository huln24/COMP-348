
compile-main:
	clang main.c aggregate.c -o build/main
	clang main1.c aggregate.c -o build/main1

run-main:
	./build/main
	./build/main1

bnr: compile-main run-main


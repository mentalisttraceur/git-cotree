default:
	# This Makefile is just for testing

clean:
	rm -rf __pycache__

test: clean
	pytest test.py

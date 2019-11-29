.PHONY: lua

help:           ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

clean:
	rm dist/*

release: clean  ## 更新服务
	python setup.py sdist
	twine upload dist/*

%:  ## cli命令
	env/bin/python3 "cli.py" $(MAKECMDGOALS)

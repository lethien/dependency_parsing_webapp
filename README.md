# Dependency Parsing Web Application
## Show-casing two dependency parsing models for Vietnamese language

This is the final project for Natural Language Processing course, Master program in Data Science, JVN Institute, 2021.

Professor: Dinh Dien - University of Science, Vietnam National University of HCM City

Students:  
- Le Thien Toan - JVN Institute, Vietnam National University of HCM City  
- Le Thi Thuy Trang - JVN Institute, Vietnam National University of HCM City

## The two models  

- SOTA: PhoNLP (https://github.com/VinAIResearch/PhoNLP)  
- Lightweight: VnCoreNLP (https://github.com/vncorenlp/VnCoreNLP)

## The Web Application

- Django framework  
- VueJs built into static files for Django Frontend  
- Bootstrap for styling  
- Vue Tree Chart for Dependency Tree graph (https://github.com/ssthouse/vue-tree-chart)

## Installation
  
- Python packages using `pip` as follows:  
	```
	pip install -r requirements.txt
	```

- Download and setup files for models with the following commands: 
	```
	python setup_models.py	
	```

- (Optional) Re-train jPTDP model:
	```
	cd jPTDP/jPTDP
	python jPTDP.py --dynet-seed 123456789 --dynet-mem 1000 --epochs 30 --lstmdims 128 --lstmlayers 2 --hidden 100 --wembedding 100 --cembedding 50 --pembedding 100  --outdir model/ --train data/train.txt --dev data/dev.txt
	cd ../..
	```

- Setup jPTDP:
	```
	cd jPTDP
	pip install .
	cd ..
	```

- Setup VueJs, install npm packages and build static files as follows:  
	```
	cd webapp/frontend_code
	npm install
	yarn serve
	Ctrl-C
	cd ../..
	```

- Setup Django:
	```
	cd webapp
	python manage.py makemigrations
	python manage.py collectstatic
	cd ..
	```

## Start the web application

```
cd webapp
python manage.py runserver
```

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

- (Optional if you want to make change in VueJs) Install npm packages and build static files as follows:  
	```
	cd webapp/frontend_code
	npm install
	yarn build
	cd ../..
	```

- Setup Django for the first time:
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

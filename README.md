
# myRisk: Communicating Breast Cancer Risk through Visual Paradigm

myRisk is a risk assessment tool that provides interactive risk visuals to enhance patient comprehension of risk to prepare patients with the knowledge needed to make informed clinical and lifestyle decisions.

## Installation Dependencies 

* Python version v2.7.9
* pip v6.1.1
* Django v1.8  
* node v0.12.2
* grunt-cli v0.1.13
* pillow v2.8.1
* pip install psycopg2  v2.2.6
* npm install bootstrap

## Getting Started

To use this program, it must be hosted on a Windows server (to run C# executable code).
* Make sure you have installed all dependencies above
* git clone https://github.com/myRisk/dynamicDNA
* Change lines 71-75 in dynamicDNA/settings.py to match your working directory
* In your working directory, enter the following code to run a local server:
```shell
python manage.py runserver
```
* Enter this link in a browser: http://127.0.0.1.8000/vizDNA/

## Bugs and Issues

Current code cannot handle user not selecting a value and just clicking "next" during risk assessment

## Copyright and License

Copyright 2014 Iron Summit Media Strategies, LLC. Code released under the [Apache 2.0](https://github.com/IronSummitMedia/startbootstrap-modern-business/blob/gh-pages/LICENSE) license.

## Credits
* Source code for the Gail Model used can be found at [National Cancer Institute](http://www.cancer.gov/bcrisktool/Default.aspx)
* Speedometer and timeline diagrams were generated through [AMCHARTS](http://www.amcharts.com/javascript-maps/)
* Home page world map data from [GLOBOCAN 2012: Estimated Cancer Incidence, Mortality and Prevalence Worldwide in 2012](http://globocan.iarc.fr/Default.aspx)

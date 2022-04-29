## Categories

### How to run project

1. Create virtual venv (using PyCharm or `virtualenv venv`)
2. Activate your virtualenv: `source venv/bin/activate`
3. Install pipenv: `pip install --user pipenv`
4. Install dependencies: `pip install`

### How to add library

1. Add library to `Pipfile`
2. Run `pipenv lock` and `pipenv install`

### The main idea

1. Finish with processing input.
   1. Automate adding `colours` and `measures`
   2. Fix problems with `hyphen` (It is not punctuation)
   3. Fix problem with some words like `DVD`, `USB`, `SSD`
   4. Integrate fuzzywuzzy and review results
2. Train ML model (`Classificator`) using data from cluster (step 1)
3. Create ML Pipline and Deploy it

### Resources:

1. Prepare data

   1. [Чистый AutoML для “грязных” данных: как и зачем автоматизировать предобработку таблиц в машинном обучении](https://habr.com/ru/company/ods/blog/657525/)
   2. [Как проверить данные во фрейме Pandas с помощью Pandera](https://habr.com/ru/company/skillfactory/blog/658473/)

2. Create Infrastructure
   1. [What is Production Machine Learning? There’s a gap!](https://medium.com/@adiwijaya25/what-is-production-machine-learning-theres-a-gap-896a639b840d)
   2. [Production Machine Learning — Clustering Case](https://puspitakaban.medium.com/production-machine-learning-clustering-case-39a5dae70159)
   3. [О хороших практиках построения инфраструктуры ML-моделей](https://habr.com/ru/company/kaspersky/blog/648371/?amp%3Butm_source=habrahabr&amp%3Butm_medium=rss%2F)

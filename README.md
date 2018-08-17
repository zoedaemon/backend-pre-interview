# Hedersgåva
Python software engineer pre-interview repository.

## Targets

  1. Provide an API for **client** to push data to this *server*
  2. The server need to **handle** a lot of data input in *10 seconds*
  3. The API should accept **XML** format only
  4. Format the data to **time based data structure** and store it into a **database**(any of your choice)
  5. Provide an API to let **client** fetch the reformatted data by time(**timestamps** or **datetime**)

### Requirements

 1. URLs
    * API to **receive** the data => POST -- `/data`
    * API to **display** the data => GET -- `/data/<id>`
 2. Request data format
 
```xml
<?xml version="1.0" encoding="UTF-8"?>
<root>
   <data>
      <element>
         <device>SGD-12344</device>
         <value>1234.266</value>
      </element>
      <element>
         <device>SGB-11233</device>
         <value>60</value>
      </element>
      <element>
         <device>SCC-525</device>
         <value>220</value>
      </element>
      <element>
         <device>SGC-1552</device>
         <value>5266.66</value>
      </element>
      <element>
         <device>SGB-11233</device>
         <value>440</value>
      </element>
      <element>
         <device>G3112</device>
         <value>32.266</value>
      </element>
      <element>
         <device>SGD-12344</device>
         <value>1234.266</value>
      </element>
   </data>
   <devices>
      <G3112>Temperature Sensor</G3112>
      <SCC-525>Voltage Meter</SCC-525>
      <SGB-11233>Current Meter</SGB-11233>
      <SGC-1552>Power Meter</SGC-1552>
      <SGD-12344>Power Meter</SGD-12344>
   </devices>
   <id>2314</id>
   <record_time>1008910273</record_time>
</root>
```

 3. Response data format
```json
[
    {
        "datetime": "2018-08-17T19:00:00+08:00",
        "value": 1274.034,
        "unit": "V"
    },
    {
        "datetime": "2018-08-17T19:00:10+08:00",
        "value": 25.253,
        "unit": "A"
    },
    {
        "datetime": "2018-08-17T19:00:20+08:00",
        "unit": "°C",
        "value": 14.0524,
    }
]
```

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need to install [pipenv] and [pyenv] before you start using this repo.

### Installing

First install the dependences via pipenv

```shell
pipenv install
```

![Installing dependences via pipenv][instal_via_pipenv]

If you want to install any dependence from PyPi, then you should run the following

```shell
pipenv install <package_name>
```

After you installed the packages, you can use this to active the virtual environment.

```shell
pipenv shell
```

## Running the tests

### Unit test

We use pytest as our unit test framework. Run the following command to do the test.

```shell
pipenv run pytest hedersgava
```

### Coding style tests

Please follow the PEP8 standard as your basic coding style. But use 100 as your line length. And run the following command to do code style test.

```shell
pipenv run pylint hedersgava/hedersgava
```

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Django REST framework](http://www.django-rest-framework.org/) - The web RESTful framework
* [Hypothesis](https://hypothesis.readthedocs.io/en/latest/) - Property based testing library
* [PyTest](https://docs.pytest.org/en/latest/) - Python unit test tools

## Authors

* **Linnovs** - *Initial work* - [linnovs47](https://github.com/linnvos47)
* **Andy** - *Initial work* - [EntrakAndyLam](https://github.com/EntrakAndyLam)

See also the list of [contributors](https://github.com/en-trak/backend-pre-interview/contributors) who participated in this project.

[pipenv]:https://docs.pipenv.org/
[pyenv]:https://github.com/pyenv/pyenv
[instal_via_pipenv]:images/install_via_pipenv.svg

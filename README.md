# IPC classifier for WIPO-alpha dataset

This is an exercise of classification of patent files from the WIPO-alpha dataset using a Naïve 
Bayes classifier to put in practice the concepts learned in the Data Mining course.

This project is a joint effort of:
* Eduardo
* Almanely
* Luis
* Francisco
* Mario

## Set up
It is recommended that you use `virtualenv` to manage an isolated and standarized development environment. 
1. You can install it with `sudo pip install virtualenv`. 
2. Then you should run `virtualenv <any name you want>` inside the project directory.
3. Type `source <any name you want>/bin/activate`. Your terminal prompt should change.
4. Now you can install required packages with `pip install -r requirements.txt`. Note that you no longer need `sudo` because the packages are installing in the project folder. Also note that if you name the virtual environment anything that's not "ipc-classifier", you should add that name to `.gitignore`, but "ipc-classifier" is encouraged.
5. Run `python` and then

```python
import nltk
nltk.download()
```
	
You will see a window pop up then go to the corpora tab and look for `stopwords`, download it.

During development, if you need a package that isn't listed in `requirements.txt`, you should install it with `pip install <package>` and then run `pip freeze > requirements.txt` so the other team members can install `<package>` easily when they fetch your changes from the repo.

Tests should be run with `nosetests` from the terminal in the root directory.

## Guidelines
The structure of the project is borrowed from [The Hitchhiker's Guide to Python](http://python-guide-pt-br.readthedocs.io/en/latest/writing/structure/) based on [Kenneth Reitz's](https://github.com/kennethreitz/samplemod) recommendations.

The team should encourage the guidelines of [this](https://gist.github.com/sloria/7001839) python best practices guide.

To ensure maximum organization and integration within the project we chose to follow the [Github flow](https://guides.github.com/introduction/flow/) workflow.

Also it might be worth reading [this guide](https://chris.beams.io/posts/git-commit/) on how to write good commit messages.

## Tasks
These tasks were on the original specification of the problem and are sequential, but are here in the form of a checklist for the team reference.

- [ ] Parse the XML patent documents in order to extract the patent number, the IPC codes and the relevant parts of each patent (title and abstract).
- [ ] Extract the individual words from the plain text of the documents in the training set, in order to build a vocabulary.
- [ ] Remove noisy words from the vocabulary (stop-words, very rare words, etc.) and apply stemming/lemmatization.
- [ ] Using the vocabulary, transform the complete dataset into a set of vectors using a tf-idf approach.
- [ ] Assign to each vector its corresponding section and class using the IPC codes.
- [ ] Train a classification system for the section level.
- [ ] Train a classification system for the class level.
- [ ] Test the classification system at the section level and choose a set of section-level categories. Test the classification system at the class level **only with the sections that were selected previously**.

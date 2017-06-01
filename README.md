# IPC classifier for WIPO-alpha dataset

This is an exercise of classification of patent files from the WIPO-alpha dataset using a Naïve 
Bayes classifier to put in practice the concepts learned in the Data Mining course.

This project is a joint effort of:
* Eduardo
* Almanely
* Luis
* Francisco
* Mario

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

The structure of the project is borrowed from [The Hitchhiker's Guide to Python](http://python-guide-pt-br.readthedocs.io/en/latest/writing/structure/) based on [Kenneth Reitz's](https://github.com/kennethreitz/samplemod) recommendations.

The team should encourage the guidelines of [this](https://gist.github.com/sloria/7001839) best practices guide.

To ensure maximum organization and integration within the project we chose to follow the [Github flow](https://guides.github.com/introduction/flow/) workflow.

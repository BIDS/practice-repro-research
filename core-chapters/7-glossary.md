Glossary
========

Ariel Rokem and Fernando Chirigati
----------------------------------

Like other technical areas, the topic of computational reproducibility has its own terminology and jargon. The terms range from key concepts of the field, that are important when defining the parameters of reproducible research, to specific techniques and practices that are used in upholding computational reproducibility. Finally, there is a plethora of technical tools and practices that are mentioned througout this book. In this chapter, we provide some important definitions to help clarify the terms, techniques, and tools that are mentioned throughout the case studies and the other chapters.

### Key Concepts

#### Scientific Experiment

A **scientific experiment**, or simply **experiment**, is a procedure carried out to validate or refute a hypothesis. In our modern times, many stages in a research project are done partially or entirely through the use of computer programs and processes, and that involve digital data that is consumed (**input data**) and produced (**output data**). This may include studies in which the experiments themselves are computational in nature. In this case, the experiment is often modelled as a **pipeline** (or **dataflow**): a sequence of *steps* that are connected by the flow of data, where the output data of a step is used as input data for the following step. A step can be represented by a computer program or a sequence of programs (a sub-pipeline), and it transforms the data it consumes as part of the procedure.

#### Reproducibility

**Reproducibility** is a cornerstone of science. Definitions vary greatly across scientific disciplines, but the meaning that we find most prevalent is the 'calculation of quantitative scientific results by independent scientists using the original datasets and methods' (Stodden, Leisch, & Peng, 2014). The goals of reproducibility go beyond duplicating someone else’s investigation: it also entails having reproducibility for yourself, defeating self-deception in scientific results (Ioannidis, 2005; Nuzzo, 2015), and extending another researcher’s methods to build your own work. Reproducibility is a matter of degree, not of kind. We say that research is reproducible if reproducibility applies to the results to some extent. That is, some of the corresponding experiments and scientific methods are deemed to be reproducible.

##### Empirical and Computational Reproducibility

We can define different types of reproducible research as follows, adapted from Stodden (2014): empirical reproducibility, and computational reproducibility.

**Empirical reproducibility** entails communicating the procedure, protocols, equipment, and observations related to the experiment, but does not require making the computational assets (code and data) used during the research publicly available. This is often a minimal standard in science: published manuscripts contain descriptions and static figures and plots, and scientists need to follow these in hopes of building upon past research.

In **computational reproducibility**, in addition to the published manuscripts, the computational assets used to test all the hypothesis and derive the results are made available, which allows the computational processes to be reproduced verbatim and, in some cases, re-used. These assets may include, but are not limited to: the input data, either in extension (raw data) or in intension (a script that generates the data); the software (in binary or in source code); and the computational environment (computational dependencies and operating system information).

The notions of **verification** and **validation** are also commonly used when referring to reproducibility (Stodden et al., 2013): verification is concerned with the code solving the problem it claims to solve, while validation is concerned with the results being consistent with observations of the phenomenon being studied. In this sense, empirical reproducibility helps in the validation process, whereas computational reproducibility helps in the verification process, since the experiment execution can be investigated in more details.

With respect to the verification process, computational reproducibility helps identify if the code is not broken, and also pinpoint any statistical issues that may invalidate the results. For instance, *p-hacking* is a common bias in science where researchers select data or statistical analyses until non-significant results become significant. By having the data and all the artifacts, including the full chain of research events, one could tweak the different variables and vary the original analysis to detect how robust and significant the claims are.

##### Reproducibility Modes

Reproducibility can also be defined with respect to how results can be reproduced. Some of the terms often used in this regard are replicability, approximate reproducibility, and modular reproducibility.

Like reproducibility, there are conflicting definitions of **replicability** across different scientific domains. In some areas of science this is a synonym for **exact reproducibility**: the reproduced results are exact the same (meaning the exact same numbers) as the ones presented and discussed in the corresponding published manuscript. The computational assets, such as software, configuration parameters, and hardware, must be ideally the same to ensure replicability. Replicability guarantees reproducibility, but not the converse (Leek & Peng, 2015). In other areas, replicability can refer to a prior study being duplicated using the same procedures but with new data (Stodden et al., 2014).

**Approximate reproducibility** is related to having results that are similar to (and not the same as) the ones produced in the original experiment run. This often includes varying configuration parameters and input files to better verify how robust the experiment is, and perhaps simulating some steps that are harder to replicate. For example, an experiment that involves parallel and distributed computation may depend on the availability of massive serves for its replication; these steps can then be simulated or conducted at smaller scale to make its reproducibility feasible (Hunold & Träff, 2013). Also, some experiments are intrinsically difficult to replicate, such as the ones that require non-deterministic steps (random number generation) and access to third-party servers (code that is on servers cannot be controlled by researchers). Note that the reproduced results need to be consistent to the original ones to allow others to validate the experiment.

When an experiment supports **modular reproducibility**, its different steps and components can be reproduced individually, i.e., the experiment does not need to be reproduced in its entirety. For instance, if a single binary is shared for the entire experiment, it may be hard to reproduce only some of its steps; however, if the source code is made available, researchers will have more flexibility to use the parts of the experiment they want/need. Modular reproducibility allows **reusability**: the experiment can be more easily re-used for other purposes, thus making it possible for others to modify and build upon the original work.

##### Reproducibility Coverage

Another important aspect in reproducibility is its **coverage** (Freire, Bonnet, & Shasha, 2012): some experiments may not be reproduced in its entirety, including the ones that rely on data derived by third-party Web services or special hardware, or that require non-deterministic computational processes. But such experiments can, sometimes, be partially reproduced. For instance, if an experiment uses data that is derived by special or proprietary hardware, the data derivation process may not be reproducible, but the downstream analyses that use these data may be reproduced by others if the original data is made available.

#### Provenance

As the volume of digital data increases and the complexity of computational processes that manipulate these data grows, it is becoming increasingly important to manage their **provenance**. The Oxford English Dictionary defines provenance as *the source or origin of an object; its history and pedigree; a record of the ultimate derivation and passage of an item through its various owners*. Provenance helps determine the value, accuracy, and authorship of an object.

**Computational provenance** enables data products derived by computational processes to be interpreted and understood (Freire, Koop, Santos, & Silva, 2008). By examining a sequence of steps that led to a result, it is possible to obtain insights into the chain of reasoning used in the production of this result; to verify that the steps were performed according to acceptable procedures; and to identify what the inputs to the experiment were and where they came from.

Provenance is a critical ingredient for reproducibility (Freire & Silva, 2012). Providing detailed information about the provenance of results of an experiment tells about both the data and the sequence of steps that generated the findings. Through this information, it is possible to detect the required components of the experiment, and this facilitates the task of making it reproducible. The availability of such provenance information not only makes it possible to replicate the findings, but it also makes it easier to re-use and extend a result (by changing inputs and modifying the sequence of steps); in other words, detailed provenance allows modular reproducibility.

Provenance can be **describable** or **executable**. Describable provenance entails having a full description of the experiment (textual description, or a graph detailing all the steps) that serves to communicate in detail the computational aspects that one need to know to reproduce each step. Executable provenance, on the other hand, entails having an executable asset that can be directly used to reproduce the experiment (a binary or a scientific workflow (Davidson & Freire, 2008)).

There are different **provenance components** that must be captured to ensure the reproducibility of an experiment (Chirigati, Shasha, & Freire, 2013):

-   ***Data*** entails the original input data used to execute the experiment, and the original output data to compare the raw results. Sharing the intermediate data (data produced by intermediate steps of the pipeline) may also be useful if some steps cannot be reproduced (see *coverage* in *Reproducibility*).

-   ***Process*** entails all the computational programs and scripts used to execute the experiment. As mentioned before, this can be done by sharing either the source code or the binaries, which influences reusability.

-   ***Environment*** entails all the assets belonging to the computational environment where the experiment was originally executed, which includes information about the operating system (e.g.: name and kernel version), hardware architecture (e.g.: 32 or 64 bits, number of computational nodes), and computational dependencies (e.g.: library and software packages on which the experiment depends to run). This component is important to allow an experiment to be portable to other computers, especially if they have different software and hardware systems.

### Techniques

#### Version Control

Version control is a set of practices and tools originally used in software development to track the versions of software. These tools monitor, track and store changes to files within a circumscribed part of the file system, often referred to as a **repository**. The first generation of these systems are referred to as **centralized version control** systems (these include the **Concurrent Versions System (CVS)** and **Subversion (SVN)**). These systems rely on the existence and setup of a centralized server that stores the history of the changes to the code. In contrast, **distributed version control** systems (such as **git**, and **Mercurial**) do not depend on the presence of a centralized server. The history is instead stored together with the files in each user’s computer. To facilitate collaboration and coordination of work on different users’ computers, centralized servers are nevertheless often used as a common point for ’push’ and ’pull’ operations that synchronize the history between repositories stored on different computers and to merge work that is concurrently done on different files, or different parts of the same files by different users. Centralized servers can be set up on websites, and such websites offer other features. For instance, they display and allow browsing of the files in a virtual file-system-like website, and they provide web pages that can be used to browse the files in the repository, without downloading them. In addition, these websites provide for collaboration and communication among users (such as **bug-trackers**, pages in which errors in the code, or “bugs”, can be reported and addressed). The use of version control tools in science has risen in recent years, with many large collaborative projects and institutions (e.g., CERN, LSST, and NCBI) using the services of websites such as **GitHub** to distribute and collaborate on software.

#### Literate Programming

Computer programs are read many more times than they are written (Wulf, 1977). Considering this fact, Knuth (Knuth, 1984) proposed that instead of focusing on computer programs as only a set of instructions to the computer, the focus of a computer program should be to explain what is (supposed to be) achieved through these instructions. This shift in focus implies a more thoughtful approach to descriptive details of the software, such as function and variable names, and a substantial focus on documentation. In a research context, computer programs are embedded within documents, such as scientific papers. This practice is also described as 'literate computing', 'literate statistical programming', 'literate data analysis', and 'literate statistical practice', in recognition of the adoption of literate programming methods from a software development context into a data analysis context. Several systems, such as **knitr** and **Jupyter** allow the writing of documents, including papers, with the code embedded or interleaved with the text.

#### Data Publication

Full access to the computational assets that led to previously reported results are essential for **computational reproducibility**. **Data publication** (also known as **"data sharing"**) refers specifically to public availability of the data that was used (as distinct from the software, for example). If the data is stored digitally, this can be done by sending the data to specific collaborators, by creating digital copies, or making files available over the Internet. It can be done by uploading the data to publicly available websites that either can be accessed unencumbered, or require agreement to certain terms and conditions of use. In some cases, data size also limits the possibility of data publication and it is more practical to send physical copies of the data (for example, the so-called “connectome in a box” (Poldrack & Gorgolewski, 2014), distributed by the NIH-funded Human Connectome Project, which is a hard-drive version of large collections of human MRI data). Other limitations may include restrictions due to participant privacy (the **HIPAA**, or Health Insurance Portability and Accountability Act, enacted into law in the United States in 1996, restricts the information that can be made public about participants in research data; other similar laws apply elsewhere). While data could be considered factual information that cannot be copyrighted, research data often undergoes several steps of transformation before it can be useful: it is collected, aggregated, and manipulated, using significant investment of time or resources. Thus, it could represent an original and creative expression of the source (or "raw") data and may be considered copyrightable intellectual property. For data sharing to achieve its goals of reproducibility, it is therefore important to consider and define appropriate conditions of license to potential users when sharing data.

#### Munging

Research data is often quite “messy”. This means that it is not immediately tractable to the standard statistical analysis without additional steps (Milliken, 2006).

**Data munging** (also known as **data cleaning**) refers to the application of transformations to the data to bring from a “messy” state to a “tidy” state (Wickham, 2014). This may include filtering operations (exclusion of certain observations that contain missing values), aggregation, and integration of data from different sources. According to some estimates, data munging is one of the principal activities of individuals conducting data analysis across different sectors, including research in both industry and academia (Dasu & Johnson, 2003; Lohr, 2014).

Figuratively, people speak collectively of these transformations and data “janitorial” work as data "munging". This word stems from either the English word "mung", which refers to a messy mixture of things (originally, a mixture of graines) (Oxford English Dictionary, 2016a), or the word "munge", referring to "eating greedily and noisily" (Oxford English Dictionary, 2016c) (possibly related to the word "munching"). More rarely, it also refers to wiping of a person’s nose (Oxford English Dictionary, 2016b), which could be a reference to the act of cleaning itself. Alternatively, this is derived from the acronym MUNG, meaning "mash until no good" (or recursively, "mung until no good"). To maintain reproducibility of these steps, **provenance tracking** must be used to maintain the transformations and intermediate states of the data.

#### Software Testing

There are several types of testing to be considered:

1.  ***Unit testing***: This type of testing focuses on the operations of individual parts of the software ("units"). One rule of thumb is that unit testing should not require disk input/output, or access to the network. Unit testing works best when coupled with modular software design. In scientific software, unit testing takes the form of verification of known results from a specific function.

2.  ***Integration testing***: This type of testing focuses on testing the combination of different parts of a system. For example, verifying that the outputs of one part of the system can be ingested as inputs by other parts of the system to produce reasonable results.

3.  ***Regression testing***: This type of testing focuses on testing that previous results of a computation are maintained over time. This is useful to assess parts of the software for which it is hard to write unit tests. For example, parts of the software that contain random number generation can be tested to not deviate from a prior stored result by more than a certain factor.

4.  ***End-to-end testing***: This type of testing verifies if the operations of an entire system, under realistic conditions, produce desired results. For example, an analysis pipeline that starts with raw experimental data (considered representative of the actual data that the system is designed to analyze) transforms and munges this data, and results in some statistical analysis. Testing an entire workflows is considered end-to-end testing (see also **continuous integration**, below).

#### Continuous Integration

In software development, **integration** refers to the steps taken at different stages of development to harmonize the operations of different parts of systems made up of small parts. The integration of new features into a software system can cause unexpected changes in its behavior. This is addressed by **software testing**: if the existing software has sufficient **test coverage** — that is, the tests exercise all the different parts of the software, and exercise a sufficiently broad range of scenarios: corner cases, handling of extreme and unusual values, etc. — then integration of a new piece of software would be evaluated against the expected behavior of the software. To make the process of integration easier, many advocate doing it *early and often* (Duvall, Matyas, & Glover, 2007). For integration testing to be **continuous**, automated systems can be configured to run the **test suite** of the software system (the full set of tests) each and every time a change to the software is introduced. Such publicly available systems include [**Travis**](https://travis-ci.com/) and [**CircleCI**](https://circleci.com/). These services integrate well with websites that provide version control repositories, such as GitHub or Bitbucket, where new contributions to the software from collaborators can be set to trigger a run of the test suite on a publicly accessible server. Continuous integration on a remote server also help make sure that the dependencies of the software are well-defined, and protects against problems that arise from changing these software dependencies by triggering a test-failure whenever these dependencies change.

#### Workflow Management

Many scientific projects rely on the execution of several steps of data processing, including data munging and different steps of data analysis. Workflow management systems help distribute and orchestrate the work that needs to be done on the computational resources that are available, but also helps in *tracking provenance* of the results, by storing details of the data, the process, and the executions that take place during the analysis (Davidson & Freire, 2008).

#### File Format Standards

Scientific data is saved in a myriad of file formats. A typical file format might include a **file header**, describing the layout of the data on disk, **metadata** associated with the data, and the data itself, often stored in binary format. In some cases (e.g., **CSV (or comma-separated value) files**), data will be stored as text. The danger of proliferation of file formats in scientific data lies in the need to build and maintain separate software tools to read, write and process all these data formats. This makes interoperability between different practitioners more difficult, and limits the value of data sharing, because access to the data in the files remains limited.

#### Licensing

In most countries in the world, creative work is protected by copyright laws. International conventions, and primarily the Berne Convention of 1886, protect the copyright of creators even across international borders for 50 years after the death of the creator. This means that copying and using the creative work is limited by conditions set by the creator, or another copyright holder. For example, in many cases musical recordings may not be copied and further distributed without the permission of the musician, or of the production company that has acquired the copyright from the musician. Facts about the universe that are discovered through research are not subject to copyright, but the collection, aggregation, analysis and interpretation of research data may be considered creative work, and could be protected by copyright laws. Thus, the consumption of research publications is governed by copyright law. Furthermore, even data sharing is often governed by copyright laws, because the compilation of data to be shared often requires a creative effort. Another case of resarch-relevant copyrighted products is software that is developed in the course of research. In all of these cases, if license terms are not explicitly specified, the work is considered to be protected as "all rights reserved". This means that no one but the creator of the work can use the work unencumbered. For software this means that copying and further distribution of the software is prohibited. Even running the software may be restricted. The exact selection of a license is beyond the scope of this section, but depends on your intentions and goals with regard to the software (Fogel, 2005; Hunter, 2004; Rosen & Einschlag, 2004).

#### Virtualization and Environment Isolation

Software often requires other software to run properly. The software and hardware elements that are required to properly run a program are known as the **software dependencies**. Because of differences in hardware and operating systems, and because of conflicting dependencies between different programs, the creation and maintenance of software environments that have all the dependencies for a software system is cumbersome, and may require substantial system administration expertise. Pre-configured software environments that include all of the dependencies, software, and sometimes also the data needed for an analysis can be provided through systems that present the user a virtual machine (or VM) that runs in an isolated manner. These systems for virtualization include **VirtualBox** and **Vagrant**.

These systems rely on the ability to store an entire virtual machine as a file that can be copied, and launched within other machine’s environment. In addition, some systems provide programmatic virtualization, and dependency management, through the creation of minimal virtual machines referred to as "containers". This includes the **Docker** system, which allows not only storing and publishing light-weight virtual machines, but also provenance tracking and version control of containers. Conflicting software dependencies can also be managed through systems that isolate a computational environment by setting the parts of the file system that are visible, including the parts of the file system into which versions of dependency libraries are installed. In Python environment, isolation can be achieved through the use of virtual environments such as **virtualenv** and **conda**.

### Tools

#### Programming Language and Related Tools

##### C/C++

C is one of the most widely used programming languages of all time. Designed to be a compiled language, C was used to re-implement the Unix operating system, and many high-level languages were implemented in C, including Python. C++ is an extension of C that provides support for object-oriented capabilities, and it has become one of the most widely used object-oriented languages, especially for large scale and high performance applications.

##### Go

[Go](https://golang.org/) is a compiled programming language developed at Google, mostly used in some of the Google’s production systems.

##### IPython

[IPython](http://ipython.org/), or Interactive Python (Pérez & Granger, 2007), is a command shell that allows interactive computing for Python, including tab completion, history (provenance capture), parallel computing tools, and support for interactive data visualization.

##### Java

[Java](https://www.java.com/) is a programming language that is compiled into Java bytecode and run on a Java Virtual Machine (JVM), which ensures that all implementations are interoperable in different environments.

##### JavaScript

[JavaScript](https://www.javascript.com/) is an interpreted programming language extensively used for World Wide Web content production, alongside HTML and CSS.

##### Jupyter

[Jupyter](http://jupyter.org/) is a Web application that allows users to create and share *notebooks*, documents that contain live and dynamic code. The Jupyter project evolved from the original IPython, generalizing the interactive environment from being Python-specific to supporting over 40 programming languages.

##### Python

[Python](https://www.python.org/) is a general-purpose interpreted programming language. While Python has a comprehensive standard library, [PyP](https://pypi.python.org/pypi) (the Python Package Index) allows users to search for and download a number of additional Python packages and libraries. Many of these packages are remarkably popular and widely used in different sciences, including:

-   [*NumPy*](http://www.numpy.org/): this library provides support for large, multi-dimensional arrays and matrices, as well as implements a plethora of high-level mathematical functions that operate on these arrays and matrices. NumPy also allows the definition of arbitrary data types, which facilitates the integration with other libraries and tools.

-   [*SciPy*](http://www.scipy.org/scipylib/index.html): this library builds on top of NumPy to provide many high-level and efficient numerical routines mainly for numerical integration and optimization.

-   [*matplotlib*](http://matplotlib.org/): this library provides 2D plotting procedures for Python.

-   [*scikit-learn*](http://scikit-learn.org/): this library provides support for a variety of machine learning algorithms, including classification, regression, clustering, dimensionality reduction, and model selection techniques. scikit-learn is built on top of NumPy, SciPy, and matplotlib.

-   [*scikit-image*](http://scikit-image.org/): this library provides support for a collection of image processing algorithms. Similar to scikit-learn, it is built on top of NumPy, SciPy, and matplotlib.

-   [*pandas*](http://pandas.pydata.org/): this library brings to Python many data analysis functionalities, including high-level data manipulation tasks (selecting, filtering, slicing, sorting, grouping, plotting, etc.)

-   [*MNE*](http://mne-tools.github.io/): this library includes a Python package for processing electroencephalography and magnetoencephalography data.

-   [*Nipype*](http://nipy.org/nipype/): this library provides a uniform interface for creating workflows that integrate a collection of neuroimaging software and applications.

##### R

[R](https://www.r-project.org/) is a widely used interpreted programming language for statistical computing, data analysis and visualization, with its popularity largely increasing in diverse scientific fields during the past few years (Tippmann, 2014). There is a large and vibrant community of scientists using and developing software in R, with over 8000 packages contributed to the [Comprehensive R Archive Network](https://cran.r-project.org/). These packages are free to download and extend the functionality of R by adding specialized statistical algorithms, visualization techniques and file handling methods. The following R packages are worth noticing:

-   [*knitr*](http://yihui.name/knitr/): this library provides support for dynamic report generation: R code can be evaluated on the fly to generate documents (PDF, HTML or MS Word files) that automatically include the results of the R analysis.

-   [*knitcitations*](https://github.com/cboettig/knitcitations): this library extends knitr by allowing users to add citations to the dynamic reports.

-   [*dplyr*](https://cran.rstudio.com/web/packages/dplyr/): this library includes high-level functions for data manipulation tasks that resemble database-like queries (selecting, filtering, and summarizing the data).

-   [*stringr*](https://cran.r-project.org/web/packages/stringr/index.html): this library provides tools for manipulating text, using regular expressions and character strings.

-   [*caret*](http://topepo.github.io/caret/index.html): this library provides an extensive suite of tools for training regression and classification models

-   [*ggplot2*](http://ggplot2.org/): this library provides data visualization procedures for R.

-   [*Rcpp*](http://www.rcpp.org/): this library enables R functions to call C++ code for high performance computing.

-   [*devtools*](https://cran.r-project.org/web/packages/devtools/index.html): this library includes functions to simplify the development of a new R package.

-   [*testthat*](https://cran.r-project.org/web/packages/testthat/index.html): this library includes functions to set up unit testing for the code.

##### RStudio

[RStudio](https://www.rstudio.com/) is an integrated development environment (IDE) for R that includes both desktop and web server versions. Its code editor provides syntax highlighting, tab-completion, indenting, and definitions. It includes a debugging console, breakpoints, an environment panel, history, tracebacks, and integrated R help and documentation. It supports 2d and 3d visualizations, data display, and data manipulation. Knitr, markdown, and git are deeply integrated into RStudio, enabling version controlled programming via R markdown documents.

##### Ruby

[Ruby](https://www.ruby-lang.org/) is an interpreted programming language commonly used in Web development, and its syntax is broadly similar to that of Python.

##### Scala

[Scala](http://www.scala-lang.org/) is a programming language intended to be compiled to Java bytecode and executed on a JVM. Java and Scala are interoperable in the sense that libraries from one language can be used inside the other language.

#### Documentation Generators

##### Doxygen

[Doxygen](http://www.stack.nl/~dimitri/doxygen/) is a tool that automatically generates documentation (in different formats) from annotated source code, supporting a number of different programming languages.

##### Read the Docs

[Rea](https://readthedocs.org/) is a hosting service for software documentation. The service facilitates the process of generating documentation for the different versions of the code, Read the Docs can be set up to automatically build the documentation whenever a new version of the code is generated.

##### Roxygen

[Roxygen](http://roxygen.org/) is a Doxygen-like system for R.

##### Sphinx

[Sphinx](http://sphinx-doc.org/) is a tool that can generate documentation in many different file formats.

##### Pandoc

[Pandoc](http://pandoc.org/) is a tool that can convert between many different file formats, including LaTeX, HTML, Microsoft Word documents, and Markdown files.

#### Version Control

##### Bitbucket

[Bitbucket](https://bitbucket.org/) is a repository hosting service for two distributed version control systems: git and [Mercurial](https://www.mercurial-scm.org/). Similar to GitHub, is provides a Web-based interface to facilitate the collaboration in a project.

##### Git

[Git](https://git-scm.com/) is a distributed version control system that has become [widely used](https://ianskerrett.wordpress.com/2014/06/23/eclipse-community-survey-2014-results/) in the past few years.

##### GitHub

[GitHub](http://github.com/) is a git repository hosting service: developers maintain their git repositories on the Web. It provides a Web-based interface, as well as a desktop application, to facilitate the collaboration with other people in the same project. GitHub has numerous features, including, among others, forking, issue tracking, pull requests, and wikis.

##### SVN

[Subversion](https://subversion.apache.org/), or SVN, is a centralized version control system.

#### Data Munging and Analysis

##### Apache Hadoop

[Hadoop](https://hadoop.apache.org/) is a popular framework for distributed processing of large datasets across clusters of computers. Hadoop uses the map-reduce programming model for scaling up to multiple machines. Apache HDFS is the distributed file system used to store input, intermediate, and output data.

##### Apache Spark

[Spark](http://spark.apache.org/) is a framework for distributed processing that, in contrast to Hadoop, provides in-memory primitives that can achieve better performance for a number of applications.

##### Connectome Workbench

[The Connectome Workbench](http://www.humanconnectome.org/software/connectome-workbench.html) is a tool that provides multiple resources for mapping neuroimaging data.

##### MATLAB

[MATLAB](http://www.mathworks.com/products/matlab/) is a numerical computing environment and also a programming language widely popular for data and statistical analysis. It provides many useful features, especially for data management, matrix manipulation, and plotting.

##### Microsoft Excel

[Excel](https://products.office.com/en-us/excel) is a spreadsheet system developed by Microsoft that has many different features, including graphing tools and support for a macro programming language.

##### MongoDB

[MongoDB](https://www.mongodb.com/) is a database system that has been widely used recently, in particular for distributed stores. Instead of storing data in multiple relational structures—such as in traditional relational systems — MongoDB is document-oriented, it stores data in a minimal number of documents.

##### pandas

[panda](http://pandas.pydata.org/) is a Python library that has many data analysis functionalities, including high-level data manipulation tasks (selecting, filtering, slicing, sorting, grouping, plotting, etc).

##### SEPlib

[SEPlib](http://sepwww.stanford.edu/doku.php?id=sep:software:seplib) is a distributed software package for seismic data processing, including seismic processing routines, a graphics library, and a IO subroutine library.

##### Stata

[Stata](http://www.stata.com/) is a commercial data analysis and statistical analysis software.

#### Data Visualization

##### Adobe Photoshop

[Adobe Photoshop](http://www.adobe.com/products/photoshop.html) is a popular commercial graphics editor, providing a plethora of features to compose and manipulate graphics.

##### D3

[D3](http://d3js.org/) is a JavaScript library used for manipulating data and creating 2D interactive information and data visualizations.

##### ggplot2

[ggplot2](http://ggplot2.org/) is a data visualization library for R.

##### matplotlib

[matplotlib](http://matplotlib.org/) is a popular 2D plotting library for Python.

#### Workflow and Provenance Management

##### EUPS

[EUPS](https://github.com/RobertLuptonTheGood/eups) is a version management tools that tracks the exact project computational dependencies.

##### Make

[GNU Make](https://www.gnu.org/software/make/) and [CMake](https://cmake.org/) are tools commonly used to build and derive executable programs from source file. These utilities obtain the dataflow of how to build a program from files called *makefiles*.

##### VisTrails

[VisTrails](http://www.vistrails.org/) is an open-source scientific workflow system that provides support for simulations, data exploration, and visualization, while having many capabilities for provenance capture, management, and analytics.

#### Software Testing and Continuous Integration

##### BuildBot

[BuildBot](http://buildbot.net/) is a Python-based continuous integration tool that automates the process of building and testing software projects.

##### CircleCI

[CircleCI](https://circleci.com/) is a hosted continuous integration service for Web and mobile applications that, similar to Travis CI, can be used to automatically build and test projects hosted at GitHub.

##### Coveralls

[Coveralls](https://coveralls.io/) is a tool that automatically identifies the test coverage in a project, showing which parts of the code are not covered by the test suite.

##### devtools

[devtools](https://cran.r-project.org/web/packages/devtools/index.html) is a library that contains a series of functions to facilitate package development for R.

##### Google Test

[Google Test](https://github.com/google/googletest) is a unit testing library for C++ developed and used by Google.

##### Jenkins

[Jenkins](https://jenkins-ci.org/) is a Java-based continuous integration tool that automates the process of building and testing software projects.

##### JIRA

[JIRA](https://www.atlassian.com/software/jira) is a commercial software for bug tracking, issue tracking, and project management.

##### Nose

[nos](https://nose.readthedocs.org/) is a Python library that implements functions to assist in writing and running software tests.

##### nose2

[nose2](https://nose2.readthedocs.org/) — a successor to nose — is a unit testing library for Python.

##### testthat

[testtha](https://cran.r-project.org/web/packages/testthat/index.html) is a unit testing library for R.

##### Travis CI

[Travis CI](https://travis-ci.com/) is a hosted, distributed continuous integration service that can be used to automatically build and test projects hosted at GitHub. If the service is configured, every new commit to the GitHub repository triggers Travis CI, which tries to build the project and run tests. Travis CI is available for a number of different languages.

#### Virtualization and Environment Isolation

##### Amazon EC2

[Amazon EC2](https://aws.amazon.com/ec2/) is a Web service that provides compute infrastructure in the cloud. Virtual environments can be created, launched, and terminated as needed, and users pay by the hour for active servers.

##### Docker

[Docker](https://www.docker.com/) is a tool that automates the deployment of applications inside software containers, which are much lighter than virtual machines: containers are isolated but share the operating system, and, when appropriate, binaries and libraries as well. [boot2docker](http://boot2docker.io) is a Linux distribution made specifically to run Docker containers.

##### Vagrant

[Vagrant](https://www.vagrantup.com/) is a tool used to create and configure virtual environments, such as virtual machines and Docker containers.

##### Virtualenv

[Virtualenv](https://virtualenv.readthedocs.org/) is a tool that creates isolated Python environments. This allows multiple Python projects that have different (and sometimes conflicting) dependencies to coexist in the same computer.

#### Data Sharing and Repositories

##### Amazon S3

[Amazon S3](https://aws.amazon.com/s3/) is a service for online file storage on the cloud. S3 has been widely used for Web hosting, image hosting, and storage for backup systems.

##### arXiv

[arXiv](http://arxiv.org/) is a repository of electronic preprints of scientific publications, and is widely used in the fields of mathematics and physics.

##### CrossRef

[CrossRef](http://www.crossref.org/) is an official Digital Object Identifier (DOI) Registration Agency. A DOI is often assigned to a publication or research data so that it can be uniquely identified, and therefore, citable. Services like Dataverse and figshare automatically generate DOI’s for data that is uploaded to their systems.

##### Dataverse

[The Dataverse Project](http://dataverse.org/) is a repository for sharing, citing, and archiving research data. It offers support for backups, recovery, data discovery and cataloging, metadata extraction, and preservation.

##### Docker Hub

[Docker Hub](https://hub.docker.com/) is a service for building and shipping Docker containers. Docker Hub allows integration with GitHub and BitBucket, as well as collaboration between different users, among other features.

##### Dropbox

[Dropbox](https://www.dropbox.com/) is a service that hosts files on the Web as well as synchronizes files across different platforms. Dropbox also has file versioning features, where users may revisit old versions of their files without losing any work.

##### figshare

[figshare](https://figshare.com/) is a repository for sharing and citing research data (results and manuscripts).

##### Flickr

[Flickr](https://www.flickr.com/) is a service to host and share images and videos on the Web. It is widely popular among photo researchers and bloggers.

##### Mendeley and Zotero

[Mendeley](https://www.mendeley.com/) and [Zoter](https://www.zotero.org/) are both Web services and desktop applications for managing and sharing research publications.

##### NeuroVault

[NeuroVault](http://neurovault.org/) is a repository for sharing statistical maps, parcellations, and atlases of the human brain.

##### Zenodo

[Zenodo](https://zenodo.org/) is a repository for sharing and citing research results, including data and publications.

#### Document Authoring

##### LaTeX

[LaTeX](https://www.latex-project.org/) is a word processor and a document markup language commonly used for writing research publications. In contrast with Microsoft Word, LaTeX is not a WYSIWYG editor: the document needs to be compiled to generate the finished product.

##### Microsoft Word

[Word](https://products.office.com/en/word) is a document and word processing software developed by Microsoft. Microsoft Word is a WYSIWYG editor, while editing, the content onscreen appears in a form that is similar to its appearance as a finished product (WYSIWYG stands for “What You See Is What You Get”).

##### Overleaf

[Overleaf](https://www.overleaf.com/) is an online platform for collaborative writing and publishing using LaTeX, with an integrated real-time preview that closely resembles a WYSIWYG editor.

#### File Formats

##### API

An API (or application programming interface) are elements of the design of a software system that that allows programmers to use the system to build applications out of it. For example, a software library API will be the design of functions and objects in the library that can be combined together to create new functions and objects.

##### CSV

The CSV (“Comma Separated Values”) file format stores data in a tabular fashion in plain text. This format is often used to transfer data between applications.

##### DO

A DO file is a Web-base Java program that is run by a Web server.

##### Dockerfile

A Dockerfile is a file that has a set of instructions and commands for building a Docker container.

##### FIF

A FIF (“Fractal Image File”) file stores images in fractals, which can be resized without losing image quality.

##### HDF5

The HDF5 file format is designed to store and organize large amounts of data. Different data models can be specified for storing data, including multidimensional arrays and tables.

##### ipynb

An ipynb file represents an IPython notebook document.

##### JSON

JSON is a data-interchange format that is both human- and machine-readable, storing and transmitting data as attribute-value pairs. It has been widely used recently, largely replacing XML.

##### Markdown

A Markdown file contains data in a simple markup language that facilitates the conversion from plain text to HTML and other formats. Common extensions for this file include *md* and *Rmd* (the latter represents an R Markdown file where R code is included among the text).

##### netCDF

The netCDF ("network common data format") file format is machine-independent format commonly used for sharing array-oriented scientific data.

##### PDF

The PDF (“Portable Document Format”) file format is commonly used to display documents in an interoperable manner.

##### RAID

RAID (redundant array of independent disks) is a system that confers robustness to data storage through redundancy across sub-partitions. Every bit of data is stored in at least two different partitions, such that if any given partition fails, it can be swapped out without incurring data loss.

##### SQL

A SQL (“Structured Query Language”) file contains a series of database queries to analyze and manage tables in a database. These queries are represented by statements written in SQL, a programming language designed for managing data in relational databases systems.

##### SVG

The SVG (“Scalable Vector Graphics”) file represents graphics using an XML-based format that offers support for interactivity and animation.

##### VT

A VT file stores a VisTrails workflow and its corresponding provenance.

##### XML

An XML (“Extensible Markup Language”) file stores data in XML, which is a markup language that encodes documents in a format that is both human- and machine-readable. XML is known to provide interoperability among different applications.

### References

Chirigati, F., Shasha, D., & Freire, J. (2013). ReproZip: Using Provenance to Support Computational Reproducibility. In *Proceedings of the 5th uSENIX workshop on the theory and practice of provenance* (pp. 1:1–1:4).

Dasu, T., & Johnson, T. (2003). *Exploratory data mining and data cleaning*. John Wiley & Sons.

Davidson, S. B., & Freire, J. (2008). Provenance and Scientific Workflows: Challenges and Opportunities. In *Proceedings of the 2008 aCM sIGMOD international conference on management of data* (pp. 1345–1350).

Duvall, P. M., Matyas, S., & Glover, A. (2007). *Continuous integration: Improving software quality and reducing risk*. Pearson Education.

Fogel, K. (2005). *Producing open source software: How to run a successful free software project*. O’Reilly Media, Inc.

Freire, J., & Silva, C. T. (2012). Making Computations and Publications Reproducible with VisTrails. *Computing in Science Engineering*, *14*(4), 18–25.

Freire, J., Bonnet, P., & Shasha, D. (2012). Computational Reproducibility: State-of-the-art, Challenges, and Database Research Opportunities. In *Proceedings of the 2012 aCM sIGMOD international conference on management of data* (pp. 593–596).

Freire, J., Koop, D., Santos, E., & Silva, C. T. (2008). Provenance for Computational Tasks: A Survey. *Computing in Science and Engineering*, *10*(3), 11–21.

Hunold, S., & Träff, J. L. (2013). On the State and Importance of Reproducible Experimental Research in Parallel Computing. *CoRR*.

Hunter, J. (2004). Why we should be using BSD. Accessed: 2015-10-25. Retrieved from <http://nipy.org/nipy/faq/johns_bsd_pitch.html>

Ioannidis, J. P. A. (2005). Why Most Published Research Findings Are False. *PLoS Med*, *2*(8), e124. <http://doi.org/10.1371/journal.pmed.0020124>

Knuth, D. E. (1984). Literate programming. *The Computer Journal*, *27*(2), 97–111.

Leek, J. T., & Peng, R. D. (2015). Opinion: Reproducible research can still be wrong: Adopting a prevention approach. *Proceedings of the National Academy of Sciences*, *112*(6), 1645–1646. <http://doi.org/10.1073/pnas.1421412111>

Lohr, S. (2014, August 17). For big-data scientists, ’janitor work’ is key hurdle to insights. *New York Times*. Retrieved from <http://www.nytimes.com/2014/08/18/technology/for-big-data-scientists-hurdle-to-insights-is-janitor-work.html>

Milliken, G. (2006). Messy data. In S. Kotz (Ed.), *Encyclopedia of statistical science*. Hoboken, NJ: Wiley.

Nuzzo, R. (2015). How scientists fool themselves – and how they can stop. *Nature*, *526*(7572), 182–185.

Oxford English Dictionary. (2016a). Mung, n.1 and adj. Oxford University Press. Retrieved from <http://www.oed.com/view/Entry/113400>

Oxford English Dictionary. (2016b). Munge, v.1. Oxford University Press. Retrieved from <http://www.oed.com/view/Entry/123777?rskey=KZFDs3&amp;result=1>

Oxford English Dictionary. (2016c). Munge, v.2. Oxford University Press. Retrieved from <http://www.oed.com/view/Entry/252110?rskey=KZFDs3&amp;result=2>

Pérez, F., & Granger, B. E. (2007). IPython: A system for interactive scientific computing. *Computing in Science and Engineering*, *9*(3), 21–29. <http://doi.org/10.1109/MCSE.2007.53>

Poldrack, R. A., & Gorgolewski, K. J. (2014). Making big data open: Data sharing in neuroimaging. *Nat. Neurosci.*, *17*(11), 1510–1517.

Rosen, L., & Einschlag, M. (2004). *Open source licensing*. Prentice Hill.

Stodden, V. (2014). What Scientific Idea is Ready for Retirement? Reproducibility. *Edge.org*. Retrieved from <http://edge.org/response-detail/25340>

Stodden, V., Bailey, D. H., Borwein, J., LeVeque, R. J., Rider, B., & Stein, W. (2013). Setting the Default to Reproducible: Reproducibility in Computational and Experimental Mathematics. *ICERM Workshop Report*. Retrieved from <http://stodden.net/icerm_report.pdf>

Stodden, V., Leisch, F., & Peng, R. D. (2014). *Implementing reproducible research*. CRC Press.

Tippmann, S. (2014). Programming tools: Adventures with R. *Nature*, *517*(7532), 109–110. <http://doi.org/10.1038/517109a>

Wickham, H. (2014). Tidy data. *J. Stat. Softw.*, *59*(10).

Wulf, W. A. (1977). Some thoughts on the next generation of programming languages. *Perspectives on Computer Science*, 217–234.

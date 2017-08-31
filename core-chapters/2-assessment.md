Assessing Reproducibility
=========================

Ariel Rokem, Ben Marwick, and Valentina Staneva
-----------------------------------------------

While understanding the full complement of factors that contribute to reproducibility is important, it can also be hard to break down these factors into steps that can immediately be adopted into an existing research program and immediately improve its reproducibility. One of the first steps to take is to assess the current state of affairs, and to track improvement as steps are taken to increase reproducibility even more. This chapter provides a few key points for this assessment.

### What it means to make research reproducible

Although one of the objectives of this book is to discover how researchers are defining and implementing reproducibility for themselves, it is important at this point to briefly review some of the current scholarly discussion on what it means to strive for reproducible research. This is important because recent surveys and commentary have highlighted that there is confusion among scientists about the meaning of reproducibility (Baker, 2016b, 2016a). Furthermore, there is disagreement about how to define 'reproducible' and 'replicable' in different fields (Casadevall & Fang, 2010; Drummond, 2009; Easterbrook, 2014; Stodden, Borwein, & Bailey, 2013). For example, Goodman, Fanelli, & Ioannidis (2016) note that in epidemiology, computational biology, economics, and clinical trials, reproducibility is often defined as:

> the ability of a researcher to duplicate the results of a prior study using the same materials as were used by the original investigator. That is, a second researcher might use the same raw data to build the same analysis files and implement the same statistical analysis in an attempt to yield the same results.

This is distinct from replicability:

> which refers to the ability of a researcher to duplicate the results of a prior study if the same procedures are followed but new data are collected.

It is noteworthy that definitions above, which are broadly consistent with usage of these terms throughout this book, are totally opposite to the Association for Computing Machinery (ACM, the world's largest scientific computing society), which take their definitions from the International Vocabulary of Metrology. Here are the ACM definitions:

> Reproducibility (Different team, different experimental setup) The measurement can be obtained with stated precision by a different team, a different measuring system, in a different location on multiple trials. For computational experiments, this means that an independent group can obtain the same result using artifacts which they develop completely independently.
>
> Replicability (Different team, same experimental setup) The measurement can be obtained with stated precision by a different team using the same measurement procedure, the same measuring system, under the same operating conditions, in the same or a different location on multiple trials. For computational experiments, this means that an independent group can obtain the same result using the author’s own artifacts.

We can see the heritage of the definitions of the ACM in literature on physics and the philosophy of science (Cartwright, 1991; Collins, 1984; Franklin & Howson, 1984). In her paper on the epistemology of scientific experimentation, Cartwright (1991), presents one of the first clear definitions of the key terms: 'replicability - doing the same experiment again' and 'reproducibility - doing a new experiment'.

The definition of Cartwright is at odd with our preferred definition, from Goodman et al. (2016). This is because we trace a different ancestry in the use of the term 'reproducible', one that recognises the central role of the computer in scientific practice, with less emphasis on empirical experimentation as the primary means for generating knowledge. Among the first to write about reproducibility in this way is geophysicist Jon Claerbout. He pioneered the use of the phrase 'reproducible research' to describe how his seismology research group used computer files to enable efficient regeneration of the figures and tables in theses and publications (Claerbout & Karrenfach, n.d.). We can see this usage more recently in Stodden, Leisch, & Peng (2014):

> Replication, the practice of independently implementing scientific experiments to validate specific findings, is the cornerstone of discovering scientific truth. Related to replication is reproducibility, which is the calculation of quantitative scientific results by independent scientists using the original datasets and methods. Reproducibility can be thought of as a different standard of validity because it forgoes independent data collection and uses the methods and data collected by the original investigator. Reproducibility has become an important issue for more recent research due to advances in technology and the rapid spread of computational methods across the research landscape.

It is this way of thinking about reproducibility that captures most of the variation in the way the contributors to this book use the term. One of the key ideas that the remainder of this chapter explores is that reproducibility is a matter of degree, rather than kind. This means that identifying the factors that can relatively easily and quickly be changed can incrementally lead to an increase in the reproducibility of a research program. Identifying more challenging points, that would require more work, helps set long-term goals towards even more reproducible work, and helps identify practical changes that can be made over time.

Reproducibility can be assessed at several different levels: at the level of an individual project (e.g., a paper, an experiment, a method or a dataset), an individual researcher, a lab or research group, an institution, or even a research field. Slightly different kinds of criteria and points of assessment might apply to these different levels. For example, an institution upholds reproducibility practices if it institutes policies that reward researchers who conduct reproducible research. Meanwhile, a research field might be considered to have a higher level of reproducibility if it develops community-maintained resources that promote and enable reproducible research practices, such as data repositories, or common data-sharing standards.

This book focuses on the first of these levels, that of a specific research project. In this chapter we consider some of the ways that reproducibility can be assessed by researchers who might be curious about how they can improve their work. We have divided this assessment of reproducibility into three different broad aspects: automation and provenance tracking, availability of software and data, and open reporting of results. For each aspect we provide a set of questions to focus attention on key details where reproducibility can be enhanced. In some cases we provide specific suggestions about how the questions could be answered, where we think the suggestions might be useful across many fields.

The diversity of standards and tools relating to reproducible research is large and we cannot survey all the possible options in this chapter. We recommend that the researcher use the detailed case studies in following chapters for inspiration, tailoring choices to the norms and standards of your discipline.

### Automation and provenance tracking

Automation of the research process means that the main steps in the project: transformations of the data -- various processing steps and calculations -- as well as the visualization steps that lead to the important inferences, are encoded in software and documented in such a way that they can reliably and mechanically be replicated. In other words, the conclusions and illustrations that appear in the article are the result of a set of computational routines, or scripts that can be examined by others, and re-run to reproduce these results.

To assess the sufficiency of automation in a project, one might ask:

-   Can all figures/calculations that are important for the inference leading to the result be reproduced in a single button press? If not a single button press, can these be produced with a reasonably small effort? One way to achieve this goal is to write software scripts that embody every step in the analysis up to the creation of figures, and derivation of calculations. In assessment, you can ask: is it possible to point to the software script (or scripts) that generated every one of the calculations and data visualizations? Is it possible to run these scripts with reasonably minimal effort?

-   Another set of questions refers to the starting point of the calculations in the previous question: what is the starting point of running these scripts? What is required as set-up steps to the calculations in these scripts? If the setup includes manual processing of data, or cumbersome setup of a computational environment, this detracts from the reproducibility of the research.

The main question underlying these criteria is how difficult it would be for another researcher to first reproduce the results of a research project, and then further build upon these results. Because research is hard, and error is ubiquitous (a point made in this context by Donoho and colleagues (2008)), the first person to benefit from automation is often the researcher performing the original research, when hunting down and eliminating error.

Provenance tracking is very closely related to automation (see glossary for definitions). It entails that the full chain of computational events that occurred from the raw data to a conclusion is tracked and documented. In cases in which automation is implemented, provenance trackingcan be instantiated and executed with a reasonably minimal effort.

When large data sets and complex analysis are involved, some processing steps may consume more time and computational resources than can be reasonably required to be repeatedly executed. In these cases, some other form of provenance tracking may serve to bolster reproducibility, even in the absence of a fully automatic processing pipeline. Items for assessment here are:

-   If software was used in (pre)processing the data, is this software properly described? This includes documentation of the the version of the software that was used, and the settings of parameters that were used as inputs to this software.

-   If databases were queried, are the queries fully documented? Are dates of access recorded?

-   Are scripts for data cleaning included with the research materials, and do they include commentary to explain key decisions made about missing data and discarding data?

Another aspect of provenance tracking is the tracking of different versions of the software, and recording of the evolution of the software, including a clear delineation of the versions of the software that were used to support specific scientific findings. This can be assesessed by asking:

-   Is the evolution of the software available for inspection through a publicly accessible version control system? Are versions that contributed to particular findings clearly tagged in the version control history?

### Availability of software and data

The public availability of the data and software are key components of computational reproducibility. To facilitate its evaluation, we suggest that researchers consider the following series of questions.

#### Availability of data

-   Are the data available through an openly accessible database? Often data is shared through the internet. Here, we might ask about the long-term reliability of the web address: are the URLs mentioned in a manuscript permanently and reliably assigned to the dataset? One example of a persistent URL is a Digital Object Identifier (DOI). Several major repositories provide these for data sets (e.g., [Figshare](http://www.figshare.com)). Datasets accessible via persistent URLs increase the reproducibility of the research, relative to use of an individually maintained website, such as a lab group website or a researcher's personal website. This is because when an individually maintained websites changes its address or structure over time, the previously published URLs may no longer work. In many academic institutions, data repositories that provide persistent URLs are maintained by the libraries. These data repositories provide a secure environment for long-term citation, access, and reuse of research data.

-   Are the data shared in a commonly used and well-documented file format? For tabular data, open file formats based on plain text, such as CSV (comma separated values) or TSV (tab separated values) are often used. The main benefit of text-based formats is their simplicity and transparency. On the other hand, they suffer from a loss of numerical precision, they are relatively large, and parsing them might still be difficult. Where available, strongly-typed binary formats should be preferred. For example multi-dimensional array data can be stored in formats such as [HDF5](http://www.hdfgroup.org/HDF5/). In addition, there are also open data formats that have been developed in specific research communities to properly store data and metadata relelvant to the analysis of data from this research domain. Examples include the FITS data format for astronomical data (Wells, Greisen, & Harten, 1981), and the NIFTI and DICOM file formats for medical imaging data (Larobina & Murino, 2014).

Proprietary file formats are problematic for reproducibility because they may not be usable on future computer systems due to intellectual property restrictions, obsolescence or incompatibility. However, one can still ask: if open formats are not suitable, is software provided to read the data into computer memory with reasonably minimal effort?

-   If community standards exist, are files laid out in the shared database in a manner that conforms with these standards? For example, for neuroimaging data, does the file layout follow the Brain Imaging Data Structure (Gorgolewski et al., 2016) format?

-   If data are updated, are different versions of the data clearly denoted? If data is processed in your analysis, is the raw data available?

-   Is sufficient metadata provided? The type and amount of metadata varies widely by area of research, but a minimal set might include the research title, authors' names, description of collection methods and measurement variables, date, and license.

-   If the data are not directly available, for example if the data are too large to share conveniently, or have restrictions related to privacy issues, do you provide sufficient instructions to obtain equivalent data? For example, are the experimental protocols used to acquire the original data sufficiently detailed?

#### Availability of software

-   Is the software available to download and install? Software can also be deposited at repositories that issue persistent URLs, just like data sets. This can improve the longevity of its accessibility.

-   Can the software easily be installed on different platforms? If a scripting language such as Python or R was used, it is better for reproducibility to share the source rather than compiled binaries that are platform-specific.

-   Does the software have conditions on the use? For example, license fees, restrictions to academic or non-commercial use, etc.

-   Is the source code available for inspection?

-   Is the full history of the source code available for inspection through a publicly available version history?

-   Are the dependencies of the software (hardware and software) described properly? Do these dependencies require only a reasonably minimal amount of effort to obtain and use? For example, if a research project requires the use of specialized hardware, it will be harder to reproduce. If it depends on expensive commercial software, likewise. Use of open-source software dependencies on commodity hardware is not always possible, but when possible electing to use these increases reproducibility.

#### Software documentation

Documentation of the software is another factor in removing barriers to re-use. Several forms of documentation can be added to a research repository and each of them adds to reproducibility. Relevant questions include:

-   Does the software include a README file? This provides information about the purpose of the software, its use and ways to contact the authors of the software (see more below).

-   Is there any function/module documentation? This closely explains the different parts of the code, including the structure of the modules that make up the code; the inputs and outputs of functions; the methods and attributes of objects, etc.

-   Is there any narrative documentation? This explains how the bits and pieces of the software work together; narrative documentation might also explain how the software should be installed and configured in different circumstances and can explain what order things should be executed.

-   Are there usage examples? This is particularly important for scientific computing, usage examples demonstrate the kinds of transformations, analysis pipelines and visualizations that can be undertaken using the software, and provide a point of departure for new explorations using the software. Systems that allow examples to be routinely run as part of compiling the documentation are particularly useful, because they are automatically updated when the code is updated. One such system that was originally developed as part of the PyMVPA software library (Hanke et al., 2009) has been widely adopted and further developed by many other scientific Python libraries, including scikit-image (Van Der Walt et al., 2014) and scikit-learn (Pedregosa et al., 2011) and is now [its own software project](http://sphinx-gallery.readthedocs.io).

#### Software engineering

While not all scientific software needs to apply rigorous software engineering practices, using these practices increases the reproducibility and long-term sustainability of the software, and enables expansion of the software to handle extensions of the work. While a full implementation of these practices may be challenging for smaller projects, an awareness of the problems they are intended to solve can lead to better practices in other areas of the software development process. A few guidelines for assessing the software engineering of a computational research codebase follow.

Software testing is a practice that automates the checking of smaller units of the code, in addition and in support of the automation of the full pipeline, described above (see glossary for a detailed definition and typology of software testing). Questions that can be used to assess the testing of the code include:

-   Is a large proportion of the code covered by automatic testing that verifies that the software runs properly and is relatively error-free? Analysis software is often developed to deal with cases that are common in the data analyzed, and it often implicitly embodies assumptions about these common cases. However, some unusual cases (also called "corner cases" or "edge cases") may appear in the data, and it is important for the software to produce correct results in these cases as well. One might therefore ask: are corner cases covered, in addition to the common cases?

-   Is a continuous integration system set up to validate the mechanisms for software installation and to run the full complement of tests? Does this system regularly update the software dependencies, such that the software properly runs on newer versions of these dependencies? Is the system set up to maintain backwards compatibility with older versions of these dependencies, in support of dependent developments?

Further open-source and software engineering practices can help support a community of users. These include:

-   [Semantic versioning](https://semver.org/) is a way to communicate about the development of the software, and to allow others to depend on it. Is the software regularly released under a semantic versioning scheme? Are releases communicated widely to the user community? When standard installation channels exist, such as package managers (e.g., apt-get, pip) and repositories (e.g. CRAN, PyPi) exist, are new versions of the software made available through these mechanisms?

-   Are there mechanisms in place to report and track bugs in the software? When bugs are fixed, are these fixes reported in release announcements?

-   While private communication can be used to help individual users of the software, these modes of communication do not scale very well to a larger community of users. Requiring such private communication sets up barriers for users to reproduce the work. Setting up a public communication channel for users of the software to ask questions about use of the software increases the reproducibility. These can include public mailing lists, forums and/or chat rooms.

#### Copyright issues and other data encumbrances

Creative work, such as research, is protected by copyright laws. While these laws protect the rights of creators and researchers, they can also impede the distribution and verification of their work. Work that has no license or copyright information is still protected by copyright law. This prevents others from having any rights to reproduce the work or build upon it. Therefore, the application of an appropriate license is important in increasing the reproducibility of the work.

*Data and copyright.* While copyright law doesn't generally protect facts or data, it does protect the creative acts that go into selection of the data that goes into a database or compilation. To remove doubt about the copyright status of data, a license needs to be chosen. To assess reproducibility, you can ask:

-   If the data is openly accessible to others, is it released under a license that would allow them to use it?

-   Is the license permissive enough to allow others to build upon the work and extend it?

One set of licenses that allows data providers to control what potential users of the data may do with the data are the [Creative Commons licenses](https://creativecommons.org/), and open licenses designed specifically for data sharing (Miller, Styles, & Heath, 2008). Stodden (2009) recommends the CC-0 (public domain) license for data to enable maximum flexibility for reuse.

*Software and copyright* The same questions apply to issues related software and copyright, with slight variations: When sharing the source code of the software for free, researchers are encouraged to provide a license which clarifies the conditions under which this code can be used, without infringing on the copyright of the author. A license which allows anybody to use the software, alter it, build upon it, include it in other software packages, and extend it facilitates reproducibility.

Permissive software licenses would allow all of the above with minimal restrictions (e.g., BSD license, MIT license). BSD licenses are unique in including a specific clause which prevents the use of the name of the software author in future derivatives, which protects the author from negative effects of unwarranted use of their software.

Copyleft licenses allow distribution and modification of the software, but require they are released under the same license. For example, if the original software is open source and free, all its copies and derivatives should be open source and free. Such license clearly restricts the use of the software within proprietary applications. For example, software developed in an academic context with a copyleft license could not be used as part of a commercial package. The GNU General Public Licence (GPL) is an example of a popular copyleft license.

-   Does the software have an open-source license?

-   Is this license sufficiently permissive to allow others to use the software, reproduce the results and extend them?

#### Proprietary information and software

Often authors may not make the data or software available due to external restrictions. We might ask the following questions to assess the effect these restrictions might have on reproducibility:

-   Is the availability and use of the data encumbered through proprietary, privacy or ethical restrictions? (For example, due to presence of sensitive personal information, or customer activity records.).

-   Are there trade restrictions, or issues of national security that prohibit the open distribution of the data?

-   Is the software closed-source or limited in its accessibility due to funding regulations (governmental restrictions, industrial sponsor requirements, etc.)?

Although these conditions obviously limit the degree of reproducibility that might be possible, there are options to improve the reproducibility of this kind of research. For example, a simulated dataset can sometimes be provided that mimics the key attributes of the real dataset. Where the software is restricted, authors are encouraged to provide sufficient information about key algorithms so that future studies might be executed on openly available data with more accessible software.

### Open reporting of results

Crucial to reproducing a study is providing sufficient details about its execution through reports, papers, lab notebooks, etc. Researchers usually aim to publish their results in journals (or conference proceedings) with the aim to broadly distribute their discoveries. However, the choice of a journal may affect the availability and accessibility of their findings. Open access journals allow readers to access articles (usually online) without requiring any subscription or fees. While open access can take many forms, there are two common types of open access publication:

*green access* - the journal charges a subscription fee to readers for access to its contents, but allows the author to post a version of their article (preprint/postprint) on an electronic print website such as [arXiv](http://arxiv.org), [EPrints Archive](http://www.eprints.org/), on their own website, or on a institutional repository.

*gold access* - the journal does not charge any fees to readers, and makes a freely accessible online version of the article available at the time of publishing. Usually the author pays an article processing charge to enable free access by readers.

Clearly gold access journals provide the easiest and most reliable access to the article. However, since there are no subscription fees to cover publishing costs at gold open access journals and articles, the author is required to pay. Often the amount is over a thousand dollars per article. Authors should check with their institution whether it provides funds for covering such fees. As a compromise, journals sometimes have an embargo on open access (delayed open access), i.e. there is a period of time during which the article cannot be freely accessed, after which either the journal automatically makes the article available or the authors are allowed to self-archive it.

Green open access is an attractive approach to making articles openly available because it is affordable to both readers and authors. According to a study of a random sample of articles in 2009 (Björk, Welling, Laakso, Majlender, & Guðnason, 2010), approximately 20% of the articles were freely accessible (9.8 % on publishers' websites and 11.9% elsewhere through search). A more recent larger study (Archambault et al., 2013) indicates that 43% of Scopus indexed papers between 2008 and 2011 were freely available by the end of 2012. It has been also shown that there is a substantial growth in the proportion of available articles. However, there are still many articles which have been given a green light for access, but they have not been self-archived. Thus it is important for authors to understand the journal's publishing policy and use the available resources (within their field, institution, and beyond) to make their work accessible to a wide audience. Many research-intensive universities, usually via the libraries, provide services to help researchers self-archive their publications.

There are many other methods for sharing research online at different stages of the work (before final results are even available). Preregistration of the hypotheses that are being tested in a study can prevent overly flexible analysis practices and HARKing (hypothesizing after results are known (Kerr, 1998)), which reduce the reproducibility of the results reported. Regular public updates can be achieved through electronic lab notebooks, wiki pages, presentation slides, blog posts, technical reports, preprints, etc. Sharing progress allows for quick dissemination of ideas, easy collaboration, and early detection and correction of flaws. Storing preliminary results and supplementary materials in centralized repositories (preregistration registries, public version control repositories, institutional reports) have potential to improve the discoverability and the availability lifespan of the works. Some important questions researchers can ask when evaluating publishing solutions include:

-   Is this electronic publishing platform going to be available in 2 years? In 5 years? Longer?

-   Can a simple web search on the topic recover a link to the publication and related materials?

Taking into account the sustainability and the ease of access of these solutions in the decision process is integral to improving the research reproducibility. There is also empirical evidence that publication in open access promotes the downstream use of the scientific findings, as evidenced by an approximately 10% increase in citations (Hajjem, Harnad, & Gingras, 2006) (and see also <http://opcit.eprints.org/oacitation-biblio.html>).

### Conclusion

This chapter has attempted to outline the factors that determine the extent to which a research project is computationally reproducible. We have surveyed three different aspects where reproducibility can be assessed: automation and provenance tracking, availability of software and data, and open reporting of results. For each topic we provide a set of questions for researchers to consider about their own work and stimulate discussion on how computationally reproducibility can be improved. There are many more questions that could be asked, but we have tried to confine ourselves to questions that are relevant to key hurdles in improving reproducibility. We have observed these questions to be key points in making our own work more reproducible, and in assessing the work of our peers.

A key theme of this chapter is that there are many degrees of reproducibility. Computational reproducibility exists on a long spectrum from completely irreproducible research to complete computational reproducibility, with data, software and results all available for scrutiny, use and further exploration. Our hope is that by raising these questions and discussing some of the options, researchers can identify ways to move their work a little further along the spectrum towards improved reproducibility. We recommend a pragmatic approach to assessing and improving reproducibility, making incremental improvements from project to project, keeping an eye on the shifting norms of the field and the evolving standards and norms for data formats, metadata, repositories, etc. Over time, some of the specific suggestions we have offered here may fall out of fashion or be replaced by superior options. However, the general principles that we focus on with our questions for are likely to endure beyond the technical details, and serve as useful prompts for assessing reproducibility well into the future.

### References

Archambault, E., Amyot, D., Deschamps, P., Nicol, A., Rebout, L., & Roberge, G. (2013). *Proportion of open access peer-reviewed papers at the european and world levels—2004-2011*. Science-Metrix. Retrieved from <http://www.science-metrix.com/pdf/SM_EC_OA_Availability_2004-2011.pdf>

Baker, M. (2016a). 1,500 scientists lift the lid on reproducibility. *Nature*, *533*(7604), 452–454.

Baker, M. (2016b). Muddled meanings hamper efforts to fix reproducibility crisis. *Nature News*. <http://doi.org/doi:10.1038/nature.2016.20076>

Björk, B.-C., Welling, P., Laakso, M., Majlender, H., P., & Guðnason, G. (2010). Open access to the scientific journal literature: Situation 2009. *PLoS ONE*, *5*(6). <http://doi.org/10.1371/journal.pone.0011273>

Cartwright, N. (1991). Replicability, reproducibility, and robustness: Comments on harry collins. *History of Political Economy*, *23*(1), 143–155. Journal Article.

Casadevall, A., & Fang, F. C. (2010). Reproducible science. *Infection and Immunity*, *78*(12), 4972–4975. <http://doi.org/10.1128/IAI.00908-10>

Claerbout, J. F., & Karrenfach, M. (n.d.). Electronic documents give reproducible research a new meaning. Conference Paper, Society of Exploration Geophysicists.

Collins, H. M. (1984). When do scientists prefer to vary their experiments? *Studies in History and Philosophy of Science Part A*, *15*(2), 169–174. Journal Article.

Donoho, D. L., Maleki, A., Rahman, I., Shahram, M., & Stodden, V. (2008). *15 years of reproducible research in computational harmonic analysis*. Department of Statistics, Stanford University.

Drummond, C. (2009). Replicability is not reproducibility: Nor is it good science. *Proc. Eval. Methods Mach. Learn. Workshop 26th ICML, Montreal, Quebec, Canada*. Retrieved from <http://cogprints.org/7691/7/icmlws09.pdf>

Easterbrook, S. M. (2014). Open code for open science? *Nature Geosci*, *7*(11), 779–781. Journal Article. <http://doi.org/10.1038/ngeo2283>

Franklin, A., & Howson, C. (1984). Why do scientists prefer to vary their experiments? *Studies in History and Philosophy of Science Part A*, *15*(1), 51–62. Journal Article.

Goodman, S. N., Fanelli, D., & Ioannidis, J. P. A. (2016). What does research reproducibility mean? *Science Translational Medicine*, *8*(341), 341ps12–341ps12. <http://doi.org/10.1126/scitranslmed.aaf5027>

Gorgolewski, K. J., Auer, T., Calhoun, V. D., Craddock, R. C., Das, S., Duff, E. P., … Poldrack, R. A. (2016). The brain imaging data structure: A standard for organizing and describing outputs of neuroimaging experiments. *bioRxiv*. <http://doi.org/10.1101/034561>

Hajjem, C., Harnad, S., & Gingras, Y. (2006). Ten-year cross-disciplinary comparison of the growth of open access and how it increases research citation impact. *arXiv Preprint Cs/0606079*.

Hanke, M., Halchenko, Y. O., Sederberg, P. B., Hanson, S. J., Haxby, J. V., & Pollmann, S. (2009). PyMVPA: A python toolbox for multivariate pattern analysis of fMRI data. *Neuroinformatics*, *7*(1), 37–53.

Kerr, N. L. (1998). HARKing: Hypothesizing after the results are known. *Personality and Social Psychology Review*, *2*(3), 196–217.

Larobina, M., & Murino, L. (2014). Medical image file formats. *Journal of Digital Imaging*, *27*(2), 200–206.

Miller, P., Styles, R., & Heath, T. (2008). Open data commons, a license for open data. *LDOW*, *369*.

Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., … others. (2011). Scikit-learn: Machine learning in python. *The Journal of Machine Learning Research*, *12*, 2825–2830.

Stodden, V. (2009). Enabling reproducible research: Open licensing for scientific innovation. *International Journal of Communications Law and Policy*, *13*, 1–25.

Stodden, V., Borwein, J., & Bailey, D. H. (2013). Setting the default to reproducible. *Computational Science Research. SIAM News*, *46*, 4–6.

Stodden, V., Leisch, F., & Peng, R. D. (2014). *Implementing reproducible research*. CRC Press.

Van Der Walt, S., Schönberger, J. L., Nunez-Iglesias, J., Boulogne, F., Warner, J. D., Yager, N., … Yu, T. (2014). Scikit-image: Image processing in python. *PeerJ*, *2*, e453.

Wells, D. C., Greisen, E. W., & Harten, R. H. (1981). FITS - a Flexible Image Transport System, *44*, 363.

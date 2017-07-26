The Basic Reproducible Workflow Template
========================================

Justin Kitzes
-------------

The core of this book consists of a set of thirty-one contributed case studies, each showing an example of a scientific workflow that was designed, at least in part, to achieve the goal of reproducibility. These case studies are concerned mainly with the goal of computational reproducibility, the ability of a second researcher to receive a set of files, including data, code, and documentation, and to recreate or recover the outputs of a research project, including figures, tables, and other key quantitative and qualitative results.

The thirty-one case studies in this volume describe a wide variety of research projects, disciplines, methods, and tools. Behind this diversity, however, all of the case studies share many key principles and practices in common. In this chapter, we describe what we view as the basic, underlying reproducible research workflow that any scientist should master before continuing on to the complexities described in the case study chapters.

To demonstrate this basic workflow, this chapter walks through a complete, concrete example of perhaps the simplest realistic data-intensive research project: a regression analysis of a single tabular data set. This example is designed to provide useful background for understanding the case studies later in this book. It will also provide a self-contained introduction to the practice of reproducible research for beginning readers looking for a template to adapt to their own research needs. We particularly encourage beginning readers to work along interactively with the example in this chapter to get a feel for how a reproducible workflow can be implemented.

We begin this chapter with a general overview of three key practices that are needed to make any research project, no matter how simple, computationally reproducible. This is followed by a high-level overview of the basic reproducible research workflow. We then provide an extended example of how this workflow can be implemented in a simple research project. We conclude with some additional considerations that arise when transitioning from this simple workflow template to more complex workflows, such as those described in the contributed case study chapters.

### Three Key Practices

Chapter 2 described a set of questions that can be used to assess, at a relatively fine grained level, the extent to which a research project is reproducible. At a higher level, we can summarize these recommendations in three general practices that arise repeatedly throughout all stages of a research project:

1.  Clearly separate, label, and document all data, files, and operations that occur on data and files

2.  Document all operations fully, automating them as much as possible, and avoiding manual intervention in the workflow when feasible

3.  Design a workflow as a sequence of small steps that are glued together, with intermediate outputs from one step feeding into the next step as inputs

At a beginning level, the first of these practices largely involves placing files in a clear directory structure and creating metadata to describe them. The second is met by writing code, or scripts, to perform each step automatically, or where this is not possible, documenting all manual steps needed to complete a task at a level that would allow a second researcher to unambiguously repeat them. The third is met through the overall workflow design, especially a clear conceptualization of the different operations that need to occur sequentially and how they support each other.

Although not described in the example below, most of the contributed case studies in this book use version control software as a tool for following the first two practices above. In short, version control is used to capture a snapshot of all of a project's files at any moment in time, allowing a researchers to easily review the history of the project and to manage future changes. Version control also provides a means of documenting and tracking changes to project files in a systematic and transparent manner.

In our experience, however, many beginners find version control more difficult to learn than the other steps described below, and thus we have chosen not to include it in this basic workflow template. However, once you feel comfortable with this basic workflow, we recommend that you progress to one of the many online tutorials that can help you learn to use version control systems. We particularly recommend the tutorials on `git` available from Software Carpentry.

### The Stages of the Basic Reproducible Workflow

The basic reproducible research workflow can be divided into three main stages: data acquisition, data processing, and data analysis. These three stages are preceded by activities related to system setup, and are succeeded by steps that automate the entire workflow as much as possible. While steps such as project brainstorming and publication may also be a key part of a research workflow, the tasks that relate to ensuring a project's reproducibility fall primarily within these stages.

Before beginning a data-intensive computational research project, a computer system with the tools necessary to complete the analysis must be located and set up. These activities can be more or less involved, depending primarily on the researchers level of access to the computer and the programming language that will be used for the analysis.

The first stage of the basic workflow is data acquisition, input, or creation. This stage commonly consists of collecting data from a primary source, such as field observation, experimental research, or surveys. However, it also may include acquiring data from an existing source, through web-scraping or communication with other researchers, or generating data via simulation. Regardless of the method, the end result of this first stage is raw data.

The second stage involves processing or cleaning of the data produced in the first stage. Depending on the tools used and the author's strategies, this stage may include tasks such as manual data entry, visual data review, or systematic data manipulation or filtering using scripts or other software. At the completion of this second stage, the relevant data is digitized, cleaned, and fully prepared for analysis. Although this stage is often treated as minor, or less important, than the other two stages surrounding it, we have found that this stage often requires as much intellectual energy, and as many difficult decisions, as the other stages in this workflow.

The third stage is data analysis. The most common form of data analysis is formal statistics, but other activities in this stage include data visualization, assessing the performance of particular algorithms, and extending the data to address a hypothesis or draw a scientific conclusion. The defining attribute of this stage is that it analyzes, in some manner, the clean data produced in the second stage, and produces the desired scientific products of the research, generally quantitative results in the form of figures and tables that are incorporated into manuscripts, talks, and other forms of communication.

Finally, following the three central stages, the reproducibility of a project can be greatly enhanced through the creation of a single controller script that can automatically execute all three stages to produce a finished result. When this type of "push button" workflow is unrealistic or impossible to achieve due to project constraints, detailed documentation of all non-automated steps should be created.

### Setup

The setup activities that precede the three core stages of a reproducible workflow consist first of gaining access to a computer, or several computers, to use for a project. For this simple example, we will presume that the entire analysis will occur on a personal computer for which the researcher has full administrator access.

There are generally three classes of tools that must be installed at this stage. The first of these is a shell or terminal program that allows access to the command line. The second is a plain text editor or a development environment that can be used to write code in a chosen language. The third is software allowing the user to write and execute code in a chosen a programming language. Alternatively, researchers may choose to use an integrated workflow program, such as [VisTrails](http://www.vistrails.org), [Taverna](https://taverna.incubator.apache.org/), or [Kepler](https://kepler-project.org/), although this approach will not be discussed here.

For the basic workflow that follows, Mac or Linux users can use the pre-installed Terminal program on their systems, while Windows users can work at the Command Prompt. All users should install a plain text editor, of which many are available for each platform. Finally, the examples below will make use of the R language, and users should download and install a recent version of [R](https://www.r-project.org/).

More detailed information on the above installation steps, as well as basic tutorials on how to use these tools, can be found in the [Software Carpentry lessons](http://software-carpentry.org/lessons/).

### Stage 1: Data Acquisition

The first stage in most data-intensive workflows involves the acquisition of raw data. For this example, we'll imagine a study in which we have collected field data on tomatoes being grown as part of an agricultural experiment.

Table 1 reports hypothetical measurements of the total yield of tomatoes, in kilograms per plant, produced by four plants in each of three fields having no management after planting (N), conventional management with fertilizers and pesticides (C), or organic management (O). The third column indicates whether substantial insect damage was noted on the plant leaves at the time of harvest. Of the fifteen plants marked for sampling, two of them, denoted with `NA` in the mass column, were killed before bearing fruit.

<!-- This table is used for the Gitbook online version of the book. It must be kept manually in sync with the main Markdown version of the table. -->

<p> Table 1: Sample tomato data set</p>
<table style="width:39%;">
<colgroup>
<col width="9%" />
<col width="13%" />
<col width="15%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Field</th>
<th align="right">Weight</th>
<th align="left">Insect</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">N</td>
<td align="right">5.8</td>
<td align="left">Y</td>
</tr>
<tr class="even">
<td align="left">N</td>
<td align="right">5.9</td>
<td align="left">N</td>
</tr>
<tr class="odd">
<td align="left">N</td>
<td align="right">1.6</td>
<td align="left">Y</td>
</tr>
<tr class="even">
<td align="left">N</td>
<td align="right">4.0</td>
<td align="left">Y</td>
</tr>
<tr class="odd">
<td align="left">N</td>
<td align="right">2.9</td>
<td align="left">Y</td>
</tr>
<tr class="even">
<td align="left">C</td>
<td align="right">12.4</td>
<td align="left">N</td>
</tr>
<tr class="odd">
<td align="left">C</td>
<td align="right">11.5</td>
<td align="left">N</td>
</tr>
<tr class="even">
<td align="left">C</td>
<td align="right">9.3</td>
<td align="left">N</td>
</tr>
<tr class="odd">
<td align="left">C</td>
<td align="right">NA</td>
<td align="left">N</td>
</tr>
<tr class="even">
<td align="left">C</td>
<td align="right">12.1</td>
<td align="left">N</td>
</tr>
<tr class="odd">
<td align="left">O</td>
<td align="right">9.9</td>
<td align="left">N</td>
</tr>
<tr class="even">
<td align="left">O</td>
<td align="right">6.7</td>
<td align="left">N</td>
</tr>
<tr class="odd">
<td align="left">O</td>
<td align="right">10.6</td>
<td align="left">Y</td>
</tr>
<tr class="even">
<td align="left">O</td>
<td align="right">3.7</td>
<td align="left">Y</td>
</tr>
<tr class="odd">
<td align="left">O</td>
<td align="right">NA</td>
<td align="left">N</td>
</tr>
</tbody>
</table>

This data should be entered into a spreadsheet program and saved as a CSV file. CSV files are a commonly used plain text format for storing tabular data, in which each row of a table is on a separate line and data for each column are separated by a comma. Plain text formats are often preferable to program-specific formats, such as XLSX, as they are more easily readable by a variety of software and by other researchers who may wish to work with this data.

Once this file is created, it should be given a name and saved in a useful location. Naming conventions vary widely between researchers, but in small projects such as this one, we recommend using names that usefully describe a file's contents, even if these are somewhat long. This table, for example, might be saved as `raw_yield_data.csv`. To avoid the possibility of errors later in the workflow, spaces, periods, and slashes should not be used in file names.

At the same time that data are saved, a metadata file should also be created and saved with it. The purpose of the metadata file is to document the source of the data and any relevant information about it. While many disciplines have standards for metadata, a minimal metadata file consists of a simple text file that describes, in plain English, where the data came from and what it describes. Such a file, which we can save as `README.txt` alongside the data file, might contain information like the following.

> Data collected by undergraduate assistants to Prof John Smith at the Berkeley Field Station. All plants were located in Field 3 and chosen for measurement when approximately 12" tall. Yields were recorded in August 2015.
>
> Field codes indicate no treatment (N), conventional (C), and organic (O). Yield is in kg, with NA indicating a plant that died prior to yield measurement. Insect damage assessed visually, Y indicates more than 25% loss of leaf area.

The question then arises of where these two files, as well as all of the subsequent files that will be part of the project, should be saved. A common convention is to place all project files in a single directory, with a single layer of subdirectories for different types of files, such as data, source code, analysis results, etc. A structure such as the below, with all files and subfolders contained in a single folder called `tomato_project`, provides a useful starting point for simple projects.

    |-- tomato_project
    |   |-- data_raw
    |   |   |-- raw_yield_data.csv
    |   |   |-- README.txt
    |   |-- data_clean
    |   |-- results
    |   |-- src

### Stage 2: Data Processing

Once raw data has been collected and placed in a project directory, it nearly always requires some form of processing or cleaning before it can be used in an analysis. This step may involve removing invalid data, subsetting the original data, removing outliers, and other similar steps. The best approach for processing a raw data set is, of course, dependent on the questions that a researcher hopes to answer with this data and the particular type of analysis planned for Stage 3.

In this example, inspection of the raw data table revealed two plants without yield measurements, which we may wish to remove from the data before any further analysis. Given a goal of eventually conducting a two-sample t-test comparing the conventional to the organic yields, we also know that we can remove the no treatment plants from the table at this stage. For a small table such as this one, removing these rows is not strictly necessary, although such subsetting can improve the efficiency of subsequent analysis of larger data sets.

To make this stage fully reproducible, every step taken to process the data must be recorded with detail fine enough that only one processed data set could result from the combination of the raw data and the set of instructions. The simplest and the recommended way to accomplish this is to encode the instructions for data processing as computer code, in a script, that will read in the raw data, execute various processing and cleaning operations, and save the resulting processed data as a new file.

Particularly for small tabular data, it can be tempting to skip this coding step, and instead open the file in a graphical editor, such as a spreadsheet program, delete the rows or columns that are not needed, and save the resulting file. In some instances, particularly where data files are stored in a proprietary format that can only be opened by certain programs, this manual approach may be the only option. Manual data processing, however, is prone to error and makes the "push button" automated workflow described later impossible.

As is the case with all research tasks, if this step must be done manually, ensure that the processed data file is accompanied by a very detailed human readable description, saved in a text file like the metadata file, that describes every operation performed on the raw data, to the level of what menu was selected and what button clicked in what order. Remember that if someone who you have never met cannot exactly, with 100% accuracy, reproduce the processed data file from the raw data and instructions, then this step is not fully reproducible. In many ways, this instruction file is itself similar to code, although it is intended to be executed by a human reader rather than by a computer.

For this tomato yield data, we can readily write a short script that will read the raw table, remove the rows with `NA` yields and those with a field code of `N`, and save the resulting processed data. The following R commands will perform these operations.

    yield_data <- read.csv("yield_data.csv")
    clean_yield_data <- na.omit(raw_yield_data[raw_yield_data$Field != "N", ])
    write.csv(clean_yield_data, "clean_yield_data.csv")

While exploring the data, the commands above can be entered interactively into an interpreter window. Once a procedure for data processing has been identified, however, all of these commands should be placed in a separate file that when executed, will read the raw data, process it, and save the resulting processed data file. This ensures definitively that all necessary steps to reproduce this stage of the workflow were recorded properly and can be easily repeated at will.

In the simple directory structure described earlier, scripts and other code are saved in the `src` subfolder. To ensure that a script in the `src` directory will locate and save the appropriate files in the appropriate folders, we can modify the code above to the below, which modifies the locations where the files are read and written. Note that we have also added comments describing what each line of code is intended to do.

    ### Read in the raw data, assuming we are working in the src directory
    raw_yield_data <- read.csv("../data_raw/raw_yield_data.csv")

    ### Clean the data by removing rows with NA and where 'Field' == N
    clean_yield_data <- na.omit(raw_yield_data[raw_yield_data$Field != "N", ])

    ### Write the clean data to disk
    write.csv(clean_yield_data, "../data_clean/clean_yield_data.csv")

The commands above, when saved as a script `clean_data.R` in the `src` subfolder, will read the table `raw_yield_data.csv` from the `data_raw` subfolder, clean it, and save the resulting cleaned table as `clean_yield_data.csv` in the `data_clean` subfolder. The cleaned data are placed in a different subfolder from the raw data to ensure that the original, raw data are never confused with any derived data products. Ideally the raw data files should never be altered, with all changes and modifications saved to a separate file. This will ensure that you can always go back to the original data if you make a data processing decision that you regret.

To execute this script, navigate to the `src` subfolder in a terminal window and run the command `r clean_data.R`. For more information on working at the command line, see the [Software Carpentry shell tutorial](http://software-carpentry.org/lessons/).

The project directory should now look like the following.

    |-- tomato_project
    |   |-- data_raw
    |   |   |-- raw_yield_data.csv
    |   |   |-- README.txt
    |   |-- data_clean
    |   |   |-- clean_yield_data.csv
    |   |-- results
    |   |-- src
    |   |   |-- clean_data.R

### Stage 3: Data Analysis

Once data are checked in and processed, the third stage of the basic reproducible workflow is data analysis. There are, of course, many different types of analyses that may be employed here and many different types of outputs that can result, including text-based results, tables, and figures. For this example, we'll perform an unpaired two sample t-test to determine whether the mean tomato yield per plant is significantly different in the conventional and organic fields.

As with data processing, data analysis may be done manually using graphical tools, such as a spreadsheet program. This is not recommended due to the difficulty of accurately capturing all of the minute details needed to allow a second researcher to exactly repeat the analysis without errors. Data analysis may also be performed interactively, with code entered into a "live" interpreter window until a final result is reached and saved. This step is often important as a means of exploration to determine what commands should be used for the analysis. Once interactive tools have been used to explore possible approaches, however, we strongly recommend that all commands needed to perform the data analysis be placed in separate file that will save the results when executed.

The code below should be saved in a script titled `analysis.R` in the `src` directory. When run, it will read the cleaned data table, perform the desired t-test, and save the summarized results of the test in the `results` subfolder as a plain text file `test_results.txt`. Although not applicable here, any other results, such as tables and figures, should also be saved in the `results` subfolder.

    ### Load clean data, assuming we are in the src directory
    clean_yield_data <- read.csv("../data_clean/clean_yield_data.csv")

    ### t-test of Weights by Field type: is there significant difference in 
    ### tomato yield in the different fields?
    t_test_Weight_Field <- with(clean_yield_data, t.test(Weight ~ Field)

    ### Write test result to plain text file 
    capture.output(t_test_Weight_Field, file = "../results/test_results.txt")

Note that several comments describing the analysis steps are included in the code above. Although the relatively simple commands here do not require extensive explanation, comments should be used liberally in all code files, as we have demonstrated in the examples here. While the code itself describes *what* operation is performed, comments should be used to describe *why*, and in a larger sense *how*, a desired analysis is being conducted. While the code itself is designed to reproduce the quantitative results of an analysis, code comments and other documentation are designed to help another researcher reproduce the thought process that went into structuring and writing code in a particular way.

At the conclusion of this stage, after the script `analysis.R` has been run in the same manner as the previous `clean_data.R` script, the project directory will appear as follows.

    |-- tomato_project
    |   |-- data_raw
    |   |   |-- raw_yield_data.csv
    |   |   |-- README.txt
    |   |-- data_clean
    |   |   |-- clean_yield_data.csv
    |   |-- results
    |   |   |-- test_results.txt
    |   |-- src
    |   |   |-- analysis.R
    |   |   |-- clean_data.R

The `test_results.txt` file indicates that there is no detectable significant difference between the yields in the conventional and organic fields (p = 0.104).

### Automation

At this stage, the reproducible workflow is essentially complete. We have written code that, when executed, will read and process our raw data table and save both a cleaned data table and the final results of our analysis. Most importantly, the final result of our analysis, the p-value for the comparison of the conventional and organic yields, can be reproduced by any researcher who has access to the original data and the code that we have written.

To make this workflow even easier to reproduce, a controller or driver script can be added to execute, in one step, all of the various subcomponents of the entire workflow. In this simple example, our workflow has only two steps that can be performed automatically: executing `clean_data.R` to generate the cleaned data table, and then executing `analysis.R` to perform the statistical test.

To create a single entry point that will perform our entire analysis, we can create a shell script, `runall.sh`, that we can save in the `src` directory. For this simple example, the script only contains two lines.

    r clean_data.R
    r analysis.R

To test out this controller script, delete the contents of the `data_clean` and the `results` directory to simulate giving a colleague only your raw data and code. From the command line, navigate to the `src` directory and run the command `sh runall.sh` to see the intermediate and final results of the workflow regenerate.

In addition to supporting reproducibility, the creation of a "push button" workflow like this has a second related side benefit, which is ensuring that any generated results are linked directly back to specific known data sets and analysis parameters. We and many of our colleagues have been known to finish working on real projects, delete all results precisely as described above, and rerun the entire workflow using a controller script. This final step ensures that all results used in subsequent interpretation and presentation were, in fact, generated from the latest data and code in the project directory.

### Conclusion

While some real world workflows are nearly as simple as the one shown here, many projects will be more complex, perhaps substantially so. The most immediate extension of the template shown here would be the need to accommodate a greater variety of file types, including many types of code files, several categories of results, binary executables, and documentation. From an organizational perspective, an additional level of subfolders can be be created within folders such as `src` and `results` to organize these additional files. Subfolders such as `doc` and `bin` within the main project directory can be used to house files related to documentation, including manuscripts, and compiled binaries.

Beyond the addition of more project files, more complex projects will require more complex workflows that allow, for example, files to be shared across multiple projects, the same analysis to be run on multiple data sets or parameter combinations, analyses to be run on remote computers, etc. Many of these additional complexities are discussed in the contributed case studies in this volume.

When moving beyond the tools and techniques described above, we first recommend that you learn to integrate version control software into your workflow. Tutorials for software such as `git` are readily available online.

A second possible direction would be to try using a literate programming approach. This approach involves creating a single source document in a language such as Markdown or LaTeX, or using a "notebook" interface such as one provided by Sage or Jupyter, that contains text describing the analysis directly alongside code, figures, tables and other results of our report. In this framework, the single source document can be executed to run the code and obtain results alongside narrative description and documentation. This approach provides a self-contained file of text and code that is convenient for circulating to other readers by email or submitting for publication.

In closing, we note once again that the structure of this basic reproducible workflow, particularly the division of the workflow into the three core stages plus setup and automation, underlies all of the more complex case studies described in this volume. We encourage researchers, both beginning and advanced, to use the template in this chapter as a basic foundational framework for understanding, organizing, and creating reproducible workflows as part of real world research projects in the data-intensive sciences.

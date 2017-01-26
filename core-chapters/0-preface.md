Preface: Nullius in Verba
=========================

P.B. Stark
----------

The origins of the scientific method, epitomized by Sir Francis Bacon's work in the early 1600s, amount to insistence on direct evidence. This is reflected in the motto of The Royal Society, founded in 1660: *Nullius in verba*, which roughly means "take nobody's word for it" (The Royal Society, 2016). Fellows of the Royal Society did not consider a claim to be scientifically established unless it had been demonstrated experimentally in front of a group of observers (other fellows), who could see with their own eyes what happened (Shapin & Schaffer, 2011). Over time, Robert Boyle and others developed conventions for documenting experiments in sufficient detail, using prose and illustrations of the apparatus and experimental set up, that the reader could imagine being in the room, observing the experiment and its outcome.

Such observability---visibility into the process of generating results---provides the evidence that the scientific claim is true. It helps ensure we are not fooling ourselves or each other, accidentally or deliberately. It is a safeguard against error and fraud, and a springboard for progress, enabling others to replicate the experiment, to refine or improve the experiment, and to leverage the techniques to answer new questions. It generates and promulgates scientific knowledge *and* the means of generating scientific knowledge.

However, science has largely abandoned that transparency and observability, resulting in a devolution from *show me* to *trust me.* Scientific publications simply do not contain the information needed to know what was done, nor to try to replicate the experiment and data analysis. Peer reviewers and journal editors, the gatekeepers we rely upon to ensure the correctness of published results, cannot possibly vet submissions well, because they are not provided enough information to do the job. There are many reasons for this regression, among them, the rise of Big Science, the size of many modern data sets, the complexity of modern data analysis and the software tools used for data analysis, and draconian limits on the length of articles and even on electronic supplemental material. But as a consequence, most scientific publications provide little scientific evidence for the results they report.

It is impractial or impossible to repeat some experiments from scratch: who can afford to replicate CERN, the Hubble Space Telescope, or the National Health and Nutrition Examination Survey? Some data sets are too large to move efficiently, or contain information restricted by law or ethics. Lack of access to the underlying data obviously makes it impossible to replicate data analysis. But even when the data are available, reliance on proprietary software or point-and-click tools and failure to publish code make it impossible to know exactly what was done to the data to generate the figures and tables in most scientific publications.

The (unfortunately rare) attempts to replicate experiments or data analyses often fail to support the original claims (Lehrer, 2010; Open Science Collaboration, 2015) Why?

One reason is the interaction between scientific publishing and statistics. Because journals are generally uninterested in publishing negative results or replications of positive results, the emphasis is on "discoveries." Selecting data, hypotheses, data analyses, and results to produce (apparently) positive results inflates the apparent signal-to-noise ratio and overstates statistical significance. The ability to automate many aspects of data analysis, such as feature selection and model selection, combined with the large number of variables measured in many modern studies and experiments, including "omics," high-energy physics, and sensor networks, make it essentially inevitable that many "discoveries" will be wrong (Ioannidis, 2005). A primary defense against being misled by this selection process, which includes *p*-hacking and the "file-drawer effect" (Nuzzo, 2015; Rosenthal, 1979), is to insist that researchers disclose what they tried before arriving at the analysis they chose to report or to emphasize.

I would argue that if a paper does not provide enough information to assess whether its results are correct, it is something other than science. Consequently, I think scientific journals and the peer review system must change radically: referees and editors should not "bless" work they cannot check because the authors did not provide enough information, including making available the software used to analyze the data. And scientific journals should not publish such work.

A crucial component of the chain of evidence is the software used to process and analyze the data. Modern data analysis typically involves dozens, if not hundreds of steps, each of which can be performed by numerous algorithms that are nominally identical but differ in detail, and each of which involves at least some ad hoc choices. If researchers do not make their code available, there is little hope of ever knowing what was done to the data, much less assessing whether it was the right thing to do.

And most software has bugs. For instance, a 2014 study by Coverity, based on code-scanning algorithms, found 0.61 errors per 1,000 lines of source code in open-source projects and 0.76 errors per 1,000 lines of source code in commercial software (Synopsys, 2015). Scientific software is not an exception, and few scientists use sound software engineering practices, such as rigorous testing---or even version control (Merali, 2010; Soergel, 2015). Using point-and-click tools, rather than scripted analyses, makes it easier to commit errors and harder to find them. One recent calamity attributable in part to poor computational practice is the work of Reinhart and Rogoff (2010), which was used to justify economic austerity measures in southern Europe. Errors in their Excel spreadsheet led to the wrong conclusion (Herndon & Pollin, 2014). If they had scripted their analysis and tested the code instead of using spreadsheet software, their errors might have been avoided, discovered, or corrected before harm was done.

Working reproducibly makes it easier to get correct results and enables others to check whether results are correct. This volume focuses on how researchers in a broad spectrum of scientific applications document and reveal what they did to their data to arrive at their figures, tables, and scientific conclusions; that is, how they make the computational portion of their work more transparent and reproducible. This enables others to assess crucial aspects of the evidence that their scientific claims are correct, and to repeat, improve, and repurpose analyses and intellectual contributions embodied in software artifacts. Infrastructure to make code and data available in useful forms needs more development, but much is possible already, as these vignettes show. The contributors share how their workflows and tools enable them to work more transparently and reproducibly, and call out "pain points" where new tools and processes might make things easier. Whether you are an astrophysicist, an ecologist, a sociologist, a statistician, or a nuclear engineer, there is likely something between these covers that will interest you, and something you will find useful to make your own work more transparent and replicable.

### References

Herndon, M. A., T., & Pollin, R. (2014). Does high public debt consistently stifle economic growth? A critique of reinhart and rogoff. *Cambridge Journal of Economics*, *38*, 257–279.

Ioannidis, J. (2005). Why most published research findings are false. *PLoS Medicine*, *2*(8), e124.

Lehrer, J. (2010). The truth wears off. *The New Yorker*. Retrieved from <http://www.newyorker.com/magazine/2010/12/13/the-truth-wears-off>

Merali, Z. (2010). Computational science: . . . Error . . . why scientific programming does not compute. *Nature*, *467*, 775–777.

Nuzzo, R. (2015). How scientists fool themselves – and how they can stop. *Nature*, *526*, 182–185.

Open Science Collaboration. (2015). Estimating the reproducibility of psychological science. *Science*, *349*, 943.

Reinhart, C., & Rogoff, K. (2010). Growth in a time of debt. *American Economic Review*, *100*, 573–578.

Rosenthal, R. (1979). The “file drawer problem” and tolerance for null results. *Psychological Bulletin*, *86*(3), 638–641.

Shapin, S., & Schaffer, S. (2011). *Leviathan and the air-pump: Hobbes, boyle, and the experimental life*. Princeton, NJ: Princeton University Press.

Soergel, D. (2015). Rampant software errors may undermine scientific results. *F1000Research*, *3*, 303.

Synopsys. (2015). Coverity scan open source report 2014. Retrieved from <http://go.coverity.com/rs/157-LQW-289/images/2014-Coverity-Scan-Report.pdf>

The Royal Society. (2016). The royal society | history. Retrieved from <https://royalsociety.org/about-us/history/>

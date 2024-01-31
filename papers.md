Following are the papers I found while doing an informal survey of
recent publications. The survey went back 4 years (until and including
2019). The following venues were reviewed:

-   [ ] ICSE
    -   [x] 2023
    -   [X] 2022
    -   [ ] 2021
    -   [ ] 2020
    -   [ ] 2019
-   [ ] FSE
    -   [X] 2023
    -   [X] 2022
    -   [ ] 2021
    -   [ ] 2020
    -   [ ] 2019
-   [ ] ASE
    -   [X] 2023
    -   [X] 2022
    -   [ ] 2021
    -   [ ] 2020
    -   [ ] 2019
-   [ ] MSR
    -   [X] 2023
    -   [X] 2022
    -   [ ] 2021
    -   [ ] 2020
    -   [ ] 2019
-   [ ] EMSE
    -   [X] 2024
    -   [X] 2023
    -   [ ] 2022
    -   [ ] 2021
    -   [ ] 2020
    -   [ ] 2019

The papers are organised as follows:

-   Papers still to be processed are under the `Inbox`{.verbatim}
    heading
-   The remaining papers are organised under headings based on the
    primary topic which include:
    -   `Testing`{.verbatim}: These are papers on testing ML/AI systems
    -   `LLMs`{.verbatim}: Papers using Large Language Models
    -   `Notebooks`{.verbatim}: Papers on Computational Notebooks

# Inbox

## obrien202223

Saved because typically papers from Sumon are high-quality. Also could
generate ideas for introduction & discussion sections of the paper.

```bibtex
@InProceedings{   obrien202223,
  series        = {ESEC/FSE ’22},
  title         = {23 shades of self-admitted technical debt: an empirical
                  study on machine learning software},
  url           = {http://dx.doi.org/10.1145/3540250.3549088},
  doi           = {10.1145/3540250.3549088},
  booktitle     = {Proceedings of the 30th ACM Joint European Software
                  Engineering Conference and Symposium on the Foundations of
                  Software Engineering},
  publisher     = {ACM},
  author        = {OBrien, David and Biswas, Sumon and Imtiaz, Sayem and
                  Abdalkareem, Rabe and Shihab, Emad and Rajan, Hridesh},
  year          = {2022},
  month         = nov,
  collection    = {ESEC/FSE ’22}
}
```

## yin2023dynamic

Maybe skim this one.

```bibtex
@InProceedings{   yin2023dynamic,
  series        = {ESEC/FSE ’23},
  title         = {Dynamic Data Fault Localization for Deep Neural Networks},
  url           = {http://dx.doi.org/10.1145/3611643.3616345},
  doi           = {10.1145/3611643.3616345},
  booktitle     = {Proceedings of the 31st ACM Joint European Software
                  Engineering Conference and Symposium on the Foundations of
                  Software Engineering},
  publisher     = {ACM},
  author        = {Yin, Yining and Feng, Yang and Weng, Shihao and Liu, Zixi
                  and Yao, Yuan and Zhang, Yichi and Zhao, Zhihong and Chen,
                  Zhenyu},
  year          = {2023},
  month         = nov,
  collection    = {ESEC/FSE ’23}
}
```

## grotov2022large-scale

For related work/discussion sections.

```bibtex
@InProceedings{   grotov2022large-scale,
  series        = {MSR ’22},
  title         = {A large-scale comparison of Python code in Jupyter
                  notebooks and scripts},
  url           = {http://dx.doi.org/10.1145/3524842.3528447},
  doi           = {10.1145/3524842.3528447},
  booktitle     = {Proceedings of the 19th International Conference on Mining
                  Software Repositories},
  publisher     = {ACM},
  author        = {Grotov, Konstantin and Titov, Sergey and Sotnikov,
                  Vladimir and Golubev, Yaroslav and Bryksin, Timofey},
  year          = {2022},
  month         = may,
  collection    = {MSR ’22}
}
```

## tufano2022methods2test

Dataset containing methods and the corresponding unit test for Java
projects.

```bibtex
@InProceedings{   tufano2022methods2test,
  series        = {MSR ’22},
  title         = {Methods2Test: a dataset of focal methods mapped to test
                  cases},
  url           = {http://dx.doi.org/10.1145/3524842.3528009},
  doi           = {10.1145/3524842.3528009},
  booktitle     = {Proceedings of the 19th International Conference on Mining
                  Software Repositories},
  publisher     = {ACM},
  author        = {Tufano, Michele and Deng, Shao Kun and Sundaresan, Neel
                  and Svyatkovskiy, Alexey},
  year          = {2022},
  month         = may,
  collection    = {MSR ’22}
}
```

## morovati2023bugs

Dataset of defects in ML. Which bugs can our tool catch?

```bibtex
@Article{         morovati2023bugs,
  title         = {Bugs in machine learning-based systems: a faultload
                  benchmark},
  volume        = {28},
  issn          = {1573-7616},
  url           = {http://dx.doi.org/10.1007/s10664-023-10291-1},
  doi           = {10.1007/s10664-023-10291-1},
  number        = {3},
  journal       = {Empirical Software Engineering},
  publisher     = {Springer Science and Business Media LLC},
  author        = {Morovati, Mohammad Mehdi and Nikanjam, Amin and Khomh,
                  Foutse and Jiang, Zhen Ming},
  year          = {2023},
  month         = apr
}
```

## bhatia2023towards

Should also reveal interesting stuff.

```bibtex
@Article{         bhatia2023towards,
  title         = {Towards a change taxonomy for machine learning pipelines:
                  Empirical study of ML pipelines and forks related to
                  academic publications},
  volume        = {28},
  issn          = {1573-7616},
  url           = {http://dx.doi.org/10.1007/s10664-022-10282-8},
  doi           = {10.1007/s10664-022-10282-8},
  number        = {3},
  journal       = {Empirical Software Engineering},
  publisher     = {Springer Science and Business Media LLC},
  author        = {Bhatia, Aaditya and Eghan, Ellis E. and Grichi, Manel and
                  Cavanagh, William G. and Jiang, Zhen Ming and Adams, Bram},
  year          = {2023},
  month         = apr
}
```

## lukasczyk2023empirical

Automated test generation tool for Python. Interesting read for
related work.

```bibtex
@Article{         lukasczyk2023empirical,
  title         = {An empirical study of automated unit test generation for
                  Python},
  volume        = {28},
  issn          = {1573-7616},
  url           = {http://dx.doi.org/10.1007/s10664-022-10248-w},
  doi           = {10.1007/s10664-022-10248-w},
  number        = {2},
  journal       = {Empirical Software Engineering},
  publisher     = {Springer Science and Business Media LLC},
  author        = {Lukasczyk, Stephan and Kroiß, Florian and Fraser,
                  Gordon},
  year          = {2023},
  month         = jan
}
```

## herbold2023differential

Differential testing for DL. Read the empirical analysis part.

```bibtex
@Article{         herbold2023differential,
  title         = {Differential testing for machine learning: an analysis for
                  classification algorithms beyond deep learning},
  volume        = {28},
  issn          = {1573-7616},
  url           = {http://dx.doi.org/10.1007/s10664-022-10273-9},
  doi           = {10.1007/s10664-022-10273-9},
  number        = {2},
  journal       = {Empirical Software Engineering},
  publisher     = {Springer Science and Business Media LLC},
  author        = {Herbold, Steffen and Tunkel, Steffen},
  year          = {2023},
  month         = jan
}
```

## tony2023llmseceval

I am primarily interested in how they organise and present the dataset
of LLM prompts.

```bibtex
@InProceedings{   tony2023llmseceval,
  title         = {LLMSecEval: A Dataset of Natural Language Prompts for
                  Security Evaluations},
  url           = {http://dx.doi.org/10.1109/MSR59073.2023.00084},
  doi           = {10.1109/msr59073.2023.00084},
  booktitle     = {2023 IEEE/ACM 20th International Conference on Mining
                  Software Repositories (MSR)},
  publisher     = {IEEE},
  author        = {Tony, Catherine and Mutas, Markus and Ferreyra, Nicolás
                  E. Díaz and Scandariato, Riccardo},
  year          = {2023},
  month         = may
}
```

## yang2023what

Could also be an interesting read. Authors present dataset of issues
collected from open-source AI projects on Github.

```bibtex
@InProceedings{   yang2023what,
  title         = {What Do Users Ask in Open-Source AI Repositories? An
                  Empirical Study of GitHub Issues},
  url           = {http://dx.doi.org/10.1109/MSR59073.2023.00024},
  doi           = {10.1109/msr59073.2023.00024},
  booktitle     = {2023 IEEE/ACM 20th International Conference on Mining
                  Software Repositories (MSR)},
  publisher     = {IEEE},
  author        = {Yang, Zhou and Wang, Chenyu and Shi, Jieke and Hoang,
                  Thong and Kochhar, Pavneet and Lu, Qinghua and Xing,
                  Zhenchang and Lo, David},
  year          = {2023},
  month         = may
}
```

## widyasari2023niche

Authors present a dataset of mature ML projects from Github. We can
use this to mine Jupyter Notebooks for our paper.

```bibtex
@InProceedings{   widyasari2023niche,
  title         = {NICHE: A Curated Dataset of Engineered Machine Learning
                  Projects in Python},
  url           = {http://dx.doi.org/10.1109/MSR59073.2023.00022},
  doi           = {10.1109/msr59073.2023.00022},
  booktitle     = {2023 IEEE/ACM 20th International Conference on Mining
                  Software Repositories (MSR)},
  publisher     = {IEEE},
  author        = {Widyasari, Ratnadira and Yang, Zhou and Thung, Ferdian and
                  Qin Sim, Sheng and Wee, Fiona and Lok, Camellia and Phan,
                  Jack and Qi, Haodi and Tan, Constance and Tay, Qijin and
                  Lo, David},
  year          = {2023},
  month         = may
}
```

## tambon2023silent

Good paper for the discussion/related work section. Can our tool help
reduce silent bugs?

```bibtex
@Article{         tambon2023silent,
  title         = {Silent bugs in deep learning frameworks: an empirical
                  study of Keras and TensorFlow},
  volume        = {29},
  issn          = {1573-7616},
  url           = {http://dx.doi.org/10.1007/s10664-023-10389-6},
  doi           = {10.1007/s10664-023-10389-6},
  number        = {1},
  journal       = {Empirical Software Engineering},
  publisher     = {Springer Science and Business Media LLC},
  author        = {Tambon, Florian and Nikanjam, Amin and An, Le and Khomh,
                  Foutse and Antoniol, Giuliano},
  year          = {2023},
  month         = nov
}
```

## li2022robust

Maybe good for discussion section?

```bibtex
@InProceedings{   li2022robust,
  series        = {ASE ’22},
  title         = {Robust Learning of Deep Predictive Models from Noisy and
                  Imbalanced Software Engineering Datasets},
  url           = {http://dx.doi.org/10.1145/3551349.3556941},
  doi           = {10.1145/3551349.3556941},
  booktitle     = {Proceedings of the 37th IEEE/ACM International Conference
                  on Automated Software Engineering},
  publisher     = {ACM},
  author        = {Li, Zhong and Pan, Minxue and Pei, Yu and Zhang, Tian and
                  Wang, Linzhang and Li, Xuandong},
  year          = {2022},
  month         = oct,
  collection    = {ASE ’22}
}
```

## yang2022data

Detecting data leakage in data science notebooks.

```bibtex
@InProceedings{   yang2022data,
  series        = {ASE ’22},
  title         = {Data Leakage in Notebooks: Static Detection and Better
                  Processes},
  url           = {http://dx.doi.org/10.1145/3551349.3556918},
  doi           = {10.1145/3551349.3556918},
  booktitle     = {Proceedings of the 37th IEEE/ACM International Conference
                  on Automated Software Engineering},
  publisher     = {ACM},
  author        = {Yang, Chenyang and Brower-Sinning, Rachel A and Lewis,
                  Grace and KÄStner, Christian},
  year          = {2022},
  month         = oct,
  collection    = {ASE ’22}
}
```

## blasi2022call

Automated test case generation tool (using LLMs). Good for related
work section.

```bibtex
@InProceedings{   blasi2022call,
  series        = {ASE ’22},
  title         = {Call Me Maybe: Using NLP to Automatically Generate Unit
                  Test Cases Respecting Temporal Constraints},
  url           = {http://dx.doi.org/10.1145/3551349.3556961},
  doi           = {10.1145/3551349.3556961},
  booktitle     = {Proceedings of the 37th IEEE/ACM International Conference
                  on Automated Software Engineering},
  publisher     = {ACM},
  author        = {Blasi, Arianna and Gorla, Alessandra and Ernst, Michael D.
                  and Pezzè, Mauro},
  year          = {2022},
  month         = oct,
  collection    = {ASE ’22}
}
```

## xie2022boosting

Skim to understand basics of Metamorphic Testing.

```bibtex
@InProceedings{   xie2022boosting,
  series        = {ASE ’22},
  title         = {Boosting the Revealing of Detected Violations in Deep
                  Learning Testing: A Diversity-Guided Method},
  url           = {http://dx.doi.org/10.1145/3551349.3556919},
  doi           = {10.1145/3551349.3556919},
  booktitle     = {Proceedings of the 37th IEEE/ACM International Conference
                  on Automated Software Engineering},
  publisher     = {ACM},
  author        = {Xie, Xiaoyuan and Yin, Pengbo and Chen, Songqiang},
  year          = {2022},
  month         = oct,
  collection    = {ASE ’22}
}
```

## eghbali2022crystalbleu

Could we use code-similarity metrics for reducing the number of
notebooks with related VA-pairs?

```bibtex
@InProceedings{   eghbali2022crystalbleu,
  series        = {ASE ’22},
  title         = {CrystalBLEU: Precisely and Efficiently Measuring the
                  Similarity of Code},
  url           = {http://dx.doi.org/10.1145/3551349.3556903},
  doi           = {10.1145/3551349.3556903},
  booktitle     = {Proceedings of the 37th IEEE/ACM International Conference
                  on Automated Software Engineering},
  publisher     = {ACM},
  author        = {Eghbali, Aryaz and Pradel, Michael},
  year          = {2022},
  month         = oct,
  collection    = {ASE ’22}
}
```

## rao2023cat-lm

Authors propose an LLM based tool that generates tests given code
(not ML).

```bibtex
@InProceedings{   rao2023cat-lm,
  title         = {CAT-LM Training Language Models on Aligned Code And
                  Tests},
  url           = {http://dx.doi.org/10.1109/ASE56229.2023.00193},
  doi           = {10.1109/ase56229.2023.00193},
  booktitle     = {2023 38th IEEE/ACM International Conference on Automated
                  Software Engineering (ASE)},
  publisher     = {IEEE},
  author        = {Rao, Nikitha and Jain, Kush and Alon, Uri and Goues,
                  Claire Le and Hellendoorn, Vincent J.},
  year          = {2023},
  month         = sep
}
```

## tıraşoğlu2023open

```bibtex
@InProceedings{   tıraşoğlu2023open,
  title         = {Open Source Software Tools for Data Management and Deep
                  Model Training Automation},
  url           = {http://dx.doi.org/10.1109/ASE56229.2023.00014},
  doi           = {10.1109/ase56229.2023.00014},
  booktitle     = {2023 38th IEEE/ACM International Conference on Automated
                  Software Engineering (ASE)},
  publisher     = {IEEE},
  author        = {Tıraşoğlu, Umut and Türker, Abdussamet and Ekici,
                  Adnan and Yiğit, Hayri and Bölükbaşı, Yusuf Enes and
                  Akgün, Toygar},
  year          = {2023},
  month         = sep
}
```

## missaoui2023semantic

Data-centric DL testing tool.

```bibtex
@InProceedings{   missaoui2023semantic,
  title         = {Semantic Data Augmentation for Deep Learning Testing Using
                  Generative AI},
  url           = {http://dx.doi.org/10.1109/ASE56229.2023.00194},
  doi           = {10.1109/ase56229.2023.00194},
  booktitle     = {2023 38th IEEE/ACM International Conference on Automated
                  Software Engineering (ASE)},
  publisher     = {IEEE},
  author        = {Missaoui, Sondess and Gerasimou, Simos and Matragkas,
                  Nicholas},
  year          = {2023},
  month         = sep
}
```

## TODO yan2023closer

Read the methodology & evaluation sections, authors use ChatGPT in the
study.

```bibtex

@InProceedings{   yan2023closer,
  title         = {A Closer Look at Different Difficulty Levels Code
                  Generation Abilities of ChatGPT},
  url           = {http://dx.doi.org/10.1109/ASE56229.2023.00096},
  doi           = {10.1109/ase56229.2023.00096},
  booktitle     = {2023 38th IEEE/ACM International Conference on Automated
                  Software Engineering (ASE)},
  publisher     = {IEEE},
  author        = {Yan, Dapeng and Gao, Zhipeng and Liu, Zhiming},
  year          = {2023},
  month         = sep
}
```

## dey2023challenges

Skim for essentials of AutoML.

```bibtex
@InProceedings{   dey2023challenges,
  title         = {Challenges of Accurate and Efficient AutoML},
  url           = {http://dx.doi.org/10.1109/ASE56229.2023.00182},
  doi           = {10.1109/ase56229.2023.00182},
  booktitle     = {2023 38th IEEE/ACM International Conference on Automated
                  Software Engineering (ASE)},
  publisher     = {IEEE},
  author        = {Dey, Swarnava and Ghose, Avik and Das, Soumik},
  year          = {2023},
  month         = sep
}
```

## gao2022adaptive

DL testing paper. I am noticing a trend amongst these papers, they are
all focused on curating better test sets. In contrast, we are studying
the process of developing AI, and proposing to generate tests from
within.

```bibtex
@InProceedings{   gao2022adaptive,
  series        = {ICSE ’22},
  title         = {Adaptive test selection for deep neural networks},
  url           = {http://dx.doi.org/10.1145/3510003.3510232},
  doi           = {10.1145/3510003.3510232},
  booktitle     = {Proceedings of the 44th International Conference on
                  Software Engineering},
  publisher     = {ACM},
  author        = {Gao, Xinyu and Feng, Yang and Yin, Yining and Liu, Zixi
                  and Chen, Zhenyu and Xu, Baowen},
  year          = {2022},
  month         = may,
  collection    = {ICSE ’22}
}
```

## yu2022automated

Automatic assertion generation, using IR and DL for traditional SE.
Good addition for related work.

```bibtex
@InProceedings{   yu2022automated,
  series        = {ICSE ’22},
  title         = {Automated assertion generation via information retrieval
                  and its integration with deep learning},
  url           = {http://dx.doi.org/10.1145/3510003.3510149},
  doi           = {10.1145/3510003.3510149},
  booktitle     = {Proceedings of the 44th International Conference on
                  Software Engineering},
  publisher     = {ACM},
  author        = {Yu, Hao and Lou, Yiling and Sun, Ke and Ran, Dezhi and
                  Xie, Tao and Hao, Dan and Li, Ying and Li, Ge and Wang,
                  Qianxiang},
  year          = {2022},
  month         = may,
  collection    = {ICSE ’22}
}
```

## wang2022bridging

Authors propose fine-tuning approach for PTMs for the task of code
understanding. Read the evaluation section, can be helpful for our
paper.

```bibtex
@InProceedings{   wang2022bridging,
  series        = {ICSE ’22},
  title         = {Bridging pre-trained models and downstream tasks for
                  source code understanding},
  url           = {http://dx.doi.org/10.1145/3510003.3510062},
  doi           = {10.1145/3510003.3510062},
  booktitle     = {Proceedings of the 44th International Conference on
                  Software Engineering},
  publisher     = {ACM},
  author        = {Wang, Deze and Jia, Zhouyang and Li, Shanshan and Yu, Yue
                  and Xiong, Yun and Dong, Wei and Liao, Xiangke},
  year          = {2022},
  month         = may,
  collection    = {ICSE ’22}
}
```

## nahar2022collaboration

For introduction and discussion sections.

```bibtex
@InProceedings{   nahar2022collaboration,
  series        = {ICSE ’22},
  title         = {Collaboration challenges in building ML-enabled systems:
                  communication, documentation, engineering, and process},
  url           = {http://dx.doi.org/10.1145/3510003.3510209},
  doi           = {10.1145/3510003.3510209},
  booktitle     = {Proceedings of the 44th International Conference on
                  Software Engineering},
  publisher     = {ACM},
  author        = {Nahar, Nadia and Zhou, Shurui and Lewis, Grace and
                  Kästner, Christian},
  year          = {2022},
  month         = may,
  collection    = {ICSE ’22}
}
```

## wang2022eagle

Testing paper. Skim.

```bibtex
@InProceedings{   wang2022eagle,
  series        = {ICSE ’22},
  title         = {EAGLE: creating equivalent graphs to test deep learning
                  libraries},
  url           = {http://dx.doi.org/10.1145/3510003.3510165},
  doi           = {10.1145/3510003.3510165},
  booktitle     = {Proceedings of the 44th International Conference on
                  Software Engineering},
  publisher     = {ACM},
  author        = {Wang, Jiannan and Lutellier, Thibaud and Qian, Shangshu
                  and Pham, Hung Viet and Tan, Lin},
  year          = {2022},
  month         = may,
  collection    = {ICSE ’22}
}
```

## haq2022efficient

Online testing of DL models deployed in safety-critical conditions. Skim for general understanding.

```bibtex
@InProceedings{   haq2022efficient,
  series        = {ICSE ’22},
  title         = {Efficient online testing for DNN-enabled systems using
                  surrogate-assisted and many-objective optimization},
  url           = {http://dx.doi.org/10.1145/3510003.3510188},
  doi           = {10.1145/3510003.3510188},
  booktitle     = {Proceedings of the 44th International Conference on
                  Software Engineering},
  publisher     = {ACM},
  author        = {Haq, Fitash Ul and Shin, Donghwan and Briand, Lionel},
  year          = {2022},
  month         = may,
  collection    = {ICSE ’22}
}
```

## wei2022free

Another DL testing paper, using fuzzing. Skim to grasp basics of
fuzzing.

```bibtex
@InProceedings{   wei2022free,
  series        = {ICSE ’22},
  title         = {Free lunch for testing: fuzzing deep-learning libraries
                  from open source},
  url           = {http://dx.doi.org/10.1145/3510003.3510041},
  doi           = {10.1145/3510003.3510041},
  booktitle     = {Proceedings of the 44th International Conference on
                  Software Engineering},
  publisher     = {ACM},
  author        = {Wei, Anjiang and Deng, Yinlin and Yang, Chenyuan and
                  Zhang, Lingming},
  year          = {2022},
  month         = may,
  collection    = {ICSE ’22}
}
```

## gu2022muffin

DL testing, albeit not related to what I am doing. But we should still
skim these papers for the related work section.

```bibtex
@InProceedings{   gu2022muffin,
  series        = {ICSE ’22},
  title         = {Muffin: testing deep learning libraries via neural
                  architecture fuzzing},
  url           = {http://dx.doi.org/10.1145/3510003.3510092},
  doi           = {10.1145/3510003.3510092},
  booktitle     = {Proceedings of the 44th International Conference on
                  Software Engineering},
  publisher     = {ACM},
  author        = {Gu, Jiazhen and Luo, Xuchuan and Zhou, Yangfan and Wang,
                  Xin},
  year          = {2022},
  month         = may,
  collection    = {ICSE ’22}
}
```

## patra2022nalin

Authors mine Jupyter Notebooks, skim methodology.

```bibtex
@InProceedings{   patra2022nalin,
  series        = {ICSE ’22},
  title         = {Nalin: learning from runtime behavior to find name-value
                  inconsistencies in jupyter notebooks},
  url           = {http://dx.doi.org/10.1145/3510003.3510144},
  doi           = {10.1145/3510003.3510144},
  booktitle     = {Proceedings of the 44th International Conference on
                  Software Engineering},
  publisher     = {ACM},
  author        = {Patra, Jibesh and Pradel, Michael},
  year          = {2022},
  month         = may,
  collection    = {ICSE ’22}
}
```

## TODO saha2022sapientml

Read the methodology, they mined Kaggle for ML pipelines and datasets.

```bibtex
@InProceedings{   saha2022sapientml,
  series        = {ICSE ’22},
  title         = {SapientML: synthesizing machine learning pipelines by
                  learning from human-writen solutions},
  url           = {http://dx.doi.org/10.1145/3510003.3510226},
  doi           = {10.1145/3510003.3510226},
  booktitle     = {Proceedings of the 44th International Conference on
                  Software Engineering},
  publisher     = {ACM},
  author        = {Saha, Ripon K. and Ura, Akira and Mahajan, Sonal and Zhu,
                  Chenguang and Li, Linyi and Hu, Yang and Yoshida, Hiroaki
                  and Khurshid, Sarfraz and Prasad, Mukul R.},
  year          = {2022},
  month         = may,
  collection    = {ICSE ’22}
}
```
## TODO biswas2022art

This has been sitting in my reading list for a long time now. Should
be useful for introduction & discussion.

```bibtex
@InProceedings{   biswas2022art,
  series        = {ICSE ’22},
  title         = {The art and practice of data science pipelines: A
                  comprehensive study of data science pipelines in theory,
                  in-the-small, and in-the-large},
  url           = {http://dx.doi.org/10.1145/3510003.3510057},
  doi           = {10.1145/3510003.3510057},
  booktitle     = {Proceedings of the 44th International Conference on
                  Software Engineering},
  publisher     = {ACM},
  author        = {Biswas, Sumon and Wardat, Mohammad and Rajan, Hridesh},
  year          = {2022},
  month         = may,
  collection    = {ICSE ’22}
}
```

## chen2022towards

Could be interesting for discussion on how our tool can help make AI
systems reproducible?

``` bibtex
@InProceedings{   chen2022towards,
  series        = {ICSE ’22},
  title         = {Towards training reproducible deep learning models},
  url           = {http://dx.doi.org/10.1145/3510003.3510163},
  doi           = {10.1145/3510003.3510163},
  booktitle     = {Proceedings of the 44th International Conference on
                  Software Engineering},
  publisher     = {ACM},
  author        = {Chen, Boyuan and Wen, Mingzhi and Shi, Yong and Lin, Dayi
                  and Rajbahadur, Gopi Krishnan and Jiang, Zhen Ming (Jack)},
  year          = {2022},
  month         = may,
  collection    = {ICSE ’22}
}
```

## lemieux2023codamosa

Paper from Microsoft. Read the methodology to learn how they used LLMs
for code generation. What prompting techniques were used? How did they
collect the data? How did then handle stochastic nature of output
generated given same prompt?

``` bibtex
@InProceedings{   lemieux2023codamosa,
  title         = {CodaMosa: Escaping Coverage Plateaus in Test Generation
                  with Pre-trained Large Language Models},
  url           = {http://dx.doi.org/10.1109/ICSE48619.2023.00085},
  doi           = {10.1109/icse48619.2023.00085},
  booktitle     = {2023 IEEE/ACM 45th International Conference on Software
                  Engineering (ICSE)},
  publisher     = {IEEE},
  author        = {Lemieux, Caroline and Inala, Jeevana Priya and Lahiri,
                  Shuvendu K. and Sen, Siddhartha},
  year          = {2023},
  month         = may
}
```

## [TODO]{.todo .TODO} mailach2023socio-technical {#mailach2023socio-technical}

More general paper, could be useful for introduction or discussion.

``` bibtex
@InProceedings{   mailach2023socio-technical,
  title         = {Socio-Technical Anti-Patterns in Building ML-Enabled
                  Software: Insights from Leaders on the Forefront},
  url           = {http://dx.doi.org/10.1109/ICSE48619.2023.00067},
  doi           = {10.1109/icse48619.2023.00067},
  booktitle     = {2023 IEEE/ACM 45th International Conference on Software
                  Engineering (ICSE)},
  publisher     = {IEEE},
  author        = {Mailach, Alina and Siegmund, Norbert},
  year          = {2023},
  month         = may
}
```

## [TODO]{.todo .TODO} liu2023contrabert {#liu2023contrabert}

Could be interesting to generate discussion points/future work.

``` bibtex
@InProceedings{   liu2023contrabert,
  title         = {ContraBERT: Enhancing Code Pre-trained Models via
                  Contrastive Learning},
  url           = {http://dx.doi.org/10.1109/ICSE48619.2023.00207},
  doi           = {10.1109/icse48619.2023.00207},
  booktitle     = {2023 IEEE/ACM 45th International Conference on Software
                  Engineering (ICSE)},
  publisher     = {IEEE},
  author        = {Liu, Shangqing and Wu, Bozhi and Xie, Xiaofei and Meng,
                  Guozhu and Liu, Yang},
  year          = {2023},
  month         = may
}
```

## [TODO]{.todo .TODO} jiang2023empirical {#jiang2023empirical}

Empirical study on model-reuse of PTMs.

``` bibtex
@InProceedings{   jiang2023empirical,
  title         = {An Empirical Study of Pre-Trained Model Reuse in the
                  Hugging Face Deep Learning Model Registry},
  url           = {http://dx.doi.org/10.1109/ICSE48619.2023.00206},
  doi           = {10.1109/icse48619.2023.00206},
  booktitle     = {2023 IEEE/ACM 45th International Conference on Software
                  Engineering (ICSE)},
  publisher     = {IEEE},
  author        = {Jiang, Wenxin and Synovic, Nicholas and Hyatt, Matt and
                  Schorlemmer, Taylor R. and Sethi, Rohan and Lu, Yung-Hsiang
                  and Thiruvathukal, George K. and Davis, James C.},
  year          = {2023},
  month         = may
}
```

## [TODO]{.todo .TODO} xia2023balancing {#xia2023balancing}

Authors propose a tool that heuristically determines the optimal
threshold in ML tests. We saw several assertions in our dataset with
such thresholds. This paper may provide ideas for the discussion
section.

``` bibtex
@InProceedings{   xia2023balancing,
  title         = {Balancing Effectiveness and Flakiness of Non-Deterministic
                  Machine Learning Tests},
  url           = {http://dx.doi.org/10.1109/ICSE48619.2023.00154},
  doi           = {10.1109/icse48619.2023.00154},
  booktitle     = {2023 IEEE/ACM 45th International Conference on Software
                  Engineering (ICSE)},
  publisher     = {IEEE},
  author        = {Xia, Chunqiu Steven and Dutta, Saikat and Misailovic, Sasa
                  and Marinov, Darko and Zhang, Lingming},
  year          = {2023},
  month         = may
}
```

## [TODO]{.todo .TODO} hu2023aries {#hu2023aries}

Paper proposes a tool that can estimate the performance of a DNN on
unlabelled data, using the information from the prior labelled data.

``` bibtex
@InProceedings{   hu2023aries,
  title         = {Aries: Efficient Testing of Deep Neural Networks via
                  Labeling-Free Accuracy Estimation},
  url           = {http://dx.doi.org/10.1109/ICSE48619.2023.00152},
  doi           = {10.1109/icse48619.2023.00152},
  booktitle     = {2023 IEEE/ACM 45th International Conference on Software
                  Engineering (ICSE)},
  publisher     = {IEEE},
  author        = {Hu, Qiang and Guo, Yuejun and Xie, Xiaofei and Cordy,
                  Maxime and Papadakis, Mike and Ma, Lei and Traon, Yves Le},
  year          = {2023},
  month         = may
}
```

## [TODO]{.todo .TODO} riccio2023when {#riccio2023when}

Authors perform an empirical study to evaluate the effectiveness of
automated validators for Test Input Generators (TIGs). I see the
translation of visual analytics properties to assertions as a form of
automatic validation.

``` bibtex
@InProceedings{   riccio2023when,
  title         = {When and Why Test Generators for Deep Learning Produce
                  Invalid Inputs: an Empirical Study},
  url           = {http://dx.doi.org/10.1109/ICSE48619.2023.00104},
  doi           = {10.1109/icse48619.2023.00104},
  booktitle     = {2023 IEEE/ACM 45th International Conference on Software
                  Engineering (ICSE)},
  publisher     = {IEEE},
  author        = {Riccio, Vincenzo and Tonella, Paolo},
  year          = {2023},
  month         = may
}
```

## [TODO]{.todo .TODO} liu2023syntax {#liu2023syntax}

Authors propose a tool that translates programs written in one
programming language to another. We are also \"translating\" code,
albeit in the same programming language. What evaluation metrics were
used?

``` bibtex
@InProceedings{   liu2023syntax,
  title         = {Syntax and Domain Aware Model for Unsupervised Program
                  Translation},
  url           = {http://dx.doi.org/10.1109/ICSE48619.2023.00072},
  doi           = {10.1109/icse48619.2023.00072},
  booktitle     = {2023 IEEE/ACM 45th International Conference on Software
                  Engineering (ICSE)},
  publisher     = {IEEE},
  author        = {Liu, Fang and Li, Jia and Zhang, Li},
  year          = {2023},
  month         = may
}
```

## [TODO]{.todo .TODO} mahbub2023explaining {#mahbub2023explaining}

Authors develop a tool that generates natural language text from corpus
of buggy code. They also perform a user-study with 2 participants. Read
the methodology, emphasis on data-collection, pre-processing steps and
the human study.

``` bibtex
@InProceedings{   mahbub2023explaining,
  title         = {Explaining Software Bugs Leveraging Code Structures in
                  Neural Machine Translation},
  url           = {http://dx.doi.org/10.1109/ICSE48619.2023.00063},
  doi           = {10.1109/icse48619.2023.00063},
  booktitle     = {2023 IEEE/ACM 45th International Conference on Software
                  Engineering (ICSE)},
  publisher     = {IEEE},
  author        = {Mahbub, Parvez and Shuvo, Ohiduzzaman and Rahman, Mohammad
                  Masudur},
  year          = {2023},
  month         = may
}
```

## [TODO]{.todo .TODO} guan2023comprehensive {#guan2023comprehensive}

Authors create a dataset of Model Optimization Bugs (MOBs). Read the
data collection part, could be interesting for us.

``` bibtex
@InProceedings{   guan2023comprehensive,
  title         = {A Comprehensive Study of Real-World Bugs in Machine
                  Learning Model Optimization},
  url           = {http://dx.doi.org/10.1109/ICSE48619.2023.00024},
  doi           = {10.1109/icse48619.2023.00024},
  booktitle     = {2023 IEEE/ACM 45th International Conference on Software
                  Engineering (ICSE)},
  publisher     = {IEEE},
  author        = {Guan, Hao and Xiao, Ying and Li, Jiaying and Liu, Yepang
                  and Bai, Guangdong},
  year          = {2023},
  month         = may
}
```

## [TODO]{.todo .TODO} croft2023data {#croft2023data}

Use this paper to motivate our manual annotation of dataset.

``` bibtex
@InProceedings{   croft2023data,
  title         = {Data Quality for Software Vulnerability Datasets},
  url           = {http://dx.doi.org/10.1109/ICSE48619.2023.00022},
  doi           = {10.1109/icse48619.2023.00022},
  booktitle     = {2023 IEEE/ACM 45th International Conference on Software
                  Engineering (ICSE)},
  publisher     = {IEEE},
  author        = {Croft, Roland and Babar, M. Ali and Kholoosi, M. Mehdi},
  year          = {2023},
  month         = may
}
```

## [TODO]{.todo .TODO} you2023regression {#you2023regression}

The methodology could be useful to craft evaluation of our LLM based
tool.

``` bibtex
@InProceedings{   you2023regression,
  title         = {Regression Fuzzing for Deep Learning Systems},
  url           = {http://dx.doi.org/10.1109/ICSE48619.2023.00019},
  doi           = {10.1109/icse48619.2023.00019},
  booktitle     = {2023 IEEE/ACM 45th International Conference on Software
                  Engineering (ICSE)},
  publisher     = {IEEE},
  author        = {You, Hanmo and Wang, Zan and Chen, Junjie and Liu, Shuang
                  and Li, Shuochuan},
  year          = {2023},
  month         = may
}
```

## mondal2023cell2doc

Read the methodology in detail, relevant for our data collection
process.

``` bibtex


@InProceedings{   mondal2023cell2doc,
  title         = {Cell2Doc: ML Pipeline for Generating Documentation in
                  Computational Notebooks},
  url           = {http://dx.doi.org/10.1109/ASE56229.2023.00200},
  doi           = {10.1109/ase56229.2023.00200},
  booktitle     = {2023 38th IEEE/ACM International Conference on Automated
                  Software Engineering (ASE)},
  publisher     = {IEEE},
  author        = {Mondal, Tamal and Barnett, Scott and Lal, Akash and
                  Vedurada, Jyothi},
  year          = {2023},
  month         = sep
}
```

## [TODO]{.todo .TODO} salama2021practitioners {#salama2021practitioners}

Recommendation from Luis, white paper on Google\'s approach to MLOps.
Should provide material for the story.

``` bibtex
@Misc{            salama2021practitioners,
  title         = {Practitioners guide to MLOps: A framework for continuous
                  delivery and automation of machine learning},
  url           = {https://services.google.com/fh/files/misc/practitioners_guide_to_mlops_whitepaper.pdf},
  author        = {Salama, Khalid and Kazmierczak, Jarek and Schut, Donna},
  year          = {2021}
}
```

## [TODO]{.todo .TODO} li2023assisting {#li2023assisting}

Recommendation from Luis, authors conduct a study on using chatGPT for
program comprehension. They focus on a bug detection program. Results
are promising.

``` bibtex
@InProceedings{   li2023assisting,
  series        = {ESEC/FSE ’23},
  title         = {Assisting Static Analysis with Large Language Models: A
                  ChatGPT Experiment},
  url           = {http://dx.doi.org/10.1145/3611643.3613078},
  doi           = {10.1145/3611643.3613078},
  booktitle     = {Proceedings of the 31st ACM Joint European Software
                  Engineering Conference and Symposium on the Foundations of
                  Software Engineering},
  publisher     = {ACM},
  author        = {Li, Haonan and Hao, Yu and Zhai, Yizhuo and Qian, Zhiyun},
  year          = {2023},
  month         = nov,
  collection    = {ESEC/FSE ’23}
}
```

\>

# Testing

## wang2023distxplore

Important paper. I think our tool complements this paper. Should
generate interesting compare & contrast points for the discussion
section.

Unfortunately, I did not gain anything from this paper. While the title
was enticing, the content of the paper did not align with my topic.
The writing was not that great, and I did not want to invest too much
time trying decipher what the authors are trying to do.

```bibtex
@InProceedings{   wang2023distxplore,
  series        = {ESEC/FSE ’23},
  title         = {DistXplore: Distribution-Guided Testing for Evaluating and
                  Enhancing Deep Learning Systems},
  url           = {http://dx.doi.org/10.1145/3611643.3616266},
  doi           = {10.1145/3611643.3616266},
  booktitle     = {Proceedings of the 31st ACM Joint European Software
                  Engineering Conference and Symposium on the Foundations of
                  Software Engineering},
  publisher     = {ACM},
  author        = {Wang, Longtian and Xie, Xiaofei and Du, Xiaoning and Tian,
                  Meng and Guo, Qing and Yang, Zheng and Shen, Chao},
  year          = {2023},
  month         = nov,
  collection    = {ESEC/FSE ’23}
}
```

# LLMs

# Notebooks

## DONE ramasamy2023visualising

Jackpot.

"Garden of forking paths".

Lots of good references in the introduction for program comprehension
and challenges when working with Computational Notebooks.

Authors conducted an empirical study with 470 real-world jupyter
Notebooks to show that data science workflow is non-linear and
contains several forks and dead-ends.

```bibtex
@Article{         ramasamy2023visualising,
  title         = {Visualising data science workflows to support third-party
                  notebook comprehension: an empirical study},
  volume        = {28},
  issn          = {1573-7616},
  url           = {http://dx.doi.org/10.1007/s10664-023-10289-9},
  doi           = {10.1007/s10664-023-10289-9},
  number        = {3},
  journal       = {Empirical Software Engineering},
  publisher     = {Springer Science and Business Media LLC},
  author        = {Ramasamy, Dhivyabharathi and Sarasua, Cristina and
                  Bacchelli, Alberto and Bernstein, Abraham},
  year          = {2023},
  month         = mar
}
```
# Empirical Methods

## fregnan2022first

This is the paper Alberto presented at SIESTA 2023. Read the
methodology to understand method used to determine sufficient number
of samples required for empirical studies.

The authors used an *a priori power analysis* to determine the number
of participants required for producing statistically significant
results.

```bibtex
@InProceedings{   fregnan2022first,
  series        = {ESEC/FSE ’22},
  title         = {First come first served: the impact of file position on
                  code review},
  url           = {http://dx.doi.org/10.1145/3540250.3549177},
  doi           = {10.1145/3540250.3549177},
  booktitle     = {Proceedings of the 30th ACM Joint European Software
                  Engineering Conference and Symposium on the Foundations of
                  Software Engineering},
  publisher     = {ACM},
  author        = {Fregnan, Enrico and Braz, Larissa and D’Ambros, Marco
                  and Çalıklı, Gül and Bacchelli, Alberto},
  year          = {2022},
  month         = nov,
  collection    = {ESEC/FSE ’22}
}
```


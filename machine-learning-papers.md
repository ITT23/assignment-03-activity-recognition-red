# Questions about Machine Learning Papers

## What are some common use cases for machine learning in practical applications or research prototypes?

Kostakos and Musolesi (2017) mention a few use cases for machine learning. One of them involves activity recognition, i.e. identifying activities such as waving or standing using machine learning. Modeling human behavior is also a popular use case for machine learning. In this scenario, the authors note that one should distinguish using the classical statistical methods of machine learning and the neural-network-based approaches. Reasons for this mention will be further explained in the answer to question 2. Furthermore, machine learning is used to develop novel user-interface techniques such as reacting to user input or optimizing system resources (Kostakos & Musolesi, 2017). The last use case they mentioned in the paper is the prediction of users' activities and interactions.
Sculley et al. (2014) only mention a system that uses machine learning for predicting the click through rate of websites.

## Which problems of machine learning do the authors of the papers identify?

Kostakos and Musolesi (2017) identified more general problems of the usage of machine learning and the interpretation of resulting data. One problem they mentioned is that ML is sometimes used inappropriately to draw conclusions about human behaviour in cases where classical methods could be used which could be easier to use and to interpret. The complexity of models can also cause problems, especially when deriving conclusions about human behaviour. Researchers should be especially careful in regard to this when they are relying on non-controlled designs. Lastly, they also mentioned the overall prevalence of mistaking correlation for causality, especially since ML involves dealing with a variety of variables. Sculley et al. (2014) go in depth about more technical issues related to ML. One big point is the erosion of boundaries. Since Machine learning logic cannot be easily expressed in software, there is a need for dependency of external data which leads to bad abstraction. One part of this is the entanglement of the model because of the mixture of data sources. This leads to a dependency between the variables in the system, for example changing one input or hyperparameter could lead to changes everywhere else in the system and different behavior. Two other parts are hidden feedback loops, which are hard to understand quickly and can make changes difficult, and undeclared customers, which could be other systems or models that rely on the input from your model and are influenced by changes in the top-level model. Data dependencies are also a big problem, since they cannot be easily analyzed and can lead to dependency chains or other issues.They could also be unstable for a variety of reasons and changes in those dependencies can lead to unintended changes in the model. Another issue could also be neglecting old dependencies in the code-base which are redundant and should be removed. Changes in those dependencies can furthermore lead to vulnerabilities in the system. Another problem can also be the dependency between different models in the system, as changing one of them could affect the others. They also mentioned issues that could occur because of the code itself, since ML often uses self-contained packages and can lead to a lot of “glue code”. One problem could also be pipeline jungles, when adding more information and preparing an increasing amount of data, as well as dead codepaths that can lead to issues or bad configuration of the system. The last problem mentioned is that ML is especially vulnerable to changes in external data, for example when not adapting thresholds or the external variables change and change their correlation between each other.



## What are the credentials of the authors with regard to machine learning? Have they published research on machine learning (or using machine-learning techniques) previously?

Vassilis Kostakos is a Professor of Human-Computer-Interaction at the University of Melbourne. He does not mention machine learning as one of his research interests (Kostakos, 2023), but he already has published a few papers using machine learning methods or about machine learning(Giannakos et al., 2019;  van Berkel et al., 2016; van Berkel et al., 2019).
Mirco Musolesi is a Professor of Computer Science at University of Bologna and at University College London, where he also leads the Machine Intelligence Lab (Musolesi, 2023). He published many papers in the field of machine learning in the last few years. His focus was especially on deep learning and reinforcement learning (Musolesi, 2023).
D. Sculley is currently the CEO of kaggle. He is especially interested in large scaled machine learning problems, and has published published many different papers in regards to ML-related topics. (Sculley, 2023)
Daniel Golovin is the founder of Vizier (Golovin et al., 2017) and also published some other research regarding ML (Golovin, 2023). Gary R. Holt and Todd Phillips also have listed 'Machine Intelligence' as Research topics, but have both only published 2 papers in general (Holt, 2023; Phillips, 2023). 
There isn't much information about the other authors of the paper 'Machine Learning The High-Interest Credit Card of Technical Debt' (Sculley et al., 2014), but most authors of the paper have a past at Google, or a currently still working and researching at Google.

### Table of Contents:

Giannakos, M. N., Sharma, K., Pappas, I. O., Kostakos, V., & Velloso, E. (2019). Multimodal data as a means to understand the learning experience. International Journal of Information Management, 48, 108-119.

Kostakos, V. (2023). Vassilis Kostakos. Retrieved from https://people.eng.unimelb.edu.au/vkostakos/index.php

Kostakos, V., & Musolesi, M. (2017). Avoiding pitfalls when using machine learning in HCI studies. interactions, 24(4), 34-37.

Musolesi, M. (2023). About Me. Retrieved from https://www.mircomusolesi.org/

Sculley, D., Holt, G., Golovin, D., Davydov, E., Phillips, T., Ebner, D., ... & Young, M. (2014). Machine learning: The high interest credit card of technical debt.

Van Berkel, N., Luo, C., Anagnostopoulos, T., Ferreira, D., Goncalves, J., Hosio, S., & Kostakos, V. (2016, May). A systematic assessment of smartphone usage gaps. In Proceedings of the 2016 CHI conference on human factors in computing systems (pp. 4711-4721).

Van Berkel, N., Goncalves, J., Hettiachchi, D., Wijenayake, S., Kelly, R. M., & Kostakos, V. (2019). Crowdsourcing perceptions of fair predictors for machine learning: A recidivism case study. Proceedings of the ACM on Human-Computer Interaction, 3(CSCW), 1-21.

Sculley, D. (2023). Retrieved from: https://research.google/people/author38217//

Holt, G. (2023). Retrieved from: https://research.google/people/GaryHolt/

Golovin, D. (2023). Retrieved from: https://research.google/people/DanielGolovin/

Phillips, T. (2023). Retrieved from: https://research.google/people/ToddPhillips/

Golovin, D., Solnik, B., Moitra, S., Kochanski, G., Karro, J., & Sculley, D. (2017, August). Google vizier: A service for black-box optimization. In Proceedings of the 23rd ACM SIGKDD international conference on knowledge discovery and data mining (pp. 1487-1495).


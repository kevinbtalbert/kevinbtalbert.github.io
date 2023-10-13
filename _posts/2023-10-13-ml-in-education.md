---
layout: single
title: "Will AI Actually "Save" Education?"
header:
  teaser: "unsplash-gallery-image-2-th.jpg"
date:   2023-10-13 12:00:00 +0000
categories: ml
tags: education ml ai cloudera

---
*summary here*

![](/assets/posts/2023-10-13-ml-in-education/thinking-prof.webp)

## How Can AI Actually "Save" Education

I watched a TED Talk about a week ago where Sal Khan described how AI could "save" education. There has been a great deal of concern amongst both my peers and the educational community at large about how educators should respond to the emergence of "ChatGPT" and other potentially significant AI research which could be leveraged by students to solve homework, complete exams, or write papers. In the video, Sal describes at length the role that AI is taking on at Khan Academy. Unlike traditional exercise interfaces on Khan Academy, "Khanmigo" (the new system he is creating) is designed to interact with students in a more personalized manner.

The conversation between the student and Khanmigo is recorded and can be viewed by the teacher. Additionally, a second AI moderates the discussion. Importantly, the system is not designed to give away answers but to guide the student toward solving problems themselves. When students ask for an answer, it prompts them to think about the next steps for solving the problem.

If a student makes a mistake, Khanmigo not only identifies it but also asks the student to explain their reasoning. The AI can identify common misconceptions, like the misuse of the distributive property in math, and correct them. The system is also capable of assisting with computer programming exercises. For example, it can understand the student's code and offer specific advice, like adding a line of code to make both clouds move in a given program.

Moreover, Khanmigo is not limited to exercises but also comprehends the context of the videos a student is watching. It can answer questions like "Why do I need to learn this?" by linking the learning material to the student's interests and aspirations.

In the Machine Learning world, we call the technical creation Sal and team built a "fine-tuned model". This exercise of creating a fine-tuned model can be done by individuals or at scale. In the educational field specifically, most of the development efforts that *are* happening in this realm seem to be done largely by companies with integrations into existing products, or through an entirely new product, but not natively through an LMS. These capabilities are essential in the commodification of machine learning on student outcomes, and I hope to see them make their way into more LMS systems natively.

## AI for Students

Khanmigo promises to be a "super tutor," offering an interactive, context-aware, and highly personalized learning experience across multiple subjects, but this is just one application of AI into education. Educators *must* learn to adjust their style of teaching to coincide with new technology. Just as we have adapted in the past to changing languages and machines in computer science, so too must we adjust to this new wave. 

In addition to personalized learning experiences, students can have the chance to get real time feedback on an assignment. What if when writing a paper, a student is instructed on best practices, misuse of grammar, better word choices, and other related research available? What if quizzes became an interactive experience, rather than a simple yes or no, multiple choice, or short answer response? We have the chance, right now, to define how the next wave of test taking can be handled. To great success, many educators have already begun employing projects as a way to more effectively assess a student's understanding of the material; using machine learning models to create questions that allow a student to interact with the content could enable a personalized test taking experience that enables the higher order of thinking we as educators want our students to reach.

One of the topics I am hearing more and more is the idea of restricting models. Given the inaccessibility primarily due to cost and technical resourcefulness to train models from scratch, we are left to use existing models to build custom implementations around. In the same likeness as how ChatGPT restricts users from asking questions related to self-harm and criminal behavior, the same could be done to ensure that a prompt provided by the user is *effectively currated* before being passed, along with its suggested behavior, to the model. This realm of predictive analytics is one not previously considered by most LMS. For my own part, I've interacted with a number of LMS and have always been unimpressed by the lack of ability these systems provide to faculty trying to better understand whether their student's are "getting it" or not. A grade on an assignment is certainly a measure of success, but is it a measure of the student's understanding of the content as a whole?

We can program these models to accept "prompts" instead of direct answers, thereby encouring critical thinking and problem-solving over traditional question and answering. This teaches logic, probing, and even allows a student to get hints instead of just an answer.

To that same end, AI can be leveraged for enhancing content delivery to students. Student's may accel at a particular topic and need more time with other topics. Coinciding with the previously stated idea that not all learning is equal, an individual's educational "path" through a course could be subjectively determined by numerical outcomes, but how much better would it be if the content they receive is deterministicly correlated with how they are able to demonstrate the knowledge successfully or not through facilitated interactions with the model?


## AI for Educators

Beyond helping the students, educators can leverage AI as well. Again, current LMS steeply lack this predictive capability. 

For starters, student evaluations, based on a grade or other calculated factors, can suggest early alerts to faculty, ensuring a student with a concerning pattern of low grades is able to get academic help early on as opposed to when its too late (or not at all). 

In creating assignments, faculty should be able to use "intelligent" autograders natively from an LMS. They should be able to select a specific set of answers as context for a model to use as context to evaluate student submissions; possibly training it on what would be "right" and "wrong" for short answers and essay responses.

In my mind, no geography teacher should have to manually grade whether or not the capital city of North Carolina is Raleigh or Greensboro; an AI  assistant should be able to effectively perform this task for them, for the class. I call out this objective example specifically, since there is only one *right* answer, and LMS systems today are *only* built for this type of analysis. With an "intelligent", or more accurately, "fine-tuned" autograder, you can imagine that a book report could also be graded by AI -- and provide *high quality feedback* to students that could assist them in their writing in the future (much like the real-time learning example mentioned previously). College professors, with 100s of code assignments can use AI to intelligently grade both the accuracy of a piece of code (or project itself), and allow the AI to guide them in providing high quality feedback for the student, beyond right and wrong but as an *optimization* problem. 

Since not all models are equal, a fine-tuned "Java programming" model could be used across classes teaching Java, with a specific ability to assist students in completing an assignment that the teacher has "trained" the Java model on. This is not nearly as difficult as it sounds for a teacher to do. These capabilities exist in abstract and in code! Right now, a professor can currate a chatbot to correspond with a student on matters of an assignment it has been trained on. The exercise of training on the assignment may take one or more of several forms: (1) a professor providing instructional feedback to tell a student what to-do or what not to-do in a given circumstance, (2) a series of hints available to assist the student as they reach certain checkmarks in the project, or (3) even an interative training of the model on the code, to ensure it is most effectively tuned to answer questions of this particular assignment. These capabilities could be abstracted to serve an input field to a professor for starter code and an acceptable outcome, and allow the student's to build their own implementations without the need to "look up" on Google, etc. since they know they can get structured help as they go along! Though this example is specific to a Computer Science course, the idea could be extrapolated to almost any domain of teaching!

## Is AI the New Calculator?

I distinctly remember a discussion in which a college Calculus professor described calculators as aids in helping us find our answers. She noted that "in the real world" you will have a calculator, so why not learn how to use it properly here? This line of thinking enables better research, better results, and calls for a higher order of thought. I think so often educators are bogged down with the notion that a student must learn how to do everything from memory, where in practicality that will never be the case. In my own career, I find StackOverflow and a healthy utilization of Slack to get me closer to solving a problem than I ever would have by trying to rely strictly on memory. We as educators must learn how to enable our students to achieve greater outcomes using *all* the tools at both our and their disposal to create an experience worth the dollar sign it cost. From an industry perspective, these tools need to be brought into mainline LMS systems with urgency or (perhaps again due to technical inaccessibility) they risk the academic community shunning AI before it even has its chance.


## References and Other Resources
If what I discussed sounds interesting to you, please be sure to check out the resources below and learn more.

[How AI Could Save (Not Destroy) Education | Sal Khan | TED](https://www.youtube.com/watch?v=hJP5GqnTrNo)
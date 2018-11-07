# Building a Slack or Facebook bot for Db2
Resources for my talk at IDUG EMEA 2018 in Malta. Things I cover(ed):
* [Slack](https://slack.com/) as query interface, using [IBM Watson Assistant](https://console.bluemix.net/docs/services/conversation/index.html#about) to process the natural language input.
* [Open source drivers for IBM database servers](https://github.com/ibmdb/) to connect the chatbot middleware and Watson Assistant to Db2.
* Code is based on the GitHub repos [Slack chatbot with Db2 integration](https://github.com/IBM-Cloud/slack-chatbot-database-watson) and [GitHub traffic stats, Slack integration](https://github.com/IBM-Cloud/github-traffic-stats/)
* Check out the blog on [automated reports with cloud functions, Db2 and Slack](https://blog.4loeser.net/2018/10/automated-reported-with-ibm-cloud.html). It shows how Db2-based statistic reports can be pushed into Slack channels on a regular basis.
* [IBM Cloud solution tutorial on how to build Db2-based Slackbot](https://console.bluemix.net/docs/tutorials/slack-chatbot-database-watson.html)
* The files [systemInfo.js](systemInfo.js) and [setupMoreActions.sh](setupMoreActions.sh) contain the code and script to add another action to the Slackbot tutorial. That action can retrieve Db2 system information. Add an intent to the conversation workspace, then nodes similar to the event retrieval and test it.

Note:
* Eine deutsche Version meines Chatbot-Talks ist im Branch [deutsch_httf](https://github.com/data-henrik/chatbot-talk2018/tree/deutsch_httf).   
* The regular english version of my chatbot talk is available in the [master branch](https://github.com/data-henrik/chatbot-talk2018/tree/master).

![](assets/images/can-chat-chatting-362.jpg)

# Overview
Here is an overview of chatbot concepts. [Wikipedia has this short description about chatbots](https://en.wikipedia.org/wiki/Chatbot) :
> A chatbot (also known as a talkbots, chatterbot, Bot, IM bot, interactive agent, or Artificial Conversational Entity) is a computer program or an artificial intelligence which conducts a conversation via auditory or textual methods.   

Accordingly, chatbots have two tasks:   
> Understanding the user's intent and producing the correct answer.

To understand the user's intent and to produce the correct answer, some additional concepts are used:
* **Intents** are what the user aims for, the desired action or result of the interaction. An intent can be to retrieve a weather report.
* **Entities** are (real or virtual) subjects or objects. For the example of the weather report, entities can be the city or country, e.g., Friedrichshafen in Germany, or date and time information such as "today afternoon".
* A **dialog**, **dialog flow** or **dialog tree** is used to structure the interaction. Typically, an interaction lasts longer than the user providing input and the chatbot returning a single answer. A dialog can be highly complex with several levels, subbranches, (directed) links between **dialog nodes** and more.   
  For a weather chatbot, a dialog could be constructed that, after a greeting, asks the user about the location and time for a weather report, then asks if additional information, such as a weather outlook for the next few days, is needed.
* **Slots** are supported by several chatbot systems. Slots are used to specify the data items that need to be specified in order to produce the result of an intent. To return a weather report, e.g., at least the location and maybe the date or time is needed.
* **Context** is state information that is carried from step to step for a specific user interaction. The context typically stores the information that is already gathered as input (see "slot"), result-related data or metadata, or general chat information, e.g., the user name.

The following architecture diagram is part of the [Cloud Insurance Co](https://github.com/IBM-Cloud/cloudco-insurance) demo. That demo features an insurance portal. A chatbot assist customers to file claims and to check coverage. Administrators have access to chat logs to improve customer satisfaction.   
![](https://github.com/IBM-Cloud/cloudco-insurance/raw/master/architecture.png)

# Resources

### Tutorials & Demos
The following tutorials give a good introduction to chatbots:
* [Getting started tutorial for Watson Assistant](https://console.bluemix.net/docs/services/conversation/getting-started.html#gettingstarted)
* [Build a database-driven Slackbot](https://console.bluemix.net/docs/tutorials/slack-chatbot-database-watson.html)
* [Build a voice-enabled Android chatbot](https://console.bluemix.net/docs/tutorials/android-watson-chatbot.html)
* [Cloud insurance Co.](https://github.com/IBM-Cloud/cloudco-insurance)
* [Bot Asset Exchange](https://developer.ibm.com/code/exchanges/bots/)

### Related blog posts
I wrote quite a number of blog posts about chatbots. The articles have links to further information.
* [Database-driven Slack chatbot with Conversation service](https://www.ibm.com/blogs/bluemix/2018/02/database-slack-chatbot-conversation/)   
* [Chatbots: Some tricks with slots in conversations](https://www.ibm.com/blogs/bluemix/2018/02/chatbots-some-tricks-with-slots-in-ibm-watson-conversation/)
* [Lively chatbots: Best Practices](https://www.ibm.com/blogs/bluemix/2017/07/lively-chatbots-best-practices/)
* [Building chatbots: more tipcs and tricks](https://www.ibm.com/blogs/bluemix/2017/06/building-chatbots-tips-tricks/)
* [Lessons and Tips from a Chatbot Hackathon](https://www.ibm.com/blogs/bluemix/2017/05/lessons-tips-chatbot-hackathon/)
* [Watson Conversation: How to Manage Workspaces](https://www.ibm.com/blogs/bluemix/2017/04/watson-conversation-manage-workspaces/)
* [Extended: Manage and interact with Watson Assistant from the command line](https://blog.4loeser.net/2018/07/extended-manage-and-interact-with.html)

### Other resources
* [Watson Conversation Variables](https://github.com/IBM-Cloud/watson-conversation-variables) has tips and tricks around processing context variables within Watson Assistant
* [watson conversation tool](https://github.com/data-henrik/watson-conversation-tool): tool to manage and interact with Watson Assistant from the command line. Written in Python using the Watson SDK.
